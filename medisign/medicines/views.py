from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import MedicineSerializer, PrescriptionSerializer, ContraindicationSerializer
from .models import Medicine, Prescription, Contraindication
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
import hashlib
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

def compute_image_hash(image):
    # 이미지 데이터를 바이트로 읽기
    data = image.read()
    # SHA-256 해시 계산
    return hashlib.sha256(data).hexdigest()

class MedicineList(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        model = Medicine.objects.all()
        serializer = MedicineSerializer(model, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = MedicineSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicineDetail(APIView):
    permission_classes = [AllowAny]
    def get(self, request, medicine_id):
        model = Medicine.objects.get(id=medicine_id)
        serializer = MedicineSerializer(model, context={'request': request})
        return Response(serializer.data)

    def put(self, request, medicine_id):
        model = Medicine.objects.get(id=medicine_id)
        serializer = MedicineSerializer(model, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, medicine_id):
        model = Medicine.objects.get(id=medicine_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

class PrescriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    
class MedicineCont(APIView):
    permission_classes = [AllowAny]

    def get(self, request, medicine_id):
        # 해당 medicine_id를 가진 Medicine 객체를 조회합니다.
        medicine = get_object_or_404(Medicine, id=medicine_id)

        # medicine의 itemSeq에서 중간 번호만 추출합니다.
        processed_itemseq = [str(seq.number)[3:-1] for seq in medicine.itemSeq.all()]

        # 중간 번호를 기반으로 Contraindication 객체들을 조회합니다.
        contraindications_a = Contraindication.objects.filter(drugNumberA__in=processed_itemseq).exclude(drugNumberB__in=processed_itemseq)
        contraindications_b = Contraindication.objects.filter(drugNumberB__in=processed_itemseq).exclude(drugNumberA__in=processed_itemseq)

        # 두 쿼리셋을 합칩니다.
        contraindications = contraindications_a.union(contraindications_b)

        # 찾아진 Contraindication 객체들을 serialize 합니다.
        serializer = ContraindicationSerializer(contraindications, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
# def search_medicine(request):
#     if request.method == "POST":
#         # 이미지 데이터 로딩
#         image = request.FILES["image"]
#         image_hash = compute_image_hash(image)

#         # DB에서 해시 값을 기반으로 이름 검색
#         try:
#             medicine = MedicineImage.objects.get(image_hash=image_hash)
#             return JsonResponse({
#                 "name": medicine.name,
#                 "prescription_image": medicine.Prescription.image.url
#             })
#         except MedicineImage.DoesNotExist:
#             return JsonResponse({
#                 "error": "Image not found in database"
#             })

#     return JsonResponse({
#         "error": "Invalid request method"
#     })
    
# def add_medicine(request):
#     if request.method == 'POST':
#         # 이미지, 이름, prescription_id 데이터 로딩
#         image = request.FILES["image"]
#         name = request.POST.get("name")
#         prescription_id = request.POST.get("prescription_id")
        
#         # 이미지의 해시 계산
#         image_hash = compute_image_hash(image)

#         # 해당 Prescription 객체 찾기
#         try:
#             prescription = Prescription.objects.get(id=prescription_id)
#         except Prescription.DoesNotExist:
#             return JsonResponse({
#                 "error": "Prescription with given ID does not exist"
#             })

#         # 새로운 MedicineImage 객체 생성 및 저장
#         medicine_image = MedicineImage(name=name, image=image, image_hash=image_hash, Prescription=prescription)
#         medicine_image.save()

#         return JsonResponse({
#             "message": "Image added successfully"
#         })
    
#     return JsonResponse({
#         "error": "Invalid request method"
#     })


# Create your views here.
def index(request):
    return render(request, 'medicines/index.html')

