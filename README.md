# Pizza Ordering Service
> Practicing using Django as server framework and gaining experience with relational database design.

> 관계형 데이터베이스 디자인과 Django 서버 프레임워크를 연습해보기 위한 웹 서버 개발.

## Pizza Restaurant's Online Ordering Service
- For CS50 Web Programming with Python and JavaScript - project 3.
- Created an online ordering service for a pizza restaurant.
- Used Django as the server framerwork.


## 온라인 피자 주문 서비스 개발
- 하버드의 CS50 MOOC(edX)의 Web Programming with Python and JavaScript 수업의 프로젝트 3.
- 온라인으로 피자를 주문할 수 있는 웹 애플리케이션 개발.
- Django를 서버 프레임워크로 사용함.
- 


## what I learned | 무엇을 배웠는가
> This

> Importance of Understanding ORM (Object Relational Mapping) with Databases
- 클래스 정의와 객체 구분하기
    - ex. order class: 객체 order1, order2 만들 수 있음
    - class 정의에 foreignkey field가 있으면 이거는 그 class의 __object__와 연결이 되는 것이다! (not the actual class)
- 모델/table 연결시키기
    - inbetween table 생각하며 어떻게 연결시킬지 생각하기
- multiple instance of one model을 한 model의 object와 link.
    - 방법: 多개인 모델 안에 foreign key 정의하여 다른 모델과 연결 (그럼 하나인 모델이 related_name으로 정의되는 reverse accessor로 다른 것을 모두 접근할 수가 있다!)
    - 그림으로 나타내기!! 하나가 여러개와 연결되는 모습
    - ex. 1 post with multiple images
    - ex. 1 order with multiple pizzas
- cf) choice option in fields for models vs. creating separate model and accessing by foreign key
    - 둘 다 foreign key로 접근하는 
    - ex. flight에 origin으로 airport 객체 지정가능 (flight 1 = 홍콩에서 출발)
    - code로 직접 수정해야 함 vs. admin에서 수정 가능 (GUI)
    - 결국, separate model 방식이 더 나음.
