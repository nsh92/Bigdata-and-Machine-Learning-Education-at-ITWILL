--subQuery_work.sql

/*
형식1)
 main query  ->2차 실행
 as
 sub query;  ->1차실행

형식2
 main query 관계연산자 (sub query);

*/

-- 형식1
create table dept01 -- 메인
as
select * from dept; -- 서브(먼저실행)

select * from dept01; -- 내용(date) + 구조(desc디스트럭쳐)



--형식2 : main(dept테이블), sub(emp테이블). emp엔 부서이름이 없다

select * from emp;

-- dept와 emp의 table join
select * from dept
where deptno = (select deptno from emp where ename='SCOTT');

--공통의 컬럼이 존재해야한다는 전제

--1. 단일행 서브쿼리 : 서브쿼리가 찾아주는 것이 행 하나


-- 실습1. SCOTT과 같은 부서에서 근무하는 사원의 이름과 부서 번호를 출력하는 SQL 문을 작성해 보시오. (EMP)
-- 메인 : emp, 서브 : emp

main
관계연산자
(sub)

select ename, deptno from emp
where deptno =
(select deptno from emp where ename = 'SCOTT');


-- 실습2. SCOTT와 동일한 직속상관(MGR)을 가진 사원을 출력하는 SQL 문을 작성해 보시오. (EMP)

select * from emp
where MGR =
(select MGR from emp where ename = 'SCOTT'); -- 7566을 찾아내고 넘겨줌

--실습3.SCOTT의 급여와 동일하거나 더 많이 받는 사원 명과 급여를 출력하시오.(EMP)

select * from emp;

select ename, sal from emp
where sal >=
(select sal from emp where ename = 'SCOTT');

--실습4. DALLAS에서 근무하는 사원의 이름, 부서 번호를 출력하시오.

select ename, deptno from emp
where deptno = 
(select DEPTNO  from dept01 where LOC = 'DALLAS');


--실습5.SALES(영업부) 부서에서 근무하는 모든 사원의 이름과 급여를 출력하시오.(서브쿼리 : DEPT01, 메인쿼리 : EMP

select * from DEPT01;

select ename, sal from emp
where deptno = 
(select deptno from dept01 where dname='SALES');

-- 급 문제) 연구부서에서 근무하는 모든 사원 정보를 출력하시오

select * from emp
where deptno = 
(select deptno from dept01 where dname = 'RESEARCH');

 

--2. 단일행 서브쿼리인데 집합함수 사용함
SELECT ENAME, SAL
FROM EMP
WHERE SAL > 
(SELECT AVG(SAL) FROM EMP);


select sum(sal) from emp;

-- 저기서 평균 이하 받는 애들은 어케 출력하노

SELECT ENAME, SAL
FROM EMP
WHERE SAL <= 
(SELECT AVG(SAL) FROM EMP) order by sal desc;


-- 3. 다중행 서브쿼리(in, any, all)
--1) in이라는 새끼
---IN (list)
SELECT ENAME, SAL, DEPTNO
FROM EMP
WHERE DEPTNO
IN
(SELECT DISTINCT DEPTNO
FROM EMP WHERE SAL>=3000);


=

SELECT ENAME, SAL, DEPTNO
FROM EMP
WHERE DEPTNO
IN
(10,20);

--실습8.  직급(JOB)이 MANAGER인 사람이 속한 부서의 부서 번호와 부서명과 지역을 출력하시오.(DEPT01과 EMP 테이블 이용)

select * from emp;
select * from dept01;

select deptno, loc from dept01
where deptno in
(select deptno from emp where job = 'MANAGER'); --=(10,20,30)

--2) all 새끼 (and개념)
--- 서브쿼리의 최대값 이상 검색

SELECT ENAME, SAL
FROM EMP
WHERE SAL > ALL
(SELECT SAL FROM EMP WHERE DEPTNO =30); --최소값950 최대값2850

--3) Any 새끼 (or개념)
---서브쿼리의 최솟값 이상 검색

SELECT ENAME, SAL
FROM EMP
WHERE SAL > ANY 
(SELECT SAL FROM EMP WHERE DEPTNO = 30 );
















