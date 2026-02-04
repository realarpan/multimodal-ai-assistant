@pytest.fixture
def test_db():
    # Setup test DB
    yield
    # Teardown
