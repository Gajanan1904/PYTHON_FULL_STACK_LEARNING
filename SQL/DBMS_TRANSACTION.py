# Transaction: A Transaction is a sequence of sql operations executed as a single unit where either all changes are commited or all rolled back(ALL ARE NOTHING)

# Start transaction
# 	SQL Statement 1
# 	SQL Statement 2
# 	SQL Statement 3
# 	SQL Statement 4
# COMMIT (Save changes)
# OR ROLLBACK

#CREATE TABLE
create table bank_acounts(
    acc_id INT,
    acc_name varchar(50),
    balance INT
    );

#INSERT VALUES
insert into bank_acounts values(1,"rahul",5000),(2,"neha",3000);
select * from bank_acount;
# +--------+----------+---------+
# | acc_id | acc_name | balance |
# +--------+----------+---------+
# |      1 | rahul    |    5000 |
# |      2 | neha     |    3000 |
# +--------+----------+---------+

#Use this before startting the transaction
start transaction;

#Debited 1500 from rahul
update bank_acounts set balance=balance-1500 where acc_id=1;

#save changes using commit
commmit;

#Use this before startting the transaction
start transaction;

#Credit 1000 to neha
update bank_acounts set balance=balance+1000 where acc_id=2;

#save changes using commit
commmit;

#see changes after transactions
select * from bank_acounts;
# +--------+----------+---------+
# | acc_id | acc_name | balance |
# +--------+----------+---------+
# |      1 | rahul    |    3500 |
# |      2 | neha     |    4000 |
# +--------+----------+---------+

