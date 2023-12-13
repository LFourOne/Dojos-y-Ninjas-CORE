from app_flask.config.mysqlconnections import connectToMySQL
from app_flask import DATA_BASE

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def create_ninja(cls, data):
        query = """
                INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
                VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);
                """
        return connectToMySQL(DATA_BASE).query_db(query, data)
    
    @classmethod
    def obtain_dojo_and_ninjas(cls, data):
        query = """
                SELECT * FROM ninjas
                JOIN dojos ON ninjas.dojo_id = dojos.id
                WHERE ninjas.dojo_id = %(id)s;
                """
        result = connectToMySQL(DATA_BASE).query_db(query, data)
        ninja_list = []
        for row in result:
            ninja_list.append(cls(row))
        return ninja_list
    
    

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = """
                SELECT * FROM dojos;
                """
        result = connectToMySQL(DATA_BASE).query_db(query)
        dojos_list = []
        for row in result:
            dojos_list.append(cls(row))
        return dojos_list

    @classmethod
    def create_dojo(cls, data):
        query = """
                INSERT INTO dojos (name, created_at, updated_at)
                VALUES (%(name)s, NOW(), NOW());
                """
        return connectToMySQL(DATA_BASE).query_db(query, data)
    
    @classmethod
    def obtain_one_dojo(cls, data):
        query = """
                SELECT * FROM dojos
                WHERE id = %(id)s;
                """
        result = connectToMySQL(DATA_BASE).query_db(query, data)
        return cls(result[0])