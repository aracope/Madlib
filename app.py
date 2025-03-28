from flask import Flask, request, render_template, redirect, url_for
from stories import stories, Story

app = Flask(__name__)

@app.route("/")
def home():
    """Homepage with dropdown to select a story."""
    return render_template("home.html", stories=stories)

@app.route("/questions")
def ask_questions():
    """Generate form dynamically based on the selected story."""
    story_id = request.args.get("story")
    story = stories.get(story_id)

    if not story:
        return "Story not found", 404

    return render_template("questions.html", story_name=story_id, prompts=story.prompts)

@app.route("/story")
def show_story():
    """Generate and display the completed madlib story."""
    story_id = request.args.get("story")
    story = stories.get(story_id)

    if not story:
        return "Story not found", 404

    answers = {key: request.args[key] for key in story.prompts}
    madlib_text = story.generate(answers)

    return render_template("story.html", text=madlib_text)

@app.route("/create-story", methods=["GET", "POST"])
def create_story():
    """Page to create a new madlib story."""
    if request.method == "POST":
        story_name = request.form["story_title"]  # Ensure name matches form
        prompts = request.form["prompts"].split(",")  # Convert comma-separated input into list
        template = request.form["story_template"]

        stories[story_name] = Story(prompts, template)  # Store new story

        return redirect(url_for("home"))  

    return render_template("create_story.html")

if __name__ == "__main__":
    app.run(debug=True)










# *****************************

# from flask import Flask, request, render_template, redirect, url_for
# from stories import stories, Story

# app = Flask(__name__)


# @app.route("/")
# def home():
#     """Homepage with dropdown to select a story."""
#     return render_template("home.html", stories=stories)

# @app.route("/questions")
# def ask_questions():
#     """Generate form dynamically based on the selected story."""
#     story_id = request.args.get("story")
#     story = stories.get(story_id)

#     if not story:
#         return "Story not found", 404

#     return render_template("questions.html", story_name=story_id, prompts=story.prompts)

# @app.route("/story")
# def show_story():
#     """Generate and display the completed madlib story."""
#     story_id = request.args.get("story")
#     story = stories.get(story_id)

#     if not story:
#         return "Story not found", 404

#     answers = {key: request.args[key] for key in story.prompts}
#     madlib_text = story.generate(answers)

#     return render_template("story.html", text=madlib_text)

# @app.route("/new-story", methods=["GET", "POST"])
# def new_story():
#     """Page to create a new madlib story."""
#     if request.method == "POST":
#         title = request.form["title"]
#         words = request.form["words"].split(",")  # Convert comma-separated words to a list
#         template = request.form["template"]

#         stories[title] = Story(words, template)  # Store new story in dictionary

#         return redirect(url_for("home"))  # Redirect to homepage

#     return render_template("new_story.html")

# @app.route('/create-story', methods=['GET', 'POST'])
# def create_story():
#     if request.method == 'POST':
#         story_name = request.form['story_name']
#         prompts = request.form.getlist('prompts')  # List of prompts (comma separated)
#         template = request.form['template']

#         # Create a new story instance
#         new_story = Story(prompts, template)
#         stories[story_name] = new_story

#         # Redirect back to the homepage after the story is created
#         return redirect(url_for('home'))  # This will redirect to the 'home' route

#     return render_template('create_story.html')

# if __name__ == "__main__":
#     app.run(debug=True)
