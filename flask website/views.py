from flask import Blueprint, render_template
from cart import cart_data
from courses import courses

class ViewsBlueprint(Blueprint):
    def __init__(self, name, import_name):
        super().__init__(name, import_name)

        self.add_url_rule("/", view_func=self.homepage)
        self.add_url_rule("/teacher", view_func=self.teacher)
        self.add_url_rule("/course", view_func=self.coursepage)
        self.add_url_rule("/about", view_func=self.aboutpage)
        self.add_url_rule("/cart", view_func=self.cart)

    def homepage(self):
        return render_template("home.html")

    def teacher(self):
        return render_template("teacher.html")

    def coursepage(self):
        return render_template("courses.html", courses=courses, cart=cart_data)

    def aboutpage(self):
        return render_template("about.html")

    def cart(self):
        return render_template("cart.html", cart=cart_data)

views = ViewsBlueprint("views", __name__)
