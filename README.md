# ALE-SHOP

#### Description:
It is my final project for CS50 which is web application about online shopping site using Flask to develop. For this website, it requires all customers to create their own account first in order to buy the product on the site. After the user have created their own account, it will provide $200000 to the account by default. Then the user can use the money to buy the product that they would like to buy via add to the cart and purchase it if they have enough money.

Also, admin/manager can also use their pre-registered account to login in order to check and update the product information or the order information.

## Introduction

- index page: 

For the index page, it will show all the product that are available on the website and allow user to click 'Add to Cart' or click 'More Info' for each product.
![image](https://user-images.githubusercontent.com/78290169/148876031-8cc09787-32bf-4f2b-b154-2b54bb771826.png)

- Register page:

If a user do not have their own account, then the user need to create their own account, it will also check for the uniqueness of the username, validation for password and email in order to avoid any error during registration
![image](https://user-images.githubusercontent.com/78290169/148876156-a10fc56f-73b0-476a-b9b9-6057413484ec.png)

- Login page:

If user have their own account, then the user can login their own account, it will check for the existance for the username that you input and correctness for the password with that username
![image](https://user-images.githubusercontent.com/78290169/148876248-1104f652-c31f-474b-a3a0-e0c24fc1ff7d.png)

- Add to Cart:

After user have login their account, user can add any product to the cart if they are interested in that product by clicking 'Add to Cart' button for that product and it will shows a sucessful message about added to the cart.

If a user would like to buy the product in the cart then they can click 'Confirm Purchase' for purchase all items in the cart or user can click 'Remove' if they would like to remove the product in the cart. 

Also, if a user do not have enoguh money to buy it, it will show a failure message to tell the user.
![image](https://user-images.githubusercontent.com/78290169/148876438-928edfb4-4720-474c-9cba-2df1d4779e23.png)

- History page:

If a user have purchase the items in the cart, then user can check their order information on the history page. Also, user can click 'View Detail' to check what product they have bought for that order
![image](https://user-images.githubusercontent.com/78290169/148876899-70cb7a1f-19c0-4021-b269-20d88689220b.png)
![image](https://user-images.githubusercontent.com/78290169/148876952-cb0e0bde-5e33-4ca6-afb7-1172d27954fd.png)

- Add Cash:

User can add any amount of cash that they would like to add by input the amount of cash in the input box and it will update immediately
![image](https://user-images.githubusercontent.com/78290169/148876836-07e668a0-e2cd-4799-a504-f07de9af384b.png)

## Reference:
- <a href="https://youtu.be/Qr4QMBUPxWo">Flask Course - Python Web Application Development</a> (Inspiration from this video and take reference about the page design)
- Stack Overflow
- Bootstrap
- W3School
