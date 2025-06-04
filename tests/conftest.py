import pytest
import os

@pytest.fixture(scope="session")
def test_data_dir():
    # Create a temporary directory for test data
    test_dir = "test_data"
    os.makedirs(test_dir, exist_ok=True)
    yield test_dir
    # Cleanup after tests
    for file in os.listdir(test_dir):
        os.remove(os.path.join(test_dir, file))
    os.rmdir(test_dir)

@pytest.fixture(scope="session")
def sample_csv(test_data_dir):
    # Create a sample CSV file for testing
    csv_path = os.path.join(test_data_dir, "sample.csv")
    with open(csv_path, "w") as f:
        f.write("column1,column2\nvalue1,value2\nvalue3,value4")
    yield csv_path
    os.remove(csv_path) 