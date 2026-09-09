from src.data_loader import DataLoader

def test_data_loader():
    loader = DataLoader()
    sample_data = [1, 2, 3]
    result = loader.load(sample_data)

    assert result == sample_data