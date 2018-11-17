# Challenges
A list of challenges prepared together with our sponsors:


* November 16-18th, 2018 - [#1 Skyhacks - AI Hackathon](#1skyhacks)
  - [ArcelorMittal - Computer Vision - UIC Wagon recognition - Computer-based solution challenge](#1sh-arcelormittal)
  - [NewVoiceMedia (Vonage) - Speech-to-text and NLP - Removing sensitive data from conversation transcriptions](#1sh-newvoicemedia-vonage)


## <a name="1skyhacks"></a>#1 Skyhacks
The biggest Hackathon in PL primarily focused on Artificial Intelligence.  
👉 300 spots for Hackers. 80 spots reserved for women 👩‍💻 #diversity  
👉 20 000+ PLN total prizes, 9 000 PLN grand prize  
👉 ArcelorMittal, NewVoiceMedia (Vonage), Google, Amazon, Microsoft, Oracle, Groupon, SAS Institute, Mayor of Gliwice, Silesian University of Technology, Geek Girls Carrots, Women in Technology, Women Techmakers Warsaw and more  
👉 Basic AI or Machine Learning skills required  
👉 Free entry, free food, free drinks + free extras!  
👉 First come, First served  
👉 Gliwice, November 16-18th 2018  
  
https://www.youtube.com/watch?v=nfnLM3U9cvM  

#ai #ml #artificialintelligence #machinelearning #hackathon #gliwice #wroclaw #cracow #katowice #silesia #warsaw #poland #berlin #vienna #prague #bratislava #budapest #london

## <a name="#1sh-arcelormittal"></a>ArcelorMittal - Computer Vision - UIC Wagon recognition - Computer-based solution challenge
### Description
**Problem**  
Hello! if you came to this repository, it means that you accept our challenge and think you can recognise the wagons identifier from a sequence of images extracted from our company's footage.

The data-set we are proposing for this challenge consists of the footage of the trains in transit in our company. Under the UIC standard, each wagon is marked according to [UIC wagon numbers ](https://en.wikipedia.org/wiki/UIC_wagon_numbers). 

Each train is recorded from both sides: left and right. For each train's folder, you have a left and right footage, as well as a _metadata.txt_ file with the label for each Wagon. Please bear in mind, that the labels of the wagons are in the same order of appearance in the footage. You will have to write an algorithm that identifies each wagon so that you can match the UIC code to the label.
**Targets / goals to be achieved:**  
The goal is to automatically identify from the video-frames the UIC code of wagon and provide the unique identifier as output.  

### Evaluation
**For this event, we have 67 trains footage split as follow**

- 49 trains footage for training. [Link here](https://jgferdiag.blob.core.windows.net/amp-skyhacks-2018-traindataset/Training.zip?sp=r&st=2018-11-16T19:50:18Z&se=2018-11-19T03:50:18Z&spr=https&sv=2017-11-09&sig=TI8l1qOUheq90w%2Fm0%2F6W9FRZv%2FPCfjefW4p4rWzl9zE%3D&sr=b)

- 10  trains footage for validation. [Link here](https://jgferdiag.blob.core.windows.net/amp-skyhacks-2018-traindataset/Validation.zip?sp=r&st=2018-11-16T19:50:48Z&se=2018-11-19T03:50:48Z&spr=https&sv=2017-11-09&sig=vWP2f7c%2BWxuxOxM8rpoVNAYcujm0EmCk2Mv%2B2BxB0o4%3D&sr=b)

During the event, you will be requested to submit for evaluation your algorithms into our test dataset, which consists of 8 trains footage. The metrics we will use to evaluate your algorithms are:
- Identify the frames for each wagon
- Identify the frames with full view of the UIC code
- And finally, the most challenging part is to read the UIC code numbers.

**Please note**

* All images should have removed images that contain faces of people, but if you'll find any faces - please let know skygate and ArcelorMittal   
* You will be provided metadata that contains the UIC code of each wagon on a train.  
* The wagons are in order, so the participants need to correlate these with the wagons (also in order).  

### Prizes
1st place - 9000 PLN  
2nd place - 4000 PLN  
3rd place - 2000 PLN  

### Honor Code
In addition to the behaviors outlined by the official competition rules, "cheating" encompasses any attempt to gain an edge in accuracy by using information that is outside of the provided Dataset, or an attempt to use the provided information in a way that is not intended. Examples of cheating include (but are not limited to):

* Attempting to use Datasets and references beyond those made available by the competition
* Attempting to abuse the competition infrastructure to gain an edge

Please note that skygate and ArcelorMittal reserves the right, but does not have the obligation, to review submitted code to disqualify any contributions demonstrating cheating, and skygate and ArcelorMittal reserves the right to determine what it believes, in its sole discretion, constitutes cheating. We respectfully request that you refrain from cheating.  

While skygate and ArcelorMittal reserves the right to take effective measures to detect and disqualify cheating, we ask that you personally abide by codes of honor and ethical behavior in your participation. We view this competition as a unique learning opportunity for all of us, equally for the organizers and the Skyhacks community, and we sincerely hope that you will join us in this goal with your most legitimate efforts.  

### Timeline

This is a two-stage competition consisting of a Training period and a Scoring period. In the Training period, teams will train their models in cloud environment based on the training set and the development set. During the Scoring period, the test set will be provided and the final score will be evaluated. Every time the team wants to submit their score, they need to psychically approach the judges table.  

* Training Period Start Date: Friday, November 16th, 2018, 11:00 PM GMT+1/CET

* Scoring Period Start Date: Sunday, November 18th, 2018, 7:00 AM GMT+1/CET

* Submission Deadline: Sunday, November 18th, 2018, 11:00 AM GMT+1/CET

* Judges Debating time: Sunday, November 18th, 2018, 11:00 AM - 1:00 PM GMT+1/CET

* Winners Announcement: Sunday, November 18th, 2018, 1:00 PM GMT+1/CET


You can still approach judges after 11:00 AM on Sunday, but your code need to be submitted to Github (or other repository) before the deadline - so be prepared to show the judges your commit date and hash.

The competition organizers reserve the right to update the contest timeline if they deem it necessary.

### Submission Instructions

You'll be given access to one or more cloud environments, thanks to the technical partners of the Hackathon:
* Oracle
* Microsoft
* Google
* Amazon

Assuming all these environment are providing "endless" possibilities and all vouchers are pretty generous (~$20-$300) as for 36 hrs of hacking - we ask your teams to measure and provide the time of computation either per each single row / result or the overall CSV submitted.

In this [link](https://jgferdiag.blob.core.windows.net/amp-skyhacks-2018-traindataset/submission_sample.csv?sp=r&st=2018-11-16T19:49:08Z&se=2018-11-19T03:49:08Z&spr=https&sv=2017-11-09&sig=yTYtoWdYA7s3O75yh6U6HO%2BJpmdwHra228aWTnO2r20%3D&sr=b), you have a sample of a submission .csv file. We evaluated the train 0_0_51_left. The file contains the following columns:

**team_name:** your team's id

**train_number:** the first digits of the folder, in this example: *0_0_51*

**left_right:** left

**frame_number:** is the number of the .jpg file

**wagon:** locomotive for the frames showing the locomotive of the train, and then a sequential numbering of consecutive frames showing each wagon

**uic_0_1:** a boolean flag that indicates that the UIC code is fully visible in the frame

**uic_label:** the UIC number

#### Submission Form

[ArcelorMittal Computer Vision - UIC Wagon recognition submission form](https://goo.gl/forms/6jQuLMmSsMCaOly93)

### Repository Requirements

See the [General Repository Requirements](#hackathon-repository-requirements).

## <a name="#1sh-newvoicemedia-vonage"></a>NewVoiceMedia (Vonage) - Speech-to-text and NLP - Removing sensitive data from conversation transcriptions

### Description

Original problem

**Setup**
Calls between agents and customers are recorded. Each call consists of two audio channels – agent and customer. Each audio channel is transcribed to text by a separate service. The transcription consists of everything that was said on the call.  
We can distinct couple of kinds of sensitive information:  
* Obvious personal data, like names, telephone numbers, email addresses, credit card numbers, etc.  
* Not obvious personal data, like descriptions of medical history, work experience, etc.  
* Non personal data looking like personal data, like public emails, call center telephone numbers, etc.  

**Problem**

Potential usage of the transcription might cause leakage of sensitive information. The transcripts might be used for various purposes:
* Agent training  
* Various presentations of how the contact center operates
* Providing examples of well and poorly led conversations
* Data for further analysis.  
In all those cases, the presence of sensitive data is undesirable. All sensitive data should be obfuscated or removed, but the context and meaning of the conversation should remain intact.  

As this problem extends the format of a Hackathon and it's too complicated, two other voice & text related problems are stated below:

**Problem for the Hackathon**

### Note
This is a Hackathon. If you see any of the provided tasks too difficult or too time consuming, try to solve just one, your team's goal is to get higher possible score in the time given, to win with other teams.  

tl;dr: Pick your battles.

#### Step 1 (30% of score) [Speech-to-text]  
You'll be provided the audio recordings in English. You'll be asked to convert them to text.

#### Step 2 (70% of score) [text-to-AMR]  
You'll be provided English sentences that you'll be asked to convert to AMR format.  

More information about AMR: http://amr.isi.edu



#### Train / Dev / Test split & dates
Datasets are split into `training` and `dev` sets. You'll receive proper transcriptions only for the `training` sets. After the Scoring Period Start Date you'll be provided with `test` sets.

### Evaluation
#### <a name="1sh-2-evaluation"></a>Part 1 (30% of score) [Speech-to-text]
In your training sets you'll find the original (*.trn), (*.flt), (*.doc) and (*.tbl) files. Your transcription files can look different, so in order to be able to compare in the evaluation files we will have this done:
* remove the timing information
* lowercase all words
* remove all the punctuation marks, like ~!?,.'-%[]<> '<L' 'L>' '<X' 'X>'
* remove all phrase that are describing sounds, like:
  * (H), (Hx), (TSK), (SNORT), (SLAP), (THROAT), (SWALLOW), (GROAN), (DRINK), (COUGH COUGH), WRITING, WHISTLE, (SNEEZE), (SNIFF), VO, WH  etc.
  * <VOX, VOX>, <BR, BR>, <YWN, YWN>, <DRINKING, DRINKING>, <WH, WH>, <Q, Q>, <P, P>, <PAR, PAR>,<SM, SM>, <HI, HI> etc.
  * single or multiple X
  * remove any digits
  * all the lines with >ENV:
  * remove anything else that you feel is not representing human speech
  


For example this part:
```
216.32 216.92   SHANE:      (H)
216.92 217.32   SHARON:     (H)= Yeah,
217.32 218.62               that takes two weeks to process.
218.62 218.82               I mean,
218.82 220.02               how do you [explain that to th-] --
219.22 219.32   KATHY:                 [Yeah but,
219.32 220.37               is the form in Eng]lish?
220.37 222.67   SHARON:     ... (H) They have a form in Spanish [al=so].
222.20 222.36   KATHY:                                          [Well,
222.36 223.30               even if ]it's in Spanish,
223.30 224.12               maybe they can't read.
```

Will look like this:

```
sharon, yeah that takes two weeks to process i mean how do you explain that to th
kathy, yeah but is the form in english
sharon, they have a form in spanish also
kathy, well even if it s in spanish maybe they can t read
```

And from there we will compare number of words well recognized only for those rows where the speaker has been recognized correctly. The accuracy will be calculated using this equation:

<img src="https://latex.codecogs.com/gif.latex?score=1-min(\left|\frac{LD(input,original)}{length(original)}\right|,1)" title="score=1-min(\left|\frac{LD(input,original)}{length(original)}\right|,1)" />

where:  
`score` - your final score ranging 0.0 - 1.0  
`input` - your submitted result  
`original` - the original transcription  
`LD` - [Levenhstein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance)

#### Part 2 (70% of score)[text-to-AMR]

The evaluation process might take some time as we will rely on the Smatch calculator provided by https://amr.isi.edu/ Team.

Please note some symbols from the Dataset might not be supported, like:
```
m / multi-sentence
alignments - see the doc inside dataset
etc.
```
To make sure which tags are supported, feel free to conduct a simple comparison of the exact two AMRs (just duplicate your input files)

Any improvements to the Smatch calculator are well seen, however extend the scope of this Hackathon. Go ahead and feel free to open a pull request in the [Author's repository](https://github.com/snowblink14/smatch/issues).


### Data
#### Part 1 (30% of score)
You'll receive access to a dataset of ~1.4GB speech & text file.

**Please note:**

* Audio files are in WAV format  
* For the training data you'll be provided with RAW transcriptions  
* For the evaluation purposes, the transcriptions need to be simplified - see [evaluation information](#1sh-2-evaluation)  

[Voice Part 1 - Dataset](https://drive.google.com/file/d/1G8MJ_b4DsIYqCchlSc8fGLJKRPNq9z3K)

#### Part 2 (70% of score)
You'll receive access to a dataset of ~30MB text file.

[Voice Part 2 - Dataset](https://drive.google.com/file/d/1FBEIlkuPIPZ0AlPBZAI3ABA6nRyxLGW_)

**Please note**

* All images should have removed images that contain faces of people, but if you'll find any faces - please let know skygate and ArcelorMittal   
* You will be provided metadata that contains the UIC code of each wagon on a train.  
* The wagons are in order, so the participants need to correlate these with the wagons (also in order).  



### Prizes
1st place - 3000 PLN + 2 x Amazon Echo dot  
2nd place - 2000 PLN + 1 x Amazon Echo dot  
3rd place - 1000 PLN + 1 x Amazon Echo dot  


### Honor Code
In addition to the behaviors outlined by the official competition rules, "cheating" encompasses any attempt to gain an edge in accuracy by using information that is outside of the provided Dataset, or an attempt to use the provided information in a way that is not intended. Examples of cheating include (but are not limited to):

* Attempting to use Datasets and references beyond those made available by the competition
* Attempting to abuse the competition infrastructure to gain an edge

Please note that skygate and NewVoiceMedia reserves the right, but does not have the obligation, to review submitted code to disqualify any contributions demonstrating cheating, and skygate and NewVoiceMedia reserves the right to determine what it believes, in its sole discretion, constitutes cheating. We respectfully request that you refrain from cheating.  

While skygate and NewVoiceMedia reserves the right to take effective measures to detect and disqualify cheating, we ask that you personally abide by codes of honor and ethical behavior in your participation. We view this competition as a unique learning opportunity for all of us, equally for the organizers and the Skyhacks community, and we sincerely hope that you will join us in this goal with your most legitimate efforts.  

### Timeline

This is a two-stage competition consisting of a Training period and a Scoring period. In the Training period, teams will train their models in cloud environment based on the training set and the development set. During the Scoring period, the test set will be provided and the final score will be evaluated. Every time the team wants to submit their score, they need to psychically approach the judges table.  

* Training Period Start Date: Friday, November 16th, 2018, 11:00 PM GMT+1/CET
* Scoring Period Start Date: Sunday, November 18th, 2018, 7:00 AM GMT+1/CET
* Submission Deadline: Sunday, November 18th, 2018, 11:00 AM GMT+1/CET
* Judges Debating time: Sunday, November 18th, 2018, 11:00 AM - 1:00 PM GMT+1/CET
* Winners Announcement: Sunday, November 18th, 2018, 1:00 PM GMT+1/CET

You can still approach judges after 11:00 AM on Sunday, but your code need to be submitted to Github (or other repository) before the deadline - so be prepared to show the judges your commit date and hash.

The competition organizers reserve the right to update the contest timeline if they deem it necessary.


### Submission Instructions

You'll be given access to one or more cloud environments, thanks to the technical partners of the Hackathon:
* Oracle
* Microsoft
* Google
* Amazon

Assuming all these environment are providing "endless" possibilities and all vouchers are pretty generous (~$20-$300) as for 36 hrs of hacking - we ask your teams to measure and provide the time of computation either per each single row / result or the overall CSV submitted.

#### For the 1st part of the task:
The submitted CSV should consist of three columns:
- Audio file ID
- Speaker name in lowercase
- Text in lowercase and without punctuation marks

#### Submission Form

[Sample submission DEV CSV](https://drive.google.com/file/d/148--_ECNeuPl2uAmSIG0aaV23NK1h8k1)

[NewVoiceMedia - Part 1 - Speech-to-Text submission](https://goo.gl/forms/lYmcbLJSdkh1DIHL2)


#### For the 2nd part of the task:

The submitted CSV should consist of three columns:
- Sentence ID
- AMR graph  (don't use end-of-line character like \r\n etc.) - make sure the Smatch calculator recognizes your graph

The submission process is to physically approach judges, but be prepared to show:
- A submission CSV file
- URL & hash of the Github commit

#### Submission Form

Sample submission DEV CSV - it's part of the dataset file.

[NewVoiceMedia - Part 2 - Text-to-AMR submission](https://goo.gl/forms/QGc2KGJIRXzgQrPr2)


### Repository Requirements

See the [Hackathon Repository Requirements](#hackathon-repository-requirements).


## <a name="#hackathon-repository-requirements"></a>Hackathon Repository Requirements
Eventually all the solutions (completed or not) need to reside on Github under the Creative Commons license. During the competition however, your code cannot be public so other participants won't be able to see it.

Therefore we suggest the following:

During the competition your Github repository should be password protected, password should be available for your team members and the judges only. You can use [git-crypt](https://github.com/AGWA/git-crypt) or any other tool / solution for that. The goal is to make sure your code is timestamped and you are not applying with code that was committed & pushed after certain deadline.

Your Github repository should be totally decrypted after Submission Deadline, so other teams can also help verifying correction of your solution as well.

The repository should consist of a description how to run the computation or ideally should run them within one command: `make start`. The whole environment setup should also be described in a README.md file. Judges can ask to add their public SSH keys should to the machine where the computation has been run to make sure about the computation times.

