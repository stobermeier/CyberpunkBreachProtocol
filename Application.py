import os
from flask import Flask, render_template, request

# import our OCR function
from ocr_core import ocr_core

# import OCR to hexdump functionality
import ocr_to_hexdump
import solver

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
            print("Processing Manual User Input...")

            print(request.form)

            seq = request.form['seq']
            ram = request.form['ram']

            e00 = request.form['e00']
            e01 = request.form['e01']
            e02 = request.form['e02']
            e03 = request.form['e03']
            e04 = request.form['e04']
            e05 = request.form['e05']

            e10 = request.form['e10']
            e11 = request.form['e11']
            e12 = request.form['e12']
            e13 = request.form['e13']
            e14 = request.form['e14']
            e15 = request.form['e15']

            e20 = request.form['e20']
            e21 = request.form['e21']
            e22 = request.form['e22']
            e23 = request.form['e23']
            e24 = request.form['e24']
            e25 = request.form['e25']

            e30 = request.form['e30']
            e31 = request.form['e31']
            e32 = request.form['e32']
            e33 = request.form['e33']
            e34 = request.form['e34']
            e35 = request.form['e35']

            e40 = request.form['e40']
            e41 = request.form['e41']
            e42 = request.form['e42']
            e43 = request.form['e43']
            e44 = request.form['e44']
            e45 = request.form['e45']

            e50 = request.form['e50']
            e51 = request.form['e51']
            e52 = request.form['e52']
            e53 = request.form['e53']
            e54 = request.form['e54']
            e55 = request.form['e55']

            hexdump = [[e00, e01, e02, e03, e04, e05],
                       [e10, e11, e12, e13, e14, e15],
                       [e20, e21, e22, e23, e24, e25],
                       [e30, e31, e32, e33, e34, e35],
                       [e40, e41, e42, e43, e44, e45],
                       [e50, e51, e52, e53, e54, e55]
                       ]
            print("Hexdump fetched")
            solution = solver.solve(hexdump, seq, ram)
            return render_template('upload.html', msg='Processing Complete', solution=solution)

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
