# # dummy_generater.py
# # !/usr/local/bin/python3

# #########################################
# #        python 3.11.4
# #########################################



from sqlalchemy import create_engine, Table, MetaData, insert, delete, text, exc
from faker import Faker

# 시간 포맷 처리를 위한 라이브러리
import time

# 정규식 처리를 위한 라이브러리
import re

# 랜덤처리용 라이브러리
import random

# json 파일 가져오기
import json

SQL_URL = 'mysql+pymysql://root:151227@localhost:3306/airportdb'
engine = create_engine(SQL_URL, echo=True)
metadata_obj = MetaData()


# tableName : 테이블명 
# insertCnt : 인서트 할 숫자
# deleteYn  : 인서트 시작 전 기존 데이터 삭제 여부 (Y or N)
def insertDummyData(tableName, insertCnt, deleteYn):
    
    # Get Table Description info
    desc = getTableDesc(tableName)
    
    if desc is None:
        print("Target table is not exist. Please Try again.")
        return
    
    # 테이블별 최대로 들어갈 수 있는 row 수를 초과하는 경우 리턴
    if tableName == "airline" and insertCnt > 1332:
        print("airline 테이블에는 1332 개의 행 이상 인서트할 수 없습니다.")
    
    # get column info from table description
    columns = descToCloumns(desc)


    if deleteYn.upper() == 'Y':
        # delete table
        deleteTable(tableName)
    

    
    # data insert start
    success = 0;
    table = Table(tableName, metadata_obj, autoload_with=engine)
    while True:
        if(success == insertCnt):
            break
        
        # make dummy data list
        dummy = getDummyData(columns)
                
        try:
            stmt = insert(table).values(dummy)
            with engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
            success += 1
            print("insert in process :: success count :: " + str(success))
        except exc.IntegrityError as e:
            print("쿼리 실행 오륲가 발생했습니다:", e)
        except Exception as e:
            print("알 수 없는 오류가 발생했습니다.", e)
            break


        
    
# stmt = insert(airline).values(iata="99", airlinename="chanhoe2", base_airport="45")
# print(stmt)

def descToCloumns(list):
    columns = []
    for row in list:
        columns.append({"name":row[0], "type":getType(row[1]), "length":getLength(row[1]), "unique":isUnique(row[3]), "autoIncrement":isAutoIncrement(row[5])})
    return columns
        
        
# get column type
def getType(str):
    if str.startswith("char") or str.startswith("varchar"):
        return "string"
    
    if str.startswith("int") or str.startswith("smallint") or str.startswith("mediumint") :
        return "int"
    
    if str.startswith("decimal"):
        return "decimal"
    
    if str.startswith("tinyint"):
        return "tinyint"
    
    if str.startswith("enum"):
        return "enum"
    
    return str
        

# get maximun length
def getLength(str):
    # enum 인 경우 스킵
    if str.startswith("enum"):
        return
    
    # char(2) 인 경우 2를, 
    # decimal(5,3) 인 경우 [5,3] 을 리턴
    if "(" in str and ")" in str:
        # 괄호 안의 문자열 추출
        extracted = str[str.index("(")+1:str.index(")")]
        # 쉼표를 기준으로 문자열을 나누고 숫자로 변환하여 리스트로 저장
        numbers = [int(num) for num in extracted.split(",")]
        # 숫자가 하나만 있는 경우 리스트로 감싸지 않고 숫자만 반환
        if len(numbers) == 1:
            return numbers[0]
        return numbers
    return

# check if the column is unique
def isUnique(str):
    if(str == "PRI" or str == "UNI"):
        return True
    return False

# check if the column is auto increment
def isAutoIncrement(str):
    if(str == "auto_increment"):
        return True
    return False

# get table description
def getTableDesc(tableName):

    query = "DESC " + tableName;

    try:
        with engine.connect() as conn:
            return conn.execute(text(query))   
    except:
        # exception occur when the table is not exist
        return None
    
    
def deleteTable(tableName):
    query = "DELETE FROM " + tableName
    try:    
        with engine.connect() as conn:
            conn.execute(text(query))
            conn.commit()
            print("Delete table success.")
    except Exception as e:
        print("Delete table fail ", e)
        

# 더미데이터를 생성
def getDummyData(columns):
    fake = Faker()
    row = {};
    
    for column in columns :
        type = column["type"]
        columnName = column["name"]
        maxLength = column["length"]
        data = ""
        
        # auto increment 인 경우 인서트시 테이블내에서 자동증가하므로 굳이 데이터를 만들지 않음
        if column["autoIncrement"] :
            continue
        
    
        # 컬럼 타입에 따른 더미데이터 생성
        if type == "int":
            data = fake.random_int(min=1, max=32000) # smallint 인 경우 32767 까지 저장가능하므로 편의상 max = 32000
            
        if type == "decimal":
            if columnName == "latitude" or columnName == "longitude":
                data = callFakerMethodOfColumnName(columnName)
            else :
                data = fake.pydecimal(maxLength[0]- maxLength[1], maxLength[1], positive=True) # 소수점 자릿수를 합산하여 decimal 형식으로 변환
            
        if type == "string":
            # faker 라이브러리에 컬럼명과 일치하는 함수가 있을 경우 해당 함수를 호출
            # 예) zipcode 등
            data = callFakerMethodOfColumnName(columnName)
            if data == "":
                len = random.randint(1,maxLength)
                strFormat = ""
                for i in range(len):
                    strFormat += "?" # strFormat 의 ? 길이만큼 데이터 자릿수가 결정됨
                data = fake.bothify(text=strFormat, letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
                
        if type == "date":
            data = fake.date()
        
        if type == "datetime":
            data = fake.date_time()
            # date = datetime.datetime(2015, 11, 8, 0, 47, 6, 804878) 
            
            # DATETIME 형식의 문자열로 변환
            data = data.strftime('%Y-%m-%d %H:%M:%S')
            
        if type == "enum":
            # 컬럼형식이 enum 인 경우 테이블에 정의된 값 중 하나를 선택하여 인서트하도록 함
            if columnName == "department":
                data = random.choice(['Marketing', 'Buchhaltung', 'Management', 'Logistik', 'Flugfeld'])
            if columnName == "weather":
                data = random.choice(['Nebel-Schneefall','Schneefall','Regen','Regen-Schneefall','Nebel-Regen','Nebel-Regen-Gewitter','Gewitter','Nebel','Regen-Gewitter'])
                
        if type == "text":
            len = random.randint(1,200)
            strFormat = ""
            for i in range(len):
                strFormat += "?"
            data = fake.bothify(text=strFormat, letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            
        if type == "time":
            data = fake.time()
            
        if type == "tinyint":
            data = random.randint(0, 1)
    
        row[columnName] = data
        
    return row
    
    

# faker 라이브러리에 컬럼명과 같은 메소드가 있는경우 실행
# 일치하는게 없거나 callabe 객체 가 아닌 경우 error 처리로 빈 스트링 문자열 리턴
def callFakerMethodOfColumnName(columnName):
    try :
        fake = Faker()
        return getattr(fake, columnName)();
    except Exception as e:
        return "";
    
    
with open("insert.json","r") as json_file:
    data = json.load(json_file)
        

for row in data :
    insertDummyData(row['table_name'], row['insert_count'],row['delete_existing'])




