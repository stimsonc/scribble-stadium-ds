## CARL STIMSON - CONTRIBUTIONS:

This is an EdTech start up I worked at for as part of the data science course at Bloom Institute of Technology. 

My contributions can be found mainly in the `/app/api` directory under [this commit](https://github.com/stimsonc/scribble-stadium-ds/commit/e6091d207fd0f82d41c2c21a79816e520a1cdd4b) and in the `/data_management/autopreprocess_testing` directory under [this commit](https://github.com/stimsonc/scribble-stadium-ds/commit/d9d8c85c8c729fe9ac48954aa1529e160e58e446).


-----------------------
### ORIGINAL REPO README:
-----------------------

## Story Squad, Team B - Data Science
[![Maintainability](https://api.codeclimate.com/v1/badges/146d9feb7549b988077a/maintainability)](https://codeclimate.com/github/Lambda-School-Labs/Labs26-StorySquad-DS-TeamB/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/146d9feb7549b988077a/test_coverage)](https://codeclimate.com/github/Lambda-School-Labs/Labs26-StorySquad-DS-TeamB/test_coverage)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Story Squad Banner](assets/story_squad_banner.png)](http://www.youtube.com/watch?v=-cDqvmmtuiE)


### TABLE OF CONTENTS
### - [What is Story Squad?](#what-is-story-squad-)
### - [Start Here](#start-here)
  * [Basics](#basics)
  * [Deployment](#deployment)
    + [**Setting up a python environment**](#--setting-up-a-python-environment--)
    + [**How to Deploy locally on a Windows Machine**](#--how-to-deploy-locally-on-a-windows-machine--)
    + [**Infrastructure**](#--infrastructure--)
    + [**Infrastructure for Training Tesseract**](#--infrastructure-for-training-tesseract--)
    + [**API Endpoints**](#--api-endpoints--)
    + [**Security**](#--security--)
    + [**Wordcloud Feature**](#--wordcloud-feature--)
    + [**Crop Cloud Setup**](#--crop-cloud-setup--)
### - [Prior Cohort Updates](#prior-cohort-updates)
  * [Transcription and Moderation](#transcription-and-moderation)
    + [**Transcription**](#--transcription--)
    + [**Safe Search**](#--safe-search--)
    + [**Low Confidence Flag**](#--low-confidence-flag--)
    + [**Sensitive Content Flagging**](#--sensitive-content-flagging--)
  * [Complexity Analysis](#complexity-analysis)
    + [**Complexity Metric**](#--complexity-metric--)
    + [**Visualizations**](#--visualizations--)
    + [**Gamification and Clustering**](#--gamification-and-clustering--)
    
    
<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# What is Story Squad?
[Story Squad](https://www.storysquad.education/) is the dream of a former teacher, Graig Peterson, to create opportunities for children to have creative writing and drawing time off-screen. Here's how it works: child users of the website are provided a new chapter in an ongoing story each weekend. They read the story, and then follow both a writing and drawing prompt to spend an hour off-screen writing and drawing. When they're done, they upload photos of each, and this is where our data science team comes in. The stories are transcribed into text, analyzed for complexity, screened for inappropriate content, and then sent to a moderator. Once all submissions have been checked over on moderation day, our clustering algorithm groups the submissions by similar complexity and creates Squads of 4 to head into a game of assigning points and voting for the best submissions in head-to-head pairings within the cluster! Then it starts all over again the following weekend.

**Want to hear an overview of all our project features?** Click the Story Squad banner above for a link to our product video from 10/22/20! Or keep scrolling to read more thorough information on each feature.

# Start Here

## Basics
Welcome to the DS Repo for Story Squad. It can be a little overwhelming for new cohorts, so here are the basics that you need. The following recommendations in this `Basics` section for future cohorts were made on 12/17/21.
 
- First, [here](https://bloomtech.notion.site/DS-Video-Archive-bef99d6bc5224e02944bb5aae4394148) is a link to our DS Video Archive. It has powerpoints and videos walking through everything from cloning this repo to your computer to building your own custom OCR model from scratch(which you don’t *have* to do, thanks to Docker!).
 
- We have a Dockerfile set up, and instructions to use it can be found in the [`custom_tesseract_training`](https://github.com/BloomTech-Labs/scribble-stadium-ds/tree/main/custom_tesseract_training) folder. This README walks you through connecting to Docker, how and where our data is stored, and how to tune and save a new model. *Improving our OCR model is one of our main tasks on the Data Science side of the project, so future cohorts should focus attention on this.*
 
- Once you’ve trained a new model, save it to the [`models`](https://github.com/BloomTech-Labs/scribble-stadium-ds/tree/main/models) folder. Its README shows our top performing OCR model at the moment. *Be sure to continue to update this README as you add new or better models.*
 
- In the [`app`](https://github.com/BloomTech-Labs/scribble-stadium-ds/tree/main/app) folder, you will find all of the files and endpoints related to the API and how they interact with each other. The folder README gives a visual of the story submission workflow.
 
- Related to the API is the [`model_transition`](https://github.com/BloomTech-Labs/scribble-stadium-ds/tree/main/model_transition) folder. This README shows what will need to be changed as we transition from the Google Vision model to our custom OCR model, once it is ready for use. *This transition will be an important task for future DS cohorts.*
 
- The current data we have is stored in the [`data`](https://github.com/BloomTech-Labs/scribble-stadium-ds/tree/main/data) folder. In the future we want to move these samples to S3 Cloud storage buckets, so that they aren’t saved on Github. We’ve also been looking into data augmentation techniques to generate more data to train with.
 
- The README of the [`data management`](https://github.com/BloomTech-Labs/scribble-stadium-ds/tree/main/data_management) folder walks through the data cleaning pipeline, to prepare a story submission to be used by our model. Currently, this is done manually. *An important task for future cohorts will be to automate this process.*
 
- The [`notebooks`](https://github.com/BloomTech-Labs/scribble-stadium-ds/tree/main/notebooks) folder has a range of topics from clustering methods, creation of the crop cloud, endpoint relationships, and more. These can give you background on how the crop cloud and other features were created. If you are working on a notebook that will be valuable for others, you can add it here.

- As new cohorts make updates and create new features to the repo, *be sure to add your progress and updates here for a better onboarding experience.*



## Deployment

### **Setting up a python environment**

It is recommended to use `pipenv` for creating a python environment. First, install python with pip. Then open a terminal and enter `pip install pipenv`. After that, navigate to the root folder of this project, and enter `pipenv install --dev`. This uses Pipfile and Pipfile.lock to recreate the same python environment used in development. We are also trying to keep the requirements in the [packages] section to a minimum. The dependencies in [packages] are only those imported into the app itself. Many of the python notebooks use packages that are not in this environment, as they contain a lot of proof of concept work that never made it into the app itself. Much of their imported data also isn't present in this repo for COPPA reasons. It would be fine to add notebook-only dependencies to the [dev-packages] section of Pipfile if this makes development easier. If you change Pipfile, please run `pipenv update` afterwards. This runs `pipenv lock` and `pipenv sync` for you, and keeps Pipfile.lock in aggreement with Pipfile. Then commit and push the changes to Pipfile.lock.

### **How to Deploy locally on a Windows Machine**

It is possible to deploy this API locally on Windows 10, but you will need to make some local changes to do so. There are other options for local deployment on a Windows machine that does not involve making changes, such as running a Ubuntu WSL (Windows Subsystem for Linux).

* Then you need to go to `app/utils/img_processing/google_api.py` and locate the code: `with open("/tmp/google.json", "wt") as fp:` in the `__init__` function (currently it is line 32) and change that to: `with open("././app/tmp/google.json", "wt") as fp:`

* In the same file and function as above, you need to also change: `environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/tmp/google.json"` (currently line 41) to : `environ["GOOGLE_APPLICATION_CREDENTIALS"] = "././app/tmp/google.json"`

  * ***NOTE:*** If the above path does not work for you, you can try to replace `"/tmp/google.json"` with `"app/tmp/google.json"`, which is the path from the repository root.

* Then, in the `app` directory, you need to create a new directory called `tmp`

* In the `tmp` directory, create an empty file named `google.json`

* Now, you should be all set to run `uvicorn app.main:app --reload` to deploy the API locally, provided you have the proper credentials. 

  > ***NOTE:***  
  > **Do NOT push these changes to GitHub!**  
  > These changes need to remain on your local machine only!


### **Infrastructure**
The infrastructure is handled by AWS Elastic Beanstalk Service using Docker containers.

These links were important to learn where to start with `AWS`:
- [The Official labs guide for DS](https://docs.labs.lambdaschool.com/data-science/)
- [A guide to setting up HTTPS on Route 53 (may require APL)](https://docs.labs.lambdaschool.com/guides/aws/elastic-beanstalk/elastic-beanstalk-dns)
- [AWS EBS Dashboard](https://console.aws.amazon.com/elasticbeanstalk/home?region=us-east-1#/environments)

### **Infrastructure for Training Tesseract**
This infrastructure is suited for Tesseract training on a local machine using Docker container.
To build a docker container to improve the Tesseract OCR model run the following command after cloning this repo from within the repo.

`docker-compose -f docker.dev.yml up -d`

Once the docker completes making the image run the container using the following command:-

`docker exec -ti scribble-ocr bash`

The directory structure for important directories of the container from **root** is shown below:-

------------

    ├── app                <- directory contains all the scribble-stadium-ds repo.
    │
    └── train              <- directory with tools to train the tesseract ocr
        │
        ├── 4.1.1.zip      <- tesseract 4.1.1.zip downloaded to unzip
        │
        ├── tessdata       <-  directory that house all the models. Currently only
        │                      eng.trainedata is available. The trained models are placed here. 
        │
        ├── tesstrain      <- tesstrain directory through which the training will be
        │                     run. Always run the `source ocr/bin/activate` to activate 
        │                     `ocr` venv before doing any training. Make sure to install 
        │                     all dependencies using `pip install -r requirements.txt` for 
        │                     initial run. For training use 
        │                     `make training MODEL_NAME=storysquad START_MODEL=eng 
        │                     TESSDATA=/train/tessdata`. For hyperparameter tuning refer 
        │                     https://tesseract-ocr.github.io/tessdoc/tess4/TrainingTesseract-4.00.html#lstmtraining-command-line
        │                   
        └── data           <- house `storysquad-ground-truth` which has all the training
                              material for tesseract to learn from. This directory is copied 
                              from `scribble-stadium-ds/data`. More data can be uploaded if 
                              it becomes available.
     
--------

### **API Endpoints**
<img src="assets/endpoints.png" alt="arch diagram"/>

- Submission subroute:
   - This subroute deals with original copy uploads of the user generated content (UGC).

   - URLs in these endpoints are verified via a SHA512 checksum that accompanies the file. These hashes are used to add an extra layer of protection to make sure that the file that is passed to the web backend and uploaded to the S3 bucket is indeed the file that we are grading.

   - In the `/text` endpoint, the transcription service and `squad_score` method are used to transcribe, flag, and score submissions,

   - A particular note about the `/cluster` endpoint. Because of the limitations with Pydantic data modeling package, we could not structure a proper request body model.
   Our request body was structured with cohort IDs as the dictionary keys, then nested dictionaries inside each contained submissionIDs as keys. Given that the cluster endpoint was a late implementation into the project, we were bound by these limitations and therefore built a model around the existing request body. in future iterations **we would HIGHLY RECOMMEND changing the request body of this endpoint** so that a proper Pydantic model can be used to build out the SwaggerUI example request body.


### **Security**
<img src="assets/security_diagram.png" alt="security"/>

- Functionality
   - Currently there is an APIRoute class that can plug into the application router for different endpoints. This function takes all incoming requests and separates the authorization header from the request client to check if that client is authorized to use the API endpoints.

- Process
   - Initially this functionality was going to get handled by the [FastAPI.middleware decorator](https://fastapi.tiangolo.com/tutorial/middleware/) to declare a custom function as middleware which is supposed to have the exact same functionality as the class that we implemented. However, during testing it was clear that the middleware function was ineffective. The function has a limited scope that it can work with, which for FastAPI that is restricted to HTTP requests made from a web browser. When hitting the endpoints from an unauthorized client through Python, the middleware function would not trigger and check the request client header. To get around this limited functionality of the built-in middleware, we customized the service that the middleware uses to receive its hook. The documentation for doing so can be found on the [FastAPI Documentation here](https://fastapi.tiangolo.com/advanced/custom-request-and-route/)
- Future Considerations
   - This method is clearly a bit of a workaround. In future iterations, this class could be completely reworked into a framework for adding custom middleware solutions that are not restricted to HTTP network traffic.
   - In our application, the value of `DS_SECRET_TOKEN` is static. In future iterations this should be given routes to regenerate new tokens and deprecate compromised or old tokens. Adding this functionality would increase the security of the tokens and decrease the attack vectors that could be exploited in a production server.

### **Wordcloud Feature**

- API
   - app/api/wordcloud_database.py is an endpoint that works with the front end to create a word cloud from the most complex words in a story submission. app/utils/wordcloud contains the algorithms used to determine complex words. This API fetches demo data from an RDS database that holds 167 stories. The endpoint requires the user to choose the story ID (1-167), and then returns all the words in the story, along with the weight of the words according to how complex it is (all the weights of the document added together equals 1). Front end takes the words and weights and creates an animated word cloud with it.

### **Crop Cloud Setup**

- Crop Cloud animation deployment
  - Whitelist your IP on the relevant RDS database -> (crop-cloud-database)
  - Fast API should be up and deployable, ready to provide gif with default values
  - Input correct username, data-base name, and other credentials for access in .env 

- Static picture Deployment (located in crop_cloud_original.py)
  - Obtain story_images.zip file from instructors
  - Place zip file in the '/data/' folder
  - Install Tesseract Binary
  - make sure your program can find where tesseract has been installed, and you should be good to go.


# Prior Cohort Updates

The main priorities for the team ending in 12/21 were to develop the ML Ops infrastructure and to improve our OCR model's accuracy.

Older updates are below to give background on the project and files in this repo. 

## Transcription and Moderation
### **Transcription**
- Functionality
   - Connects to Google Cloud Vision API (GCV) to perform transcription of the user uploaded written story. Utilizes the `document_text_detection` method as that is best for Handwritten Text Recognition. Currently being hosted using Google credentials belonging to one of the team members - a new DS team would need to set up their own credentials. It is free to sign up and they provide $300 in free credit. During our time working on this project, we didn’t accrue any charges. While we found using our own credentials sufficient for our purposes, the stakeholders do have Google credentials that they are willing to provide if you prefer.
- Future Considerations
   - While GCV was the best model we had access to, we still came across an issue of transcription errors. These errors are crucial to understand as they affected our ability to extract meaningful and reliable complexity metrics. Improving the transcription would improve the complexity metrics which in turn would improve the visualizations on the parent dashboard and our clustering algorithm. We found that the images with the worst handwriting typically had the most transcription errors. In lieu of the students improving their handwriting, the best place to improve transcription accuracy would be by improving the quality of the images by utilizing pre-processing techniques. A good [article](https://towardsdatascience.com/pre-processing-in-ocr-fc231c6035a7) for exploring pre-processing images.
   - Another team working on Story Squad at the same time as us spent a lot of time working on training their own OCR with Tesseract. Their use of pre-processing seemed very effective. Explore their [notebook](https://github.com/Lambda-School-Labs/Labs26-StorySquad-DS-TeamC/blob/main/notebooks/UGC_Preprocessing_Exploration.ipynb).
   - Spell checking was explored to improve the output of the transcription. Currently, it is not implemented as the transcription errors were too high to overcome with a spell checker. If the transcription accuracy can be improved, this could be implemented. The `count_spelling_errors` [notebook](notebooks/count_spelling_errors.ipynb) contains the exploration of two different spell check methods. A third team working on Story Sqaud implemented a spell checker [here](https://github.com/Lambda-School-Labs/Labs26-StorySquad-DS-TeamA/blob/main/project/app/ocr/text_complexity.py).
- Links
   - The `transcribed_stories` [notebook](notebooks/transcribed_stories.ipynb) creates a CSV with all of the transcriptions from the stories provided by the stakeholders.
   - The `google_api.py` [script](project/app/utils/img_processing/google_api.py) builds the class that the application utilizes to connect to GCV API.
   - The calculation of the error metric was leveraged from a prior DS team’s [notebook](https://github.com/Lambda-School-Labs/story-squad-ds/blob/master/Notebooks/addingmetrics.ipynb).

### **Safe Search**
- Functionality
   - Utilizes the SafeSearch method provided by Google Cloud Vision, which screens user-uploaded drawings for inappropriate content. Google will return the likelihood of the image being ‘adult’, ‘racy’, or ‘violent’. A flag will be raised and returned to the administration dashboard if Google returns a probability of ‘Possible’ or above for any of these categories.
- Process
   - This functionality was not actually requested by the stakeholders. Under COPPA regulation, every illustration that is uploaded by the students is required to have human moderation to prevent inappropriate material being displayed to the other students.
   - We decided to include the SafeSearch functionality because it was a simple implementation that would help the moderators prioritize their work.
   - On that same note, we decided to have a lower threshold to ensure that our recall rate was optimized. As the SafeSearch flags will be confirmed by human eyes we felt that it was better to flag too many submissions than potentially miss inappropriate images.
- Future Considerations
   - Through our testing, this system seems to work very well. If future teams decide the SafeSearch is too sensitive or not sensitive enough, the threshold can be adjusted.

### **Low Confidence Flag**
- Functionality
   - This feature raises a flag if the Google Cloud Vision API is less than 85% confident about its transcription. The logic is that a low confidence transcription will result in higher transcription errors. High transcription errors will, in turn, produce an unreliable evaluation metric for that submission. By monitoring this confidence level, we hope to return a disclaimer to the user that the evaluation metric may not be accurate and tips to improve image and handwriting quality to improve our transcription. While the framework for this feature is completed on the data science end, it is not a feature that the web team has implemented on their side yet. Currently, the threshold is set fairly low which will serve to catch the submissions that are likely to be severely impacted by poor translation.
- Process
   - We were given 167 images of stories as well as their human transcriptions by the stakeholders. We used these human transcriptions alongside the transcriptions created with Google Cloud Vision to calculate the error rate of the GCV transcription. The hope was that the error rate and confidence level were directly correlated. Unfortunately, the highest correlation we saw was 0.49.
- Future Considerations
   - Future improvements on transcription quality, such as implementing pre-processing, may improve the correlation between the error metric and the confidence level. Additionally, different methods of calculating the error may result in higher correlation. A higher correlation would allow us to select a more discerning threshold that will flag submissions that are being negatively affected by poor transcription. A deeper discussion on discovering errors in the human transcriptions, with the missing pages identified, can be found in the `transcription_confidence` [notebook](notebooks/transcription_confidence.ipynb).
   - As mentioned above, this feature has not been implemented on the web team’s end yet.
- Links
   - The notebook exploring the transcription confidence levels can be found in `transcription_confidence` [notebook](notebooks/transcription_confidence.ipynb). The correlation matrix and scatter plot exploring the relationship between the confidence level and error metric can be found in this notebook. Additionally, this notebook creates a CSV with the API transcriptions, human transcriptions, calculated error between the two and Google API confidence level for each submission.
    
### **Sensitive Content Flagging**
- Functionality
   - This feature is not currently functional, but the goal is to be able to add the sensitive content flag in addition to the inappropriate content flag, to flag both for the moderator. The current implementation will just always return a `False` flag for `SensitiveContent`.
- Process
   - This feature is not fully functional, because the idea came up too late in the project. The idea was prompted by a story (ID 5114) that alluded to an abusive mother. We realized that we may need to have additional screening for sensitive content that could even necessitate some kind of proactive action/intervention by Story Squad staff. We brought this to the stakeholders, and they said that while Story Squad will not be a [legally mandated reporter](https://www.socialworkdegreeguide.com/faq/what-is-a-mandated-reporter/), they want to try to do the right thing, and keep this potential in mind.
   - Ultimately, we only got a very bare bones implementation ready to go to screen for sensitive content (including potential abuse or suicide/self-harm), but the stakeholder requested we simply document our progress, and allow for a future team to create a more thorough solution. See [this Google Doc](https://docs.google.com/document/d/1HusCK9FqadwIFyfAwQVN03bq2LCqujxZX0QwZCLA7do/edit?usp=sharing) for a write-up of our MVP implementation idea and general considerations.
- Future Considerations
   - Ideally, this type of content moderation would be done through a pre-trained model that could generate a flag based on context and natural language understanding, rather than simply a dictionary check of potentially indicative words. Of course, this is difficult due to the limitations of our use-case: small amount of training data, errors in children’s spelling, and errors in transcription. But the importance of this feature, both for moderating what content is put in front of other children, and for noticing if a child might be in unsafe circumstances, necessitates this type of feature exploration.

## Complexity Analysis
### **Complexity Metric**
- Functionality
   - We named our complexity metric the "Squad Score". The functionality of each Squad Score version is fully documented in the Release notes of both [v1.0](https://github.com/Lambda-School-Labs/Labs26-StorySquad-DS-TeamB/releases/tag/v1.0) and [v1.1](https://github.com/Lambda-School-Labs/Labs26-StorySquad-DS-TeamB/releases/tag/v1.1).
   - Essentially, the Squad Score feature generates a complexity metric for each story transcription, that is used both for visualizations on the parent dashboard to show student progress, and used to cluster child users for the gamification component.
   - Formula: story_length(1)(30) + avg_word_len(1)(30) + quotes_number(1)(30) + unique_words(1)(30) + adj_num(1)(30)
   - See Release notes for further information on the formula, including the features, initialized weights, and metrics.
- Process / Reasoning
   - Check out [this Medium article](https://medium.com/@lori.schlatter/simplicity-of-complexity-the-realities-of-data-science-decision-making-af0ef737a5bf) for more thorough detail on the process of developing this metric.
   - Coming into the project, we assumed we would be using some kind of advanced NLP techniques for this text analysis. Then the stakeholder’s initial guidance on a complexity metric was for it to resemble a [Lexile score](https://www.lexialearning.com/blog/more-number-what-is-lexile-measure), which we quickly realized was a proprietary metric that we wouldn’t be able to replicate. We did find a [free Lexile analyzer](https://la-tools.lexile.com/help/), but it specifically indicated that student writing was not a good candidate for use as input. We then looked into the Python [`textstat`](https://pypi.org/project/textstat/) package and explored the origins of all of those metrics (see [this doc](https://docs.google.com/document/d/1e-LcyRn0DHQJa9pueNpCjKAYj-dyjI3fDtynhTrlGy4/edit?usp=sharing) for that writeup). Ultimately, however, we came to a similar conclusion that the previous team did -- that these metrics are all trained on professionally edited and proofread text, and did not have a guarantee of generalizing to unedited, un-proofread, error-prone transcriptions of children’s writing.
   - We wanted to generate a metric that would be as minimally impacted in its consistency by inevitable errors we knew would come up in our transcribed text, but also would have a high likelihood of being generalizable to new data. Therefore, we opted to build our own simple metric for our MVP that would only use features that we could justify based either on features that:
      - showed up in other validated complexity metrics (such as word length)
      - or
      - were specifically requested by our stakeholder (such as quotes number)
      - and
      - that were implemented in ways that minimized error (such as using word length by character rather than syllable, or number of quotes rather than aiming for a percentage-of-dialogue feature, or number of unique words rather than a comparison to a set list of complex words).
   - See the [`squad_score_mvp` notebook](notebooks/squad_score_mvp.ipynb) for creation of the Squad Score and exploration of some additional features.
   - v1.0 utilized only the metrics that could be generated with Python alone, and then v1.1 implemented `nltk` with the number of adjectives feature.
   - Given that we did not have a labeled dataset, we opted to not fine-tune any of the weights for the features, as there was no way to test this kind of customization. See [this doc](https://docs.google.com/document/d/1JfJY4qY-1BGgdbpDrtCxG0Vz8SHXcCAHQLBAlZunxm0/edit?usp=sharing) transcribing a conversation with the stakeholder about potential solutions to this problem. After this conversation, our stakeholder provided us with a small set of labels midway through the project, of 25 stories that were hand-ranked by a third party (see `rankings.csv` in [`data`](data/) folder). We did use this ranking to generate our metric for our formula in terms of correlation, but did not use it to generate weights since it was such a small, and potentially subjective list of labels.
- Future Considerations
   - It’s worth additional conversation with the stakeholder about whether or not labels can ever be generated on the existing and incoming data. This would provide the best way to provide a little more confidence about adding weights or more experimental features. In lieu of this, the stakeholders were clear that they still value exploration of this metric, as long as it is heavily documented and versioned (we used GitHub releases for our versioning) so that any iteration can easily be pulled up. Note that if at any time labels are added, the stakeholders were also clear that the labels would need to be treated as imperfect, since it’s nearly impossible to have totally objective metrics for this writing.
   - If new data is provided in the future, the MinMaxScaler in the [`squad_score_mvp` notebook](notebooks/squad_score_mvp.ipynb) will need to be retrained with the entire corpus, and re-pickled and deployed.

### **Visualizations**
- Functionality
   - Creates two visualizations for the parent dashboard. This will allow the parents to keep an eye on the progress of their student. The final visuals are a result of discussions with the stakeholders. One visual is a histogram that plots the distribution of all of that week’s scores for the student’s specific grade. The student’s score for that week is plotted as a vertical line to be able to see how they compare to the other submissions for that week. The second visual is a line graph that charts the history of the student’s submissions. At least one submission must be made for the parents to be able to view these visuals. Additionally, scores will not be available to display until the submissions have successfully gone through the moderation process at which point they will be released by the web back-end.
- Process
   - This is a new feature idea that was the result of a lot of back and forth discussion between the stakeholders and our DS team member Lori. The stakeholders were very supportive of this idea but very specific in its implementation. They want to provide visibility so that the parents can be engaged in their student's progress, but they do not want to display any metrics to either the student or parent user. They feel this would take away from the creative safe-space they are trying to cultivate for the students.
   - This [Google Doc](https://docs.google.com/document/d/1VZZFP49LhYGMO5QV2quwKQsNbxUSRlIXdT3vI9jmJgY/edit) was sent to the stakeholders and outlines our thought process and includes mockups of various visualizations.
   - The stakeholders requested a working model by the end of our time working on this project (10/23/20) so they could test it in front of a panel of parent users for feedback.
- Future Considerations
   - For a future iteration, we had an idea that the stakeholders were very excited about. Our idea is to populate a dynamic sentence at the bottom of the line graph that highlights an area that the student improved in for that week. By keeping track of the metrics for each of the student’s submissions, we can highlight improvements against either their average performance or their last submission. Again we would want to do this at a high level without disclosing specific numbers. The idea is to always be able to highlight something positive about the student’s writing that week. For example: “It looks like Bobby used more description adjectives than average this week!” or “Bobby increased his use of dialogue this week compared to last week!”
   - Again, the stakeholders will be testing this new feature in front of parent users at some point and will have feedback on what to change, keep or may decide against the feature altogether.
- Links
   - The `score_visual` [notebook](notebooks/score_visual.ipynb) explores various visuals that we presented to the stakeholders. The `histogram.py` [file](project/app/utils/visualizations/histogram.py) and the `line_graph.py` [file](project/app/utils/visualizations/line_graph.py) include the scripts for the final approved visualizations. They produce a JSON file for the web to display on the parent dashboard.
![line_graph](assets/line_graph.png)
![histogram](assets/histogram.png)


### **Gamification and Clustering**
- Functionality
   - The current clustering function we have implemented is a basic MVP for clustering, which sorts moderator-accepted submissions for each cohort (meaning the group of users that is on a given chapter of the story) by Squad Score, and returns clusters of 4 by submission ID to the web backend to be randomly paired.
   - For cohorts with submission counts not divisible by 4, some submission IDs are duplicated (that are still close in Squad Score) to ensure that only clusters of 4 are returned. This is coded such that, if at all possible, no cluster will have more than 1 submission ID that is also found in another cluster.
   - If there are under 4 submissions in a cohort, a message is returned instead, that there are not enough submissions to form a cluster.
- Process
   - We did not end up implementing a DS database, meaning that unless we requested the web backend to store story transcriptions (which could be an option for a future iteration), we would need to re-transcribe stories after they were moderated each week in order to generate a more sophisticated clustering algorithm based on features. As it is, without either of these things in place, the best way to cluster was simply by ordered Squad Score. However, other potential clustering algorithms were explored in the [clustering notebook](notebooks/clustering.ipynb).
   - One big issue that has yet to have a fully engineered solution is the “remainder problem”, which is essentially that the gamification framework requires there to be 4 players per cluster, but of course there will not always be a number of submissions divisible by 4. Our idea for a solution is to duplicate submissions (as mentioned above), meaning we’d pull in another story submitted that week with a similar Squad Score, but without being attached to an actual user. This way, the others in the cluster can still view 4 stories, but then have a default code script in place that will auto-vote and assign points on behalf of the duplicated submissions, essentially having a “bot” as part of the team (and thus, we want to ensure no more than 1 bot per cluster). However, this structure that would generate the “bot” auto-play is not yet in place on our web backend, so the remainder problem isn’t fully solved in our deployed implementation.
- Future Considerations
   - Of course, a more sophisticated clustering algorithm would be preferred. In order to avoid re-transcribing stories (which would take a lot of extra time, and would add to the Google Cloud bill), either the web database could store transcriptions after initial submission, or DS could generate its own database. Note that if DS creates its own database, it needs to have the same considerations that Web’s does: i.e. how to handle stories that are moderated out of gamification, etc.

