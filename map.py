#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import json

# Normally, you'd separate HTML templates up into another file and read it in
WEBPAGE = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Koala Mapping Example</title>
    <base target="_blank">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin="" />
    <style>body { margin: 0; } .map { width: 100vw; height: 100vh; }</style>
  </head>
  <body>
    <div class="map" id="mapid"></div>

    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
    <script>
      const DATA = %s;
      const map = L.map('mapid').setView([-21, 145], 6);

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map);

      DATA.forEach(record =>
        L.marker([record.lat, record.lng])
          .bindPopup(`
            <h2>${record.name}</h2>
            <strong>Scientific name:</strong> ${record.species}<br>
            <strong>Locality:</strong> ${record.locality}<br>
            <strong>Project:</strong> ${record.project}<br>
            <strong>Organisation:</strong> ${record.organisation}
          `)
          .addTo(map)
      );
    </script>
  </body>
</html>
"""

COMMON_NAMES = {
    "Phascolarctos cinereus": "Koala"
}

# Python "web framework" libraries offer a simpler way of doing this
class MyHTTPServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Pass through ?records=1234 to adjust the records shown
        records_option = self.path.split('records=')
        records = int(records_option[1]) if len(records_option) == 2 else 1000

        # Load the Koala data API
        API_URL = f"https://www.data.qld.gov.au/api/3/action/datastore_search?resource_id=8dbceb06-aa8f-411a-baae-13d66475fdd7&limit={records}"
        with urllib.request.urlopen(API_URL) as response:
            api = json.load(response)
            all_records = api["result"]["records"]

            # Pull out just the specific part of the API we want & cleanup
            records = [{
                "lat": record["Latitude"],
                "lng": record["Longitude"],
                "name": COMMON_NAMES[record["ScientificName"]],
                "species": record["ScientificName"],
                "locality": record["LocalityDetails"].title().rstrip(','),
                "project": record["ProjectName"],
                "organisation": record["OrganisationName"]
            } for record in all_records]

        # Create the page to display, insert the data into the HTML itself
        html_page = WEBPAGE % json.dumps(records)

        # Boilerplate to send to the browser
        # Web framework libraries like Flask handle this for you!
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=UTF-8")
        self.end_headers()
        self.wfile.write(html_page.encode("utf-8"))

# Start up the web server - web framework libraries usually do this for you
if __name__ == "__main__":
    server = HTTPServer(('localhost', 8080), MyHTTPServer)
    print(f"Server started http://{server.server_address[0]}:{server.server_address[1]}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("Server has shut down, exiting")
