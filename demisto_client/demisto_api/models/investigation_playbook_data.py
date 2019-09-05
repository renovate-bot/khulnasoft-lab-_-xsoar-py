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

from demisto_client.demisto_api.models.investigation_playbook_state import InvestigationPlaybookState  # noqa: F401,E501
from demisto_client.demisto_api.models.investigation_playbook_task import InvestigationPlaybookTask  # noqa: F401,E501
from demisto_client.demisto_api.models.playbook_inputs import PlaybookInputs  # noqa: F401,E501
from demisto_client.demisto_api.models.playbook_outputs import PlaybookOutputs  # noqa: F401,E501
from demisto_client.demisto_api.models.playbook_view import PlaybookView  # noqa: F401,E501


class InvestigationPlaybookData(object):
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
        'ready_playbook_inputs': 'dict(str, dict(str, object))',
        'auto_extracting': 'bool',
        'comment': 'str',
        'inputs': 'PlaybookInputs',
        'investigation_id': 'str',
        'name': 'str',
        'outputs': 'PlaybookOutputs',
        'playbook_id': 'str',
        'start_date': 'datetime',
        'start_task_id': 'str',
        'state': 'InvestigationPlaybookState',
        'sub_playbook_inputs': 'dict(str, PlaybookInputs)',
        'sub_playbook_outputs': 'dict(str, PlaybookOutputs)',
        'tasks': 'dict(str, InvestigationPlaybookTask)',
        'view': 'PlaybookView'
    }

    attribute_map = {
        'ready_playbook_inputs': 'ReadyPlaybookInputs',
        'auto_extracting': 'autoExtracting',
        'comment': 'comment',
        'inputs': 'inputs',
        'investigation_id': 'investigationId',
        'name': 'name',
        'outputs': 'outputs',
        'playbook_id': 'playbookId',
        'start_date': 'startDate',
        'start_task_id': 'startTaskId',
        'state': 'state',
        'sub_playbook_inputs': 'subPlaybookInputs',
        'sub_playbook_outputs': 'subPlaybookOutputs',
        'tasks': 'tasks',
        'view': 'view'
    }

    def __init__(self, ready_playbook_inputs=None, auto_extracting=None, comment=None, inputs=None, investigation_id=None, name=None, outputs=None, playbook_id=None, start_date=None, start_task_id=None, state=None, sub_playbook_inputs=None, sub_playbook_outputs=None, tasks=None, view=None):  # noqa: E501
        """InvestigationPlaybookData - a model defined in Swagger"""  # noqa: E501

        self._ready_playbook_inputs = None
        self._auto_extracting = None
        self._comment = None
        self._inputs = None
        self._investigation_id = None
        self._name = None
        self._outputs = None
        self._playbook_id = None
        self._start_date = None
        self._start_task_id = None
        self._state = None
        self._sub_playbook_inputs = None
        self._sub_playbook_outputs = None
        self._tasks = None
        self._view = None
        self.discriminator = None

        if ready_playbook_inputs is not None:
            self.ready_playbook_inputs = ready_playbook_inputs
        if auto_extracting is not None:
            self.auto_extracting = auto_extracting
        if comment is not None:
            self.comment = comment
        if inputs is not None:
            self.inputs = inputs
        if investigation_id is not None:
            self.investigation_id = investigation_id
        if name is not None:
            self.name = name
        if outputs is not None:
            self.outputs = outputs
        if playbook_id is not None:
            self.playbook_id = playbook_id
        if start_date is not None:
            self.start_date = start_date
        if start_task_id is not None:
            self.start_task_id = start_task_id
        if state is not None:
            self.state = state
        if sub_playbook_inputs is not None:
            self.sub_playbook_inputs = sub_playbook_inputs
        if sub_playbook_outputs is not None:
            self.sub_playbook_outputs = sub_playbook_outputs
        if tasks is not None:
            self.tasks = tasks
        if view is not None:
            self.view = view

    @property
    def ready_playbook_inputs(self):
        """Gets the ready_playbook_inputs of this InvestigationPlaybookData.  # noqa: E501


        :return: The ready_playbook_inputs of this InvestigationPlaybookData.  # noqa: E501
        :rtype: dict(str, dict(str, object))
        """
        return self._ready_playbook_inputs

    @ready_playbook_inputs.setter
    def ready_playbook_inputs(self, ready_playbook_inputs):
        """Sets the ready_playbook_inputs of this InvestigationPlaybookData.


        :param ready_playbook_inputs: The ready_playbook_inputs of this InvestigationPlaybookData.  # noqa: E501
        :type: dict(str, dict(str, object))
        """

        self._ready_playbook_inputs = ready_playbook_inputs

    @property
    def auto_extracting(self):
        """Gets the auto_extracting of this InvestigationPlaybookData.  # noqa: E501


        :return: The auto_extracting of this InvestigationPlaybookData.  # noqa: E501
        :rtype: bool
        """
        return self._auto_extracting

    @auto_extracting.setter
    def auto_extracting(self, auto_extracting):
        """Sets the auto_extracting of this InvestigationPlaybookData.


        :param auto_extracting: The auto_extracting of this InvestigationPlaybookData.  # noqa: E501
        :type: bool
        """

        self._auto_extracting = auto_extracting

    @property
    def comment(self):
        """Gets the comment of this InvestigationPlaybookData.  # noqa: E501


        :return: The comment of this InvestigationPlaybookData.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this InvestigationPlaybookData.


        :param comment: The comment of this InvestigationPlaybookData.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def inputs(self):
        """Gets the inputs of this InvestigationPlaybookData.  # noqa: E501


        :return: The inputs of this InvestigationPlaybookData.  # noqa: E501
        :rtype: PlaybookInputs
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this InvestigationPlaybookData.


        :param inputs: The inputs of this InvestigationPlaybookData.  # noqa: E501
        :type: PlaybookInputs
        """

        self._inputs = inputs

    @property
    def investigation_id(self):
        """Gets the investigation_id of this InvestigationPlaybookData.  # noqa: E501


        :return: The investigation_id of this InvestigationPlaybookData.  # noqa: E501
        :rtype: str
        """
        return self._investigation_id

    @investigation_id.setter
    def investigation_id(self, investigation_id):
        """Sets the investigation_id of this InvestigationPlaybookData.


        :param investigation_id: The investigation_id of this InvestigationPlaybookData.  # noqa: E501
        :type: str
        """

        self._investigation_id = investigation_id

    @property
    def name(self):
        """Gets the name of this InvestigationPlaybookData.  # noqa: E501


        :return: The name of this InvestigationPlaybookData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InvestigationPlaybookData.


        :param name: The name of this InvestigationPlaybookData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def outputs(self):
        """Gets the outputs of this InvestigationPlaybookData.  # noqa: E501


        :return: The outputs of this InvestigationPlaybookData.  # noqa: E501
        :rtype: PlaybookOutputs
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this InvestigationPlaybookData.


        :param outputs: The outputs of this InvestigationPlaybookData.  # noqa: E501
        :type: PlaybookOutputs
        """

        self._outputs = outputs

    @property
    def playbook_id(self):
        """Gets the playbook_id of this InvestigationPlaybookData.  # noqa: E501


        :return: The playbook_id of this InvestigationPlaybookData.  # noqa: E501
        :rtype: str
        """
        return self._playbook_id

    @playbook_id.setter
    def playbook_id(self, playbook_id):
        """Sets the playbook_id of this InvestigationPlaybookData.


        :param playbook_id: The playbook_id of this InvestigationPlaybookData.  # noqa: E501
        :type: str
        """

        self._playbook_id = playbook_id

    @property
    def start_date(self):
        """Gets the start_date of this InvestigationPlaybookData.  # noqa: E501


        :return: The start_date of this InvestigationPlaybookData.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this InvestigationPlaybookData.


        :param start_date: The start_date of this InvestigationPlaybookData.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def start_task_id(self):
        """Gets the start_task_id of this InvestigationPlaybookData.  # noqa: E501

        FirstTask is the root task of the playbook  # noqa: E501

        :return: The start_task_id of this InvestigationPlaybookData.  # noqa: E501
        :rtype: str
        """
        return self._start_task_id

    @start_task_id.setter
    def start_task_id(self, start_task_id):
        """Sets the start_task_id of this InvestigationPlaybookData.

        FirstTask is the root task of the playbook  # noqa: E501

        :param start_task_id: The start_task_id of this InvestigationPlaybookData.  # noqa: E501
        :type: str
        """

        self._start_task_id = start_task_id

    @property
    def state(self):
        """Gets the state of this InvestigationPlaybookData.  # noqa: E501


        :return: The state of this InvestigationPlaybookData.  # noqa: E501
        :rtype: InvestigationPlaybookState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InvestigationPlaybookData.


        :param state: The state of this InvestigationPlaybookData.  # noqa: E501
        :type: InvestigationPlaybookState
        """

        self._state = state

    @property
    def sub_playbook_inputs(self):
        """Gets the sub_playbook_inputs of this InvestigationPlaybookData.  # noqa: E501


        :return: The sub_playbook_inputs of this InvestigationPlaybookData.  # noqa: E501
        :rtype: dict(str, PlaybookInputs)
        """
        return self._sub_playbook_inputs

    @sub_playbook_inputs.setter
    def sub_playbook_inputs(self, sub_playbook_inputs):
        """Sets the sub_playbook_inputs of this InvestigationPlaybookData.


        :param sub_playbook_inputs: The sub_playbook_inputs of this InvestigationPlaybookData.  # noqa: E501
        :type: dict(str, PlaybookInputs)
        """

        self._sub_playbook_inputs = sub_playbook_inputs

    @property
    def sub_playbook_outputs(self):
        """Gets the sub_playbook_outputs of this InvestigationPlaybookData.  # noqa: E501


        :return: The sub_playbook_outputs of this InvestigationPlaybookData.  # noqa: E501
        :rtype: dict(str, PlaybookOutputs)
        """
        return self._sub_playbook_outputs

    @sub_playbook_outputs.setter
    def sub_playbook_outputs(self, sub_playbook_outputs):
        """Sets the sub_playbook_outputs of this InvestigationPlaybookData.


        :param sub_playbook_outputs: The sub_playbook_outputs of this InvestigationPlaybookData.  # noqa: E501
        :type: dict(str, PlaybookOutputs)
        """

        self._sub_playbook_outputs = sub_playbook_outputs

    @property
    def tasks(self):
        """Gets the tasks of this InvestigationPlaybookData.  # noqa: E501


        :return: The tasks of this InvestigationPlaybookData.  # noqa: E501
        :rtype: dict(str, InvestigationPlaybookTask)
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this InvestigationPlaybookData.


        :param tasks: The tasks of this InvestigationPlaybookData.  # noqa: E501
        :type: dict(str, InvestigationPlaybookTask)
        """

        self._tasks = tasks

    @property
    def view(self):
        """Gets the view of this InvestigationPlaybookData.  # noqa: E501


        :return: The view of this InvestigationPlaybookData.  # noqa: E501
        :rtype: PlaybookView
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this InvestigationPlaybookData.


        :param view: The view of this InvestigationPlaybookData.  # noqa: E501
        :type: PlaybookView
        """

        self._view = view

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
        if issubclass(InvestigationPlaybookData, dict):
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
        if not isinstance(other, InvestigationPlaybookData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
