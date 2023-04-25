import db_connect as db


def get_all_instances():
    instance_list = []
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT CarID, Reg_Number, VIN, Engine_type FROM Cars")
            for instance in cursor.fetchall():
                instance_dict = {
                    'CarID': instance[0],
                    'Reg_Number': instance[1],
                    'VIN': instance[2],
                    'Engine_type': instance[3]
                }
                instance_list.append(instance_dict)
    return instance_list


def create_new_instance(Car):
    existing_instance = get_one_instance(Car['Reg_Number'])
    if existing_instance:
        return {'error': f"Instance with Registration number {Car['Reg_Number']} already exists"}, 409

    with db.crete_connection() as connection:
        with connection.cursor() as cursor:
            query = "INSERT INTO instances (CarID, Reg_Number, VIN, Engine_type) VALUES (%s, %s, %s, %s);"
            values = (instance['CarID'], instance['Reg_Number'], instance['VIN'], instance['Engine_type'])
            cursor.execute(query, values)
            connection.commit()
    return existing_instance, 201


def get_one_instance(CarID):
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT CarID, Reg_Number, VIN, Engine_type FROM Cars WHERE Reg_Number ='" + CarID + "'")
            instance = cursor.fetchone()
            if instance is not None:
                return {
                    'CarID': instance[0],
                    'Reg_Number': instance[1],
                    'VIN': instance[2],
                    'Engine_type': instance[3]
                }
            else:
                return None


def delete_instance(CarID):
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            delete_query = "DELETE FROM Cars WHERE Reg_Number ='" + CarID + "'"
            cursor.execute(delete_query)
            conn.commit()
            return cursor.rowcount


def update_instance(CarID, instance):
    with db.crete_connection() as conn:
        with conn.cursor() as cursor:
            update_query = "UPDATE Cars SET Reg_Number = %s, VIN = %s, Engine_type = %s, WHERE CarID = %s"
            values = (instance['Reg_Number'], instance['VIN'], instance['Engine_type'], CarID)
            cursor.execute(update_query, values)
            conn.commit()
        return instance