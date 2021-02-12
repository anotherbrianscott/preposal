from datetime import datetime, timezone
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_all_patient_observations():
    """Tests getting all of the Observations for a particular patient
    """
    response = client.get("/patientData/bb463b8b-b76c-4f6a-9726-65ab5730b69b")
    assert response.status_code == 200
    res_json = response.json()
    assert isinstance(res_json, list)
    assert len(res_json) == 100

def test_get_all_patient_boolean_observations():
    """Tests getting all booleanObservations for a particular patient
    """
    params = {
        'observationType': 'booleanObservation'
    }
    response = client.get("/patientData/218b86a4-d7bb-495b-a5a5-5334fac1c606", params=params)
    assert response.status_code == 200
    res_json = response.json()
    assert isinstance(res_json, list)
    for obs in res_json:
        assert obs['observationType'] == 'booleanObservation'
        assert isinstance(obs['valueBoolean'], bool)

def test_get_all_patient_string_observations():
    """Tests getting all stringObservations for a particular patient
    """
    params = {
        'observationType': 'stringObservation'
    }
    response = client.get("/patientData/614e6ceb-f887-4991-8576-ade4177f3869", params=params)
    assert response.status_code == 200
    res_json = response.json()
    assert isinstance(res_json, list)
    for obs in res_json:
        assert obs['observationType'] == 'stringObservation'
        assert isinstance(obs['valueString'], str)

def test_get_all_patient_integer_observations():
    """Tests getting all integerObservations for a particular patient
    """
    params = {
        'observationType': 'integerObservation'
    }
    response = client.get("/patientData/dc948650-456b-4ade-887a-49d94a8d215c", params=params)
    assert response.status_code == 200
    res_json = response.json()
    assert isinstance(res_json, list)
    for obs in res_json:
        assert obs['observationType'] == 'integerObservation'
        assert isinstance(obs['valueInteger'], int)

def test_get_all_patient_observations_after():
    """Tests getting all Observations for a particular patient after a certain date
    """
    start_date = datetime(2020, 6, 1, tzinfo=timezone.utc)
    params = {
        'startDate': start_date.isoformat()
    }
    response = client.get("/patientData/379318e2-aebf-4079-8882-42cb158be836", params=params)
    assert response.status_code == 200
    res_json = response.json()
    assert isinstance(res_json, list)
    assert len(res_json) > 0
    for obs in res_json:
        assert datetime.fromisoformat(obs['observationDateTime']) >= start_date

def test_get_all_patient_observations_before():
    """Tests getting all Observations for a particular patient before a certain date
    """
    end_date = datetime(2020, 6, 1, tzinfo=timezone.utc)
    params = {
        'endDate': end_date.isoformat()
    }
    response = client.get("/patientData/379318e2-aebf-4079-8882-42cb158be836", params=params)
    assert response.status_code == 200
    res_json = response.json()
    assert isinstance(res_json, list)
    assert len(res_json) > 0
    for obs in res_json:
        assert datetime.fromisoformat(obs['observationDateTime']) <= end_date

def test_get_all_patient_observations_between():
    """Tests getting all Observations for a particular patient between a certain date range
    """
    start_date = datetime(2020, 6, 1, tzinfo=timezone.utc)
    end_date = datetime(2020, 12, 1, tzinfo=timezone.utc)
    params = {
        'startDate': start_date.isoformat(),
        'endDate': end_date.isoformat()
    }
    response = client.get("/patientData/379318e2-aebf-4079-8882-42cb158be836", params=params)
    assert response.status_code == 200
    res_json = response.json()
    assert isinstance(res_json, list)
    assert len(res_json) > 0
    for obs in res_json:
        assert datetime.fromisoformat(obs['observationDateTime']) >= start_date
        assert datetime.fromisoformat(obs['observationDateTime']) <= end_date

def test_get_integer_patient_observations_between():
    """Tests getting all integerObservations for a particular patient between a certain date range
    """
    start_date = datetime(2020, 6, 1, tzinfo=timezone.utc)
    end_date = datetime(2020, 12, 1, tzinfo=timezone.utc)
    params = {
        'observationType': 'integerObservation',
        'startDate': start_date.isoformat(),
        'endDate': end_date.isoformat()
    }
    response = client.get("/patientData/379318e2-aebf-4079-8882-42cb158be836", params=params)
    assert response.status_code == 200
    res_json = response.json()
    assert isinstance(res_json, list)
    assert len(res_json) > 0
    for obs in res_json:
        assert obs['observationType'] == 'integerObservation'
        assert isinstance(obs['valueInteger'], int)
        assert datetime.fromisoformat(obs['observationDateTime']) >= start_date
        assert datetime.fromisoformat(obs['observationDateTime']) <= end_date

def test_get_no_patient_observations():
    """Tests getting no Observations for a particular patient when none exist
    """
    end_date = datetime(2018, 6, 1, tzinfo=timezone.utc)
    params = {
        'endDate': end_date.isoformat()
    }
    response = client.get("/patientData/379318e2-aebf-4079-8882-42cb158be836", params=params)
    assert response.status_code == 204

def test_get_no_patient():
    """Tests getting no Observations when patient doesn't exist
    """
    response = client.get("/patientData/dc948650-456b-4ade-887a-49d94a8d215d")
    assert response.status_code == 404
