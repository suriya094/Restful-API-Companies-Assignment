from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load companies data from JSON file
with open('companies.json', 'r') as file:
    companies = json.load(file)

# Search endpoint: Returns up to 50 companies matching the query string
@app.route('/company/list', methods=['GET'])
def search_companies():
    # Get the search query from the request URL parameters, default to an empty string if not provided
    query = request.args.get('q', '').lower()
    if not query: 
        # If query is empty, return an empty list as JSON response
        return jsonify([])

    # Filter companies that match the query in the name or description
    matched_companies = []
    for company in companies:
        company_name = company.get('company_name', '').lower()
        description = company.get('description', '').lower()
        if query in company_name or query in description:
            matched_companies.append(company)
    # Return first 50 matched companies as a JSON response
    return jsonify(matched_companies[:50])

# Update endpoint: Updates a company's details based on the given fields
@app.route('/company/<company_name_id>', methods=['PUT'])
def update_company(company_name_id):
    # Get the updated data from the request body in JSON Format
    updated_data = request.json
    # Iterate through the list of companies to find the one with the matching ID
    for company in companies:
        if str(company.get('company_name_id')) == str(company_name_id):
            # Updates company information with the new request body data
            company.update(updated_data)
            # Saves updated list of companies back to companies.json
            with open('companies.json', 'w') as file:
                json.dump(companies, file, indent=4)

            return jsonify(company)
    
    # Returns 404 error if no company has that id
    return jsonify({"error": "Company not found"}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
