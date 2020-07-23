select * from STUDENT; -- profno, deptno01
select * from PROFESSOR; -- profno

-- [문1] STUDENT 테이블 검색 결과(sub)를 이용하여 STUDENT01 테이블 생성(main) 
-- Sub(STUDENT), Main(STUDENT01)
create table student01
as
select * from Student
select * from Student01

-- [문2] 교수번호가 2001인 지도교수를 모시는 전체 학생 명부 출력
-- Sub(PROFESSOR), Main(STUDENT01)
select * from student01
where profno
=
(select profno from professor where profno=2001);


-- [문3] 보너스를 받는 교수들의 이름, 직위, 급여, 보너스 출력
-- 조건)   IN()함수 이용 : 다중 행 처리  
select name, position, pay, bonus from professor
where bonus In
(select distinct bonus from professor where bonus > 0);




-- [문4] 301 학과(DEPTNO) 교수들 보다 더 많은 급여를 받는 교수들의 이름, 직위, 급여, 학과 출력
-- 조건) ALL()함수 이용 : 다중 행 처리 
select name, position, pay, bonus from professor
where pay > all
(select distinct pay from professor where deptno=301);


       
       
       
       
       
       
       
       
       
       
       