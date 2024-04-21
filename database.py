# # # database.py
# # # !/usr/local/bin/python3

# # #########################################
# # #        python 3.11.4
# # #########################################


# #엔진과 세션 만들어주는 SQLAlchemy 사용에 기본적인 부분입니다
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# # 이미 만들어진 데이터베이스의 테이블을 사용하는데 필요한 부분입니다.
# from sqlalchemy import Table, MetaData
# from sqlalchemy import insert, delete
# from sqlalchemy import text

# import yeri

# # 정규식 처리를 위한 라이브러리
# import re

# SQL_URL = 'mysql+pymysql://root:151227@localhost:3306/airportdb'
# engine = create_engine(SQL_URL, echo=True)

# with engine.connect() as conn:
#     result = conn.execute(text("DESC airline"))
#     print(result.all())

# metadata_obj = MetaData()

# print(metadata_obj.reflect(engine))

# temp = ()
# stmt = insert(airline).values(iata="99", airlinename="chanhoe2", base_airport="45")
# print(stmt)
      
# airline = {
#     "table" : Table("airline", metadata_obj, autoload_with=engine)
#     ,"columns" : [
#         {"name":"airline_id", "type":"int", "length":"", "unique":True}
#         ,{"name":"iata", "type":"string", "length":"2", "unique":True}
#         ,{"name":"airlinename", "type":"string", "length":"30", "unique":False}
#         ,{"name":"base_airport", "type":"int", "length":"", "unique":False}
#     ]
# }      

# airplane = {
#     "table" : Table("airplane", metadata_obj, autoload_with=engine)
#     ,"columns" : [
#         {"name":"airline_id", "type":"int", "length":"", "unique":True}
#         ,{"name":"capacity", "type":"int", "length":"", "unique":False}
#         ,{"name":"type_id", "type":"int", "length":"", "unique":False}
#         ,{"name":"airline_id", "type":"int", "length":"", "unique":False}
#     ]
# }

# airplane_type = {
#     "table" : Table("airplane_type", metadata_obj, autoload_with=engine)
#     ,"columns" : [
#         {"name":"type_id", "type":"int", "length":"", "unique":True}
#         ,{"name":"identifier", "type":"string", "length":"50", "unique":False}
#         ,{"name":"description", "type":"string", "length":"200", "unique":False}
#     ]
# }

# airport = {
#     "table" : Table("airport", metadata_obj, autoload_with=engine)
#     ,"columns" : [
#         {"name":"airport_id", "type":"int", "length":"", "unique":True}
#         ,{"name":"iata", "type":"string", "length":"3", "unique":True}
#         ,{"name":"icao", "type":"string", "length":"4", "unique":False}
#         ,{"name":"name", "type":"string", "length":"50", "unique":False}
#     ]
# }

# airport_geo = {
#     "table" : Table("airport_geo", metadata_obj, autoload_with=engine)
#     ,"columns" : [
#         {"name":"airport_id", "type":"int", "length":"", "unique":True}
#         ,{"name":"name", "type":"string", "length":"3", "unique":True}
#         ,{"name":"city", "type":"string", "length":"4", "unique":False}
#         ,{"name":"country", "type":"string", "length":"50", "unique":False}
#         ,{"name":"latitude", "type":"string", "length":"11", "unique":False}
#         ,{"name":"longitude", "type":"string", "length":"11", "unique":False}
#     ]
# }

# airport_reachable = {
#     "table" : Table("airport_reachable", metadata_obj, autoload_with=engine)
#     ,"columns" : [
#         {"name":"airport_id", "type":"int", "length":"", "unique":True}
#         ,{"name":"hops", "type":"int", "length":"", "unique":True}
#     ]
# }

# booking = {
#     "table" : Table("airport_reachable", metadata_obj, autoload_with=engine)
#     ,"columns" : [
#         {"name":"airport_id", "type":"int", "length":"", "unique":True}
#         ,{"name":"hops", "type":"int", "length":"", "unique":True}
#     ]
# }

# airline = Table("airline", metadata_obj, autoload_with=engine);
# airplane = Table("airplane", metadata_obj, autoload_with=engine);
# airplane_type = Table("airplane_type", metadata_obj, autoload_with=engine);
# airport = Table("airport", metadata_obj, autoload_with=engine);
# airport_geo = Table("airport_geo", metadata_obj, autoload_with=engine);
# airport_reachable = Table("airport_reachable", metadata_obj, autoload_with=engine);
# booking = Table("booking", metadata_obj, autoload_with=engine);
# employee = Table("employee", metadata_obj, autoload_with=engine);
# flight = Table("flight", metadata_obj, autoload_with=engine);
# flight_log = Table("flight_log", metadata_obj, autoload_with=engine);
# flightschedule = Table("flightschedule", metadata_obj, autoload_with=engine);
# passenger = Table("passenger", metadata_obj, autoload_with=engine);
# passengerdetails = Table("passengerdetails", metadata_obj, autoload_with=engine);
# weatherdata = Table("weatherdata", metadata_obj, autoload_with=engine);

# # stmt = insert(airline).values(iata="99", airlinename="chanhoe2", base_airport="45")
# # print(stmt)

# # with engine.connect() as conn:
# #     result = conn.execute(stmt)
# #     conn.commit()
    
