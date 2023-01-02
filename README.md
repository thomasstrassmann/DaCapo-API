# DaCapo RESTful API
## The backend API for the DaCapo React Project

![Overview of the DaCapo-API](./static/img/documentation/root-route.png  "Overview of the DaCapo-API")

[Click here for the full website access](https://dacapo-api.herokuapp.com/)



## Frontend Project (React)
[Click here to see the frontend repository](https://)


## Table of contents
1. [Introduction](#introduction) 
2. [Preparation](#preparation)
3. [Development](#development)
4. [CRUD](#crud)
5. [Testing](#testing)
6. [Deployment](#deployment) 
7. [Notes](#notes) 
8. [Credits / attributes](#credits) 



## Introduction 
This repository is used for version control and documentation of the DaCapo-API development process. In the following sections, general information about the approach and the different functionalities of the interface are listed, such as the schema design (models), manual and automatic testing, CRUD operations, deployment process, etc. 

## Preparation
In terms of preparation for API development, many issues played a role: 
* Which data should be queried / stored? What is really necessary, or perhaps even redundant? 
* How should this data be structured and built? What are the constraints on the data fields? 
* How do data models relate to each other? Which dependencies exist? 
* What do the permissions look like? What are non-authorized visitors allowed to do and what not? 

In order to get an answer to these and several other questions, the data model was visualized using an entity relational diagram. This is the quickest way to visualize the schema design.

![ERD of the DaCapo-API](./static/img/documentation/erd-dacapo-api.png  "ERD of the DaCapo-API")

The creation of the ERD was actually the first step and was used as a guide during development. 
 
## Development

The development process was aligned with the ERD as described, whereby the ERD was essentially determined by the user stories of the frontend. From this point of view, all functions and options of the frontend were the source of ideas for the backend development and must therefore not be omitted at this point: 

[Click here to see the user stories of the frontend](https://)

In the following, the development process is described in more detail: 
The DRF repository and project were started first. To directly cover all security measures, environment variables (secret key and cloudinary url) were created and committed only after updating the settings. This ensured that no sensitive content was published. 

Subsequently, the profiles, instruments, bookmarks and followers apps were designed, one after the other. It was avoided to work synchronously on different apps and to finish first one app completely. This has some advantages: 
* Focus on the content and increased concentration
* Better overview (less open tabs in the editor)
* Faster development

The individual steps of the app development always followed the same sequence: 
* Development of the model according to ERD specifications
* Creation of the serializer
* Creation of the views and the corresponding URLs
* updating the main URL patterns

At first, the views were supposed to use the APIView to write more explicit code, but due to time constraints, generic views were used in the further course. These achieve the same with much less code and time. To create uniformity, all views that used the API view were refactored. 


Once the base of all apps was in place, more features were added towards the end of API development. These included among others: 
- Implementation of count method in bookmarks, followers and instruments to show the current state of the data.
- The use of a search field for instruments.
- The creation of filters in instruments and profiles (e.g. filter by instrument category or by popularity).
- Pagination.
- Cosmetic changes like the DateTime format.
- The development of a compressed root url with useful hints (endpoints). 




## CRUD


## Testing 

The API was tested manually as well as automatically. For a better overview, these two areas are now treated separately from each other. 

**Manual testing**



**Automatic testing**


The suite consists of 15 tests, all of which pass at the time of project release.
![Test suite](./  "Test suite")


## Deployment 


[You can access the deployed version right here](https://)


## Notes

**Security**

In the course of the creation attention was paid to security at all times. All sensitive information is stored in environment variables and at no time was the project deployed to Heroku with sensible / critical information accessible. 

**Requirements**




**Custom models**




## Credits
