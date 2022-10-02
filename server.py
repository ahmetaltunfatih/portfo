from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_name(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open("database.txt", "a") as database1:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database1.write(f"\n{email}, {subject}, {message}")


def write_to_csv(data):
    with open("database.csv", "a", newline="") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter =",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "The data could not be saved to database"
    else:
        return "form was not submitted. Try again"

# to receive data of the submiited form in the contact,
# name must be specified for email, subject, and message
# in the contact.html.

# To send thank you message, the contact.html copied as
# thankyou.html and the part related to email entries was deleted.
# The text was modified.
# With redirect function, thankyou.html file was opened with submission the data

# To write the data received from the user to a file, the write_to_file function is used.