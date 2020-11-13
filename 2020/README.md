# Silesia Travel – Computer Vision & NLP competition

## Description

Do you know all interesting places in Silesia? We guess neither of us knows. There are so many beautiful attractions in Silesia that even the inhabitants of Silesia have not seen all of them.

The main goal of the task is to tag photos from different parts of Silesia with objects that are on them. These tags may, in the future, allow us to propose a Silesian attraction as a replacement for another similar attraction in the world.

### Dataset description


The dataset consists of two parts. One is a folder with photos from various parts of Silesia and a .csv file with the names of the photo files and a logical value for each of the 38 categories, determining whether it is in the photo. The second is a folder with video and audio files.

The dataset is private, it can only be used for this hackathon. Before downloading the data, you must accept the terms & conditions.

### First task (60% of total score):

Having a collection of training photos and their tags, create a system or model that will tag new photos that we provide you.

### Second task (40% of total score):


Prepare a web application (link publicly available), take takes a audio or video file as an input -> and returns statistics on how often objects of the classes and exact moments in these files (ranges of moments) - where the objects (same 38 categories from the first task) are appearing or mentioned. In audio files - these objects doesn't need to be mentioned directly, can also be mentioned indirectly.

## Evaluation


To speed up the evaluation of the first assignment, please send all your responses in a .csv file. The output should look similar to the .csv file added to the training image set, but the filenames should be the names of the files in the test photo folder. The column with names should be sorted alphabetically. 
Only "0" and "1" values are allowed in the remaining columns.

You are required to give full answer for every picture in test set.

Your score will be evaluated by the f1 score of your answers to reference answers. Example first task scoring:

Answer:

| Name | Animals | Bench | Building | Castle | Cave |
| --- | --- | --- | --- | --- | --- |
| Answer0.jpg | 1 | 1 | 0 | 0 | 1 |
| Answer1.jpg | 1 | 0 | 1 | 0 | 1 |
| Answer2.jpg | 0 | 1 | 0 | 1 | 0 |
| Answer3.jpg | 0 | 0 | 1 | 0 | 1 |
| Answer4.jpg | 0 | 0 | 0 | 1 | 1 |
| Answer5.jpg | 1 | 0 | 1 | 0 | 1 |
| Answer6.jpg | 0 | 0 | 0 | 0 | 0 |
| Answer7.jpg | 0 | 0 | 0 | 1 | 0 |

Reference:

| Name | Animals | Bench | Building | Castle | Cave |
| --- | --- | --- | --- | --- | --- |
| Answer0.jpg | 1 | 0 | 1 | 1 | 1 |
| Answer1.jpg | 1 | 0 | 1 | 0 | 1 |
| Answer2.jpg | 0 | 1 | 0 | 0 | 0 |
| Answer3.jpg | 0 | 0 | 1 | 0 | 1 |
| Answer4.jpg | 1 | 1 | 1 | 0 | 0 |
| Answer5.jpg | 0 | 1 | 0 | 0 | 1 |
| Answer6.jpg | 1 | 0 | 0 | 0 | 1 |
| Answer7.jpg | 0 | 1 | 1 | 0 | 0 |

F1 Score = ![](https://user-images.githubusercontent.com/1634660/67600935-76539680-f773-11e9-9b5c-5927fad5feac.png)


The second task will be subjectively assessed by judges. 
In addition to the .pdf file, you should also provide us with a repository with access to the code.


## Submission instructions

Submit once per 15 minut.
