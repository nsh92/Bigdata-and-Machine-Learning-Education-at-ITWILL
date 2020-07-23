-- 1. 숫자 처리 함수


-- 1) abs
select -10, abs(-10) from dual;

-- 2) round 반올림베이비
select 12.345, round(12.345, 2) from dual;

select 34.5678, round(34.5678, -1) from dual; --1의 자리 반올림, -2는 10의 자리 반올림

-- 3) mod : 나머지 값 (if(num % 2) ==0)
select mod(10,2), mod(27,2) from dual;
select * from professor where mod(deptno, 2)=0;
--deptno가  짝수의 경우를 찾아냈음

---사번이 홀수인 새끼를 찾아보자 emp
select * from emp
select * from emp where mod(empno, 2)=1;
--or
select * from emp where mod(empno, 2)!=0; --0과 같지 않은

-- 2. 문자처리 함수
-- 1) upper : 대문자로 바꿔줌, 원래 대문자는 그대로 유지
SELECT 'Welcome to Oracle', UPPER('Welcome to Oracle') FROM DUAL;

-- 2) lower : 소문자로 바꿔줌, 원래 소문자는 유지
SELECT 'Welcome to Oracle', LOWER('Welcome to Oracle') FROM DUAL;

-- 3) Initcap : 단어의 첫자 대문자
SELECT 'WELCOME TO ORACLE', INITCAP('WELCOME TO ORACLE') FROM DUAL;

-- 실습 2번
SELECT EMPNO, ENAME, JOB
FROM EMP
WHERE JOB='manager';
-- 안 보인다
SELECT EMPNO, ENAME, JOB
FROM EMP
where job = upper('manager'); --이렇게 해야 보인다

-- 4) Length / LengthB
select * from emp;
select ename, length(ename), lengthb(ename) from emp;
select NAME, length(NAME), lengthb(NAME)from student;

select * from student;

-- 5) SUBSTR 서브스트링 : 특정한 문자, 구간을 추출함
Select Substr('Welcome to Oracle', 4, 3) from dual;
Select Substr('191020-1234567', 3, 2) from dual;

-- 10월생 추출해보자 student

select name, birthday, substr(birthday, 4, 2) from student -- 연도에서 앞의 두자리는 생략되어있는 상태임
-- 더하여 조건절로도 활용 가능
where substr (birthday, 4, 2)=10; --10월생 조회하겠따

-- 실습 3번
select empno, job, mgr, hiredate, sal, comm, deptno from emp
where substr(hiredate, 4, 2) = 09;

-- 6) Trim / LTrim / RTrim : 공백을 제거한다, 앞, 뒤의 공백 (중간 공백은 못 함)
SELECT LTRIM(' Oracle ') FROM DUAL; -- 앞부분 공백
SELECT RTRIM(' Oracle ') FROM DUAL; -- 뒷부분 공백
SELECT TRIM(' Oracle ') FROM DUAL; -- 앞뒤공백

-- 3. 날짜처리 함수

-- 1) sysdate
select sysdate from dual;

-- 2) Add_Months
-- 형식) Add_Months(컬럼명, 월수)
select hiredate, add_months(hiredate, 12) from professor;

-- 3) Next_Day
SELECT SYSDATE, NEXT_DAY(SYSDATE, '수요일')
FROM DUAL;


-- 4. 형 변환 함수
/*
 * 기존에 있던 자료형을 다른 자료형으로 바꾼다
 * to_char() : 날짜, 숫자 -> 문자형
 * to_date() : 날짜형으로 바꾼다
 * to_number() : 숫자로 바꾼다
 */

---1)to_char(컬럼명, 'format')
SELECT SYSDATE, TO_CHAR(SYSDATE, 'YYYY-MM-DD') FROM DUAL;
SELECT SYSDATE, TO_CHAR(SYSDATE, 'YYYY/MM/DD') FROM DUAL; --날짜자료형 --> 문자자료형

SELECT HIREDATE, TO_CHAR (HIREDATE, 'YYYY/MM/DD DAY') FROM EMP;

SELECT TO_CHAR(SYSDATE, 'YYYY/MM/DD, HH24:MI:SS') FROM DUAL;

SELECT ENAME, SAL, TO_CHAR (SAL, 'L999,999') FROM EMP;
SELECT ENAME, SAL, TO_CHAR (SAL, 'L000,999') FROM EMP; -- 아래 위 차이 인지하기

---2)To_date() : date 컬럼 
SELECT ENAME, HIREDATE FROM EMP
WHERE HIREDATE=TO_DATE(19810220,'YYYYMMDD')

---3) To_Number('string', 'format')
select 20000-10000 from dual;
SELECT TO_NUMBER('20,000', '99,999') - TO_NUMBER('10,000', '99,999')
FROM DUAL;

--- 5. Null 처리 함수
/*
 * 1.NVL(컬럼명, 값) : 해당 컬럼명 값이 널이면 뒤에 있는 값으로 대체한다.
 * 2.NVL2(컬럼명, 값1, 값2) : 컬럼명 Null -> 값2, Not Null -> 값1
 */

select name, pay, bonus, nvl2(bonus, bonus*2, 0) from professor where deptno = 101;

-- 6. decode() 함수
--- 형식 : decode(컬럼명, 값, 디코딩내용)
select * from emp
Select ename, deptno, decode(deptno, 10, '기획실',
                                       20, '연구실',
                                       30, '영업부')
from emp;















