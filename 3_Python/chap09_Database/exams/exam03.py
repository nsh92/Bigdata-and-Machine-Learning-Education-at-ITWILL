'''
문제3) 다음과 같은 메뉴를 이용하여 goods 테이블을 관리하시오.
    [레코드 처리 메뉴 ]
1. 레코드 조회
2. 레코드 추가
3. 레코드 수정
4. 레코드 삭제
5. 프로그램 종료
    메뉴번호 입력 :
'''
import pymysql

config = {
    'host': '127.0.0.1',
    'user': 'scott',
    'password': 'tiger',
    'database': 'work',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True}

try:
    # db 연결 객체 생성
    conn = pymysql.connect(**config)
    # SQL 실행 객체 생성
    cursor = conn.cursor()

    while True:  # 무한루프
        print('\t[레코드 처리 메뉴 ]')
        print('1. 레코드 조회')
        print('2. 레코드 추가')
        print('3. 레코드 수정')
        print('4. 레코드 삭제')
        print('5. 프로그램 종료')
        menu = int(input('\t메뉴번호 입력 : '))

        if menu == 1:  # 레코드 조회
            print('조회 메뉴 세부 선택')
            seboo = int(input("1. 전체 조회, 2. 상품명으로 조회, 3. 상품코드로 조회"))
            if seboo == 1:
                sql = "select * from goods"
                cursor.execute(sql)
                data = cursor.fetchall()
                for row in data:
                    print(row[0], row[1], row[2], row[3])
                print('전체 레코드 수 :', len(data))
            elif seboo == 2:
                name = input("조회 상품명 입력 :")
                sql = f"select * from goods where name like '%{name}%'"
                cursor.execute(sql)
                data2 = cursor.fetchall()
                if data2:
                    for row in data2:
                        print(row)
                else:
                    print('조회 상품 없음')
            elif seboo == 3:
                code = int(input("조회 코드 입력 :"))
                sql = f"select * from goods where code = {code}"
                cursor.execute(sql)
                row = cursor.fetchone()
                if row:
                    print(row)
                else:
                    print('조회 코드 없음')
            else:
                print('코드를 제대로 누르세요')

        elif menu == 2:  # 2. 레코드 추가
            code = int(input("code :"))
            name = input("name :")
            su = int(input("su :"))
            dan = int(input("dan :"))
            sql = f"insert into goods values({code}, '{name}', {su}, {dan})"  # name에 ''표시 강조
            cursor.execute(sql)
            conn.commit()
            print("레코드 추가 완료")

        elif menu == 3:  # 3. 레코드 수정
            code = int(input("수정 code :"))
            su = int(input("수정 su :"))
            dan = int(input("수정 dan :"))
            sql = f"update goods set su = {su}, dan = {dan} where code = {code}"
            cursor.execute(sql)
            conn.commit()
            print("레코드 수정 완료")

        elif menu == 4:  # 4. 레코드 삭제
            code = int(input("삭제 code :"))
            cursor.execute(f"select * from goods where code = {code}")
            row = cursor.fetchone()
            if row:
                cursor.execute(f"delete from goods where code = {code}")
                conn.commit()
            else:
                print('해당 코드 없음')
            print("레코드 삭제 완료")

        elif menu == 5:
            print('프로그램 종료')
            break  # 반복 exit
        else:
            print('해당 메뉴는 없습니다.')

# DB 연결 예외 처리
except Exception as e:
    print('db 연동 오류 : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
