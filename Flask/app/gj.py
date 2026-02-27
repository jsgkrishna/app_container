from flask import Flask, jsonify, abort
import  requests

app = Flask(__name__)


@app.route("/<username>")
def get_user_gists(username):
    url = f"https://api.github.com/users/{username}/gists"
    response = requests.get(url)

    if response.status_code == 404:
        abort(404, description="User not found")

    response.raise_for_status()

    gists = response.json()

    data = []
    for gist in gists:
        item = {
            "id": gist["id"],
            "description": gist["description"],
            "url": gist["html_url"]
        }
        data.append(item)

    return jsonify({
        "user": username,
        "gists": data
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
