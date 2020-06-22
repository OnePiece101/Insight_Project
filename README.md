# Insight_Project - Treat Your Lips
## Background
* When seeing someone in a photo wearing lipstick with beautiful color, the user may want to know how
and where to buy that lipstick for herself or the significant other. I designed “Treat Your Lips”, a tool that automatically identify lip color in a photo by automatically detecting facial features and using a clustering model to provide users with lipsticks that best match the lip color from a dozen brands and hundreds of lipsticks 
* Connected postgresql with python to query from database and applied pandas and sklearn to analyzing and modeling data and built the web app with flask, HTML, and AWS
## Data
* Web scraping from Sephora website, see the [Scraping_Sephora_Lipsticks.ipynb](https://github.com/OnePiece101/Insight_Project/blob/master/Scraping_Sephora_Lipsticks.ipynb) for code
* Connect to [posgreql](https://github.com/OnePiece101/Insight_Project/blob/master/PSQL.ipynb)
## Packages
* Install packages in `insight.yaml`
* Install packages for lip detection: 
  ```shell
  # imultis
  pip install imutils
  # opencv
  sudo pip install opencv-contrib-python
  # dlib
  sudo apt-get install build-essential cmake
  sudo apt-get install libgtk-3-dev
  sudo apt-get install libboost-all-dev
  pip install dlib
  ```
## Modeling
* Lip Detection: `flaskexample/lip_bgr.py`
* Color Identification: `flaskexample/color_Model.py`
## Deployment
* Flask: `flaskexample/views.py`
* HTML: `flaskexample/templates/file_upload.html`, `flaskexample/templates/match.html`
## AWS Setup
- Create Ubuntu server on EC2 and connect to server following procedures on the [slides](https://docs.google.com/presentation/d/1Kh9UMl15EorOJ53PDFPmyGNHX9L_cDkLD3hE8cvtY_g/present#slide=id.p1)
- Increase size of eb2 volume and extend file system after resizing following instructions [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html)
- Change the instance type if needed (not enough RAM space/CPU) following the instructions in this [link](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html)
- Install packages on the local env
  ```shell  
  conda list --explicit > env_file.txt
  conda create --name env_name --file env_file.txt
  ```
  or
  ```shell
  conda env export > env_file.yaml
  conda env create -f env_file.yaml
  ```
- Install other packages:
  ```shell
  # nginx and gunicorn
  sudo apt-get update
  sudo apt-get install nginx gunicorn
  # psycopg2-binary
  sudo apt install libpq-dev python3-dev
  sudo apt install postgresql-server-dev-all
  pip install psycopg2-binary
  # opencv
  sudo pip install opencv-contrib-python
  # dlib
  sudo apt-get install build-essential cmake
  sudo apt-get install libgtk-3-dev
  sudo apt-get install libboost-all-dev
  pip install dlib
  ```
- Copy a file from local computer, run jupyter, install postgresql following the procedures in this [repo file](https://github.com/bjmarsh/WatchCBB/blob/master/ec2_setup.sh)
  If creating a <username> other than ubuntu, ec2 automatically created a dir under home `/home/<username>`. So need to move .sql file to that dir in order to copy the database contents. 
  ```shell
  sudo mv <path_database.sql> /home/<username>/database.sql
  ```
- Run web app on elastic IP: change `host='0.0.0.0'` in `run.py`
- Change Nginx configuration to avoid "request entity too large" error
  ```shell
  sudo nano /etc/nginx/nginx.conf
  ```
  - Add `client_max_body_size 100M;` to http context
  - Restart nginx: `sudo /etc/init.d/nginx restart`
- Schedule operations in Linux by setting up a [cron job](https://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/#:~:text=Cron%20allows%20Linux%20and%20Unix,%2Ftmp%2F%20directories%20and%20more.)
  ```shell
  # delete files older than 2 days in a directory everyday at 4 am
  0 4 * * * find /path/to/image/dir/* -type f -mtime +2 -delete
  ```
## Web App: [Treat Your Lips](treatyourlips.club)
## [Demo](https://www.youtube.com/watch?v=Y1kdQVGlDow)
