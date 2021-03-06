# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_path_computation_path_objective_function import TapiPathComputationPathObjectiveFunction  # noqa: F401,E501
from tapi_server.models.tapi_path_computation_path_optimization_constraint import TapiPathComputationPathOptimizationConstraint  # noqa: F401,E501
from tapi_server.models.tapi_path_computation_routing_constraint import TapiPathComputationRoutingConstraint  # noqa: F401,E501
from tapi_server import util


class TapiPathComputationOptimizep2ppathInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, routing_constraint=None, path_id_or_name=None, optimization_constraint=None, objective_function=None):  # noqa: E501
        """TapiPathComputationOptimizep2ppathInput - a model defined in OpenAPI

        :param routing_constraint: The routing_constraint of this TapiPathComputationOptimizep2ppathInput.  # noqa: E501
        :type routing_constraint: TapiPathComputationRoutingConstraint
        :param path_id_or_name: The path_id_or_name of this TapiPathComputationOptimizep2ppathInput.  # noqa: E501
        :type path_id_or_name: str
        :param optimization_constraint: The optimization_constraint of this TapiPathComputationOptimizep2ppathInput.  # noqa: E501
        :type optimization_constraint: TapiPathComputationPathOptimizationConstraint
        :param objective_function: The objective_function of this TapiPathComputationOptimizep2ppathInput.  # noqa: E501
        :type objective_function: TapiPathComputationPathObjectiveFunction
        """
        self.openapi_types = {
            'routing_constraint': TapiPathComputationRoutingConstraint,
            'path_id_or_name': str,
            'optimization_constraint': TapiPathComputationPathOptimizationConstraint,
            'objective_function': TapiPathComputationPathObjectiveFunction
        }

        self.attribute_map = {
            'routing_constraint': 'routing-constraint',
            'path_id_or_name': 'path-id-or-name',
            'optimization_constraint': 'optimization-constraint',
            'objective_function': 'objective-function'
        }

        self._routing_constraint = routing_constraint
        self._path_id_or_name = path_id_or_name
        self._optimization_constraint = optimization_constraint
        self._objective_function = objective_function

    @classmethod
    def from_dict(cls, dikt) -> 'TapiPathComputationOptimizep2ppathInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.path.computation.optimizep2ppath.Input of this TapiPathComputationOptimizep2ppathInput.  # noqa: E501
        :rtype: TapiPathComputationOptimizep2ppathInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def routing_constraint(self):
        """Gets the routing_constraint of this TapiPathComputationOptimizep2ppathInput.


        :return: The routing_constraint of this TapiPathComputationOptimizep2ppathInput.
        :rtype: TapiPathComputationRoutingConstraint
        """
        return self._routing_constraint

    @routing_constraint.setter
    def routing_constraint(self, routing_constraint):
        """Sets the routing_constraint of this TapiPathComputationOptimizep2ppathInput.


        :param routing_constraint: The routing_constraint of this TapiPathComputationOptimizep2ppathInput.
        :type routing_constraint: TapiPathComputationRoutingConstraint
        """

        self._routing_constraint = routing_constraint

    @property
    def path_id_or_name(self):
        """Gets the path_id_or_name of this TapiPathComputationOptimizep2ppathInput.

        none  # noqa: E501

        :return: The path_id_or_name of this TapiPathComputationOptimizep2ppathInput.
        :rtype: str
        """
        return self._path_id_or_name

    @path_id_or_name.setter
    def path_id_or_name(self, path_id_or_name):
        """Sets the path_id_or_name of this TapiPathComputationOptimizep2ppathInput.

        none  # noqa: E501

        :param path_id_or_name: The path_id_or_name of this TapiPathComputationOptimizep2ppathInput.
        :type path_id_or_name: str
        """

        self._path_id_or_name = path_id_or_name

    @property
    def optimization_constraint(self):
        """Gets the optimization_constraint of this TapiPathComputationOptimizep2ppathInput.


        :return: The optimization_constraint of this TapiPathComputationOptimizep2ppathInput.
        :rtype: TapiPathComputationPathOptimizationConstraint
        """
        return self._optimization_constraint

    @optimization_constraint.setter
    def optimization_constraint(self, optimization_constraint):
        """Sets the optimization_constraint of this TapiPathComputationOptimizep2ppathInput.


        :param optimization_constraint: The optimization_constraint of this TapiPathComputationOptimizep2ppathInput.
        :type optimization_constraint: TapiPathComputationPathOptimizationConstraint
        """

        self._optimization_constraint = optimization_constraint

    @property
    def objective_function(self):
        """Gets the objective_function of this TapiPathComputationOptimizep2ppathInput.


        :return: The objective_function of this TapiPathComputationOptimizep2ppathInput.
        :rtype: TapiPathComputationPathObjectiveFunction
        """
        return self._objective_function

    @objective_function.setter
    def objective_function(self, objective_function):
        """Sets the objective_function of this TapiPathComputationOptimizep2ppathInput.


        :param objective_function: The objective_function of this TapiPathComputationOptimizep2ppathInput.
        :type objective_function: TapiPathComputationPathObjectiveFunction
        """

        self._objective_function = objective_function
