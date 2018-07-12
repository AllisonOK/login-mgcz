

import pymysql
phone=18843695827
def sms_code(phone):
    connection = pymysql.connect(
        host="101.132.106.107",

        port=3306,

        user="lidawei",

        password="G1EoqS$7Jgf9l6!a",

        db="mgcz",

        charset="utf8")

    try:

        with connection.cursor() as cursor:
            sql = 'SELECT verification_code FROM mgcz_ucenter.uc_sms_verification where status=1 and mobile=' + str(phone)
            cout = cursor.execute(sql)
            results = cursor.fetchall()
            results1 = str(results)
            print(results1.strip("(',)"))
            return results1.strip("(',)")
            connection.commit()

    finally:

        connection.close()

sms_code(phone)