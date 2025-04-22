## Company Directory Flask API

This is a lightweight Flask-based API that allows users to search for companies and update company details stored in a JSON file.

**GitHub Repository:** [https://github.com/suriya094/Restful-API-Companies-Assignment](https://github.com/suriya094/Restful-API-Companies-Assignment)

---

## Project Structure

. ├── companies.py # Flask application code ├── companies.json # JSON file containing company data ├── README.md # Project documentation
---

## Features
- Search companies by name or description
- Update a company’s information by `company_name_id`
- Data stored in a JSON file for simplicity
---

## Setup Instructions
1. Clone the Repository

```bash
git clone https://github.com/suriya094/Restful-API-Companies-Assignment.git
cd Restful-API-Companies-Assignment```

2. Create a Virtual Environment
```python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows```

3. Install Dependencies
-  pip install Flask

4. Run the Application
  python companies.py

Visit http://localhost:5000 to access the API

## API Reference
GET /company/list?q=<query>
Search for companies by query string.
Query Param: q (string, optional) — the search keyword
Returns: Up to 50 matched companies in JSON format

Example Request:
GET /company/list?q=tech
Example Response:
[
  {
    "company_name_id": 101,
    "company_name": "Tech Innovators",
    "description": "A leading tech company..."
  }
]


PUT /company/<company_name_id>
Update a company’s details by ID.
Path Param: company_name_id — ID of the company to update
Request Body: JSON object with updated fields
Returns: The updated company object

Example Request:
PUT /company/101
Content-Type: application/json

{
  "description": "A newly updated company description.",
  "location": "New York"
}

Example Response:
{
  "company_name_id": 101,
  "company_name": "Tech Innovators",
  "description": "A newly updated company description.",
  "location": "New York"
}
