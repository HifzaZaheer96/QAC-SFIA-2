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
  5. Utilising Feature-Branch Model and creating an Ansible Playbook

<a name ="solution"></a>
## My Solution
My application is created using Boostrap, Jinja2 and Flask for the Front-End and Python and MySQL for the Back-End Development.It is a website where user's can organise a party and each time, random party theme, outfit colour, location and ticket price would be generated. Lucky winner can also have free entry ticket to the party. User's input is also taken into consideration as if a user is a child, the theme of the party generated would be suitable for children for example "Princess Party" where as for adults it would display different results for example "Halloween Parrty". The website is user-friendly and responsive for better user experience.  

<a name ="trello"></a>
## 2. Trello Board
Trello Board was used to plan, organize and prioritize my project so that not only all user requirements are fully met but to also meet project deadline. 


<a name ="userstories"></a>
### User Stories

[userstories]: https://i.imgur.com/B7WRuif.png

![userstories][userstories]

<a name ="initialtrello"></a>
### Inital Trello Board
Initial Trello board has all the product backlog, sprint backlog which is then broken down into small and manageable tasks. Once each task is completed, it is then moved to Done and during that process if any errors were encountered, those were listed in bugs.

[initialtrello]: https://i.imgur.com/SZcPjPZ.png

![initialtrello][initialtrello]

<a name ="progresstrello"></a>
## Progress Trello Board

[progresstrello]: https://i.imgur.com/SV1Qasy.png

![progresstrello][progresstrello]


<a name ="finaltrello"></a>
## Final Trello Board

[finaltrello]: 

![finaltrello][finaltrello]


<a name ="riskassessment"></a>
## 3. Risk Assessment
Risk Assessment was carried out to consider what could go wrong during the project and deciding on which control measures are to be taken in such situations. As a result, these control measures would help eliminate and reduce any risk involved during the project.

Below is the Initial Risk Assessment displayed in the Table:

[riskassessmentmatrix]: https://i.imgur.com/wU753n5.png

![riskassessmentmatrix][riskassessmentmatrix]


[riskassessment]: https://i.imgur.com/CmbI4ip.png

![riskassessment][riskassessment]


Below is the Final Risk Assessment displayed in the Table:

[finalriskassessment]: https://i.imgur.com/lVM8bXd.png

![finalriskassessment][finalriskassessment]



<a name ="architecture"></a>
## 4. Architecture
Before bulding the application, design stage was considered, which involved series of steps to help me define and plan my application. 


<a name ="appflow"></a>
## Application flowchart
Application flowchart showing the design process of the application

[appflow]: https://i.imgur.com/2ybSWtt.jpg

![appflow][appflow]


Micro-service orientated architecture for the application

[mic]: https://i.imgur.com/iWms8EJ.png

![mic][mic]

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
