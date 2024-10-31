#!/usr/bin/env python3
"""
Server module for paginating a dataset of popular baby names.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a specific page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of data based on pagination parameters.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows for the specified page.
        """
        p = "page must be a positive integer"
        ps = "page_size must be a positive integer"
        # Check if page and page_size are valid integers greater than 0
        assert isinstance(page, int) and page > 0, p
        assert isinstance(page_size, int) and page_size > 0, ps

        # Get start and end index for the requested page
        start, end = index_range(page, page_size)

        # Return the appropriate slice of the dataset
        dataset = self.dataset()
        return dataset[start:end]if start < len(dataset) else []
