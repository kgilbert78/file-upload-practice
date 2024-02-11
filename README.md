# File Upload Practice

Testing simplified file upload functionality to diagnose problems with adapting CLA database to upload files

### Endpoints

**GET:**

- All files: `http://localhost:8000/api/files/`
- Specific file: add id to the end of the GET url like this `http://localhost:8000/api/files/1/`

**POST:**

Send requests to `http://localhost:8000/api/files/`

- Headers:

  - Content-Type: multipart/form-data

- Body:

  - set to form-data

  - KEY is _document_,

  - under VALUE select File from dropdown and then use the button to open file browser and select your file
