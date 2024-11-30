# 1. 베이스 이미지 설정
FROM python:3.10-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 의존성 파일 복사
COPY requirements.txt ./requirements.txt

# 4. Python 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. FastAPI 코드 복사
COPY src/ /app/

# 6. Uvicorn을 통해 FastAPI 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
