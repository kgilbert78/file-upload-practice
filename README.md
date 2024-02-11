# File Upload Practice

Testing simplified file upload functionality to diagnose problems with adapting CLA database to upload files

### Endpoints

**GET:**

- All files: `http://localhost:8000/api/files/`
- Specific file: add id to the end of the GET url like this `http://localhost:8000/api/files/1/`

**POST:**

Send requests to `http://localhost:8000/api/files/`

To use json:

- Headers:

  - Content-Type: application/json

- Body:

  - set to raw, then select json from the dropdown to the right

  - body format should be `{ "document": "~/path/to/file.pdf" }`


To use the postman fields:

- Headers:

  - Content-Type: multipart/form-data

- Body:

  - set to form-data

  - KEY is _document_,

  - under VALUE select File from dropdown and then use the button to open file browser and select your file
