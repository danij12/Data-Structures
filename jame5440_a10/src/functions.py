"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-10-15"
-------------------------------------------------------
"""
def get_broad(cursor, broadId=None):
    """
    -------------------------------------------------------
    Queries the broad table.
    Use: rows = get_broad(cursor)
    Use: rows = get_broad(cursor, broadId=v)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        broadId - a broad ID (int)
    Returns:
        rows - (list of broad table data)
            if broadId is not None:
                rows matching broadId
            else:
                the entire broad table
            Sorted by broad description
    -------------------------------------------------------
    """
    
