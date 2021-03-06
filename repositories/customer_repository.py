from db.run_sql import run_sql
from models.customer import Customer
from models.animal import Animal
import repositories.animal_repository as animal_repository

def save(customer):
    sql = "INSERT INTO customers (name, contact_details) VALUES (%s, %s) RETURNING *"
    values = [customer.name, customer.contact_details]
    results = run_sql(sql, values)
    id = results[0]['id']
    customer.id = id
    return customer

def select_all():
    customers = []

    sql = "SELECT * FROM customers ORDER by name"
    results = run_sql(sql)

    for row in results:
        customer = Customer(row["name"],row["contact_details"], row["id"])
        customers.append(customer)
    return customers

def select(id):
    customer = None
    sql ="SELECT * FROM customers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
   
    if result is not None:
        customer = Customer(result['name'], result['contact_details'], result['id'])
    return customer 

def delete_all():
    sql = "DELETE FROM customers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM customers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(customer):
    sql = "UPDATE customers SET (name, contact_details) = (%s, %s) WHERE id = %s"
    values = [customer.name, customer.contact_details, customer.id]
    run_sql(sql, values)

def animals(customer_id):
    animals = []
    sql = """SELECT *
            FROM animals
            WHERE customer_id = %s"""
    values = [customer.id]
    results = run_sql(sql, values)

    for result in results:
        animal =  Animal(
        result ["name"],
        result ["dob"], 
        result ["animal_type"], 
        result["notes"],
        customer, 
        result ["id"])
        animals.append(animal)
    return animals