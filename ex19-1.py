def salary_breakdown(salary):
	salary_i = float(salary)
	weekly = (salary_i / 52) 
	bi_weekly = round((salary_i / 52) * 2,2)
	monthly = round((salary_i / 52) * 4,2)
	print "Your salary per week is: %r" % weekly
	print "your salary bi weekly is: %r" % bi_weekly
	print "Your monthly salary is: %r" % monthly
	
salary_breakdown(200000) 