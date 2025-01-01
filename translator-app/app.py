from flask import Flask, render_template, request
import boto3

app = Flask(__name__)

# AWS Translate client
translate = boto3.client('translate', region_name='us-east-1')  # You can change the region as needed

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    source_text = request.form['sourceText']
    source_lang = request.form['sourceLang']
    target_lang = request.form['targetLang']

    try:
        response = translate.translate_text(
            Text=source_text,
            SourceLanguageCode=source_lang,
            TargetLanguageCode=target_lang
        )
        translated_text = response['TranslatedText']
    except Exception as e:
        translated_text = f"Error: {e}"

    return render_template('index.html', source_text=source_text, translated_text=translated_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
