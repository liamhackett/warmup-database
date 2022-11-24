import csv
import sqlite3
import os
import re
from xml.etree.ElementTree import tostring

def process(columns, condition, order):
    sql_statement1 = "SELECT "  
    sql_statement2 = " FROM song JOIN artist on fpkName = pmkName "
    
    # check each of the english versions of the column name and
    # add the real column name to the SQL statement
    for column in columns:
        if (column == "English pmkName"):
            sql_statement1 += "pmkName"
        elif (column == "English fldGender"):
            sql_statement1 += "fldGender"
        elif (column == "English fldDescription"):
            sql_statement1 += "fldDescription"
        elif (column == "English fldCountry"):
            sql_statement1 += "fldCountry"
        elif (column == "English fldTrack"):
            sql_statement1 += "fldTrack"
        elif (column == "English fpkName"):
            sql_statement1 += "fpkName"
        elif (column == "English fldGenre"):
            sql_statement1 += "fldGenre"
        elif (column == "English fldBPM"):
            sql_statement1 += "fldBPM"
        elif (column == "English fldLength"):
            sql_statement1 += "fldLength"
        
        # add comma at the end of every column
        # name except the last one
        if (column != columns[len(columns)-1]):
            sql_statement1 += ", "
    
    sql_statement = sql_statement1 + sql_statement2
    
    if (condition != ""):
        condition = str.replace(condition, "is greater than", ">")
        condition = str.replace(condition, "is less than", "<")
        condition = str.replace(condition, "is greater than or equal to", ">")
        condition = str.replace(condition, "is less than or equal to", "<")
        condition = str.replace(condition, "is", "=")
        condition = str.replace(condition, "English pmkName", "pmkName")
        condition = str.replace(condition, "English fldGender", "fldGender")
        condition = str.replace(condition, "English fldDescription", "fldDescription")
        condition = str.replace(condition, "English fldCountry", "fldCountry")
        condition = str.replace(condition, "English fldTrack", "fldTrack")
        condition = str.replace(condition, "English fpkName", "fpkName")
        condition = str.replace(condition, "English fldGenre", "fldGenre")
        condition = str.replace(condition, "English fldBPM", "fldBPM")
        condition = str.replace(condition, "English fldLength", "fldLength")
        
        sql_statement += (condition + " ")
    
    if (order != ""):
        sql_statement3 = "ORDER BY "
        order = str.replace(order, "English pmkName", "pmkName")
        order = str.replace(order, "English fldGender", "fldGender")
        order = str.replace(order, "English fldDescription", "fldDescription")
        order = str.replace(order, "English fldCountry", "fldCountry")
        order = str.replace(order, "English fldTrack", "fldTrack")
        order = str.replace(order, "English fpkName", "fpkName")
        order = str.replace(order, "English fldGenre", "fldGenre")
        order = str.replace(order, "English fldBPM", "fldBPM")
        order = str.replace(order, "English fldLength", "fldLength")
        sql_statement3 += order
        sql_statement += sql_statement3
            
    # pmkName, fldGender, fldDescription, fldCountry
    # fldTrack, fpkName, fldGenre, fldBPM, fldLength


def print_statement(statement):
    rows = cursor.execute(statement).fetchall()
    print("=================================")
    print("statement: " + statement)
    print("=================================\n")
    for r in rows:
        x = re.search(".*\(.*",str(r[0]))
        
        result = ""
        for l in r:
            result += ", " + l
        result = result[2:]
        result = str.lower(result)
        print(result)

    print("\n=================================\n")