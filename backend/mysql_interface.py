import mysql.connector
class MysqlInterface:
    def __init__(self) -> None:
        self.conn = mysql.connector.connect(
            host="localhost",  # 数据库主机地址
            user="root",  # 用户名
            password="Zx20020720",  # 密码
            database="hospital_info"  # 数据库名称
        )

        # 创建游标对象
        self.cursor = self.conn.cursor()

    def create_patient(self, id: int, name: str, gender: str, telnumber: str, age: int):
        sql = '''INSERT INTO PatientInfo (ID, Name, Gender, ContactNumber, Age)
                VALUES (%s, %s, %s, %s, %s)'''
        values = (id, name, gender, telnumber, age)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("病人记录创建成功，ID = {}".format(id))

    def retrieve_patient(self, id: int) -> tuple:
        sql = "SELECT * FROM PatientInfo WHERE ID = %s"
        self.cursor.execute(sql, (id,))
        patient = self.cursor.fetchone()
        if patient:
            return patient
        else:
            return None

    def update_patient(self, id: int, updated_data: dict):
        sql = '''UPDATE PatientInfo SET Name=%s, Gender=%s, ContactNumber=%s, Age=%s
                 WHERE ID = %s'''
        values = (updated_data.get('name'), updated_data.get('gender'), updated_data.get('telnumber'), updated_data.get('age'), id)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("病人记录更新成功，ID = {}".format(id))

    def delete_patient(self, id: int):
        sql = "DELETE FROM PatientInfo WHERE ID = %s"
        self.cursor.execute(sql, (id,))
        self.conn.commit()
        print("病人记录删除成功，ID = {}".format(id))

    def create_doctor(self, id: int, name: str, gender: str, telnumber: str, email: str, address: str, department: str):
        sql = '''INSERT INTO DoctorInfo (ID, Name, Gender, ContactNumber, Email, Address, Department)
                VALUES (%s, %s, %s, %s, %s, %s, %s)'''
        values = (id, name, gender, telnumber, email, address, department)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("医生记录创建成功，ID = {}".format(id))

    def retrieve_doctor(self, id: int) -> tuple:
        sql = "SELECT * FROM DoctorInfo WHERE ID = %s"
        self.cursor.execute(sql, (id,))
        doctor = self.cursor.fetchone()
        if doctor:
            return doctor
        else:
            return None

    def update_doctor(self, id: int, updated_data: dict):
        sql = '''UPDATE DoctorInfo SET Name=%s, Gender=%s, ContactNumber=%s, Email=%s, Address=%s, Department=%s
                 WHERE ID = %s'''
        values = (updated_data.get('name'), updated_data.get('gender'), updated_data.get('telnumber'),
                  updated_data.get('email'), updated_data.get('address'), updated_data.get('department'), id)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("医生记录更新成功，ID = {}".format(id))

    def delete_doctor(self, id: int):
        sql = "DELETE FROM DoctorInfo WHERE ID = %s"
        self.cursor.execute(sql, (id,))
        self.conn.commit()
        print("医生记录删除成功，ID = {}".format(id))


# # 使用示例
# mysql_interface = MysqlInterface()

# # 创建病人记录
# mysql_interface.create_patient(1, "张三", "男", "1234567890", 30)

# # 查询病人记录
# patient = mysql_interface.retrieve_patient(1)
# if patient:
#     print("病人ID:", patient[0])
#     print("姓名:", patient[1])
#     print("性别:", patient[2])
#     print("联系电话:", patient[3])
#     print("年龄:", patient[4])
# else:
#     print("找不到病人记录")

# # 更新病人记录
# mysql_interface.update_patient(1, {"name": "李四", "gender": "女", "telnumber": "9876543210", "age": 35})

# # 删除病人记录
# mysql_interface.delete_patient(1)

# # 创建医生记录
# mysql_interface.create_doctor(1, "王医生", "男", "1234567890", "wang@example.com", "北京市", "内科")

# # 查询医生记录
# doctor = mysql_interface.retrieve_doctor(1)
# if doctor:
#     print("医生ID:", doctor[0])
#     print("姓名:", doctor[1])
