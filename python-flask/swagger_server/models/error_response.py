# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ErrorResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, error: str=None, description: str=None):  # noqa: E501
        """ErrorResponse - a model defined in Swagger

        :param error: The error of this ErrorResponse.  # noqa: E501
        :type error: str
        :param description: The description of this ErrorResponse.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'error': str,
            'description': str
        }

        self.attribute_map = {
            'error': 'error',
            'description': 'description'
        }

        self._error = error
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'ErrorResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ErrorResponse of this ErrorResponse.  # noqa: E501
        :rtype: ErrorResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error(self) -> str:
        """Gets the error of this ErrorResponse.


        :return: The error of this ErrorResponse.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error: str):
        """Sets the error of this ErrorResponse.


        :param error: The error of this ErrorResponse.
        :type error: str
        """
        if error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

    @property
    def description(self) -> str:
        """Gets the description of this ErrorResponse.


        :return: The description of this ErrorResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this ErrorResponse.


        :param description: The description of this ErrorResponse.
        :type description: str
        """

        self._description = description
