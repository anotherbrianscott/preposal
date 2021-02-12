from datetime import datetime
from fastapi import FastAPI, Response, status
import psycopg2

conn = psycopg2.connect("dbname=postgres user=postgres password=secretpassword port=5433 host=localhost")

app = FastAPI()

@app.get("/patientData/{patientId}")
async def read_patient_data(patientId: str, response: Response, observationType: str = None, startDate: str = None, endDate: str = None):
    """Handler function to retrieve Patient Observation data.
    :param patientId: The UUID of the Patient.
    :param observationType: The type of Observation to retrieve.
    :returns: List of Observations matching search criteria.
    """
    observations = []
    cur = conn.cursor()
    # Initialize query and args
    query_str = 'SELECT * FROM public."Observations" WHERE patient_id = %s'
    args = [patientId]
    # Check if patient exists
    query_exists = 'SELECT COUNT(*) FROM public."Patients" WHERE patient_id = %s;'
    cur.execute(query_exists, args)
    exists = cur.fetchone()
    if exists[0] == 0:
        response.status_code = status.HTTP_404_NOT_FOUND
        return observations
    # if observationType is provided
    if observationType:
        query_str = query_str + ' AND observation_type = %s'
        args.append(observationType)
    # if startDate is provided
    if startDate:
        query_str = query_str + ' AND observation_datetime >= %s'
        args.append(datetime.fromisoformat(startDate))
    # if endDate is provided
    if endDate:
        query_str = query_str + ' AND observation_datetime <= %s'
        args.append(datetime.fromisoformat(endDate))
    query_str = query_str + ';'
    cur.execute(query_str, args)
    for row in cur:
        observations.append({
            'observationId': row[0],
            'observationType': row[1],
            'observationDateTime': row[2],
            'valueString': row[3],
            'valueBoolean': row[4],
            'valueInteger': row[5],
            'patientId': row[9],
        })
    # Ensure a 204 is sent back when no results
    if len(observations) == 0:
        response.status_code = status.HTTP_204_NO_CONTENT
    return observations