from flask import Flask, render_template, flash, redirect, url_for, request, make_response
from views import views
from cart import cart_data
from courses import courses

app = Flask(__name__)
app.secret_key = '1234'

app.register_blueprint(views, url_prefix="/")

class App:
    def __init__(self):
        @app.route('/')
        def index():
            return render_template('home.html', courses=cart_data.get_courses())

        @app.route('/add_to_cart/<int:product_id>')
        def add_to_cart(product_id):
            product = None

            # Find the product with the given product_id
            for product in courses:
                if product['id'] == product_id:
                    break

            if product:
                if product_id in cart_data:
                    flash('Product already exists in cart', 'error')
                else:
                    cart_data[product_id] = {
                        'name': product['name'],
                        'price': product['price'],
                        'selected_level': 'beginner'
                    }
                    flash('Product added to cart', 'success')
            else:
                flash('Invalid product')

            return redirect(url_for('views.coursepage'))

        @app.route('/cart')
        def view_cart():
            return render_template('cart.html', cart=cart_data.get_cart_data())

        @app.route('/update_price/<int:course_id>', methods=['POST'])
        def update_price(course_id):
            selected_level = request.form['level']

            # Update the price for the corresponding course based on the selected level
            if course_id in cart_data:
                course = cart_data[course_id]

                # Convert the price to float to not encounter problems with integers having extra numbers
                base_price = float(course['price'])

                if 'base_price' not in course:
                    # Store the original base price for reference
                    course['base_price'] = base_price

                if 'price_updated' in course:
                    # Revert to the original base price before applying the new level's increase
                    course['price'] = str(course['base_price'])
                    del course['price_updated']

                if selected_level != 'beginner':

                    # Apply the increase factor to the current price
                    if selected_level == 'amateur':
                        increase_factor = 1.2
                    elif selected_level == 'advanced':
                        increase_factor = 1.3
                    elif selected_level == 'pro':
                        increase_factor = 1.4
                    else:
                        increase_factor = 1.0

                    course['price'] = str(float(course['price']) * increase_factor)  # Convert to string
                    course[
                        'price_updated'] = True  # Set the flag to indicate price update (this is to avoid some confusion in the code)

                course['selected_level'] = selected_level

                return redirect(url_for('view_cart'))

            flash('Course not found in cart', 'error')
            return redirect(url_for('index'))


        @app.route('/checkout')
        def checkout():

            # Default Total for the Reciept only showed if the user did not choose something
            total = 0

            # Receipt Header

            receipt = '\n----------RECEIPT----------\n'

            for product_id, product_data in cart_data.items():
                product_name = product_data['name']
                product_price = product_data['price']
                product_level = product_data['selected_level']
                total += float(product_price)

                # Format the Receipt

                receipt += f'Item: {product_name}\n'
                receipt += f'Level: {product_level}\n'
                receipt += f'Price: ${product_price}\n'
                receipt += '---------------------------\n'

            receipt += f'Total: ${total}\n'

            # Clear the cart

            cart_data.clear()

            # Create a response with the receipt data and uses the make_response function by flask

            response = make_response(receipt)
            response.headers['Content-Disposition'] = 'attachment; filename=receipt.txt'
            response.headers['Content-type'] = 'text/plain'

            return response

if __name__ == '__main__':
    app_instance = App()
    app.run(debug=True)
