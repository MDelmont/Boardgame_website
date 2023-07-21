#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Check_data():
    def __init__(self):
        pass


    def check_if_data_is_good_for_request(self,list_of_data=[]):


        is_valid = True
        list_of_value_exclud = ['1=1','1= 1','1 = 1','1 =1','RANSOMWARE','select','update',';','=','>','<']

        for value in list_of_data:
            value = str(value).lower()
            for exclud in list_of_value_exclud:
                if str(exclud).lower() in value:
                    is_valid = False
        return is_valid