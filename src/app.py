from flask import Flask, render_template, request
import Spotify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the artist name from the form submission
        artist_name = request.form.get("artist_name")
        # Call the Spotify functionality to search for the artist
        token = Spotify.get_token()
        artist_data = Spotify.search_for_artist(token, artist_name)
        if artist_data:
            # If artist data is found, get the artist's top tracks and image
            artist_id = artist_data["id"]
            songs = Spotify.get_songs_by_artist(token, artist_id)
            artist_image = Spotify.get_artist_image(token, artist_id)

            return render_template("index.html", data={"artist": artist_data, "songs": songs, "image": artist_image})
        else:
            # If artist data is not found, display an error message
            return render_template("index.html", error="Artist not found.")
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5100)
