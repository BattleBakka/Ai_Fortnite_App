import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_cosmetic', methods=['POST'])
def generate_cosmetic():
    try:
        # Get prompt from the request body (which is sent by the JavaScript)
        prompt = request.json.get('prompt')
        
        # Call OpenAI API to generate image based on the prompt
        response = openai.Image.create(
            prompt=prompt,  # Use the prompt received from the front-end
            n=1,  # Number of images to generate
            size="1024x1024"  # Size of the generated image
        )
        
        # Extract the image URL from the API response
        image_url = response['data'][0]['url']
        
        # Send the image URL back to the front-end
        return jsonify({'image_url': image_url})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
