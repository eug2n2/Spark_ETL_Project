import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def create_spark_session():
    spark = SparkSession.builder \
        .appName("ETL Pipeline Example") \
        .getOrCreate()
    return spark

def extract_data(file_path):
    df = pd.read_csv(file_path, encoding='euc-kr')
    # print("원본 데이터 출력:")
    # print(df.head())
    return df

def transform_data(df):
    df['측정일시'] = pd.to_datetime(df['측정일자'] + ' ' + df['측정시간'])
    df = df.drop(['측정일자', '측정시간'], axis=1)
    
    df['기온'] = pd.to_numeric(df['기온'], errors='coerce')
    df['습도'] = pd.to_numeric(df['습도'], errors='coerce')
    df['재비산먼지 평균농도'] = pd.to_numeric(df['재비산먼지 평균농도'], errors='coerce')

    # 결측치는 평균 대체
    df['기온'].fillna(df['기온'].mean(), inplace=True)
    df['습도'].fillna(df['습도'].mean(), inplace=True)
    df['재비산먼지 평균농도'].fillna(df['재비산먼지 평균농도'].mean(), inplace=True)
    
    print("전처리된 데이터 출력:")
    print(df.head())
    return df

def load_data(df, spark):
    # pandas DataFrame을 Spark DataFrame으로 변환
    spark_df = spark.createDataFrame(df)
    
    # 지역별 평균 기온 계산 (Spark에서 그룹화하여 집계)
    region_summary = spark_df.groupBy('지역').agg(
        {'기온': 'avg', '재비산먼지 평균농도': 'avg'}
    )
    print("지역별 정보")
    region_summary.show()

    return region_summary

def main():
    # 파일 경로 설정
    file_path = 'data/한국환경공단_도로 재비산먼지 측정 정보_20241130.csv'
    
    # Spark 세션 생성
    spark = create_spark_session()

    # ETL 파이프라인 실행
    df = extract_data(file_path)
    transformed_df = transform_data(df)
    load_data(transformed_df, spark)

if __name__ == "__main__":
    main()