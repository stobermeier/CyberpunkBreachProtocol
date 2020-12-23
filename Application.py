import os
from flask import Flask, render_template, request

# import our OCR function
from ocr_core import ocr_core

# import OCR to hexdump functionality
import ocr_to_hexdump

# define a folder to store and later serve the images
UPLOAD_FOLDER = '\\temp'

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# route and function to handle the home page
@app.route('/')
def home_page():
    return render_template('index.html')


# route and function to handle the upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if manual input is present
        if 'seq' in request.form:
            '''
            row0 = request.form['row0']
            row1 = request.form['row1']
            row2 = request.form['row2']
            row3 = request.form['row3']
            row4 = request.form['row4']
            row5 = request.form['row5']
            rows = ocr_to_hexdump.convert_rows_to_hexdump([row0, row1, row2, row3, row4, row5])[0]
            return render_template('upload.html', msg='Manual Input processed', extraction_success=1,
                                   row0=rows[0],
                                   row1=rows[1],
                                   row2=rows[2],
                                   row3=rows[3],
                                   row4=rows[4],
                                   row5=rows[5])
            '''

        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):
            # save file
            # file.save(UPLOAD_FOLDER + file.filename)
            print(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

            # call the OCR function on it
            extracted_text = ocr_core(file)
            rows_and_hexdump = ocr_to_hexdump.convert_ocr_to_hexdump(extracted_text)
            rows = rows_and_hexdump[0]

            '''
            hexdump = rows_and_hexdump[1]
            ocr_to_hexdump.print_hexdump(hexdump)
            for row in rows:
                print(row)
            '''

            # extract the text and display it
            return render_template('upload.html',
                                   msg='Image successfully processed',
                                   extraction_success=1,
                                   img_src=os.path.join(app.config['UPLOAD_FOLDER'], file.filename),
                                   row0=rows[0],
                                   row1=rows[1],
                                   row2=rows[2],
                                   row3=rows[3],
                                   row4=rows[4],
                                   row5=rows[5])

    elif request.method == 'GET':
        return render_template('upload.html')


if __name__ == '__main__':
    app.run()
