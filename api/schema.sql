drop table if exists readings;
create table readings (
  id integer primary key autoincrement,
  sensor_id integer not null,
  'timestamp' timestamp without time zone not null,
  value real not null
);

#create index 
#https://www.postgresql.org/docs/9.1/static/sql-createindex.html