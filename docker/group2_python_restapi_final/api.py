import db_data
from flask import make_response


def read_all():
    return db_data.get_all_instances(), 200


def create_instance(instance):
    instance, status_code = db_data.create_new_instance(instance)
    return instance, status_code


def read_one_instance(name):
    return db_data.get_one_instance(name), 200


def delete_instance(name):
    rows_affected = db_data.delete_instance(name)

    if rows_affected > 0:
        return make_response(f"{name} successfully deleted", 200)
    else:
        return make_response(f"Deletion of {name} failed. Instance not found.", 404)


def update_instance(name, instance):
    return db_data.update_instance(name, instance), 200
