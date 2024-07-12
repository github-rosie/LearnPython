import pytest


# Define a fixture that sets up some state
@pytest.fixture
def example_fixture():
    # Setup code
    resource = "example resource"
    yield resource
    # Teardown code (if any) would go here



def test_using_fixture(example_fixture):
    # The fixture is injected into the test function
    assert example_fixture == "example resource"

def test_another_using_fixture(example_fixture):
    # Another test using the same fixture
    assert example_fixture.startswith("example")