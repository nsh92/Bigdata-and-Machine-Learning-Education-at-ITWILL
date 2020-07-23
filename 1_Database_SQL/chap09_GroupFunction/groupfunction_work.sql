-- groupfunction_work.sql


/*
 * 그룹함수 : 그룹 단위 집계/통계 구하는 함수
 * - 사용칼럼 : 범주형(집단형) 칼럼
 */

-- 1. 그룹함수

-- 1) sum()
SELECT SUM(SAL) FROM EMP;
select comm from emp
SELECT SUM(COMM) FROM EMP; --null 무시

-- 2) avg()
SELECT AVG(SAL) FROM EMP;
SELECT round(AVG(SAL), 3) FROM EMP;

SELECT AVG(comm)FROM EMP; --null 무시했으니 550
=
select sum(comm)/4 from emp;

-- 3) min/max()
SELECT MAX(SAL), MIN(SAL) FROM EMP;


select * from emp;
select to_char(Max(hiredate), YY/MM/dd) "최근 입사일", to_char(min(hiredate), yy/mm/dd) "가장 오래된 입사일" from emp;
--시발

-- 4) COUNT 함수
SELECT COUNT(COMM) FROM EMP; 
select count(hpage) from professor;
select count(*) from professor; -- 다 셈

select count(comm) from emp where deptno=10;
select * from emp
새로운 문 'SCOTT' 사원과 같은 부서에 근무하는 사원에 대한 급여 합계 평균을 구하셈
select sum(sal), avg(sal) from emp where deptno = (select deptno from emp where ename = 'SCOTT');

-- 6. 분산과 표준편차 : 산포도 : 강의교제에 없음
select Variance(bonus) from professor; -- 분산 = (편차)^2의 총합 / 변수의 개수
select Stddev(bonus) from professor; -- 분산의 양의 제곱근
select sqrt(variance(bonus)) from professor;


-- 2. Group By 절 : 범주형 컬럼(집단형 변수)
--  동일한 집단별로 묶어서 집단별 집계를 구하는 함수	

SELECT DEPTNO FROM EMP GROUP BY DEPTNO; -- 10/20/30 구분
select deptno, sum(sal), avg(sal) from emp group by deptno;

SELECT DEPTNO, MAX(SAL), MIN(SAL) FROM EMP GROUP BY DEPTNO;

--교수 테이블에서 직급별 교수의 평균 급여 계산해보셈
select * from professor;
select position 직급, round(avg(pay),3) "급여 평균" from professor group by position;

/*
 * sql문에서 조건절
 * 1. select * from 테이블명 where 조건식
 * 2. select * from 테이블명 group by 컬럼명 having 조건식;
 * 그러니까 집단의 조건으로 해빙을 쓴다, 집단을 셀렉트 하기 전에 집단에 대한 조건을 건다
 */


-- 3. Having 조건
SELECT DEPTNO, AVG(SAL)
FROM EMP
GROUP BY DEPTNO
HAVING AVG(SAL) >= 2000;
--똑같은 결과
SELECT DEPTNO, AVG(SAL)
FROM EMP
GROUP BY DEPTNO
HAVING deptno in(10,20);

SELECT DEPTNO, MAX(SAL), MIN(SAL)
FROM EMP
GROUP BY DEPTNO
HAVING MAX(SAL) > 2900;

SELECT DEPTNO, MAX(SAL), MIN(SAL)
FROM EMP
GROUP BY DEPTNO
HAVING Min(SAL) > 900;

-- 그룹바이 상태에서 having 대신 where를 쓰면 오류가 뜸

-- 학생 테이블에서 학년별 몸무게 평균이 60이상인 학생 정보를 조회하시오

select * from student;

select grade, avg(weight), avg(height) from student group by grade
having avg(weight) >= 60;

-- 교수 테이블에서 학과별 급여의 평균이 300 미만인 교수 정보 조회하기
select deptno, avg(pay) from professor group by deptno having avg(pay) < 300;
select * from professor;







