from app import requests, request, replicate
from app.models import create, get_predictions



def processing_prediction(prompt_input):
    prompt_input = request.form["prompt"]
    try:
        prediction = replicate.run(
            "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
            input={"prompt": prompt_input}
            )
        url = prediction[0]
        prompt_input = str(prompt_input).replace(" ","_")
        require_img = requests.get(url)
        with open(f'app/static/{ prompt_input }.png', 'wb') as img:
            img.write(require_img.content)
        create(prompt_input)
        return prompt_input
    
    except Exception as e:
        print('Error: ',e)
        return "Error: ",e

def get_predictions_list():
    predictions = get_predictions()
    context = {}
    for i in predictions:
        context[f'{i[2]}.png'] = f'app/static/{i[2]}.png'
    return context