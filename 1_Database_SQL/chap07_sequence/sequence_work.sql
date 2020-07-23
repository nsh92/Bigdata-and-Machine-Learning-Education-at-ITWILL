-- 1. 테이블 생성
select * from dept01;
drop table dept01 purge;

-- 구조 복사
create table dept01
as
select * from dept where 0=1;

--2. sequence 생성
create sequence dept_deptno_seq
increment by 1 
start with 1;

--3. 레코드 삽입
insert into dept01 values(dept_dpetno_seq.nextval,'test', '서울시');
insert into dept01 values(dept_dpetno_seq.nextval, 'test2', '대전시');

--4. sequence 목록 보기
select * from tab; -사용자가 만든 테이블 목록을 확인
select * from user_tables; - 전체 테이블 확인, 위와 동일한 결과
select * from user_sequence; - 전체 시퀀스 목록

-- [실습]
-- 1. 시퀀스 생성
CREATE SEQUENCE EMP_SEQ
START WITH 1
INCREMENT BY 1
MAXVALUE 100000 ;

-- 2. 테이블 생성
DROP TABLE EMP01;
CREATE TABLE EMP01(
EMPNO NUMBER(4) PRIMARY KEY,
ENAME VARCHAR2(10),
HIREDATE DATE
);

-- 3. 레코드 삽임
INSERT INTO EMP01
 VALUES(EMP_SEQ.NEXTVAL, 'JULIA' , SYSDATE);

INSERT INTO EMP01
 VALUES(EMP_SEQ.NEXTVAL, 'JULIA2' , SYSDATE);

select * from emp01;
delete from emp01 where empno = 2;

INSERT INTO EMP01
 VALUES(EMP_SEQ.NEXTVAL, 'JULIA3' , SYSDATE);

 --5. 시퀀스 삭제
 drop sequence dept_deptno_seq;
 select * from user_sequence; --지워졌나 확인
 
-- 6.문자열 + 시퀀스 숫자
create table board(
bno varchar(20) primary key,
writer varchar(20) not null
);

-- 시퀀스 생성 --시퀀스는 숫자라서 varchar타입에 못들어감 그래서 문자로 교환해줘야댐
create sequence bno_seq
start with 1001
increment by 1;

-- 홍길동 1001, 이순신1002
insert into board 
values('홍길동'||to_char(bno_seq.nextval), '홍길동'); --문자로 형변환 시켜줘서 합체시킴, 홍길동은 중복되지만 각 게시물에 대하여 고유번호가 생기는 셈
insert into board 
values('이순신'||to_char(bno_seq.nextval), '이순신');
insert into board 
values('홍길동'||to_char(bno_seq.nextval), '홍길동');
select * from board;


