ur.executescript("""Create Table prani( id INTEGER,name TEXT,marks INTEGER);
#                     Insert into prani values (1,"amit",90),(2,"Gajanan",100);
#                     Update prani set marks=80 where id=2;
#                     Alter table prani add age INTEGER;
#                     """)