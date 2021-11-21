 
from sys import*;

import os;

import hashlib;


def hashfile(path, blocksize = 1024):

	fd = open(path,'rb');

	hasher = hashlib.md5();

	buf = fd.read(blocksize);

	while len(buf) > 0:

		hasher.update(buf);

		buf = fd.read(blocksize);

	fd.close();

	return hasher.hexdigest();


def checksum(path):

	flag = os.path.isabs(path);

	if not flag:

		path = os.path.abspath(path);

	exists = os.path.isdir(path);


	if exists:

		for floder,subfloder,files in os.walk(path):

			print("current floder is:",floder);

			for file in files:
				
				file = os.path.join(floder, file);

				print(file);

				print(hashfile(file));

				print('');

	else:
 
		print("Invalid Path");

