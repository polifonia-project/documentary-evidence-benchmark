import csv
import requests
import urllib.parse

def main():
    csv_filename = "data/experiences.csv"
    output_filename = "data/experiences_kg.txt"
    base_url = "https://data.open.ac.uk/sparql"
    headers = {
        'Accept': 'text/plain',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    with open(csv_filename, "r") as csv_file, open(output_filename, "w") as output_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row if exists

        counter = 0
        for row in csv_reader:
            if len(row) >= 2:
                counter += 1
                uri = row[1]
                query = makeQuery(uri)

                response = make_http_request(base_url, query, headers)

                print(f"Counter: {counter}\n")
                print(f"Experience URI: {uri}\n")
                output_file.write(f"{response}\n")

def make_http_request(url, query, headers):
    try:
        data = "query="+query
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()  # Raise an exception if request fails
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return f"Request failed: {e}"

def makeQuery(uri):
    query = 'DESCRIBE <'+uri+'> ?related FROM <http://data.open.ac.uk/context/led> WHERE { <'+uri+'> ?p ?related}'
    return urllib.parse.quote_plus(query)

if __name__ == "__main__":
    main()
