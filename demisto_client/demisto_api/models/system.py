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

from demisto_client.demisto_api.models.system_agent import SystemAgent  # noqa: F401,E501
from demisto_client.demisto_api.models.terminal_options import TerminalOptions  # noqa: F401,E501


class System(object):
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
        'agent': 'SystemAgent',
        'arch': 'str',
        'ciphers': 'list[str]',
        'credentials': 'str',
        'engine_id': 'str',
        'host': 'str',
        'integrationinstanceid': 'str',
        'issharedagent': 'bool',
        'name': 'str',
        'os': 'str',
        'password': 'str',
        'smb': 'int',
        'smbport': 'int',
        'sshkey': 'str',
        'sshport': 'int',
        'terminal_options': 'TerminalOptions',
        'user': 'str',
        'workgroup': 'str'
    }

    attribute_map = {
        'agent': 'agent',
        'arch': 'arch',
        'ciphers': 'ciphers',
        'credentials': 'credentials',
        'engine_id': 'engineId',
        'host': 'host',
        'integrationinstanceid': 'integrationinstanceid',
        'issharedagent': 'issharedagent',
        'name': 'name',
        'os': 'os',
        'password': 'password',
        'smb': 'smb',
        'smbport': 'smbport',
        'sshkey': 'sshkey',
        'sshport': 'sshport',
        'terminal_options': 'terminalOptions',
        'user': 'user',
        'workgroup': 'workgroup'
    }

    def __init__(self, agent=None, arch=None, ciphers=None, credentials=None, engine_id=None, host=None, integrationinstanceid=None, issharedagent=None, name=None, os=None, password=None, smb=None, smbport=None, sshkey=None, sshport=None, terminal_options=None, user=None, workgroup=None):  # noqa: E501
        """System - a model defined in Swagger"""  # noqa: E501

        self._agent = None
        self._arch = None
        self._ciphers = None
        self._credentials = None
        self._engine_id = None
        self._host = None
        self._integrationinstanceid = None
        self._issharedagent = None
        self._name = None
        self._os = None
        self._password = None
        self._smb = None
        self._smbport = None
        self._sshkey = None
        self._sshport = None
        self._terminal_options = None
        self._user = None
        self._workgroup = None
        self.discriminator = None

        if agent is not None:
            self.agent = agent
        if arch is not None:
            self.arch = arch
        if ciphers is not None:
            self.ciphers = ciphers
        if credentials is not None:
            self.credentials = credentials
        if engine_id is not None:
            self.engine_id = engine_id
        if host is not None:
            self.host = host
        if integrationinstanceid is not None:
            self.integrationinstanceid = integrationinstanceid
        if issharedagent is not None:
            self.issharedagent = issharedagent
        if name is not None:
            self.name = name
        if os is not None:
            self.os = os
        if password is not None:
            self.password = password
        if smb is not None:
            self.smb = smb
        if smbport is not None:
            self.smbport = smbport
        if sshkey is not None:
            self.sshkey = sshkey
        if sshport is not None:
            self.sshport = sshport
        if terminal_options is not None:
            self.terminal_options = terminal_options
        if user is not None:
            self.user = user
        if workgroup is not None:
            self.workgroup = workgroup

    @property
    def agent(self):
        """Gets the agent of this System.  # noqa: E501


        :return: The agent of this System.  # noqa: E501
        :rtype: SystemAgent
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this System.


        :param agent: The agent of this System.  # noqa: E501
        :type: SystemAgent
        """

        self._agent = agent

    @property
    def arch(self):
        """Gets the arch of this System.  # noqa: E501


        :return: The arch of this System.  # noqa: E501
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this System.


        :param arch: The arch of this System.  # noqa: E501
        :type: str
        """

        self._arch = arch

    @property
    def ciphers(self):
        """Gets the ciphers of this System.  # noqa: E501


        :return: The ciphers of this System.  # noqa: E501
        :rtype: list[str]
        """
        return self._ciphers

    @ciphers.setter
    def ciphers(self, ciphers):
        """Sets the ciphers of this System.


        :param ciphers: The ciphers of this System.  # noqa: E501
        :type: list[str]
        """

        self._ciphers = ciphers

    @property
    def credentials(self):
        """Gets the credentials of this System.  # noqa: E501


        :return: The credentials of this System.  # noqa: E501
        :rtype: str
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this System.


        :param credentials: The credentials of this System.  # noqa: E501
        :type: str
        """

        self._credentials = credentials

    @property
    def engine_id(self):
        """Gets the engine_id of this System.  # noqa: E501


        :return: The engine_id of this System.  # noqa: E501
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        """Sets the engine_id of this System.


        :param engine_id: The engine_id of this System.  # noqa: E501
        :type: str
        """

        self._engine_id = engine_id

    @property
    def host(self):
        """Gets the host of this System.  # noqa: E501


        :return: The host of this System.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this System.


        :param host: The host of this System.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def integrationinstanceid(self):
        """Gets the integrationinstanceid of this System.  # noqa: E501


        :return: The integrationinstanceid of this System.  # noqa: E501
        :rtype: str
        """
        return self._integrationinstanceid

    @integrationinstanceid.setter
    def integrationinstanceid(self, integrationinstanceid):
        """Sets the integrationinstanceid of this System.


        :param integrationinstanceid: The integrationinstanceid of this System.  # noqa: E501
        :type: str
        """

        self._integrationinstanceid = integrationinstanceid

    @property
    def issharedagent(self):
        """Gets the issharedagent of this System.  # noqa: E501


        :return: The issharedagent of this System.  # noqa: E501
        :rtype: bool
        """
        return self._issharedagent

    @issharedagent.setter
    def issharedagent(self, issharedagent):
        """Sets the issharedagent of this System.


        :param issharedagent: The issharedagent of this System.  # noqa: E501
        :type: bool
        """

        self._issharedagent = issharedagent

    @property
    def name(self):
        """Gets the name of this System.  # noqa: E501


        :return: The name of this System.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this System.


        :param name: The name of this System.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def os(self):
        """Gets the os of this System.  # noqa: E501


        :return: The os of this System.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this System.


        :param os: The os of this System.  # noqa: E501
        :type: str
        """

        self._os = os

    @property
    def password(self):
        """Gets the password of this System.  # noqa: E501


        :return: The password of this System.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this System.


        :param password: The password of this System.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def smb(self):
        """Gets the smb of this System.  # noqa: E501


        :return: The smb of this System.  # noqa: E501
        :rtype: int
        """
        return self._smb

    @smb.setter
    def smb(self, smb):
        """Sets the smb of this System.


        :param smb: The smb of this System.  # noqa: E501
        :type: int
        """

        self._smb = smb

    @property
    def smbport(self):
        """Gets the smbport of this System.  # noqa: E501


        :return: The smbport of this System.  # noqa: E501
        :rtype: int
        """
        return self._smbport

    @smbport.setter
    def smbport(self, smbport):
        """Sets the smbport of this System.


        :param smbport: The smbport of this System.  # noqa: E501
        :type: int
        """

        self._smbport = smbport

    @property
    def sshkey(self):
        """Gets the sshkey of this System.  # noqa: E501


        :return: The sshkey of this System.  # noqa: E501
        :rtype: str
        """
        return self._sshkey

    @sshkey.setter
    def sshkey(self, sshkey):
        """Sets the sshkey of this System.


        :param sshkey: The sshkey of this System.  # noqa: E501
        :type: str
        """

        self._sshkey = sshkey

    @property
    def sshport(self):
        """Gets the sshport of this System.  # noqa: E501


        :return: The sshport of this System.  # noqa: E501
        :rtype: int
        """
        return self._sshport

    @sshport.setter
    def sshport(self, sshport):
        """Sets the sshport of this System.


        :param sshport: The sshport of this System.  # noqa: E501
        :type: int
        """

        self._sshport = sshport

    @property
    def terminal_options(self):
        """Gets the terminal_options of this System.  # noqa: E501


        :return: The terminal_options of this System.  # noqa: E501
        :rtype: TerminalOptions
        """
        return self._terminal_options

    @terminal_options.setter
    def terminal_options(self, terminal_options):
        """Sets the terminal_options of this System.


        :param terminal_options: The terminal_options of this System.  # noqa: E501
        :type: TerminalOptions
        """

        self._terminal_options = terminal_options

    @property
    def user(self):
        """Gets the user of this System.  # noqa: E501


        :return: The user of this System.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this System.


        :param user: The user of this System.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def workgroup(self):
        """Gets the workgroup of this System.  # noqa: E501


        :return: The workgroup of this System.  # noqa: E501
        :rtype: str
        """
        return self._workgroup

    @workgroup.setter
    def workgroup(self, workgroup):
        """Sets the workgroup of this System.


        :param workgroup: The workgroup of this System.  # noqa: E501
        :type: str
        """

        self._workgroup = workgroup

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
        if issubclass(System, dict):
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
        if not isinstance(other, System):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
