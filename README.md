# Car-go - Backend
**Project By:** Isaac Santacruz


## Descripton
Car-go is a website that will help you store your car brands that you have and store them with the details of model, year, price and picture so you can show to future buyers and help you sale cars more easily.
</br>

## Link
[**Github**](https://github.com/isaacxdd/Project4-backend#link)
[**Deployment**](https://car-go-ekyq.onrender.com/car/)
</br>

## Technologies Used
- Django
- Postman
- Python
</br>

## Backend Endpoints

| ENDPOINT | METHOD | PURPOSE |
|----------|--------|---------|
| /shift | GET | return list of car brands|
| /shift/:id | DELETE | delete a car brand entry from database |
| /shift/:id | PUT | receive info & update of car brand in database |
| /shift | POST | receive info from new form & create new car brand in database |
| /shift/:id | GET | render page with the car brand|
</br>

## ERD

``` 
Diagram
    USER {
        id primaryKey
        username string 
        password string
    }
    USER ||--|{ SHIFTS : Create
    SHIFTS {
        all makes foreignKey
        all models string
        year string 
        price  string 
        picture string 
    }
    }
```