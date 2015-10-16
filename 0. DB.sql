
-- 一个问答信息表


CREATE DATABASE IF NOT EXISTS tophot default charset utf8;



-- 问题
create table question(
  qid int unsigned auto_increment,
  title varchar(200),
  description TEXT,
  createTime TIMESTAMP DEFAULT NOW(),
  primary key(qid)
)DEFAULT CHARSET=utf8;

INSERT INTO question(title, description) values("哈哈", "呱呱");



-- 回答
/*
  

*/
create table answer(
  uid
  content
  answerTime
)DEFAULT CHARSET=utf8;

-- 登陆账户
/* 
  用户id
  登陆邮箱
  密码
  账户创建时间
*/
create table account(
  aid int unsigned auto_increment,
  email varchar(100),
  password varchar(1024),
  signupTime  timestamp default now(),
  primary key(aid)
)DEFAULT CHARSET=utf8;




-- 用户信息
/*
  

*/
create table user(
  uid
  name
  gender
  birthday
  portt
)DEFAULT CHARSET=utf8;


-- 
create table xx(
  
)DEFAULT CHARSET=utf8;































