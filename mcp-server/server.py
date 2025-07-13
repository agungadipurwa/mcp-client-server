import os
import json
from utils.creds import get_credentials
from googleapiclient.discovery import build
from utils  import sheets
import httpx
import asyncio

from dotenv import load_dotenv
load_dotenv()

async def get_current_time():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://timeapi.io/api/time/current/zone",
                headers={"Accept": "application/json"},
                params={"timeZone": "Etc/GMT-7"}
            )
            response.raise_for_status()
            current_time = response.json()
            return current_time
    except httpx.RequestError as e:
        print(f"An error occurred while making the request: {e}")
        return None

async def get_employee_logtime()->dict|None:
    spreadsheet_id, sheet_range = sheets.sheet['dummy'].values()
    try:
        def fetch_data():
            # Use the get_credentials function to authenticate
            creds = get_credentials()
            service = build('sheets', 'v4', credentials=creds)

            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                        range=sheet_range[0]).execute()
            
            return result.get('values', [])
        
        current_time = await get_current_time()
        values = await asyncio.to_thread(fetch_data)
        if not values:
            print('No data found.')
            return []
        else:
            json_output = []
            headers = values[0]
            rows = values[1:]
            for row in rows:
                row_dict = dict(zip(headers, row))
                json_output.append(row_dict)
            print('Data retrieved successfully.')
            return json.dumps({
                "current_time":current_time,
                "logs":json_output
            }, indent=4)
            # return values # Skip header row if present
    except Exception as e:
        print(f"Error retrieving data from Google Sheets: {e}")
        return []


# initialize headers for Clockify API requests

CLOCKIFY_API_KEY = os.getenv("CLOCKIFY_API_KEY")
CLOCKIFY_BASE_URL = "https://api.clockify.me/api/v1"
CLOCKIFY_REAPORT_URL= "https://reports.api.clockify.me/v1"
CLOCKIFY_WORKSPACE_ID = os.getenv("CLOCKIFY_WORKSPACE_ID")

headers = {
    "X-Api-Key": CLOCKIFY_API_KEY,
    "Content-Type": "application/json"
}

async def get_all_projects():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{CLOCKIFY_BASE_URL}/workspaces/{CLOCKIFY_WORKSPACE_ID}/projects",
                headers=headers
            )
            response.raise_for_status()
            projects = response.json()
            return projects
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        return None

async def get_active_projects():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{CLOCKIFY_BASE_URL}/workspaces/{CLOCKIFY_WORKSPACE_ID}/projects",
                headers=headers,
                params={"active": "true"}  # Filter for active projects
            )
            response.raise_for_status()
            projects = response.json()
            return projects
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        return None

async def get_total_logtime():
    request_body = {
        "amountShown":"HIDE_AMOUNT",
        "detailedFilter": {
            "options": {
                "totals": "EXCLUDE"
            },
            "page": 1,
            "pageSize": 20,
            "sortColumn": "ID"
        },
        "billable": True,
        "dateRangeEnd": "2025-06-30T23:59:59.999Z",
        "dateRangeStart": "2025-06-18T00:00:00Z",
        "summaryFilter": {
            "groups": ["PROJECT"],
            "sortColumn": "GROUP"
        },
        "exportType": "JSON"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{CLOCKIFY_REAPORT_URL}/workspaces/{CLOCKIFY_WORKSPACE_ID}/reports/detailed",
                headers=headers,
                json=request_body
            )
            response.raise_for_status()
            report_data = response.json()
            return report_data
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        return None

async def get_summary_project():
    data = dict()
    try:
        data["current_time"] = await get_current_time()
        data["total"] = await get_total_logtime()
        data["list_of_projects"] = await get_all_projects()
        data["active_projects"] = await get_active_projects()
        return data
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        return None