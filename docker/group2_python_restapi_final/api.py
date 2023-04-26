import db_data
from flask import make_response


def read_all():
    return db_data.get_all_instances(), 200


def create_instance(car):
    instance, status_code = db_data.create_new_instance(car)
    return instance, status_code


def read_one_instance(carid):
    return db_data.get_one_instance(carid), 200


def delete_instance(carid):
    rows_affected = db_data.delete_instance(carid)

    if rows_affected > 0:
        return make_response(f"{carid} successfully deleted", 200)
    else:
        return make_response(f"Deletion of {carid} failed. Instance not found.", 404)


def update_instance(carid, car):
    return db_data.update_instance(carid, car), 200

