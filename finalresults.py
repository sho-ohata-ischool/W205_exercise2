import sys
import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

def lookup_postgres(word):
	cur = conn.cursor()
	cur.execute("""SELECT word, count from Tweetwordcount where word =%s;""", (word,))
	records = cur.fetchone()
	if cur.rowcount != 0:
		print 'Total number of occurences of "%s": %d' % (records[0], records[1])
	else:
		print 'Total number of occurences of "%s": 0' % word
	conn.commit()
	conn.close()

def postgres_output_all():
	cur = conn.cursor()
	cur.execute("SELECT word, count from Tweetwordcount order by word")
	records = cur.fetchall()
	for rec in records:
	   print '"%s": %d' % (rec[0], rec[1]), '\n'
	conn.commit()
	conn.close()

if __name__ == '__main__':
   if len(sys.argv) != 1: 
       for a in range(1, len(sys.argv)):
       		lookup_postgres(sys.argv[a])
   else: 
       postgres_output_all()

    