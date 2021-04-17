import sqlite3
conn=sqlite3.connect("medDB.db")
print("Связь с БД установлена")

conn.execute("Drop table if EXISTS PATIENT")
conn.execute("Drop table if EXISTS CONTACT_NO")
conn.execute("Drop table if EXISTS ROOM")
conn.execute("Drop table if EXISTS ANALYZES")
conn.execute("Drop table if EXISTS MEDICINE")

conn.execute("""Create table PATIENT
                (PATIENT_ID int(10) primary key,
                NAME VARCHAR(20) not null,
                SEX varchar(10) not null,
                BLOOD_GROUP varchar(5) not null,
                DOB date not null,
                ADDRESS varchar(100) not null,
                CONSULT_TEAM varchar(50) not null,
                EMAIL varchar(20) not null
             )""")
print("Таблица ПАЦИЕНТ успешно создана")

conn.execute("""CREATE TABLE CONTACT_NO
                 (PATIENT_ID int(10) PRIMARY KEY,
                 CONTACTNO int(15) not null,
                 ALT_CONTACT int(15),
                 FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID));
            """)
print("Таблица КОНТАКТНЫЙ НОМЕР успешно создана")

conn.execute("""Create table ROOM
                 (PATIENT_ID int(10)not NULL ,
                 ROOM_NO varchar(20) PRIMARY KEY ,
                 ROOM_TYPE varchar(10) not null,
                 RATE int(10) not null,
                 DATE_ADMITTED date,
                 DATE_DISCHARGED date NULL,
                 FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID));
            """)
print("Таблица КОМНАТА успешно создана")

conn.execute("""CREATE TABLE ANALYZES
                 (PATIENT_ID int(10) primary key,
                 AN_DATE date,
                 AN_NAME varchar(15) not null,
                 AN_COST int(10) not null,
                 AN_STATUS varchar(15) not null,
                 FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID));
             """)
print("Таблица АНАЛИЗЫ успешно создана")

conn.execute("""CREATE TABLE employee
                (EMP_ID varchar(10) primary key,
                 EMP_NAME varchar(20)not null,
                 SEX varchar(10) not null,
                 AGE int(5) not null,
                 DESIG varchar(20) not null,
                 SAL float(10) not null,
                 EXP varchar(100) not null,
                 EMAIL varchar(20) not null,
                 PHONE int(12));
            """)

print("Таблица РАБОТНИК успешно создана")

conn.execute("DROP TABLE if EXISTS appointment")
conn.execute("""CREATE TABLE appointment
                (
                 PATIENT_ID int(20) not null,
                 EMP_ID varchar(10) not null,
                 AP_NO varchar(10) primary key,
                 AP_TIME time,
                 AP_DATE date,
                 description varchar(100),
                 foreign key(PATIENT_ID) references patient(PATIENT_ID),
                 foreign key(EMP_ID) references doctor(EMP_ID));
             """)

print("Таблица ПАЛАТА успешно создана")