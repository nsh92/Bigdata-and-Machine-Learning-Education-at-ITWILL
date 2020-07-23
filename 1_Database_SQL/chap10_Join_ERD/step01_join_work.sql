-- step01_join_work.sql

/*
 * 조인(join)
 *  - 특정 칼럼(외래키)을 이용하여 두 개 이상의 테이블을 연결하는 DB 기법
 */

/*
 * 조인 절차
 * 1. 기본키를 갖는 테이블 생성
 * 2. 그 테이블에 레코드 추가
 * 3. 외래키를 갖는 테이블 생성
 * 4. 레코드 추가
 * 
 * 조인 테이블 삭제 : 위 선수의 역순
 * 강제 테이블 삭제 : drop table 테이블명 cascade constraint;
 */


-- 단계1 : 기본키를 갖는 테이블 생성
create table product(
code char(4) primary key,
name varchar(30) not null
);

-- 단계2 : 레코드 삽입
insert into product values('p001', '냉장고');
insert into product values('p002', '세탁기');
insert into product values('p003', '전화기');
select * from product;

-- 단계3 : 외래키 컴온요(다른 테이블의 기본키를 참조하겠다)
create table sale(
code char(4) not null,
sdate date not null,
price int not null,
foreign key(code)
references product(code)
);

-- 단계4 : 레코드 추가
insert into sale values('p001', '2020-02-24', 850000);
insert into sale values('p002', sysdate, 550000);
insert into sale values('p003', '2020-02-25', 150000);
select * from sale;
--무참조 무결성 제약 조건 위배 : 에러
insert into sale values('p004', '2020-02-25', 150000);
commit work; --db반영

-- 단계5 : join 이용 (특정)데이터 조회
select p.code, p.name, s.sdate, s.price
from product p, sale s --별칭으로 지정해주면 아래 where에서처럼 사용가능해짐
where p.code = s.code and p.name like '%기';