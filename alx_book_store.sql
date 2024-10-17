CREATE TABLE Books(

    book_id int primary key
    title  VARCHEAR(130) 
    author_id int key
    price DOUBLE
    publication_date DATE


);

CREATE TABLE Author(

    author_id primary key
    author_name VARCHAR(215)
    email VARCAHR(215)
    address TEXT

);

CREATE TABLE Orders(

    order_id primary key 
    customer_id
    order_date DATE

);

CREATE TABLE Order_Details(

    order_details_id primary key
    order_id 
    quantity DOUBLE
);