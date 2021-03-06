# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_oam_getoamserviceendpoint_input import TapiOamGetoamserviceendpointInput  # noqa: F401,E501
from tapi_server import util


class InlineObject22(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, input=None):  # noqa: E501
        """InlineObject22 - a model defined in OpenAPI

        :param input: The input of this InlineObject22.  # noqa: E501
        :type input: TapiOamGetoamserviceendpointInput
        """
        self.openapi_types = {
            'input': TapiOamGetoamserviceendpointInput
        }

        self.attribute_map = {
            'input': 'input'
        }

        self._input = input

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject22':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_22 of this InlineObject22.  # noqa: E501
        :rtype: InlineObject22
        """
        return util.deserialize_model(dikt, cls)

    @property
    def input(self):
        """Gets the input of this InlineObject22.


        :return: The input of this InlineObject22.
        :rtype: TapiOamGetoamserviceendpointInput
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this InlineObject22.


        :param input: The input of this InlineObject22.
        :type input: TapiOamGetoamserviceendpointInput
        """

        self._input = input
