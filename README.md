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
  ```
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
## Web App: [Treat Your Lips](treatyourlips.club)
## [Demo](https://www.youtube.com/watch?v=Y1kdQVGlDow)
