# Millie

Django REST Framework(DRF)를 사용하여 쇼핑몰의 상품 관리 API를 구현합니다. 
API는 기본 상품 리스트 및 카테고리별 진열 기능을 제공하며 상품 상세 페이지에서는 할인율 및 쿠폰 적용에 따른 가격 변동을 처리하는 비즈니스 로직을 구현해야 합니다.

## 📋 **목차**

1. [특징](#특징)
2. [사용 기술](#사용-기술)
3. [필수 조건](#필수-조건)
4. [설치](#설치)
    - [레포지토리 클론](#레포지토리-클론)
    - [환경 변수 설정](#환경-변수-설정)
    - [Docker 설정](#docker-설정)
    - [Pipenv 설정](#pipenv-설정)
    - [데이터베이스 마이그레이션](#데이터베이스-마이그레이션)
    - [서버 실행](#서버-실행)

---

## 특징

- **상품 관리:** 상품 생성, 조회, 수정, 삭제 기능 제공.
- **상세 상품 정보:** 원래 가격, 할인 가격, 쿠폰 적용 시 최종 가격을 포함한 상세 정보 조회.
- **API 문서화:** Swagger UI와 ReDoc을 통한 인터랙티브한 API 문서 제공.
- **컨테이너화:** Docker와 Docker Compose를 사용한 간편한 설정 및 배포.
- **의존성 관리:** Pipenv를 통한 효율적인 의존성 관리.
- **보안:** `django-environ`을 사용한 환경 변수 관리.

---

## 사용 기술

- **백엔드 프레임워크:** Django 3.0.11
- **API 프레임워크:** Django REST Framework(DRF) 3.12.4
- **API 문서화:** drf-yasg
- **데이터베이스:** MySQL 8.0
- **컨테이너화:** Docker, Docker Compose
- **의존성 관리:** Pipenv
- **환경 변수 관리:** django-environ

---

## 필수 조건

프로젝트를 설정하기 전에, 다음 소프트웨어가 시스템에 설치되어 있는지 확인하세요:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.9](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.pypa.io/en/latest/install/#install-pipenv)

---

## 설치

다음 단계를 따라 Millie 프로젝트를 로컬 머신에 설정하고 실행하세요.

### 레포지토리 클론

```bash
git clone https://github.com/yourusername/millie.git
cd millie
