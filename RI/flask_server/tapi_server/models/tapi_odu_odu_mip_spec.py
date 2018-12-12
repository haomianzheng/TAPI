# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_odu_odu_defect_pac import TapiOduOduDefectPac  # noqa: F401,E501
from tapi_server.models.tapi_odu_odu_mip_pac import TapiOduOduMipPac  # noqa: F401,E501
from tapi_server.models.tapi_odu_odu_ncm_pac import TapiOduOduNcmPac  # noqa: F401,E501
from tapi_server.models.tapi_odu_odu_pm_pac import TapiOduOduPmPac  # noqa: F401,E501
from tapi_server.models.tapi_odu_odu_tcm_mip_pac import TapiOduOduTcmMipPac  # noqa: F401,E501
from tapi_server import util


class TapiOduOduMipSpec(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, odu_mip=None, odu_pm=None, odu_ncm=None, odu_tcm=None, odu_defect=None):  # noqa: E501
        """TapiOduOduMipSpec - a model defined in OpenAPI

        :param odu_mip: The odu_mip of this TapiOduOduMipSpec.  # noqa: E501
        :type odu_mip: TapiOduOduMipPac
        :param odu_pm: The odu_pm of this TapiOduOduMipSpec.  # noqa: E501
        :type odu_pm: TapiOduOduPmPac
        :param odu_ncm: The odu_ncm of this TapiOduOduMipSpec.  # noqa: E501
        :type odu_ncm: TapiOduOduNcmPac
        :param odu_tcm: The odu_tcm of this TapiOduOduMipSpec.  # noqa: E501
        :type odu_tcm: TapiOduOduTcmMipPac
        :param odu_defect: The odu_defect of this TapiOduOduMipSpec.  # noqa: E501
        :type odu_defect: TapiOduOduDefectPac
        """
        self.openapi_types = {
            'odu_mip': TapiOduOduMipPac,
            'odu_pm': TapiOduOduPmPac,
            'odu_ncm': TapiOduOduNcmPac,
            'odu_tcm': TapiOduOduTcmMipPac,
            'odu_defect': TapiOduOduDefectPac
        }

        self.attribute_map = {
            'odu_mip': 'odu-mip',
            'odu_pm': 'odu-pm',
            'odu_ncm': 'odu-ncm',
            'odu_tcm': 'odu-tcm',
            'odu_defect': 'odu-defect'
        }

        self._odu_mip = odu_mip
        self._odu_pm = odu_pm
        self._odu_ncm = odu_ncm
        self._odu_tcm = odu_tcm
        self._odu_defect = odu_defect

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOduOduMipSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.odu.OduMipSpec of this TapiOduOduMipSpec.  # noqa: E501
        :rtype: TapiOduOduMipSpec
        """
        return util.deserialize_model(dikt, cls)

    @property
    def odu_mip(self):
        """Gets the odu_mip of this TapiOduOduMipSpec.


        :return: The odu_mip of this TapiOduOduMipSpec.
        :rtype: TapiOduOduMipPac
        """
        return self._odu_mip

    @odu_mip.setter
    def odu_mip(self, odu_mip):
        """Sets the odu_mip of this TapiOduOduMipSpec.


        :param odu_mip: The odu_mip of this TapiOduOduMipSpec.
        :type odu_mip: TapiOduOduMipPac
        """

        self._odu_mip = odu_mip

    @property
    def odu_pm(self):
        """Gets the odu_pm of this TapiOduOduMipSpec.


        :return: The odu_pm of this TapiOduOduMipSpec.
        :rtype: TapiOduOduPmPac
        """
        return self._odu_pm

    @odu_pm.setter
    def odu_pm(self, odu_pm):
        """Sets the odu_pm of this TapiOduOduMipSpec.


        :param odu_pm: The odu_pm of this TapiOduOduMipSpec.
        :type odu_pm: TapiOduOduPmPac
        """

        self._odu_pm = odu_pm

    @property
    def odu_ncm(self):
        """Gets the odu_ncm of this TapiOduOduMipSpec.


        :return: The odu_ncm of this TapiOduOduMipSpec.
        :rtype: TapiOduOduNcmPac
        """
        return self._odu_ncm

    @odu_ncm.setter
    def odu_ncm(self, odu_ncm):
        """Sets the odu_ncm of this TapiOduOduMipSpec.


        :param odu_ncm: The odu_ncm of this TapiOduOduMipSpec.
        :type odu_ncm: TapiOduOduNcmPac
        """

        self._odu_ncm = odu_ncm

    @property
    def odu_tcm(self):
        """Gets the odu_tcm of this TapiOduOduMipSpec.


        :return: The odu_tcm of this TapiOduOduMipSpec.
        :rtype: TapiOduOduTcmMipPac
        """
        return self._odu_tcm

    @odu_tcm.setter
    def odu_tcm(self, odu_tcm):
        """Sets the odu_tcm of this TapiOduOduMipSpec.


        :param odu_tcm: The odu_tcm of this TapiOduOduMipSpec.
        :type odu_tcm: TapiOduOduTcmMipPac
        """

        self._odu_tcm = odu_tcm

    @property
    def odu_defect(self):
        """Gets the odu_defect of this TapiOduOduMipSpec.


        :return: The odu_defect of this TapiOduOduMipSpec.
        :rtype: TapiOduOduDefectPac
        """
        return self._odu_defect

    @odu_defect.setter
    def odu_defect(self, odu_defect):
        """Sets the odu_defect of this TapiOduOduMipSpec.


        :param odu_defect: The odu_defect of this TapiOduOduMipSpec.
        :type odu_defect: TapiOduOduDefectPac
        """

        self._odu_defect = odu_defect