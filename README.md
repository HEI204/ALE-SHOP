# ALE-SHOP

#### Description:
It is my final project for CS50 which is web application about online shopping site using Flask to develop. For this website, it requires all customers to create their own account first in order to buy the product on the site. After the user have created their own account, it will provide $200000 to the account by default. Then the user can use the money to buy the product that they would like to buy via add to the cart and purchase it if they have enough money.

Also, admin/manager can also use their pre-registered account to login in order to check and update the product information or the order information. (Account: admin123, Password: admin)

## Introduction

### User page
- index page: <br>
For the index page, it will show all the product that are available on the website and allow user to click 'Add to Cart' or click 'More Info' for each product.
![image](https://user-images.githubusercontent.com/78290169/169677981-bf16a426-ea98-4e54-88e1-19aad7f08d48.png)

- Register page: <br>
If a user do not have their own account, then the user need to create their own account, it will also check for the uniqueness of the username, validation for password and email in order to avoid any error during registration
![image](https://user-images.githubusercontent.com/78290169/169677986-d5eb2522-fd47-4ece-a73a-c27393f7e34c.png)

- Login page: <br>
If user have their own account, then the user can login their own account, it will check for the existance for the username that you input and correctness for the password with that username
![image](https://user-images.githubusercontent.com/78290169/169677993-e99b877f-c5b2-4aed-afe9-7f2f8fc5a291.png)

- Add to Cart: <br>
After user have login their account, user can add any product to the cart if they are interested in that product by clicking 'Add to Cart' button for that product and it will shows a sucessful message about added to the cart. If a user would like to buy the product in the cart then they can click 'Confirm Purchase' for purchase all items in the cart or user can click 'Remove' if they would like to remove the product in the cart.  Also, if a user do not have enoguh money to buy it, it will show a failure message to tell the user.
![image](https://user-images.githubusercontent.com/78290169/168472507-abe453cc-4cf6-47d1-ac5d-09e64d5da6d1.png)

- Product info page: <br>
After user clicked the button "More Info" for the product in index page, it will redirect to another page which have more detail information regarding to that product
![image](https://user-images.githubusercontent.com/78290169/169678082-dae95578-550b-4af6-ba9d-bf1ed6c05959.png)


- History page: <br>
If a user have purchase the items in the cart, then user can check their order information on the history page. Also, user can click 'View Detail' to check what product they have bought for that order
![image](https://user-images.githubusercontent.com/78290169/168472515-0cb5f30d-5f53-43f5-acfd-ca87c3cb3337.png)
![image](https://user-images.githubusercontent.com/78290169/168472526-00ad621a-c9a0-4701-8b0a-ba1c7b6d1fee.png)

- Add Cash: <br>
User can add any amount of cash that they would like to add by input the amount of cash in the input box and it will update immediately
![image](https://user-images.githubusercontent.com/78290169/168472532-e0901053-e2a6-41c1-87c4-5c86fbccf9cd.png)

### Admin page
- Dashboard: <br>
Admin can view the product info and click update for update the relevant information about the product
![image](https://user-images.githubusercontent.com/78290169/168472544-42831b7f-4ba8-4625-8274-f2144a49c181.png)

- Update Product <br>
If admin click the button 'update' in the dashboard, then it will goes to the page for admin to update the information of that particular product
![image](https://user-images.githubusercontent.com/78290169/168472552-5642ca0b-1291-4109-9eac-366dcf5755b5.png)

- Add Product <br>
Admin can also add product to the database by input relevant information based on the form 
![image](https://user-images.githubusercontent.com/78290169/168472575-ddf7cdc2-ce4e-4f18-8e73-3d1a8106c9bc.png)

## Reference:
- <a href="https://youtu.be/Qr4QMBUPxWo">Flask Course - Python Web Application Development</a> (Inspiration from this video and take reference about the page design)
- Logo Design from <a href="https://www.freelogodesign.org/">FreeLogo Design</a>
- Stack Overflow
- Bootstrap
- W3School
