-- dml_work.sql
/*
 * DML : Select, Insert, Delete, Update
 *  commit 대상 : Insert, Delete, Update
 *          -> 기본 쿼리 실습
 *          -> 서브쿼리 실습
 *  Select는 커밋이 필요 없다, 알아서 DB에 반영한다
 *  Commit : 작업 내용을 DB에 반영
 */


--테이블 생성
drop table dept01 purge;
CREATE TABLE DEPT01(
DEPTNO NUMBER(4),
DNAME VARCHAR2(30),
LOC VARCHAR2(20)
);

-- 1. 레코드 삽입
INSERT INTO DEPT01
(DEPTNO, DNAME, LOC)
VALUES(10, 'ACCOUNTING', 'NEW YORK');

select * from dept01;

-- 전체 칼럼 입력 시 -> 칼럼명 생략 가
Insert into dept01 values(20,'REARSEARCH','DALLAS');

create table sam01
as 
(select EMPNO, ENAME, JOB, SAL from emp where 1=0); 

select * from sam01;

Insert into sam01 values(1000,'APPLE','POLICE',10000);
Insert into sam01 values(1010,'BANANA','NURSE',15000);
Insert into sam01 values(1020,'ORANGE','DOCTOR',25000);


-- NULL입력
--1)암시적 입력
INSERT INTO DEPT01
(DEPTNO, DNAME) --loc까지 써야대는대 생략함
VALUES (30, 'SALES');

--2)명시적 입력
INSERT INTO DEPT01
VALUES (40, 'OPERATIONS', NULL);

select * from dept01;


Insert into sam01(empno, ename, sal) values(1030, 'VERY', 25000);
Insert into sam01 values(1040, 'CAT', null, 2000);

-- 서브쿼리를 이용한 레코드 삽임
-- 1) 먼저 테이블을 준비
drop table dept02 purge;

create table dept02
as
select * from dept where 1=0;
select * from dept02

-- 2) 준비된 테이블에 레코드를 삽입하라 서브쿼리 이용해서
Insert into dept02 --as없음을 주목
select * from dept;

select * from emp;

Insert into sam01
select empno, ename, job, sal from emp where deptno=10;

select * from sam01

--2. 다중행 테이블에 다중 행 삽입하기
--1)테이블 2개 준비
create table emp_HIR
as
select EMPNO, ENAME, HIREDATE from emp where 1=0;

create table emp_MGR
as
select EMPNO, ENAME, MGR from emp where 1=0;

--2) 다중 테이블에 다중 행 삽입하기
INSERT ALL
INTO EMP_HIR VALUES(EMPNO, ENAME, HIREDATE)
INTO EMP_MGR VALUES(EMPNO, ENAME, MGR)
SELECT EMPNO, ENAME, HIREDATE, MGR
FROM EMP
WHERE DEPTNO=20;

select * from emp_hir;
select * from emp_mgr;

-- 3. Update
select * from emp01;
create table emp01
as
select * from emp;

-- 기본 쿼리문 : 레코드 수정
UPDATE EMP01 SET DEPTNO=30; -- 전체 레코드 대상이 돼버렸음
-- 전체 사원 급여 10% 인상
UPDATE EMP01 SET SAL = SAL * 1.1 where deptno = 30;
-- 입사년도 수정
update emp01 set hiredate = sysdate;


--where 이용 특정 행만 업데이트
update emp01 set sal = sal * 1.1 where sal <= 2000;


-- 특정 입사년도에 입사한 사람들만 연도 수정
UPDATE EMP01
SET HIREDATE = SYSDATE
WHERE SUBSTR(HIREDATE, 1, 2)='87';
--87년도에 입사한 양반들만 sysdate로 수정하라는거

--SAM01 테이블에 저장된 사원 중 급여가 10000 이상인
--사원들의 급여만 5000원씩 삭감하시오.

update sam01
set sal = sal + 5000
where sal > 10000;

select * from sam01;


--2개 이상 컬럼 수정 (부서번호와 직책)
UPDATE EMP01
SET DEPTNO=20, JOB='MANAGER' --(콤마로 구분)
WHERE ENAME='SCOTT'; 

select * from EMP01

--서브쿼리 이용 업데이트
UPDATE DEPT01
SET LOC=(SELECT LOC
FROM DEPT01
WHERE DEPTNO=10)
WHERE DEPTNO=20;

select * from DEPT01

create table sam02
as
(select ename, sal, hiredate, deptno from emp);

select * from sam02

update sam02
set sal = sal + 1000
where deptno = 
(select deptno from dept where loc ='DALLAS');


select * from sam02

-- 서브쿼리로 두 개 이상 칼럼 수정
UPDATE DEPT01
SET (DNAME, LOC)=(SELECT DNAME, LOC
FROM DEPT01
WHERE DEPTNO=10)
WHERE DEPTNO=40;


select * from emp;

update sam02
set (sal, hiredate)=
(select sal, hiredate from emp
where ename = 'KING');


select * from sam02

select * from emp01;
delete from emp01;
where comm is not null;


--얘도 서브쿼리 잘지정하면 더 복잡하게할수잇다



