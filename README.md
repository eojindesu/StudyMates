# STUDY MATES

## 1. Project Description
> 2023.04. - 2023.05.

### Contests
📌 2023 웹클라이언트컴퓨팅 강의 중간 프로젝트

<br>

### 프로젝트 소개
'STUDY MATES' 는 사용자들이 각자의 관심사나 목표를 공유하고, 다양한 분야의 그룹 스터디를 구성해 참여할 수 있는 웹서비스입니다.
이는 사용자들이 보다 편리하고 쉽게 스터디 그룹을 만들고 참여할 수 있는 서비스를 제공하여, 그들의 학습 및 성장을 돕는 것을 목적으로 합니다.

<br>

## 2.1. 사용 가이드

To use this template to start your own project:

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin startproject <project_name> .

<br>

## 2.2. 시작 가이드

Activate the virtualenv for your project.

<br>

Then simply apply the migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate
    
You can now run the development server:

    $ python manage.py runserver
---

## 3. Stacks

### Environment
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)

### Development
![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=Bootstrap&logoColor=white)

### Front-End
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white)

---

## 4. 화면 구성
| 메인 페이지  |  JOIN 페이지   |
| :-------------------------------------------: | :------------: |
|  <img width="329" src="https://github.com/meoowwing/StudyMates/assets/124228910/2658ce1a-64fb-40a9-a172-8316b4664a1c.png"/> | <img width="329" src="https://github.com/meoowwing/StudyMates/assets/124228910/ae79824f-c483-4ed8-bd2d-e13112080d01.png"/>|
| BOARD 페이지  |  ToDoList 페이지   |
| <img width="329" src="https://github.com/meoowwing/StudyMates/assets/124228910/1e3a222f-ddc5-4e3e-a39b-77bfc11bfaaa.png"/> | <img width="329" src="https://github.com/meoowwing/StudyMates/assets/124228910/26c48625-a1a5-4309-b2b3-709a645f900b.png"/>

---

## 5. 주요 기능

### ⭐️ 스터디 그룹 개설 및 참여 기능
- JOIN 게시판을 활용하여 복잡한 절차를 거치지 않아도 간단한 정보를 입력하면 쉽게 스터디 그룹을 만들 수 있습니다.
- 참여자 또한 다양한 분야의 스터디 중 각자의 관심사나 목표에 맞는 그룹을 찾아 참여할 수 있습니다.

### ⭐️ 사용자 계정 관리 기능
- 사용자는 프로필 사진, 이메일, 비밀번호, comment 변경 가능
- 로그인/로그아웃/회원가입/회원탈퇴 가능

### ⭐️ 서로 소통하고 자료를 공유할 수 있는 게시판 기능
- BOARD 게시판을 활용하여 스터디원들은 자료 및 질문과 조언을 공유하고 서로 소통할 수 있습니다.

### ⭐️ 일정을 관리할 수 있는 To Do List 기능
- TODO 페이지를 활용하여 사용자는 개개인의 일정 및 할 일을 정리할 수 있습니다.
