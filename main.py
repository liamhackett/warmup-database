# Import required modules
import csv
from multiprocessing.sharedctypes import Value
import sqlite3
import os
import re
from xml.etree.ElementTree import tostring

global cursor
global connection
# Connecting to the geeks database
connection = sqlite3.connect('database.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()
def load_data():
    #remove old database
    try:
        os.remove("database.db")
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
    except FileNotFoundError:
        pass
    


    
    # Table Definition
    create_artist_table = '''CREATE TABLE artist(
                    pmkName TEXT PRIMARY KEY NOT NULL,
                    fldGender TEXT NOT NULL,
                    fldDescription TEXT NOT NULL,
                    fldCountry TEXT NOT NULL);
                    '''
                    
    create_song_table = '''CREATE TABLE song(
                    pmkRank INTEGER PRIMARY KEY AUTOINCREMENT,
                    fldTrack TEXT NOT NULL,
                    fpkName  TEXT NOT NULL,
                    fldGenre TEXT NOT NULL,
                    fldBPM INT NOT NULL,
                    fldLength INT NOT NULL);
                    '''
    
    # Creating the table into our
    # database

    cursor.execute(create_artist_table)
    cursor.execute(create_song_table)

    # Opening the person-records.csv file
    artists_file = open('artists.csv', encoding="utf8", errors="ignore")
    songs_file = open('top50.csv', encoding="utf8", errors="ignore")

    # Reading the contents of the
    # person-records.csv file
    artist_contents = csv.reader(artists_file)
    song_contents = csv.reader(songs_file)

    # SQL query to insert data into the
    # artist and song table
    insert_artist_records = "INSERT INTO artist (pmkName, fldGender, fldDescription, fldCountry) values (?, ?, ?, ?)"
    insert_song_records = "INSERT INTO song (fldTrack, fpkName, fldGenre, fldBPM, fldLength) values (?, ?, ?, ?, ?)"

    # Importing the contents of the file
    # into our person table



    cursor.executemany(insert_artist_records, artist_contents)
    cursor.executemany(insert_song_records, song_contents)


    # SQL query to retrieve all data from
    # the person table To verify that the
    # data of the csv file has been successfully
    # inserted into the table


    # Committing the changes
    connection.commit()

    print("Data loaded!")
    



def printStatement(statement):
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

    print("\n=================================\n")

test1 = "SELECT fldTrack FROM song JOIN artist on fpkName = pmkName WHERE pmkName = 'Ed Sheeran'"
test2 = "SELECT fldTrack FROM song JOIN artist on fpkName = pmkName WHERE fldBPM = 92"
test3 = "SELECT fldTrack, pmkName FROM song JOIN artist on fpkName = pmkName"

# printStatement(test1)
# printStatement(test2)
# printStatement(test3)



# pass this a string array of the column names in english
# pass the condition in english, if none specified then pass an empty string
# pass the order in english, if none specified then pass an empty string

#EXAMPLE: rank where artist is "ed sheeran"
#Column : rank
#Conditional: where artist is "ed sheeran"

#EXAMPLE: artist where song is "old town road"
#Column : artist
#Conditional: where song is "old town road"

#EXAMPLE: song where artist is "lil nas x" order by length
#Column : artist
#Conditional: where song is "old town road"
#order: "length"

# ALSO:
# "is" is interchangable with....
# "is greater than"
# "is less than"
# "is greater than or equal to"
# "is less than or equal to"


def convertToFld(field):
    field = str.replace(field, "artist", "pmkName")
    field = str.replace(field, "gender", "fldGender")
    field = str.replace(field, "group", "fldDescription")
    field = str.replace(field, "country", "fldCountry")
    field = str.replace(field, "track", "fldTrack")
    field = str.replace(field, "genre", "fldGenre")
    field = str.replace(field, "bpm", "fldBPM")
    field = str.replace(field, "length", "fldLength")
    field = str.replace(field, "rank", "pmkRank")
    return field 

def process(column, condition, order):
    sql_statement1 = "SELECT "  
    sql_statement2 = " FROM song JOIN artist on fpkName = pmkName "
    # tried to add feature for how many songs
    sql_statement3 = ""
    if condition == " " and order == " ":
        sql_statment3 = column
        executeSQL(sql_statement3)
    else:
        print(column)
        # check each of the english versions of the column name and
        # add the real column name to the SQL statement
        if (column == "artist"):
            sql_statement1 += "pmkName"
        elif (column == "gender"):
            sql_statement1 += "fldGender"
        elif (column == "English fldDescription"):
            sql_statement1 += "fldDescription"
        elif (column == "country"):
            sql_statement1 += "fldCountry"
        elif (column == "track"):
            sql_statement1 += "fldTrack"
        elif (column == "genre"):
            sql_statement1 += "fldGenre"
        elif (column == "bpm"):
            sql_statement1 += "fldBPM"
        elif (column == "length"):
            sql_statement1 += "fldLength"
        elif (column == "rank"):
            sql_statement1 += "pmkRank"
        
        # if (condition != ""):
        #     result = condition.split(" is")
        #     result = result[0].split("where ")[1]
        #     result = convertToFld(result)
        #     if (result != sql_statement1):
        #         sql_statement1 += (", " + result)
        
        sql_statement = sql_statement1 + sql_statement2
        
        if (condition != ""):
            condition = str.replace(condition, " is greater than", " >")
            condition = str.replace(condition, " is less than ", " <")
            condition = str.replace(condition, " is greater than or equal to ", " >=")
            condition = str.replace(condition, " is less than or equal to ", " <=")
            condition = str.replace(condition, " is ", " =")
            condition = convertToFld(condition)

            
            sql_statement += (condition + " ")
        
            if (order != ""):
                sql_statement3 = "ORDER BY "
                order = convertToFld(order)
                sql_statement3 += order
                sql_statement += sql_statement3
            
            print(sql_statement)
            executeSQL(sql_statement)
            
def executeSQL(sql_statement):
    rows = cursor.execute(sql_statement).fetchall()
    print("=================================")
    print("RESULTS")
    print("=================================\n")
    for r in rows:
        result = ""
        for l in r:
            result += ", " + str(l)
        result = result[2:]
        result = str.lower(result)
        print(result)

    print("\n=================================\n")
    

def quit():
    # closing the database connection
    connection.close()