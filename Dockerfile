# 이미지의 베이스로 사용될 Python 이미지 선택
FROM python:3.10.11

# 환경변수 설정
ENV PYTHONUNBUFFERED 1

# 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
COPY requirements4doc.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements4doc.txt

# 프로젝트의 모든 파일 복사
COPY . /app/
