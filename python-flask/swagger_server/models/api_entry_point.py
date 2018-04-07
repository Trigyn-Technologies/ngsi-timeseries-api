# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class APIEntryPoint(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, entities_url: str=None, types_url: str=None, subscriptions_url: str=None):  # noqa: E501
        """APIEntryPoint - a model defined in Swagger

        :param entities_url: The entities_url of this APIEntryPoint.  # noqa: E501
        :type entities_url: str
        :param types_url: The types_url of this APIEntryPoint.  # noqa: E501
        :type types_url: str
        :param subscriptions_url: The subscriptions_url of this APIEntryPoint.  # noqa: E501
        :type subscriptions_url: str
        """
        self.swagger_types = {
            'entities_url': str,
            'types_url': str,
            'subscriptions_url': str
        }

        self.attribute_map = {
            'entities_url': 'entities_url',
            'types_url': 'types_url',
            'subscriptions_url': 'subscriptions_url'
        }

        self._entities_url = entities_url
        self._types_url = types_url
        self._subscriptions_url = subscriptions_url

    @classmethod
    def from_dict(cls, dikt) -> 'APIEntryPoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The APIEntryPoint of this APIEntryPoint.  # noqa: E501
        :rtype: APIEntryPoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entities_url(self) -> str:
        """Gets the entities_url of this APIEntryPoint.

        URL which points to the entities resource  # noqa: E501

        :return: The entities_url of this APIEntryPoint.
        :rtype: str
        """
        return self._entities_url

    @entities_url.setter
    def entities_url(self, entities_url: str):
        """Sets the entities_url of this APIEntryPoint.

        URL which points to the entities resource  # noqa: E501

        :param entities_url: The entities_url of this APIEntryPoint.
        :type entities_url: str
        """
        if entities_url is None:
            raise ValueError("Invalid value for `entities_url`, must not be `None`")  # noqa: E501

        self._entities_url = entities_url

    @property
    def types_url(self) -> str:
        """Gets the types_url of this APIEntryPoint.

        URL which points to the types resource  # noqa: E501

        :return: The types_url of this APIEntryPoint.
        :rtype: str
        """
        return self._types_url

    @types_url.setter
    def types_url(self, types_url: str):
        """Sets the types_url of this APIEntryPoint.

        URL which points to the types resource  # noqa: E501

        :param types_url: The types_url of this APIEntryPoint.
        :type types_url: str
        """
        if types_url is None:
            raise ValueError("Invalid value for `types_url`, must not be `None`")  # noqa: E501

        self._types_url = types_url

    @property
    def subscriptions_url(self) -> str:
        """Gets the subscriptions_url of this APIEntryPoint.

        URL which points to the subscriptions resource  # noqa: E501

        :return: The subscriptions_url of this APIEntryPoint.
        :rtype: str
        """
        return self._subscriptions_url

    @subscriptions_url.setter
    def subscriptions_url(self, subscriptions_url: str):
        """Sets the subscriptions_url of this APIEntryPoint.

        URL which points to the subscriptions resource  # noqa: E501

        :param subscriptions_url: The subscriptions_url of this APIEntryPoint.
        :type subscriptions_url: str
        """
        if subscriptions_url is None:
            raise ValueError("Invalid value for `subscriptions_url`, must not be `None`")  # noqa: E501

        self._subscriptions_url = subscriptions_url
