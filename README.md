# ALE-SHOP

#### Description:
It is my final project for CS50 which is web application about online shopping site using Flask to develop. For this website, it requires all customers to create their own account first in order to buy the product on the site. After the user have created their own account, it will provide $200000 to the account by default. Then the user can use the money to buy the product that they would like to buy via add to the cart and purchase it if they have enough money.

Also, admin/manager can also use their pre-registered account to login in order to check and update the product information or the order information. (Account: admin123, Password: admin)

## Introduction

### User page
- index page: 

For the index page, it will show all the product that are available on the website and allow user to click 'Add to Cart' or click 'More Info' for each product.
![image](https://user-images.githubusercontent.com/78290169/155998032-f329b304-4be7-470f-8d8f-73d1273e3438.png)

- Register page:

If a user do not have their own account, then the user need to create their own account, it will also check for the uniqueness of the username, validation for password and email in order to avoid any error during registration
![image](https://user-images.githubusercontent.com/78290169/155998112-3f4f215c-188b-4296-95da-26824d504053.png)

- Login page:

If user have their own account, then the user can login their own account, it will check for the existance for the username that you input and correctness for the password with that username
![image](https://user-images.githubusercontent.com/78290169/155998250-74ea6e4c-82cf-4763-87df-06e8d9ea436d.png)

- Add to Cart:

After user have login their account, user can add any product to the cart if they are interested in that product by clicking 'Add to Cart' button for that product and it will shows a sucessful message about added to the cart.

If a user would like to buy the product in the cart then they can click 'Confirm Purchase' for purchase all items in the cart or user can click 'Remove' if they would like to remove the product in the cart. 

Also, if a user do not have enoguh money to buy it, it will show a failure message to tell the user.
![image](https://user-images.githubusercontent.com/78290169/155998766-39f182f6-9c9d-4386-9a38-b0e303687279.png)

- History page:

If a user have purchase the items in the cart, then user can check their order information on the history page. Also, user can click 'View Detail' to check what product they have bought for that order
![image](https://user-images.githubusercontent.com/78290169/155998806-a226eb77-e0d9-46c0-89d4-8e4e4234566e.png)
![image](https://user-images.githubusercontent.com/78290169/155998829-a3015686-52be-455f-8e3f-c2cfbaa562fe.png)

- Add Cash:

User can add any amount of cash that they would like to add by input the amount of cash in the input box and it will update immediately
![image](https://user-images.githubusercontent.com/78290169/155998860-23e4064f-5f41-4a1e-b7b8-4d5ca1427c1a.png)

### Admin page
- Dashboard:
Admin can view the product info and click update for update the relevant information about the product
![image](https://user-images.githubusercontent.com/78290169/155999068-218588c8-073a-4d1e-af8b-0e144dc8f108.png)

- Update Product
If admin click the button 'update' in the dashboard, then it will goes to the page for admin to update the information of that particular product
![image](https://user-images.githubusercontent.com/78290169/155999230-ce66c9a7-7c13-429c-9443-c03aa6b0ac8b.png)

- Add Product
Admin can also add product to the database by input relevant information based on the form 
![image](https://user-images.githubusercontent.com/78290169/155999484-b3ea4746-049d-4a1f-8f63-2d2fb930f723.png)

## Reference:
- <a href="https://youtu.be/Qr4QMBUPxWo">Flask Course - Python Web Application Development</a> (Inspiration from this video and take reference about the page design)
- Stack Overflow
- Bootstrap
- W3School
