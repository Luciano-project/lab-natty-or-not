from config import connection

def get_predictions():
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM predictions ORDER BY created DESC")
        predictions = cursor.fetchall()
        return predictions
        #return [Prediction(prompt, id) for prompt, id in predictions]

def create(prompt):
    try:
        print(prompt)
        with connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO predictions (prompt, id) VALUES (?, ?)",
                            (prompt, None )
                            )
            connection.commit()
            return 0
    except Exception as e:
        print('Error: ',e)
        return 1

"""def update(prompt, id):
    try:
        with connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE predictions SET prompt = ? WHERE id = ?",
                            (prompt, id)
                            )
            connection.commit()
            return 0 
    except Exception as e:
        print('Error: ',e)
        return 1
"""
"""def destroy(id):
    try:
        with connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM predictions WHERE id = ?", (id,))
            connection.commit()
            return 0
    except Exception as e:
        print('Error: ',e)
        return 1"""