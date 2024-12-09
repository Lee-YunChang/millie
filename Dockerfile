# 베이스 이미지로 Python 3.9 사용
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 의존성 설치
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

# pipenv 설치
RUN pip install pipenv

# Pipfile과 Pipfile.lock 복사
COPY Pipfile Pipfile.lock /app/

# 의존성 설치
RUN pipenv install --system --deploy

# 소스 코드 복사
COPY . /app/

# 포트 노출
EXPOSE 8000

# 기본 명령어는 docker-compose.yml에서 설정
