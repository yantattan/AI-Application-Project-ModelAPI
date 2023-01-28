# Libraries required
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from keras.models import load_model
# from keras.preprocessing import image as image_utils
# from keras.applications.imagenet_utils import preprocess_input

app = Flask(__name__)
# model = load_model('contamination_detector.h5')

label_map = {
    'clean_bottle': 0, 
    'clean_can': 1, 
    'clean_cardboard': 2, 
    'clean_paper': 3, 
    'dirty_bottle': 4, 
    'dirty_paper': 5, 
    'filled_bottle': 6, 
    'rusted_can': 7, 
    'stained_cardboard': 8
}

load_dotenv()

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         data = request.get_json()
#         image_path = os.getenv('UPLOAD_URL') + data['filename']
#     except Exception as e:
#         return jsonify({'error': e})

#     try:
#         image = image_utils.load_img(image_path, target_size=(224, 224))
#         image = image_utils.img_to_array(image)
#         image = image.reshape(1,224,224,3)
#         image = preprocess_input(image)

#         preds = model.predict(image)
#         pred_index = preds.argmax(axis=-1)[0]
#         label = list(filter(lambda x: x[1] == pred_index, label_map.items()))[0][0]
#         confidence = preds[0][pred_index]

#         return jsonify({
#             'prediction': label,
#             'confidence': confidence
#         })
#     except Exception as e:
#         print(e)
#         return jsonify({
#             'error': 'Error occurred. Either the server is offline or target image is not found'
#         }), 500

@app.route('/weee', methods=['GET'])
def lol():
    return jsonify({'lol': 'You got it'})

@app.route('/weee', methods=['POST'])
def lolol():
    return jsonify({'lol': 'You did it'})

if __name__ == "__main__":
    app.run(debug=True)
