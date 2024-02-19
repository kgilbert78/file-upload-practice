# File Upload Practice

Testing simplified file upload functionality to diagnose problems with adapting CLA database to upload files

## Endpoints

### First App: file_api

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

### Second App: base64_uploads

WORK IN PROGRESS - CURRENTLY ADDS EMPTY {} TO THE JSON LIST AND DOESN'T MOVE FILE...BUT NO ERRORS

**GET:**

- All files: `http://localhost:8000/base64api/files/`

**POST:**

Send requests to `http://localhost:8000/base64api/files/`

These instructions are based on [this youtube video on base64 in postman](https://www.youtube.com/watch?v=s847Onr3IC4)

How to prepare the file:

- in terminal, in folder of document to encode, type `openssl base64 -in filename.ext > encoded.txt` to encode the file into a text file called encoded.

- in terminal `tr --delete '\n' < encoded.txt > encoded-no-spaces.txt` to replace the new line breaks between all the lines of the encoded info.

- open `encoded-no-spaces.txt` and copy the contents to paste into postman.

How to fill in the Postman tabs:

- Headers:

  - Content-Type: application/json

- Body:

  - set to raw, then select json from the dropdown to the right

  - body format should be `{ "document": "encoded-stuff-pasted-here" }`

### Third App: keywords

Created to replicate CLA DB problem with keyword data being split into one character for each keyword saved to the DB.

Instructions are the same as for the First App (file_api) but with the endpoint as `http://localhost:8000/keywords/files/`
