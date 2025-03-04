# coding: utf-8

"""
    Version 3 of CANDY HOUSE’s Sesame API

    We use RESTful API to provide basic manipulation of the Sesame smart lock, including: * Get Sesame lock/unlock status * Get battery status * Lock and unlock Sesame * Sync Sesame status * Get results for lock, unlock, and sync commands   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: sesame@candyhouse.co
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class GetSesameResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'device_id': 'str',
        'serial': 'str',
        'nickname': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'serial': 'serial',
        'nickname': 'nickname'
    }

    def __init__(self, device_id=None, serial=None, nickname=None):  # noqa: E501
        """GetSesameResponse - a model defined in OpenAPI"""  # noqa: E501

        self._device_id = None
        self._serial = None
        self._nickname = None
        self.discriminator = None

        self.device_id = device_id
        self.serial = serial
        self.nickname = nickname

    @property
    def device_id(self):
        """Gets the device_id of this GetSesameResponse.  # noqa: E501

        Sesame unique ID  # noqa: E501

        :return: The device_id of this GetSesameResponse.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this GetSesameResponse.

        Sesame unique ID  # noqa: E501

        :param device_id: The device_id of this GetSesameResponse.  # noqa: E501
        :type: str
        """
        if device_id is None:
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501

        self._device_id = device_id

    @property
    def serial(self):
        """Gets the serial of this GetSesameResponse.  # noqa: E501

        Sesame serial  # noqa: E501

        :return: The serial of this GetSesameResponse.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this GetSesameResponse.

        Sesame serial  # noqa: E501

        :param serial: The serial of this GetSesameResponse.  # noqa: E501
        :type: str
        """
        if serial is None:
            raise ValueError("Invalid value for `serial`, must not be `None`")  # noqa: E501

        self._serial = serial

    @property
    def nickname(self):
        """Gets the nickname of this GetSesameResponse.  # noqa: E501

        Sesame nickname  # noqa: E501

        :return: The nickname of this GetSesameResponse.  # noqa: E501
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this GetSesameResponse.

        Sesame nickname  # noqa: E501

        :param nickname: The nickname of this GetSesameResponse.  # noqa: E501
        :type: str
        """
        if nickname is None:
            raise ValueError("Invalid value for `nickname`, must not be `None`")  # noqa: E501

        self._nickname = nickname

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetSesameResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
