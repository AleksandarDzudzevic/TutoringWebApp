# CS_IA_Aleks TutorFlix web application
![](https://github.com/AleksandarDzudzevic/CS_IA_Aleks/blob/main/cs_ia_pic.jpg)
Fig.1 shows the picture created for TutorFlix using Dream AI[^1] generated on the prompt "Art representing Tutoring services, presenting a tutor and a student".

## 1. [Criteria A: Planning](#criteria-a-planning)

1.1. [Definition of the problem](#problem-definition)

1.2. [Rationale for proposed solution](#rationale-for-proposed-solution)

1.3. [Design Statement](#design-statement)

1.4. [Success Criteria](#success-criteria)
## 2. [Criteria B: Design](#criteria-b-design)

2.1[System Diagram](#system-diagram)

2.2. [Wireframe Diagram](#wireframe-diagram)

2.3. [ER Diagram](#er-diagram)

2.4. [UML Diagram](#uml-diagram)

2.5. [Flow Diagram](#flow-diagram)

2.6. [Test plan](#test-plan)

2.7. [Record of tasks](#record-of-tasks)

## 3. [Criteria C: Development](#criteria-c-development)

3.1.[Tools and techniques used](#tools-and-techniques-used)

3.2. [Sources](#sources)

3.3[Development](#development)

## 4. [Criteria D: Functionality](#criteria-d-functionality)
 
4.1 [SNS Video](#video-showcase)

## 5. [Criteria E: Evaluation](#criteria-e-evaluation)

5.1 [Table of Evaluation](#evaluation-table)

## 6. [Appendix](#Appendix)
# Criteria A: Planning

## Problem Definition
As a student, I often struggled with not having a place to find the right tutor. Just like many, I ended up going with the tutors recommended by friends or relatives, which usually turned out to be better at selling their services than actually teaching and that bothered me. I also struggled with finding ones that lived close to me, and as I usually just got their phone number as a contact, I wasn't aware of who they were and how much they charged. I got contacted by my client, a teacher, who saw a similar issue and explained that in the past he tried using online selling platforms such as eBay or Craigslist to post his advertisement for tutoring services, but was unsuccessful as the students that wanted to find him couldn't due to many other tutors teaching the same subject. Even with less experience, charging too much, and leaving far away, the number of other advertisements made it impossible for him to find students, even though he thought in 2 different languages which gave him a competitive advantage. To change this, my client requested a web application that would serve as a multi-language tutoring platform where students can find tutors that are well-ranked not well-advertised, live close to them, and are within their price range so that tutoring services can finally be on the level that they are supposed to. This problem definition was established with the help of the data gathered through questionnaires.(referred to in the [appendix](#appendix))



## Rationale for Proposed Solution
To revolutionize tutoring services and allow the best-ranked tutors to get the most exposure, instead of the ones with the best advertising, I have decided to develop a web application for my client that will serve as an inclusive platform that will connect highly ranked tutors and students seeking their help, allowing the most optimal learning experience.

## Design Statement
I will design an innovative web application that will make connecting tutors and students easier. The development will be done using the software Flask framework in Python, CSS, and HTML. It will take around 10 weeks to develop and will be evaluated according to the success criteria stated below by the client.

### Why Web Application?
Web applications are more adequate when developing a platform that offers services like the one I am making because it allows easier access to many different tutors across multiple devices without the need for downloading and installing an application. With a constant addition of new tutors across different subjects, the web application doesn't ask for constant updates. Students that are looking for a tutor can simply access the website through a web browser on their desktop or mobile devices. This increases the potential user number and makes it easier for users to share their experience with tutors with others, allowing high-quality tutors to jump out from the rest. Lastly, web applications can be maintained easily. They can be optimized for search engines, making it easier for new users to discover and join this platform both as tutors and as students, depending on their needs.

### Why Python?
Python contains many versatile features, which make it a better choice compared to other languages, for example, PHP[^2]. Python's Flask framework is ideal for developing a website for a tutoring platform due to its lightweight and flexible nature [^3]. Flask's simplicity and ease of use make it an excellent choice for this project, allowing developers to focus on the website's core features and functionality. It also offers a range of libraries and extensions, making it easier to implement complex features such as authentication and database connectivity, when compared to its competitors such as PHP or ruby [^4]. With Python's object-oriented programming, developers can write code that is easy to read, modify, and maintain. This is essential when creating a complex web application such as a social network website. Additionally, Python has an active community of developers who offer support and resources, making it easier to learn and develop with the language.

### Why SQL?
To store the vast amounts of data needed for an online tutoring platform, a reliable and efficient database is essential. While non-SQL databases can be an option, SQL databases offer several advantages that make them better suited for this purpose. The main advantage of SQL databases is their ability to handle large amounts of data efficiently, thanks to their relational structure[^5]. The relational structure of SQL databases makes it easier to manage and query data, as it is stored in tables. This feature also ensures that data is consistent and accurate, as it is subject to strong data integrity constraints[^6]. With all the data that is being stored for both student and tutor accounts, an SQL database is essential to ensure efficient data handling and management.


## Success Criteria
1) Tutoring platform will have a secure register system, unique for student and tutor accounts with access to different features on the platform (possible Google sign-in)
>[ I often struggled with not having a place to find the right tutor/I usually just got their phone number as a contact]
2) Tutoring platform will contain useful filter options such as search by name, city, subject, and price range.
>[I also struggled with finding ones that lived close to me, and as I usually just got their phone number as a contact, I wasn't aware of who they were and how much they charged]
3) Tutoring platform will allow tutor accounts to upload/delete multiple tutoring posts for different subjects and topics that they offer to teach, all on one account.
>[in the past he tried using online selling platforms such as eBay or Craigslist to post his advertisement for tutoring services, but was unsuccessful]
4) Tutoring platform will have a grading system for tutors and will list tutors by highest average grade so that the best-performing ones gain the most exposure.
>[ which usually turned out to be better at selling their services than actually teaching]
5) Tutoring platform will allow students to see all posts by a specific tutor.
>[was unsuccessful as the students that tried to find him couldn't due to many other tutors teaching the same subject.]
6) Tutoring platform will have multiple language features.
>[even though he thought in 2 different languages/would serve as a multi-language tutoring platform]
# Criteria B: Design
## System Diagram
![](https://github.com/AleksandarDzudzevic/CS_IA_Aleks/blob/main/IA%20System%20DiagramLAST.png)
Fig.2 shows the system diagram of the online tutoring platform.
## Wireframe Diagram

## ER Diagram

## UML Diagram

## Flow Diagram

## Test plan
|Test Number|Description|Test Type| Target|Procedure|Expected Outcome|
|-----------|-----------|--------|-----------|-----------------|----|


## Record of Tasks
| Task No | Planned Action                                              | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
|1|Write problem definition (Planning)|Have a clear problem that states the issue, its consequences, and a clear approach and solution that is being proposed| 20 min |8.7.2023 |A | 
|2|First client meeting: success criteria and required information (Planning)|Have a first client meeting and get the client to state the success criteria and basic information needed in order to establish a design statement and rationale for the solution that will be proposed to the client | 30 min|10.7.2023 |A |
|3|Write the first version of the rationale for the proposed solution and design statement (Planning)|Write down the rationale and design statement that will be presented to the client |35 min |10.7.2023 |A |
|4| Rewrite rationale for the proposed solution (Planning| Rewrite design statement so that it better explains methodology and tools that will be used for this web application development| 15 min | 11.7.2023| A|
|5| Design first version of the System diagram (Design)| Have the system diagram of the web application finsihed|20 min | 13.7.2023| B| 
|6| Add table of content (Planning)	 | Add table of content at the top of the file that will allow easier inspection of the project| 15 min|13.7.2023 | A|
|7| Construct the first version of database structures needed for the web application (Design)| Have the sketch of the databases for the initial idea of how the web application will be structured| 14.7.2023|30 min| B|
|8| | | | | |
|9| | | | | |
|10| | | | | |
|11| | | | | |
|12| | | | | |
|13| | | | | |
|14| | | | | |
|15| | | | | |
|16| | | | | |
|17| | | | | |
|18| | | | | |
|19| | | | | |
|20| | | | | |
|21| | | | | |
|22| | | | | |
|23| | | | | |
# Criteria C: Development
## Tools and techniques used
## Sources
## Development

# Criteria D: Functionality
## Video showcase

# Criteria E: Evaluation
## Evaluation table
|Criteria number| Criteria| Final product| Criteria success|
|---------------|----------|-------------------------------|--------------|

## Client interview

## Recommendation


# Appendix
![](https://github.com/AleksandarDzudzevic/CS_IA_Aleks/blob/main/client_consultation1.png)

 ### The first client consultation was done remotely on July 10th, 2023 13:15 pm, during which success criteria were established.
[^1]: Dream AI prompt: "Art representing Tutoring services, presenting a tutor and a student". 6 July 2023 https://dream.ai/create
[^2]: Sengar, Ritesh. “Python vs PHP: Which Is Better for Web Development?” Hackernoon, 7 Jan. 2021, hackernoon.com/python-vs-php-which-is-better-for-web-development-cj1236mj. 
[^3]: "Welcome to Flask." Flask Documentation, 15 Jan. 2023, flask.palletsprojects.com/en/2.1.x/. 
[^4]: Grinberg, Miguel. Flask Web Development: Developing Web Applications with Python. 2nd ed., O'Reilly Media, Inc., 2018. 
[^5]: “What Is a Database?” Oracle, https://www.oracle.com/database/what-is-database/. 
[^6]: "What is SQL?" W3Schools, W3Schools, https://www.w3schools.com/sql/
[^7]: https://www.smashingmagazine.com/2010/01/color-theory-for-designers-part-1-the-meaning-of-color/
[^8]: 4. Auth0. “JSON Web Tokens.” Auth0 Docs, https://auth0.com/docs/secure/tokens/json-web-tokens. 
