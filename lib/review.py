from __init__ import CURSOR, CONN
from department import Department
from employee import Employee


class Review:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, year, summary, employee_id, id=None):
        self.id = id
        self.year = year
        self.summary = summary
        self.employee_id = employee_id

    def __repr__(self):
        return (
            f"<Review {self.id}: {self.year}, {self.summary}, "
            + f"Employee: {self.employee_id}>"
        )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Review instances """
        sql = """
            CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            year INT,
            summary TEXT,
            employee_id INTEGER,
            FOREIGN KEY (employee_id) REFERENCES employee(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Review  instances """
        sql = """
            DROP TABLE IF EXISTS reviews;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the year, summary, and employee id values of the current Review object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        pass

    @classmethod
    def create(cls, year, summary, employee_id):
        """ Initialize a new Review instance and save the object to the database. Return the new instance. """
        pass
   
    @classmethod
    def instance_from_db(cls, row):
        """Return an Review instance having the attribute values from the table row."""
        id = row[0]
        if id in cls.all:
            return cls.all[id]
        
        review = cls(row[1], row[2], row[3], id)
        cls.all[id] = review
        return review
        # Check the dictionary for  existing instance using the row's primary key
        pass
   

    @classmethod
    def find_by_id(cls, id):
        """Return a Review instance having the attribute values from the table row."""
        CURSOR.execute('SELECT * FROM reviews WHERE id = ?', (id,))
        row = CURSOR.fetchone()
        if row:
            return cls.instance_from_db(row)
        return None
        pass

    def update(self):
        """Update the table row corresponding to the current Review instance."""
        CURSOR.execute(
            'UPDATE reviews SET year = ?, summary = ?, employee_id = ? WHERE id = ?',
            (self.year, self.summary, self.employee_id, self.id)
        )
        CONN.commit()
        pass

    def delete(self):
        """Delete the table row corresponding to the current Review instance,
        delete the dictionary entry, and reassign id attribute"""
        CURSOR.execute('DELETE FROM reviews WHERE id = ?',(self.id,))
        CONN.commit()
        if self.id in self.__class__.all:
            del self.__class__.all[self.id]
            self.id = None
        pass


    @classmethod
    def get_all(cls):
        """Return a list containing one Review instance per table row"""
        CURSOR.execute('SELECT * FROM reviews')
        rows = CURSOR.fetchall()
        return[cls.instance_from_db(row) for row in rows]
        pass
@property
def year(self):
    return self._year

@year.setter
def year(self, value):
    if isinstance(value, int) and value >= 2000:
        self._year = value
    else:
        raise ValueError("Year must be an integer greater than or equal to 2000")

@property
def summary(self):
    return self._summary

@summary.setter
def summary(self, value):
    if isinstance(value, str) and len(value) > 0:
        self._summary = value
    else:
        raise ValueError("Summary must be a non-empty string")

@property
def employee_id(self):
    return self._employee_id

@employee_id.setter
def employee_id(self, value):
    CURSOR.execute('SELECT * FROM employees WHERE id = ?', (value,))
    if CURSOR.fetchone():
        self._employee_id = value
    else:
        raise ValueError("Employee ID must correspond to a valid Employee instance")
 

