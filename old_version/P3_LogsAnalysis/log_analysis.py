#!/usr/bin/env python3

import psycopg2
db = psycopg2.connect("dbname=news")
c = db.cursor()
q_rank_articles = """
    select count(l.path) as num, ar.title
    from articles ar, log l
    where l.path = concat('/article/', ar.slug)
    group by ar.title order by num desc limit 3;"""
c.execute(q_rank_articles)
rank_rows = c.fetchall()
print()
print("The most viewed articles: ")
for idx, row in enumerate(rank_rows):
    print(str(idx+1) + ": " + row[1] + " - " + str(row[0])+" views")

q_rank_author = """
    select count(l.path) as num, au.name
    from log l, articles ar, authors au
    where l.path = concat('/article/', ar.slug) and au.id = ar.author
    group by au.name order by num desc;"""
c.execute(q_rank_author)
rank_author = c.fetchall()
print()
print("Popular authors:")
for idx, row in enumerate(rank_author):
    print(str(idx+1) + ": " + row[1] + " - " + str(row[0])+" views")

q_most_err = """
    select * from (
    select date_trunc('day', l.time) as day,
    (count(*) filter (where l.status like '4%'
    or l.status like '5%')::numeric)/(count(*)::numeric) as perc
    from log l group by day order by perc desc)
    as tmp_table where perc > 0.01;"""
c.execute(q_most_err)
days_res = c.fetchall()
print()
print("Days, whose error queries are more than 1%:")
for idx, row in enumerate(days_res):
    print(
        str(idx+1) + ": Date: " + row[0].strftime("%Y-%b-%d") +
        " - " + "{0:.2f}".format(row[1]*100) + "% query errors"
        )
db.close()
