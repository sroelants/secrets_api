"""
/api/secrets: - GET: return a list of all secrets
              - POST: Add a secret to the db
/api/secrets/<int:page>: - GET: Gets a page of secrets

/api/secret: - POST: Updates a secret
"""
from datetime import datetime


# GET /api/secrets

def test_get_secrets(test_client):
    """
    GIVEN: A test client
    WHEN: I hit the secrets endpoint
    THEN: I get a list of secrets
    """
    retval = test_client.get("/api/secrets", follow_redirects=True)
    assert retval.status_code == 200
    assert b"This is a first secret" in retval.data


def test_post_secret(test_client):
    """
    GIVEN: A test client
    WHEN: I add a secret
    THEN: I receive a status 200
    """
    retval = test_client.post("/api/secrets",
                              json={"secret": "Latest secret",
                                    "date_posted": datetime.now().isoformat(),
                                    "likes": 0},
                              follow_redirects=True)
    assert retval.status_code == 200


# POST /api/secrets

def test_add_to_db(test_client):
    """
    GIVEN: A test client
    WHEN: I add a secret
    THEN: I can retrieve it from the database
    """
    secret = {"secret": "Latest secret",
              "date_posted": datetime.now().isoformat(),
              "likes": 0}

    test_client.post("/api/secrets", json=secret, follow_redirects=True)
    retval2 = test_client.get("/api/secrets", follow_redirects=True)
    stored_secret = retval2.get_json()[-1]

    assert stored_secret["secret"] == secret["secret"]
    assert stored_secret["date_posted"] == secret["date_posted"]


# GET /api/secrets/<int:id>

def test_get_secret_page(test_client):
    """
    GIVEN: A test client
    WHEN: I query the first page of secrets
    THEN: I get a list of secrets
    """
    retval = test_client.get("/api/secrets/1", follow_redirects=True)
    assert retval.status_code == 200
    assert b"Latest secret" in retval.data


# PUT /api/secret

def test_update_secret(test_client):
    """
    GIVEN: A test client
    WHEN: I add update a secret
    THEN: I can verify it was updated
    """
    # Get a secret from the db
    retval = test_client.get("/api/secrets", follow_redirects=True)
    initial_secret = retval.get_json()[-1]
    # Update it
    initial_secret["likes"] = 100
    test_client.post("/api/secret", json=initial_secret, follow_redirects=True)
    # Retrieve it again
    retval2 = test_client.get("/api/secrets", follow_redirects=True)
    updated_secret = retval2.get_json()[-1]

    assert initial_secret["secret"] == updated_secret["secret"]
    assert initial_secret["date_posted"] == updated_secret["date_posted"]
