import db_connect as db


def get_all_instances():
    instance_list = []
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT carid, reg_number, VIN, Engine_type FROM Cars")
            for instance in cursor.fetchall():
                instance_dict = {
                    'carid': instance[0],
                    'reg_number': instance[1],
                    'VIN': instance[2],
                    'Engine_type': instance[3]
                }
                instance_list.append(instance_dict)
    return instance_list


def create_new_instance(car):
    existing_instance = get_one_instance(car['reg_number'])
    if existing_instance:
        return {'error': f"Instance with Registration number {car['carid']} already exists"}, 409

    with db.crete_connection() as connection:
        with connection.cursor() as cursor:
            query = "INSERT INTO Cars (carid, reg_number, VIN, Engine_type) VALUES (%s, %s, %s, %s);"
            values = (car['carid'], car['reg_number'], car['VIN'], car['Engine_type'])
            cursor.execute(query, values)
            connection.commit()
    return car, 201


def get_one_instance(carid):
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT carid, reg_number, VIN, Engine_type FROM Cars WHERE reg_number ='" + carid + "'")
            instance = cursor.fetchone()
            if instance is not None:
                return {
                    'carid': instance[0],
                    'reg_number': instance[1],
                    'VIN': instance[2],
                    'Engine_type': instance[3]
                }
            else:
                return None


def delete_instance(carid):
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            delete_query = "DELETE FROM Cars WHERE reg_number ='" + carid + "'"
            cursor.execute(delete_query)
            conn.commit()
            return cursor.rowcount


def update_instance(car, reg_number):
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            update_query = "UPDATE Cars SET reg_number = %s, VIN = %s, Engine_type = %s WHERE reg_number = %s"
            values = (car['reg_number'], car['VIN'], car['Engine_type'], reg_number)
            cursor.execute(update_query, values)
            conn.commit()
        return car