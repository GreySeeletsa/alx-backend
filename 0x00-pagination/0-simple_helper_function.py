#!/usr/bin/env python3
"""module for task 0
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list for the
    given pagination parameters
    """
    # calc start index by sub 1 from curr page num
    # and then multiplying by the page size
    start_index = (page - 1) * page_size
    # calc end index by adding start index t page size
    end_index = start_index + page_size
    # return start and end indexes as tuple
    return (start_index, end_index)
