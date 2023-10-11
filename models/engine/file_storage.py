#!/usr/bin/python3
"""Defines the file storage"""
import os
from json import load, dump, dumps
from models.base_model import BaseModel

class FileStorage():
    """Class File Storage"""
    __file_path = str()
    __objects = dict()

    def all(self):
        """Return the dictionary"""
        return (self.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = type(obj).__name__+'.'+obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        output = dict()
        for k, v in self.__objects.items():
            output[k] = v.to_dict()
        self.__file_path = "storage.json"
        print(output)
        with open(self.__file_path, "a+") as file:
            dump(output, file)
            file.write(str('\n'))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file"""
        self.__file_path = "storage.json"
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as file:
                #load(file)
                print("1")

