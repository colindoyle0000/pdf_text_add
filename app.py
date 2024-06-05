from flask import Flask, request, render_template, send_file
import PyPDF2
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    text_to_add = request.form['text']
    pdf_file = request.files['pdf']
    if pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_writer = PyPDF2.PdfWriter()
        # Example of adding text - this part would need to be customized based on your script logic
        for page in pdf_reader.pages:
            # Modify pages here
            pdf_writer.add_page(page)
        output_pdf_path = 'modified_pdf.pdf'
        with open(output_pdf_path, 'wb') as out:
            pdf_writer.write(out)
        return send_file(output_pdf_path, as_attachment=True)
    return 'No file uploaded', 400

if __name__ == '__main__':
    app.run(debug=True)
