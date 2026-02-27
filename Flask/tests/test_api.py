from app.gj import app

mytest = app.test_client()

def test_octocat_gists():
    response = mytest.get("/octocat")
    data = response.get_json()
    assert response.status_code == 200

    print(f"\nGists by {data['user']}:")
    for gist in data["gists"]:
        print(f"- ID: {gist['id']}, Description: {gist['description']}, URL: {gist['url']}")
