from erddap_management import app
import json
import unittest

class TestPlatformController(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_crud(self):
        doc = {
            "reference_designator" : "CP04OSPM-WTF11",
            "display_name": "(Fixed) Pioneer Offshore Profiler Mooring - Surface Buoy"
        }
        response = self.app.post('/platforms', data=doc)
        assert response.status_code == 200

        response = self.app.get('/platforms')
        assert response.status_code == 200
        response = json.loads(response.data)
        response = { r['reference_designator'] : r for r in response }
        assert doc['reference_designator'] in response
        assert 'id' in response[doc['reference_designator']]
        
        doc_id = response[doc['reference_designator']]['id']

        response = self.app.get('/platforms/%s' % doc_id)
        assert response.status_code == 200
        response = json.loads(response.data)

        assert response['reference_designator'] == doc['reference_designator']

        response = self.app.delete('/platforms/%s' % doc_id)
        assert response.status_code == 200

        response = self.app.get('/platforms')
        assert response.status_code == 200

        response = json.loads(response.data)
        response = { r['reference_designator'] : r for r in response }
        assert doc['reference_designator'] not in response

        response = self.app.get('/platforms/%s' % doc_id)
        assert response.status_code == 204

