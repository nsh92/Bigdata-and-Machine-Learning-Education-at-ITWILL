select * from emp;
SELECT empno, ename, sal, job FROM emp;
SELECT ename, sal, sal+300 FROM emp;
SELECT empno, ename, sal, comm, sal+comm/100 FROM emp
SELECT ename,sal,comm,sal*12+NVL(comm,0) FROM emp
SELECT ename AS 이름, sal 급여 FROM emp;
select ename || ' ' || job from emp;
SELECT ename || ' ' || job AS "employees" FROM emp;
 select distinct job from emp;
 SELECT DISTINCT deptno, job FROM emp;

 -- 2. 조건검색 (특정행 검색)(1.은 전체 검색  or 특정 검색 이었음)
 select * from emp;
 SELECT empno, ename, job, sal FROM emp WHERE sal >= 3000;
 SELECT empno, ename, job, sal, deptno FROM emp WHERE job = 'MANAGER'
select empno,ename,job,sal,hiredate,deptno from emp
where hiredate >= to_date('1982/01/01', 'yyyy/mm/dd')
--to_date('문자상수', '날짜포맷') : 문자상수 -> 날짜 형식으로 변환

--sql연산자
SELECT ename, job, sal, deptno
FROM emp
WHERE sal BETWEEN 1300 AND 1500;  	
--관계+논리 연산자
SELECT ename, job, sal, deptno
FROM emp
where sal >= 1300 and sal<=1500; -- >= <= 얘내는 관계연산자, and는 논리연산자

--in연산자
SELECT empno,ename,job,sal,hiredate
FROM emp
WHERE empno IN (7902,7788,7566);

SELECT empno,ename,job,sal,hiredate,deptno
FROM emp
where hiredate >= to_date('1982/01/01', 'yyyy/mm/dd') and
hiredate <= to_date('1982/12/31', 'yyyy/mm/dd');

select empno,ename,job,sal,hiredate,deptno
from emp
where hiredate between to_date('1982/01/01', 'yyyy/mm/dd') and to_date('1982/12/31', 'yyyy/mm/dd');

SELECT empno,ename,job,sal,hiredate,deptno
FROM emp
where hiredate LIKE '87%'; --% : 암거나 갠찬

select * from emp where ename like 'M%';

select * from student where name like '%수';

SELECT empno,ename,job,sal,hiredate,deptno
FROM emp
WHERE sal >= 1100 AND job = 'MANAGER';


SELECT empno,ename,job,sal,hiredate,deptno
from emp
where deptno=10 and sal>=2500;

SELECT empno,ename,job,sal,hiredate,deptno
from emp
where job='CLERK' or deptno=30;


SELECT empno,ename,job,sal,comm,deptno
FROM emp
WHERE comm IS NULL; --널인 애만 수당없음

SELECT empno,ename,job,sal,comm,deptno
FROM emp
WHERE comm IS not NULL; --널이 아닌 애만 수당있음

--검색레코드정렬
SELECT hiredate,empno,ename,job,sal,deptno FROM emp
ORDER BY hiredate;

SELECT hiredate,empno,ename,job,sal,deptno
FROM emp
ORDER BY hiredate desc; 

--별칭 이용 정렬
SELECT empno,ename,job,sal,sal*12  연봉 FROM emp ORDER BY 연봉; --별칭 지정한거에 대하여 정렬해라
--수식이용정렬
 SELECT empno,ename,job,sal,sal*12 annsal FROM emp ORDER BY sal*12; --수식에 의해서 정렬해라
 --컬럼위치정렬
  SELECT empno,ename,job,sal,sal*12 annsal FROM emp ORDER BY 5; --5번째 위치로 정렬해라

-- 두 개 이상 칼럼을로 정렬
SELECT deptno,sal,empno,ename,job
FROM emp
ORDER BY deptno, sal DESC; 
--1차정렬 : 부서번호 오름차순
--2차정렬 : 급여로 내림차순























