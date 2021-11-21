
import sys;
import os;
import hashlib;
import psutil;
import time;
import smtplib;
import urllib.request as urllib2;
from email import encoders;
from email.mime.base import MIMEBase;
from email.mime.multipart import MIMEMultipart;
from email.mime.text import MIMEText;


def hashfile(path, blocksize = 1024):

	fd = open(path,'rb');

	hasher = hashlib.md5();

	buf = fd.read(blocksize);

	while len(buf) > 0:

		hasher.update(buf);

		buf = fd.read(blocksize);

	fd.close();

	return hasher.hexdigest();




def finddupfile(path):

	try:

		flag = os.path.isabs(path);

		if not flag:

			path = os.path.abspath(path);

		exists = os.path.isdir(path);

		dict = {};

		a = 0;

		if exists:

			for folder,subfolder,files in os.walk(path):
		
				for file in files:

					a += 1;
	
					path = os.path.join(folder,file);

					hash_file = hashfile(path);

					if hash_file in dict.keys():

						dict[hash_file].append(path);
					else:

						dict[hash_file] = [path];	


		return dict, a;

	except Exception:

		pass;


def deletedupfile(dict1):

	try:

		b = 0;

		path = 'Marvellous';

		flag = os.path.isabs(path); 

		if not flag:

			path = os.path.abspath(path);

		exists = os.path.isdir(path);

		if not exists:

			path = str(os.mkdir('Marvellous'));


		fname ="\log_%s.txt"%time.ctime();

		fname = fname.replace(" ","_");

		fname = fname.replace(":","_");
	
		fname = os.getcwd()+'\Marvellous' + fname;

		fd = open(fname,'w');

		result = list(filter(lambda x:len(x) > 1 , dict1.values()));

		if len(result) > 0:

			fd.write('Duplicate files are:\n');

			for re in result:

				icnt = 0;

				for subre in re:

					icnt += 1;

					if icnt > 1:

						fd.write("\t\t%s\n"%subre);

						os.remove(subre);

						b += 1;


		else:

			fd.write('Duplicate files are not found\n');

		fd.close();	

		return fname, b;

	except Exception:
		
		pass;

	


def is_connected():

	try:
		urllib2.urlopen('http://216.58.192.142',timeout = 1);
		
		return True;

	except urllib2.URLError as err:

		return False;



def mailsender(filename, time1, scfile, dupfile, toaddr):


	try:

		fromaddr = 'sachinaybhujbal98@gmail.com';

		msg = MIMEMultipart();


		msg['From'] = fromaddr;
		msg['To'] = toaddr;

		body = """

Hello %s,

	please find the attached log file of duplicate files deleted from specified directory.

Starting time of scanning is %s.
Total number of files scanned are %d
Total number of duplicate files found are %d"""%(toaddr,time1,scfile,dupfile);


		subject = """ Duplicate file removal log at %s"""%time.ctime;

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

		s.login('sachinaybhujbal98@gmail.com','password');

		text = msg.as_string();

		s.sendmail(fromaddr, toaddr, text);

		s.quit();


	except Exception as E:
		
		pass;






