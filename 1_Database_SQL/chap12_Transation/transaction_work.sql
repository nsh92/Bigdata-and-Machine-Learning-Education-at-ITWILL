-- transaction_work.sql

--1.  table 생성
create table dept_test
as
select * from dept;

select * from dept_test;


--2. SavePoint
savepoint s1;

delete from dept_test where  deptno = 40;
select * from dept_test;

Savepoint s2;

delete from dept_test where  deptno = 30;
select * from dept_test;

savepoint s3;

delete from dept_test where  deptno = 20;
select * from dept_test;

--레코드 복원
rollback to s3;
select * from dept_test;

rollback to s1;
select * from dept_test;


-- 4. commit : db반영(롤백불가)
delete from dept_test where deptno=40;

commit; -- db반영
savepoint s4
delete from dept_test where deptno=30;

rollback s4;
select * from dept_test;















