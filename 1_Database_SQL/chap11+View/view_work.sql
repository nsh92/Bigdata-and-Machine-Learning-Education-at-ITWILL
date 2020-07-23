-- view_work.sql

-- 뷰(view) : 가상 테이블

-- 1. 물리적 테이블 생성
create table db_view_tab(
id varchar(15) primary key,
name varchar(10) not null,
email varchar(50),
regdate date not null
);

insert into db_view_tab values('hong', '홍길동', 'hong@naver.com', sysdate);
insert into db_view_tab values('admin', '관리자', 'admin@naver.com', sysdate);
select * from db_view_tab
commit work;

-- 2. view 생성 : 서브쿼리 이용
create view admin_view --가상테이블, 기존에 똑같은 이름의 뷰가 있으면 create 대신 replace 명령으로 교체 가능
as 
select * from db_view_tab where id = 'admin'  --물리적인 테이블에서 서브쿼리를 지정해준다 오류가 난다면 권한설정이 안되었기떄문
--이 마지막에 with read only를 추가하면 저 계정은 읽기 전용으로 됨


-- view 전체 목록 확인
select * from user_views;
-- view 내용 확인
select * from admin_view

-- view 삭제
drop view admin_view;

---------------------------------------뷰의 라이프 사이클------------------------------------------------------

-- <실습> 뷰 정의
-- 물리적 테이블 : EMP
-- 가상의 테이블 : EMP_VIEW30(사번 이름 부서번호) 읽기전용
SELECT * FROM EMP

create view EMP_VIEW30
as
SELECT empno, ename, deptno FROM EMP 
where deptno = 30 with read only;

select * from emp_view30;

-- 3. view 사용 용도(목적)
/*
 * 1) 복잡한 sql 사용 시 편리함
 * 2) 보안 목적 : 접근 권한에 따라 서로 다르게 정보를 제공함
 */

-- 1) 복잡한 sql 사용 시 편리함
select * from product;
select * from sale;

create or replace view join_view
as
(select p.code, p.name, s.price, s.sdate
from product p, sale s
where p.code = s.code and p.name like = '%기')
with read only;

select * from join_view;


-- 2) 보안 목적 : 접근 권한에 따라 서로 다르게 정보를 제공함
select * from emp;

-- (1) 영업사원에게 제공하는 view 만들어보자
create or replace view sales_view
as
(select empno, ename, comm from emp where job = 'SALESMAN')
with read only;

select * from sales_view;

delete from sales_view where empno = 7499; -- 리드온리가 되었는지 검증 : 에러가 뜨는 것이 정상

-- (2) 일반사원에게 제공하는 뷰
create or replace view clerk_view
as
(select empno, ename, mgr, hiredate, deptno
from emp where job='CLERK')
with read only;

select * from clerk_view;

-- (3) 관리자에게 제공하는 뷰
-- 조건1. 뷰이름 : manager_view
-- 조건2. 대상 컬럼 : 전체
-- 조건3. 직책(영업사원, 사원, 분석자)
-- 조건4. 물리적인 테이블 : EMP

create or replace view manager_view
as
(select * from emp
where job in ('SALESMAN', 'CLERK', 'ANALYST'))
with read only;

select * from manager_view;

-- 4. 의사컬럼(rownum : 행번호) 이용 view 생성
-- ex) 최초 입사자 top5, 급여 수령자 top3

select rownum, empno, ename from emp
where rownum <= 5;

-- (1) 입사일 TOP5 view 생성
create or replace view top5_hire_view
as
select empno, ename, hiredate
from emp order by hiredate
with read only;

select rownum, empno, ename, hiredate from top5_hire_view
where rownum <= 5;

-- (2) 가장 많은 급여 수령 탑3 뷰 생성
-- 뷰 이름 : top3_sal_view
-- 선택 칼럼 : 사번 이름 급여 입사일
create view top3_sal_view
as
select empno, ename, sal, hiredate
from emp
where rownum <= 3
order by sal desc
with read only;

select * from top3_sal_view

--근대 이렇게 하니,
--실제 데이터랑 다르네

--rownum 숫자 자체는 실제 입력한 순서에 근거하는 거라서 왜곡된듯


create or replace view top3_sal_view
as
select empno, ename, sal, hiredate
from emp order by sal desc
with read only;

select rownum, empno, ename, sal, hiredate
from top3_sal_view
where rownum <= 3;

