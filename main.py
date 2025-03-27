from flask import Flask, render_template, send_file, request, redirect, url_for
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "educational_purposes_only")

@app.route('/')
def index():
    """Home page with project information and educational disclaimer."""
    return render_template('index.html')

@app.route('/documentation')
def documentation():
    """Documentation page with detailed explanations."""
    return render_template('documentation.html')

@app.route('/detection')
def detection():
    """Information on how keyloggers can be detected."""
    return render_template('detection.html')

@app.route('/source')
def source_code():
    """Page to view the keylogger source code."""
    return render_template('source.html')

@app.route('/download')
def download():
    """Page for downloading the educational package."""
    return render_template('download.html')

@app.route('/download/package')
def download_package():
    """Endpoint to download the keylogger package."""
    try:
        # This would normally zip the files, but in this demo we'll just provide the Python file
        return send_file('keylogger.py', 
                        mimetype='text/plain',
                        as_attachment=True,
                        download_name='educational_keylogger.py')
    except Exception as e:
        logging.error(f"Download error: {e}")
        return render_template('error.html', error="Download failed")

@app.route('/lab')
def lab():
    """Interactive educational lab environment."""
    return render_template('lab.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)