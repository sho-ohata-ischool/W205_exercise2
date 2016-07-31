import sys
import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

def lookup_postgres(count1, count2):
	cur = conn.cursor()
	cur.execute("SELECT word, count from Tweetwordcount where count between %s and %s order by count", % (count1, count2))
	records = cur.fetchall()
	if cur.rowcount != 0:
		for rec in records:
	   		print '"%s": %d' % (rec[0], rec[1]), '\n'
	else:
		print 'No words with occurences between %s and %s', % (count1, count2)
	conn.commit()
	conn.close()

if __name__ == '__main__':
	if len(sys.argv) == 3: 
		if float(sys.argv[1]) % 1 == 0 && float(sys.argv[2]) % 1 == 0:
			if int(sys.argv[1]) < int(sys.argv[2]):
				lookup_postgres(sys.argv[1], sys.argv[2])
			else:
				lookup_postgres(sys.argv[2], sys.argv[1])
       	else:
       		print 'Please pass two integers'
   else: 
       print 'Please pass two integers'