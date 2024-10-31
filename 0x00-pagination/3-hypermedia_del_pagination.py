#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}  # noqa: E501
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:  # noqa: E501
        """
        Provide a deletion-resilient hypermedia pagination.

        Args:
            index (int): The start index of the page.
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: A dictionary containing the pagination info.
        """
        assert isinstance(index, int) and 0 <= index < len(self.indexed_dataset()), "Index out of range"  # noqa: E501
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"  # noqa: E501

        indexed_data = self.indexed_dataset()
        data = []
        current_index = index
        collected_items = 0

        # Collect page data while skipping over any deleted indices
        while collected_items < page_size and current_index < len(indexed_data):  # noqa: E501
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                collected_items += 1
            current_index += 1

        next_index = current_index if current_index < len(indexed_data) else None  # noqa: E501

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
