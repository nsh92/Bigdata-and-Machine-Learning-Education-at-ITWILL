/*
 * 집합 함수(COUNT,MAX,MIN,SUM,AVG) 
 * 작업 대상 테이블 : EMP, STUDENT, PROFESSOR
 * '별'로 끝난다 = 그룹바이를 써라
 */
select * from emp;
select * from student;
select * from professor;

--Q1. EMP 테이블에서 소속 부서별 최대 급여와 최소 급여 구하기
select max(sal) "최대 급여", min(sal) "최소 급여" from emp group by deptno;

--Q2. EMP 테이블에서 JOB의 수 출력하기
select job, count(job) "직책의 수" from emp group by job; -- 내가푼거
select count(distinct job) from emp;--교수님이 푼거

--Q3. EMP 테이블에서 전체 사원의 급여에 대한 분산과 표준편차 구하기
select round(variance(sal),3) 분산, round(stddev(sal),3) 표준편차 from emp;

--Q4. Professor 테이블에서 학과별 급여(pay) 평균이 400 이상 레코드 출력하기
select deptno 학과번호, avg(pay) 급여평균 from professor group by deptno having avg(pay) >= 400;

--Q5. Professor 테이블에서 학과별,직위별 급여(pay) 평균 구하기
select deptno 학과, position 직위, avg(pay) 급여평균 from professor group by deptno, position;
--학과별 : 1차 그루핑, 직위별 : 2차 그루핑

--Q6. Student 테이블에서 학년(grade)별로 
-- weight, height의 평균값, 최대값, 최소값을 구한 
-- 결과에서 키의 평균이 170 이하인 경우 구하기

select grade 학년, avg(weight) 평균몸무게, max(weight) 최대몸무게, min(weight) 최소몸무게, avg(height) 평균키, max(height) 최대키, min(height) 최소키
from student group by grade having avg(height)<=170;