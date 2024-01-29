#!/usr/bin/env python3
"""module for task 1
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list for the
    given pagination parameters
    """
    # calc start index by sub 1 from the curr page num
    # and then multiplying by the page size
    start_index = (page - 1) * page_size
    # calc end index by adding start index to page size
    end_index = start_index + page_size
    # return start and end indexes as tuple
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        # a private attribute to store dataset
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset

        Returns:
            List[List]: List of rows representing the dataset.
        """
        # Check if dataset has not been loaded yet
        if self.__dataset is None:
            # open csv file
            with open(self.DATA_FILE) as f:
                # Read csv file
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # Store dataset in private attribute
            self.__dataset = dataset[1:]
        # Return the dataset
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a specific page of the dataset of popular baby names
        """
        # Verify that both page and page_size are integers greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        # Find correct start and end indexes for curr page
        start_index, end_index = index_range(page, page_size)
        # Retrieve dataset
        dataset = self.dataset()
        # Check if end_index is greater than length of dataset
        # If it is, return an empty list
        if end_index > len(dataset):
            return []
        # Return appropriate page of the dataset
        return dataset[start_index:end_index]
