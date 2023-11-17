# Database Converter (CSV)
This program can save data from MySQL database tables into csv files. The program lists the tables of the predefined database. From the list you can select the tables whose data you want to save in a csv file.
### Technologies used
- [Python 3.9.13](https://www.python.org/downloads/release/python-3913/)
- [wxPython](https://www.wxpython.org/)
### How To Deploy
1. Download the project as ZIP.
2. Start a MySQL database and configure the connection settings in the config.ini file. (src\config\config.ini)
   - [USBWebserver](https://www.usbwebserver.net/webserver/) (Free software for running a MySQL database.)
   - There is a sql script for building a sample database in the root of the project. (example.sql)
3. Run the "Run.bat" file, which creates a virtual environment for the program and installs all the modules required by the program. After installing the modules, the batch file starts the program.
