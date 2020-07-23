--ddl_work.sql
/*
 * DDL : 테이블 생성(제약조건), 구조변경, 테이블 삭제
 *  - 자동 커밋(Auto Commit) : 실행시키는 즉시 알아서 반영됨(DML의 경우 사용자는 일일히 commit 해야됨)
 */





-- 의사컬럼 (rownum, rowid) : 가짜 컬럼
select * from emp; -- 14 row

-- 로넘으로 레코드 순번을 넣음으로써 필요한 양까지만 추출한 와꾸
SELECT ROWNUM, EMPNO, ENAME, ROWID --(rownum과 rowid는 emp에 없는 상태)
FROM EMP WHERE ROWNUM <=10 ; --(로넘은 걍 행 번호, 로아이디는 고유식별아이디, 해시값 부여)

-- 로넘 : 5~10
SELECT ROWNUM, EMPNO, ENAME, ROWID
FROM EMP WHERE ROWNUM >= 5 and rownum <= 10;
-- 로넘에선 크다는 논리가 안 통함 1~n은 가능하나, n~(n+m)는 불가능하다

-- 특정 범위 행 검색 :  의사컬럼, 서브쿼리
select rnum, empno, ename
from (select empno, ename, rownum as rnum from emp)
where rnum >= 5 and rnum <= 10;
--별칭을 활용하면 가능해진다, 서브쿼리에서 먼저 별칭 적용되게끔 해주면 메인쿼리에서 받아 쓸 수 있다.


--2. 실수형 데이터 저장 테이블
drop table emp01 purge;

CREATE TABLE EMP01(
EMPNO NUMBER(4),
ENAME VARCHAR2(20),
SAL NUMBER(7, 2)); --(전체, 소숫점)

Insert into emp01 values(1, '홍길동', 1234.1);
Insert into emp01 values(2, '이순신', 1234.123); -- 짤린다
Insert into emp01 values(3, '강감찬', 1234.125); -- 반올림
Insert into emp01 values(4, '홍길동', 123456.12345); --안들어가짐 : 8자리
Insert into emp01 values(5, '김스팸', 1234567);

select * from emp01


--3.서브쿼리를 이용 테이블 생성
create table EMP02   --메인쿼리
as
select * from emp; --서브

select * from emp02; -- 내용 + 구조 복제

-- 특정 컬럼 + 내용 복제
create table emp03
as
select empno, ename, sal, comm from emp;

select * from emp03;


create table emp04
as
select empno, ename, sal from emp;
select * from emp04

-- 특정 행 구조 + 내용 복제
CREATE TABLE EMP05
AS
SELECT * FROM EMP
WHERE DEPTNO=10; -- 부서번호 10번만 
select * from emp05;

-- 문) 직책이 매니저만 대상으로 테이블 생성해보셈
Create table emp_test
as
select * from EMP
where job = 'MANAGER';
select * from emp_test;

-- 테이블 구조(스키마) 복제 = 내용은 제외한다
CREATE TABLE EMP06
AS
SELECT * FROM EMP WHERE 1=0; -- 조건식(FALSE) 1=0 개소리를 써놓음오로써 아무것도 안뽑아오게 함 10=20 이렇게해도댐
select * from emp06;

create table dept02
as
select * from dept where 1=0;

select * from dept02;

insert into dept02 values(10, '기획실', '대전')


--4. 제약조건
---1)기본키(primary key) : 중복불가, 널불가
create table test_tab1(
id number(2) primary key, --(컬럼레벨)
name varchar2(30));

create table test_tab2(
id number(2),
name varchar2(30),
primary key(id) --(테이블레벨)
);


insert into test_tab1 values(11, '홍길동');
insert into test_tab1 values(22, '유관순');
insert into test_tab1(name) values('홍길동'); -- 널 값을 넣겟당 - 응 오류 cannot insert null
insert into test_tab1 values(null, '홍길동'); -- 이래도 허용 안됨
--아무튼 아이디는 기본키라 정했기에 널이 안댄다
insert into test_tab1 values(11, '이순신'); -- 응오류, 아이디 기본키라 중복ㄴㄴ함 메세지에서 유니크 제약조건 워딩 나옴

---2)외래키  : 특정 테이블의 기본키를 다른 테이블에서 참조하는 키
----작업절차 : 기본키 테이블을 생성 -> 외래키 테이블 생성

-- 2-1)기본키를 갖는 테이블을 생성함
create table dept_tab(
deptno number(2) primary key,
dname varchar(10) not null,
loc varchar(10) not null
);
--레코드삽입
insert into dept_tab values(10, '기획', '대전');
insert into dept_tab values(20, '총무', '서울');
insert into dept_tab values(30, '판매', '미국');
select * from dept_tab;

-- 2-2)외래키 테이블 생성

drop table emp_tab purge;
create table emp_tab(
empno number(4) primary key,
ename varchar(30),
sal number(7),
deptno number(2) not null,  --다른 테이블의 기본키를 참조하고 싶음
foreign key(deptno) references dept_tab(deptno) -- 외래키를 씀
);

insert into emp_tab values(1111, '홍길동', 1500000,10);
insert into emp_tab values(2222, '이순신', 2500000,20);
insert into emp_tab values(3333, '유관순', 1000000,30);
-- 참조무결성 위배
insert into emp_tab values(4444, '강감찬', 3000000,40); --참조되는 마스터 테이블엔 없는 부서번호라서 오류뜸 딱 이 용도임

--문) 서브쿼리를 이용하여 2222 사번을 갖는 사원의 부서 정보 출력하기
-- 서브(emp_tab), 메인(dept_tab)
select * from dept_tab
where deptno = 
(select deptno from emp_tab where empno=2222);

-- 3. 유일키(unique key)
CREATE TABLE UNI_TAB1 (
DEPTNO NUMBER(2)
CONSTRAINT UNI_TAB_DEPTNO_UK 
UNIQUE, DNAME CHAR(14), LOC CHAR(13)  --null 허용 만약 낫 널을 추가한다면 사실상 기본키가 됨
);

select * from uni_tab1;

insert into uni_tab1 values(11, '영업부', '서울');
insert into uni_tab1 values(22, '기획실', '대전');
insert into uni_tab1(dname, loc) values('영업부', '대전');

insert into uni_tab1 values(22, '기획실', '대전'); --중복땜에 오류


-- 4)not null : 컬럼레벨에서만 가능함
-- 5) check 
CREATE TABLE CK_TAB1 (
DEPTNO NUMBER(2) NOT NULL CHECK (DEPTNO IN (10,20,30,40,50)),
DNAME CHAR(14),
LOC CHAR(13)
);

insert into ck_tab1 values(10, '회계', '서울');
insert into ck_tab1 values(60, '연구부서', '대전'); -- 응안대 check
insert into ck_tab1(dname, loc) values('연구부', '대전'); --응안대 낫널 체크 모두

--5. 테이블 구조 변경(alter table)

--1) 컬럼 추가
select * from emp01;

ALTER TABLE EMP01
ADD(JOB VARCHAR2(9));

-- 기존 내용이 있는 경우! -> 데이터가 없고 형식만 있으면 가능해짐
ALTER TABLE EMP01
ADD(JOB2 VARCHAR2(9) Not null); -- 오류 발생 널값이 못가게 막았으니 안대지

--과제3
select * from dept02;
alter table dept02
add(DMGR varchar(2));

--2)컬럼 수정 : 컬럼명은 못 바꿈, 컬럼의 자료형, 크기, 기본값을 수정함
alter table dept02
modify(DMGR varchar(10));

alter table emp01
modify(job varchar2(30));

alter table dept02
modify(dmgr number(4));
 
--3)컬럼 삭제
ALTER TABLE EMP01
DROP COLUMN JOB;

select * from emp01;

alter table dept02
drop column dmgr;

select * from dept02;

--6. 테이블의 모든 row(레코드) 제거
select * from emp01;
truncate table emp01; -- 내용삭제

--7. 테이블 삭제
drop table emp01;

-- 전체 테이블 목록 확인
select * from tab; -- tab : 의사테이블, 임시파일 확인되었고
purge recyclebin;










