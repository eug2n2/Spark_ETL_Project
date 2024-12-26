## 🌟 PySpark와 MySQL을 활용한 ETL 파이프라인 구축
이 프로젝트는 PySpark를 사용하여 환경 데이터를 처리하고, 변환(Transform), 로드(Load)하는 ETL 파이프라인을 구현한 예제입니다.
데이터를 정리하고 지역별 통계를 분석하며, Docker로 Spark와 MySQL 환경을 컨테이너화하여 실행할 수 있습니다.

📌 ETL 프로젝트 특징
📥 Extract: pandas를 활용해 CSV 데이터를 불러옵니다.
🛠 Transform:
날짜와 시간을 하나의 컬럼으로 변환합니다.
결측치 데이터를 평균값으로 채워 데이터 품질을 향상시킵니다.
데이터를 숫자형으로 변환하여 분석이 용이하도록 처리합니다.
📊 Load:
PySpark를 사용해 지역별 평균 기온과 재비산먼지 농도를 계산합니다.
Spark DataFrame에서 집계 결과를 출력합니다.

🐳 Docker 환경: Spark와 MySQL을 컨테이너에서 실행할 수 있는 docker-compose.yml 제공.
📂 디렉토리 구조
```
.  
├── data/                      # 데이터 파일 디렉토리  
│   └── 한국환경공단_도로 재비산먼지 측정 정보_20241130.csv  
├── docker-compose.yml         # Docker 설정 파일  
├── etl_pipeline.py            # ETL 파이프라인 Python 코드  
└── README.md                  # 프로젝트 설명 파일 (현재 파일)
```  
⚙️ 설치 및 실행
1️⃣ 환경 구축
Docker, Docker Compose, Python, PySpark를 설치

2️⃣ 데이터 준비
https://www.data.go.kr/tcs/dss/selectFileDataDetailView.do?publicDataPk=15021888

한국환경공단_도로 재비산먼지 측정 정보를 사용하였습니다. 한국환경공단_도로 재비산먼지 측정 정보는 특수제작한 이동측정차량으로 주행하는 차량의 타이어(휠)와 도로면의 마찰에 의해서 재비산되는 먼지(PM10)를 측정한 월간 평균 자료입니다. 

3️⃣ Docker 컨테이너 실행

4️⃣ ETL 코드 실행

🐳 Docker 설정
docker-compose.yml 설명
Spark Master: Spark 클러스터의 마스터 노드 역할을 합니다.
Spark Worker: Spark 작업을 수행하는 워커 노드입니다.
MySQL Database: ETL 결과를 저장하거나 다른 데이터 작업을 위한 데이터베이스 역할을 합니다.

💻 Spark 실행 화면 예시
Spark에서 집계된 지역별 데이터를 출력한 예시:

```
+--------+--------------------+-----------------------+  
| 지역   |avg(재비산먼지 평균농도)|       avg(기온)       |  
+--------+--------------------+-----------------------+  
| 전북   |            34.3     |             16.45    |
| 충북   |  27.62857142857143  |  13.914285714285715  |  
+--------+------------------+-----------------------+  
```
🔗 참고 자료
PySpark 공식 문서
Docker Compose 공식 문서
