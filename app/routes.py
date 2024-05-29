from app import *
from app.views import processing_prediction, get_predictions_list

app_flask = Flask(__name__)

@app_flask.route('/prediction', methods=['POST'])  # Método HTTP que será usado na requisi
def prediction():
    if request.form["generate"] and request.form["prompt"]:
        processing_prediction(request.form["prompt"])
        return redirect('/')
    else:
        return redirect(url_for('/'))
    
@app_flask.route('/', methods=['GET'])
def files():
    context = get_predictions_list()
    return render_template('generated.html', context=context)
