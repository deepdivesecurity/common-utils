import pytest
from unittest.mock import patch
from src.file_utils import FileHandler

@pytest.fixture
def mock_file_handler():
    return FileHandler()

@patch("tkinter.filedialog.askopenfilename")
def test_select_file_success(mock_askopenfilename, mock_file_handler):
    # Simulating the user selecting a file
    mock_askopenfilename.return_value = "/path/to/test_file.csv"

    mock_file_handler.select_file()

    # Assert that the file path and extension are set correctly
    assert mock_file_handler.get_file_path() == "/path/to/test_file.csv"
    assert mock_file_handler.get_file_extension() == ".csv"


@patch("tkinter.filedialog.askopenfilename")
def test_select_file_cancel(mock_askopenfilename, mock_file_handler):
    # Simulating the user canceling the file selection
    mock_askopenfilename.return_value = ""

    mock_file_handler.select_file()

    # Assert that both file path and extension are None after canceling
    assert mock_file_handler.get_file_path() is None
    assert mock_file_handler.get_file_extension() is None


def test_get_file_path(mock_file_handler):
    mock_file_handler.file_path = "/path/to/test_file.csv"
    assert mock_file_handler.get_file_path() == "/path/to/test_file.csv"


def test_get_file_extension(mock_file_handler):
    mock_file_handler.file_extension = ".xlsx"
    assert mock_file_handler.get_file_extension() == ".xlsx"


@patch("tkinter.filedialog.askopenfilename")
def test_select_file_invalid_extension(mock_askopenfilename, mock_file_handler):
    # Simulating the selection of a file with an invalid extension
    mock_askopenfilename.return_value = "/path/to/invalid_file.txt"

    mock_file_handler.select_file()

    # Assert that the file path is set and the extension is `.txt`
    assert mock_file_handler.get_file_path() == "/path/to/invalid_file.txt"
    assert mock_file_handler.get_file_extension() == ".txt"