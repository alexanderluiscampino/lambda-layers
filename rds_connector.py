import os
import pyodbc

class RDS(object):
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    driver = os.getenv('DRIVER')

    def __init__(self, database: str):
        self.establish_connecion_string(database)

    def establish_connecion_string(self, database):
        def edit(string):
            remove = ['\t', '\n']
            for char in remove:
                string = string.replace(char, ' ')
            return string.replace('  ', '')

        self.connection = edit(f"""DRIVER={{{self.driver}}};
                    		      Server={self.host};
                                  PORT={self.port};
                    		      Database={database};
                    		      UID={self.username};
                    		      PWD={self.password};
                    		      ColumnEncryption=Enabled;
                    		      """
                               )
                               
rds = RDS(database)
connexion = pyodbc.connect(rds.connection)

# Proceed to use connexion to run a query against the database
