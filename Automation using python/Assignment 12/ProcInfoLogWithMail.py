import psutil;
import sys;
import os;
import time;
import smtplib;
import urllib.request as urllib2;
from email import encoders;
from email.mime.base import MIMEBase;
from email.mime.multipart import MIMEMultipart;
from email.mime.text import MIMEText;



def processlog():

	list = [];
	for process in psutil.process_iter():

		try:
			pinfo = process.as_dict(attrs = ['pid','name','username']);
			pinfo['vms'] = process.memory_info().vms/(1024*1024), 'MB';
			list.append(pinfo);

		except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
			pass;

	return list;


def logprocess(path):

	flag = os.path.isabs(path);

	if not flag:

		path = os.path.abspath(path);

	if os.path.isdir(path):

		t = time.time();

		name = "%s/log%s.txt"%(path,t);

		fd = open(name,'w');

		fd.write("Current running processes are \n\n");

		for items in processlog():

			items = str(items);

			fd.write("%s\n"%items);

	return name;




def is_connected():

	try:
		urllib2.urlopen('http://216.58.192.142',timeout = 1);
		return True;

	except urllib2.URLError as err:
		return False;




def mailsender(filename, time, toaddr):

	try:
		fromaddr = 'sachinaybhujbal98@gmail.com';

		msg = MIMEMultipart();


		msg['From'] = fromaddr;
		msg['To'] = toaddr;

		body = """

		Hello %s,
			please find the attached file which contain information of runing processes.
		
		Logfile is created at:%s
		"""%(toaddr, time)


		subject = """ Process log generated at : %s"""%time;

		msg['Subject'] = subject;

		msg.attach(MIMEText(body, 'plain'));

		attachment = open(filename, 'rb');

		p = MIMEBase('application','octet-stream');

		p.set_payload((attachment).read());

		encoders.encode_base64(p);

		p.add_header('content-Disposition',"attachment; filename = %s"%filename);

		msg.attach(p);

		s = smtplib.SMTP('smtp.gmail.com',587);

		s.starttls();

		s.login('sachinaybhujbal98@gmail.com','Sachinay@98');

		text = msg.as_string();

		s.sendmail(fromaddr, toaddr, text);

		s.quit();
	
		print('Mail send successfully');


	except Exception as E:
		
		print("Unable to send mail.",E);



def main():

	print("Application name is",sys.argv[0]);

	

	try:
		filename = logprocess(sys.argv[1]);
		
		connected = is_connected();

		if connected:

			starttime = time.time();

			mailsender(filename, time.ctime(),sys.argv[2]);
		
			endtime = time.time();
		
			print("Time taken is ",endtime - starttime);

		else:

			print("Their is no internet connection");


	except Exception as E:

		print("Error:Invaild input",E);	





if __name__=="__main__":
	main();


