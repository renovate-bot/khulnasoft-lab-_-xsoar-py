# coding: utf-8

"""
    Demisto API

    This is the public REST API to integrate with the demisto server. HTTP request can be sent using any HTTP-client.  For an example dedicated client take a look at: https://github.com/demisto/demisto-py.  Requests must include API-key that can be generated in the Demisto web client under 'Settings' -> 'Integrations' -> 'API keys'   Optimistic Locking and Versioning\\:  When using Demisto REST API, you will need to make sure to work on the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you to override a newer item). In addition, you can pass 'version\\: -1' to force data override (make sure that other users data might be lost).  Assume that Alice and Bob both read the same data from Demisto server, then they both changed the data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s? To solve this, each data item in Demisto has a numeric incremental version. If Alice saved an item with version 4 and Bob trying to save the same item with version 3, Demisto will rollback Bob request and returns a DB version conflict error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using 'curl'\\:  ``` curl 'https://hostname:443/incidents/search' -H 'content-type: application/json' -H 'accept: application/json' -H 'Authorization: <API Key goes here>' --data-binary '{\"filter\":{\"query\":\"-status:closed -category:job\",\"period\":{\"by\":\"day\",\"fromValue\":7}}}' --compressed ```  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TerminalOptions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'echo': 'int',
        'terminal': 'bool',
        'terminal_height': 'int',
        'terminal_type': 'str',
        'terminal_width': 'int',
        'ty_i_speed': 'int',
        'ty_o_speed': 'int'
    }

    attribute_map = {
        'echo': 'Echo',
        'terminal': 'Terminal',
        'terminal_height': 'TerminalHeight',
        'terminal_type': 'TerminalType',
        'terminal_width': 'TerminalWidth',
        'ty_i_speed': 'TyISpeed',
        'ty_o_speed': 'TyOSpeed'
    }

    def __init__(self, echo=None, terminal=None, terminal_height=None, terminal_type=None, terminal_width=None, ty_i_speed=None, ty_o_speed=None):  # noqa: E501
        """TerminalOptions - a model defined in Swagger"""  # noqa: E501

        self._echo = None
        self._terminal = None
        self._terminal_height = None
        self._terminal_type = None
        self._terminal_width = None
        self._ty_i_speed = None
        self._ty_o_speed = None
        self.discriminator = None

        if echo is not None:
            self.echo = echo
        if terminal is not None:
            self.terminal = terminal
        if terminal_height is not None:
            self.terminal_height = terminal_height
        if terminal_type is not None:
            self.terminal_type = terminal_type
        if terminal_width is not None:
            self.terminal_width = terminal_width
        if ty_i_speed is not None:
            self.ty_i_speed = ty_i_speed
        if ty_o_speed is not None:
            self.ty_o_speed = ty_o_speed

    @property
    def echo(self):
        """Gets the echo of this TerminalOptions.  # noqa: E501


        :return: The echo of this TerminalOptions.  # noqa: E501
        :rtype: int
        """
        return self._echo

    @echo.setter
    def echo(self, echo):
        """Sets the echo of this TerminalOptions.


        :param echo: The echo of this TerminalOptions.  # noqa: E501
        :type: int
        """

        self._echo = echo

    @property
    def terminal(self):
        """Gets the terminal of this TerminalOptions.  # noqa: E501


        :return: The terminal of this TerminalOptions.  # noqa: E501
        :rtype: bool
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this TerminalOptions.


        :param terminal: The terminal of this TerminalOptions.  # noqa: E501
        :type: bool
        """

        self._terminal = terminal

    @property
    def terminal_height(self):
        """Gets the terminal_height of this TerminalOptions.  # noqa: E501


        :return: The terminal_height of this TerminalOptions.  # noqa: E501
        :rtype: int
        """
        return self._terminal_height

    @terminal_height.setter
    def terminal_height(self, terminal_height):
        """Sets the terminal_height of this TerminalOptions.


        :param terminal_height: The terminal_height of this TerminalOptions.  # noqa: E501
        :type: int
        """

        self._terminal_height = terminal_height

    @property
    def terminal_type(self):
        """Gets the terminal_type of this TerminalOptions.  # noqa: E501


        :return: The terminal_type of this TerminalOptions.  # noqa: E501
        :rtype: str
        """
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, terminal_type):
        """Sets the terminal_type of this TerminalOptions.


        :param terminal_type: The terminal_type of this TerminalOptions.  # noqa: E501
        :type: str
        """

        self._terminal_type = terminal_type

    @property
    def terminal_width(self):
        """Gets the terminal_width of this TerminalOptions.  # noqa: E501


        :return: The terminal_width of this TerminalOptions.  # noqa: E501
        :rtype: int
        """
        return self._terminal_width

    @terminal_width.setter
    def terminal_width(self, terminal_width):
        """Sets the terminal_width of this TerminalOptions.


        :param terminal_width: The terminal_width of this TerminalOptions.  # noqa: E501
        :type: int
        """

        self._terminal_width = terminal_width

    @property
    def ty_i_speed(self):
        """Gets the ty_i_speed of this TerminalOptions.  # noqa: E501


        :return: The ty_i_speed of this TerminalOptions.  # noqa: E501
        :rtype: int
        """
        return self._ty_i_speed

    @ty_i_speed.setter
    def ty_i_speed(self, ty_i_speed):
        """Sets the ty_i_speed of this TerminalOptions.


        :param ty_i_speed: The ty_i_speed of this TerminalOptions.  # noqa: E501
        :type: int
        """

        self._ty_i_speed = ty_i_speed

    @property
    def ty_o_speed(self):
        """Gets the ty_o_speed of this TerminalOptions.  # noqa: E501


        :return: The ty_o_speed of this TerminalOptions.  # noqa: E501
        :rtype: int
        """
        return self._ty_o_speed

    @ty_o_speed.setter
    def ty_o_speed(self, ty_o_speed):
        """Sets the ty_o_speed of this TerminalOptions.


        :param ty_o_speed: The ty_o_speed of this TerminalOptions.  # noqa: E501
        :type: int
        """

        self._ty_o_speed = ty_o_speed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(TerminalOptions, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TerminalOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
