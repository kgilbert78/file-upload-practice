# File Upload Practice

Testing simplified file upload functionality to diagnose problems with adapting CLA database to upload files

### Endpoints

**GET:**

- All files: `http://localhost:8000/api/files/`
- Specific file: add id to the end of the GET url like this `http://localhost:8000/api/files/1/`

**POST:**

Send requests to `http://localhost:8000/api/files/`

To use the postman fields:

- Headers:

  - Content-Type: multipart/form-data

- Body:

  - set to form-data

  - KEY is _document_,

  - under VALUE select File from dropdown and then use the button to open file browser and select your file

Do not use json, it submits without errors but puts the full filepath after `media/` in the document field and doesn't actually move/save the file. It's possible to send json from the frontend with headers Content-Type: multipart/form-data and use `new FormData()` to create the request - see [FormData MDN](https://developer.mozilla.org/en-US/docs/Web/API/FormData)

~~To use json:~~

- ~~Headers:~~
  - ~~Content-Type: application/json~~
- ~~Body:~~

  - ~~set to raw, then select json from the dropdown to the right~~

  - ~~body format should be `{ "document": "~/path/to/file.pdf" }`~~
