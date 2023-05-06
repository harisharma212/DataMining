Initial Steps:
-------------
1. Download the Source code & Copy into D drive

2. Make sure the python 3.10 installation has been completed.
	(https://www.python.org/ftp/python/3.10.9/python-3.10.9.exe) 
	(Select Add Python to Path checkbox)
	
3. Install any IDE (Preferably Sublime Text) (Optional) (https://www.sublimetext.com/3)

4. Install virtual environment library.
	("pip install virtualenv") 

5. Create Virtual Environment.
	* Open CMD
	* Type D:
	* type ("virtualenv <ENV_NAME>")

6. Activate virtual environment
	(ENV_NAME\Scripts\activate)

7. Run below commandd to install required libraries.
	"pip insstall -r requirements.txt"

Running the server:
-------------------
1. Open Command Prompt.

2. Type D:

3. Activate virtual environment
	(ENV_NAME\Scripts\activate)

4. Run below command to activate the Django Server.
	"python DataMining\manage.py runserver"

5. Copt the URL (http://127.0.0.1:8000)

6. Paste in GoogleChrome browser.

7. Deactivate the virtualenv using below command.
	("ENV_NAME\Scripts\deactivate")


Running the server in Intranet:
------------------------------
1. Open Command Prompt.

2. Type D:

3. Activate virtual environment
	("ENV_NAME\Scripts\activate")

4. Get Intranet IP address (Type "ipconfig" and copy the ipv4 address XXX.XXX.X.XXX)

4. Run below command to activate the Django Server.
	"python BloodDonor\manage.py runserver IP_ADDRESS:PORT"  (PORT is any 4 digit number)

5. Copt the URL (http://IP_ADDRESS:PORT)

6. Paste in GoogleChrome browser.

7. Deactivate the virtualenv using below command.
	("ENV_NAME\Scripts\deactivate")
