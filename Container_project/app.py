from flask import Flask, render_template, request
from forms import ProductForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Define the volume of six rectangular containers (example volumes in cubic cm)
containers = {
    'container_1': 400 * 500,  # Container 1 volume
    'container_2': 350 * 450,  # Container 2 volume
    'container_3': 300 * 400,  # Container 3 volume
    'container_4': 250 * 350,  # Container 4 volume
    'container_5': 200 * 300,  # Container 5 volume
    'container_6': 150 * 250  # Container 6 volume
}


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ProductForm()
    if form.validate_on_submit():
        length = form.length.data
        width = form.width.data
        height = form.height.data
        container_type = form.container.data

        # Calculate the volume of the product
        product_volume = length * width * height

        # Get the volume of the selected container
        container_volume = containers.get(container_type)

        # Calculate how many products can fit into the container
        if container_volume and product_volume:
            num_products = container_volume // product_volume
        else:
            num_products = 0

        return render_template('result.html', num_products=int(num_products), container=container_type)

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)