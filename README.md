# SFIA-2
DEVOPS

# HZ Random Party Themes Generator
1. [Brief](#brief)
  + [My Solution](#solution)
2. [Trello Board](#trello)
  + [User Stories](#userstories)
  + [Initial Trello](#initialtrello)
  + [Progress Trello](#progresstrello)
  + [Final Trello](#finaltrello)
3. [Risk Assessment](#riskassessment)

4. [Architecture](#architecture)
  + [Application Flowchart](#appflow)
  + [Initial Database](#initialdatabase)
  + [Final Database](#finaldatabase)
  + [Wesbite Sitemap](#sitemap)
  + [Website Wireframe](#wireframe)
  
5. [Implementation/ Visual Representation of App](#implementation)
  
6. [Testingn App](#testing)
  + [Unit Testing](#unittesting)
  + [Coverage Testing](#coveragetesting)
  
7. [Deployment](#deployment)

8. [Retrospect](#retrospect)

9. [Authors](#authors)

10. [Acknowledgements](#acknowledgements) 


<a name ="brief"></a>
## 1. The Product Brief
To create:
  1. An application that generates “Objects” upon a set of predefined rules
  2. A micro-service orientated architecture for the application
  3. Utilisation of Flask,Jinja2 for front-end website and integrated API's while Python and MySQL for back-end
  4. Generating Random Objects
  5. Utilising Feature-Branch Model and creating an Ansible Playbook to install all dependencies via Playbook
  6. Utilising Jenkins, Ansible, Docker for CI/CD and Nginx for Load Balancing 

<a name ="solution"></a>
## My Solution
My application is created using Boostrap, Jinja2 and Flask for the Front-End and Python and MySQL for the Back-End Development.It is a website where user's can generate a party theme and each time, random party theme, outfit colour, location and ticket price would be generated. Lucky winner can also have free entry ticket to the party. User's input is also taken into consideration as if a user is a child, the theme of the party generated would be suitable for children for example "Princess Party" where as for adults it would display different results for example "Halloween Parrty". The website is user-friendly and responsive for better user experience. 

### Service 1: 
+ Renders website to the user
+ Takes User Input
+ Displays the theme generated from Service 4
+ Stores the displayed theme into the database

### Service 2:
+ Generates random colour of the outfit

### Service 3:
+ Generates random location, ticket price and theme party considering the user's age

### Service 4:
+ Calls Service 2 and Service 3 and generates output combined from Service 2 and Service 3 and displays it back to Service 1

### Technologies:
+ Nginx used as Reverse Proxy to load balance all microservices on Docker Swarm and distribute traffic among them
+ Using Ansible as Configuration Management tool to install all dependencies/packages
+ Using Jenkins to deploy Ansible Playbooks and automate Docker Swarm

<a name ="trello"></a>
## 2. Trello Board
Trello Board was used to plan, organize and prioritize my project so that not only all user requirements are fully met but to also meet project deadline. 


<a name ="userstories"></a>
### User Stories

[userstories]: https://i.imgur.com/UuDxumL.png

![userstories][userstories]

<a name ="initialtrello"></a>
### Inital Trello Board
Initial Trello board has all the product backlog, sprint backlog which is then broken down into small and manageable tasks. Once each task is completed, it is then moved to Done and during that process if any errors were encountered, those were listed in bugs.

[initialtrello]: https://i.imgur.com/6wF8cSO.png

![initialtrello][initialtrello]

<a name ="progresstrello"></a>
## Progress Trello Board

[progresstrello]: https://i.imgur.com/mOSXUUn.png

![progresstrello][progresstrello]


<a name ="finaltrello"></a>
## Final Trello Board

[finaltrello]: https://i.imgur.com/emJH2UG.png

![finaltrello][finaltrello]


<a name ="riskassessment"></a>
## 3. Risk Assessment
Risk Assessment was carried out to consider what could go wrong during the project and deciding on which control measures are to be taken in such situations. As a result, these control measures would help eliminate and reduce any risk involved during the project.

Below is the Initial Risk Assessment displayed in the Table:

[riskassessmentmatrix]: https://i.imgur.com/u2w7SrF.png

![riskassessmentmatrix][riskassessmentmatrix]


[riskassessment]: https://i.imgur.com/CmbI4ip.png

![riskassessment][riskassessment]


Below is the Final Risk Assessment displayed in the Table:

[finalriskassessment]:https://i.imgur.com/euUrgjE.png

![finalriskassessment][finalriskassessment]



<a name ="architecture"></a>
## 4. Architecture
Before bulding the application, design stage was considered, which involved series of steps to help me define and plan my application. 


<a name ="appflow"></a>

## Application flowchart
Application flowchart showing the design process of the application

[appflow]: https://i.imgur.com/2ybSWtt.jpg

![appflow][appflow]


## Micro-service orientated architecture for the application

[mic]: https://i.imgur.com/iWms8EJ.png

![mic][mic]

## Feature Branch Model
Using feature branch while still working on the app/creating new features and comitting to that branch locally and regularly unless the change is ready to be merged to the master branch. 

After the new features are revised they are now ready to merged to the master branch. On the master branch, the code is deployable and is deployed onto the production servers. This allows me to have stable versions which are ready for production through master branch.

[fbm]: https://i.imgur.com/k6Tl2Sm.png

![fbm][fbm]

<a name ="initialdatabase"></a>
## Initial Database
Below is the initial Database for my project where I had minimum of one table that stores the randomly generated objects/sentence that appears on the front-end. 

[initialdatabase]: https://i.imgur.com/gZMfgTu.png

![initialdatabase][initialdatabase]



<a name ="finaldatabase"></a>
## Final Database

This is my final Database where I also added users table, so that user's can also submit theme/message in case they couldn't find a fun theme for the party.As it is important to get feedback from the users to support their needs and demands.


[finaldatabase]: https://i.imgur.com/CZEOumu.png

![finaldatabase][finaldatabase]


<a name ="sitemap"></a>
## Website Sitemap
Sitemap was created which is a blueprint to show the structure of the website and how the pages are linked. 

[sitemap]: https://i.imgur.com/UaMzCeN.png

![sitemap][sitemap]

<a name ="wireframe"></a>
## Website Wireframe
Wireframe was created to help arrange the elements on the website and to achieve the optimum outcome. The wireframe was created considering the project brief of creating random objects while using micro-service architecture.

Below shows the initial wireframe of the home page.

[initialwireframe]: https://i.imgur.com/0YzOmpH.png

![initialwireframe][initialwireframe]


Below shows the final wireframe of the home page.

[finalwireframe]: https://i.imgur.com/5P1tCh2.png

![finalwireframe][finalwireframe]


<a name ="implementation"></a>
## 5. Visual Representation of App 

### Link to The Party Themes Generator :
### Manager Node
http://35.197.228.70/
### Worker Node
http://35.246.125.202/

## Home Page

[home]: https://i.imgur.com/u8pKOVK.png

![home][home]


## Submit Theme Page

[submittheme]: https://i.imgur.com/SOfLJam.png

![submittheme][submittheme]


## About Us Page

[about]: https://i.imgur.com/poLPNex.png

![about][about]

<a name ="testing"></a>
## 6. Testing
Testing the application to ensure it runs successfully. 
Two types of tests were carried out including unit testing and coverage testing.

<a name ="unittesting"></a>
## Unit Testing
+ Testing URL to check whether the app has been deployed successfully and each web page is up and running. 
+ Testing Database to ensure data gets inserted and deleted successfully via the web application to ensure there are no errors runnung the Dynamic Web Application and to validate each unit of the software performs as it is designed to do so.

### Unit Testing URLs:
All the web pages were tested and even pages that don't exist were tested too to ensure that the user can access what is accessible to them and can't access what is not accessible to them.

Below shows the result of the URL Testing carried out:

[urltest]: https://i.imgur.com/4VaNPx5.png

![urltest][urltest]

[urltest1]: https://i.imgur.com/nlR5Hm5.png

![urltest1][urltest1]

### Unit Testing Database:
Database tested to allow user to input as desinged to while submitting theme, storing the random theme generated into the database to ensure the database is fully functional.

Below shows all the testing/ queries carried out for Database:

[dbtest]: https://i.imgur.com/DDN71Cf.png

![dbtest][dbtest]

[dbtest1]: https://i.imgur.com/RYrClQx.png

![dbtest1][dbtest1]

### Unit Testing Service 2 File Reader:

[s2]: https://i.imgur.com/Ze2VTdL.png

![s2][s2]

### Combining the 3 types of Unit Testing:

[bothtest]: https://i.imgur.com/XuN8Xq5.png

![bothtest][bothtest]


<a name ="coveragetesting"></a>
## Coverage Testing
Coverage Testing carried out to generate metric that will show how much of the source is tested to assess the test suite quality.

### URL Coverage Testing:
 
 [urlcoverage]:  https://i.imgur.com/hKCsan7.png

![urlcoverage][urlcoverage]

### Database Coverage Testing:
 
  [dbcoverage]: https://i.imgur.com/T0asvua.png

![dbcoverage][dbcoverage]


### Combining All types of Coverage Testing:
 The coverage metrics went down when both URL and Database were tested together due to the complexity of the application and by importing more libraries.
 
  [bothcoverage]: https://i.imgur.com/RG0OiIL.png

![bothcoverage][bothcoverage]


### Sourcing the testing file to generate coverage report

 [all]: https://i.imgur.com/LoYcsaM.png

![all][all]

### HTML coverage report

[html]: https://i.imgur.com/BsVo5wd.png

![html][html]

### Comparison of coverage report:
While running the coverage test report for the whole application, it showed 38% of the source code tested whereas when sourcing the test file and running the coverage test , coverage report showed 100% result as all the tests in the testing file have been passed successfully.


<a name ="deployment"></a>
## 7. Deployment
The App was deployed using Jenkinns,Github and Docker hub. Github webhooks was also integrated to trigger the build whenever the developer commits any change to the branch where docker hub is connected to github so all the build process of images and pushing them onto the docker hub is done automatically.

 As Jenkins is connected to Github, this way when webhook was added to the job, it ensured that the build was triggered automatically everytime the code is commited to the Github.Therefore, Jenkins triggers the build automatically and then deploys ansible playbook which installs Docker on Manager and worker node and automates docker swarm. 

This prevents human error as ansible is a configuration management tool therefore, it deploys the same software to as many worker nodes automatically without installing them manually which not only saves time but also prevents human error.

Below is the diagram demonstrating the Technology Overview:

[deployment]:  https://i.imgur.com/244Tka0.png

![deployment][deployment]


## How the process works:

### 1. Jenkins waiting to trigger the build once change was fully committed:

[build]: https://i.imgur.com/IakNROG.png

![build][build]

### 2. Jenkins Build triggered automatically once change was committed:

[build2]: https://i.imgur.com/sZwSVBP.png

![build2][build2]

### 3. App Deployed successfully using Jenkins while automatically triggering build when code is committed to GitHub. Build process deploys the App onto the Development Environment:

[build3]: https://i.imgur.com/NNTYw8N.png

![build3][build3]


[build4]: https://i.imgur.com/gF56IrY.png

![build4][build4]

### 4. Deploying Ansible File to Install Docker on manager and worker node and automate docker swarm

[build5]: https://i.imgur.com/9wktd6W.png

![build5][build5]

### 5. Automatically deploying the stack 

[build6]: https://i.imgur.com/KeyBBbt.png

![build6][build6]

### 6. Tests the App using Pytest

[build7]: https://i.imgur.com/J2tbgwh.png

![build7][build7]

### 7. Docker Swamr Deployed Successfully 

#### Manager Node

[build8]: https://i.imgur.com/DJdVeMI.png

![build8][build8]

#### Services Replicated successfully on Manager Node

[b]: https://i.imgur.com/ov1elUJ.png

![b][b]

#### Worker Node

[build9]: https://i.imgur.com/16FVDSJ.png

![build9][build9]

## Security of the Application

+ **Container Security**: No ports are exposed , port 5000 is also not exposed to the world.

[security1]: https://i.imgur.com/xleRs34.png

![security1][security1]


+ **NGINX**: Only port 80 exposed which is doing reverse proxy into microservice 1.

[security2]: https://i.imgur.com/VBZGsTs.png

![security2][security2]

[security3]: https://i.imgur.com/h4w29UH.png

![security3][security3]

[security4]: https://i.imgur.com/PhWnPnD.png

![security4][security4]

+ **Jenkins**: Port 8080 for jenkins is not exposed to the world as Jenkins run on port 8080.
+ **Front- End**: The app is accessible to everyone using 0.0.0.0/0 firewall rule. 
+ **Firewall Rule**: Configuring firewall for Docker Swarm allowing it to run on port 2377 tcp.

[security5]: https://i.imgur.com/XLUiqJx.png

![security5][security5]

## List of technologies used:
+ Trello Board - Project Planning and Tracking Board
+ MySQL - Relational Database for Application
+ Python - Coding in Flask
+ Flask - Framework
+ Testing - Pytest (Unit Testing, Coverage Testing)
+ Github Project - Version Control System
+ Google Cloud Platform (MySQL DB, GCP VM)
+ Docker: Containerisation
+ Dockerhub: Repository for container images
+ Ansible: Configuration Management Tool
+ NGINX: Load Balancing
+ Jenkins - CI/CD Server for Deploying the Application


 

<a name ="retrospect"></a>
## 8. Retrospect

### What went well:

### Challenges faced:

### Future Improvements:

<a name ="authors"></a>
## 9. Authors

Hifza Zaheer

<a name ="acknowledgements"></a>
## 10. Acknowledgements

I acknowledge the help and support that I have received throughout my project, Special thanks to my tutor, Syed Ahmed for his guidance through each phase of the project which helped me achieve my potential.
