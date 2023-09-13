from fastapi import FastAPI, HTTPException
import os,sys,json
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from controller.utils.DataHandler import getBothTasks,analyzer,percentageCalculator
import unittest,requests


class TestMainIntegration(unittest.TestCase):

    def testAnalyzeRoute(self):

        DEFAULT_BASE_URL = "http://localhost:5000"
        BASE_URL = os.environ.get("API_BASE_URL",DEFAULT_BASE_URL)
        endpoint_path = "/analyze"  
        full_url = BASE_URL + endpoint_path


        response = requests.get(full_url)

        if response.status_code == 200:
            try:
                data = response.json()
                self.assertIn('Finished_Tasks',data)
                self.assertIn('Total_Tasks',data)
                
            except json.JSONDecodeError as e:
                print("Error decoding JSON:", str(e))
        else:
            print("Request failed with status code:", response.status_code)
            print("Response content:", response.text)


