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

from demisto_client.demisto_api.models.ending_type import EndingType  # noqa: F401,E501
from demisto_client.demisto_api.models.entry_category import EntryCategory  # noqa: F401,E501
from demisto_client.demisto_api.models.entry_history import EntryHistory  # noqa: F401,E501
from demisto_client.demisto_api.models.entry_reputation import EntryReputation  # noqa: F401,E501
from demisto_client.demisto_api.models.entry_task import EntryTask  # noqa: F401,E501
from demisto_client.demisto_api.models.entry_type import EntryType  # noqa: F401,E501
from demisto_client.demisto_api.models.file_metadata import FileMetadata  # noqa: F401,E501
from demisto_client.demisto_api.models.human_cron import HumanCron  # noqa: F401,E501


class Entry(object):
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
        'shard_id': 'int',
        'brand': 'str',
        'category': 'EntryCategory',
        'contents': 'object',
        'contents_size': 'int',
        'created': 'datetime',
        'cron': 'str',
        'cron_view': 'bool',
        'deleted': 'bool',
        'ending_date': 'datetime',
        'ending_type': 'EndingType',
        'entry_task': 'EntryTask',
        'error_source': 'str',
        'file': 'str',
        'file_id': 'str',
        'file_metadata': 'FileMetadata',
        'format': 'str',
        'has_role': 'bool',
        'history': 'list[EntryHistory]',
        'human_cron': 'HumanCron',
        'id': 'str',
        'instance': 'str',
        'investigation_id': 'str',
        'modified': 'datetime',
        'note': 'bool',
        'parent_content': 'object',
        'parent_entry_truncated': 'bool',
        'parent_id': 'str',
        'pinned': 'bool',
        'playbook_id': 'str',
        'previous_roles': 'list[str]',
        'read_only': 'bool',
        'recurrent': 'bool',
        'reputation_size': 'int',
        'reputations': 'list[EntryReputation]',
        'roles': 'list[str]',
        'scheduled': 'bool',
        'sort_values': 'list[str]',
        'start_date': 'datetime',
        'system': 'str',
        'tags': 'list[str]',
        'tags_raw': 'list[str]',
        'task_id': 'str',
        'times': 'int',
        'timezone_offset': 'int',
        'type': 'EntryType',
        'user': 'str',
        'version': 'int'
    }

    attribute_map = {
        'shard_id': 'ShardID',
        'brand': 'brand',
        'category': 'category',
        'contents': 'contents',
        'contents_size': 'contentsSize',
        'created': 'created',
        'cron': 'cron',
        'cron_view': 'cronView',
        'deleted': 'deleted',
        'ending_date': 'endingDate',
        'ending_type': 'endingType',
        'entry_task': 'entryTask',
        'error_source': 'errorSource',
        'file': 'file',
        'file_id': 'fileID',
        'file_metadata': 'fileMetadata',
        'format': 'format',
        'has_role': 'hasRole',
        'history': 'history',
        'human_cron': 'humanCron',
        'id': 'id',
        'instance': 'instance',
        'investigation_id': 'investigationId',
        'modified': 'modified',
        'note': 'note',
        'parent_content': 'parentContent',
        'parent_entry_truncated': 'parentEntryTruncated',
        'parent_id': 'parentId',
        'pinned': 'pinned',
        'playbook_id': 'playbookId',
        'previous_roles': 'previousRoles',
        'read_only': 'readOnly',
        'recurrent': 'recurrent',
        'reputation_size': 'reputationSize',
        'reputations': 'reputations',
        'roles': 'roles',
        'scheduled': 'scheduled',
        'sort_values': 'sortValues',
        'start_date': 'startDate',
        'system': 'system',
        'tags': 'tags',
        'tags_raw': 'tagsRaw',
        'task_id': 'taskId',
        'times': 'times',
        'timezone_offset': 'timezoneOffset',
        'type': 'type',
        'user': 'user',
        'version': 'version'
    }

    def __init__(self, shard_id=None, brand=None, category=None, contents=None, contents_size=None, created=None, cron=None, cron_view=None, deleted=None, ending_date=None, ending_type=None, entry_task=None, error_source=None, file=None, file_id=None, file_metadata=None, format=None, has_role=None, history=None, human_cron=None, id=None, instance=None, investigation_id=None, modified=None, note=None, parent_content=None, parent_entry_truncated=None, parent_id=None, pinned=None, playbook_id=None, previous_roles=None, read_only=None, recurrent=None, reputation_size=None, reputations=None, roles=None, scheduled=None, sort_values=None, start_date=None, system=None, tags=None, tags_raw=None, task_id=None, times=None, timezone_offset=None, type=None, user=None, version=None):  # noqa: E501
        """Entry - a model defined in Swagger"""  # noqa: E501

        self._shard_id = None
        self._brand = None
        self._category = None
        self._contents = None
        self._contents_size = None
        self._created = None
        self._cron = None
        self._cron_view = None
        self._deleted = None
        self._ending_date = None
        self._ending_type = None
        self._entry_task = None
        self._error_source = None
        self._file = None
        self._file_id = None
        self._file_metadata = None
        self._format = None
        self._has_role = None
        self._history = None
        self._human_cron = None
        self._id = None
        self._instance = None
        self._investigation_id = None
        self._modified = None
        self._note = None
        self._parent_content = None
        self._parent_entry_truncated = None
        self._parent_id = None
        self._pinned = None
        self._playbook_id = None
        self._previous_roles = None
        self._read_only = None
        self._recurrent = None
        self._reputation_size = None
        self._reputations = None
        self._roles = None
        self._scheduled = None
        self._sort_values = None
        self._start_date = None
        self._system = None
        self._tags = None
        self._tags_raw = None
        self._task_id = None
        self._times = None
        self._timezone_offset = None
        self._type = None
        self._user = None
        self._version = None
        self.discriminator = None

        if shard_id is not None:
            self.shard_id = shard_id
        if brand is not None:
            self.brand = brand
        if category is not None:
            self.category = category
        if contents is not None:
            self.contents = contents
        if contents_size is not None:
            self.contents_size = contents_size
        if created is not None:
            self.created = created
        if cron is not None:
            self.cron = cron
        if cron_view is not None:
            self.cron_view = cron_view
        if deleted is not None:
            self.deleted = deleted
        if ending_date is not None:
            self.ending_date = ending_date
        if ending_type is not None:
            self.ending_type = ending_type
        if entry_task is not None:
            self.entry_task = entry_task
        if error_source is not None:
            self.error_source = error_source
        if file is not None:
            self.file = file
        if file_id is not None:
            self.file_id = file_id
        if file_metadata is not None:
            self.file_metadata = file_metadata
        if format is not None:
            self.format = format
        if has_role is not None:
            self.has_role = has_role
        if history is not None:
            self.history = history
        if human_cron is not None:
            self.human_cron = human_cron
        if id is not None:
            self.id = id
        if instance is not None:
            self.instance = instance
        if investigation_id is not None:
            self.investigation_id = investigation_id
        if modified is not None:
            self.modified = modified
        if note is not None:
            self.note = note
        if parent_content is not None:
            self.parent_content = parent_content
        if parent_entry_truncated is not None:
            self.parent_entry_truncated = parent_entry_truncated
        if parent_id is not None:
            self.parent_id = parent_id
        if pinned is not None:
            self.pinned = pinned
        if playbook_id is not None:
            self.playbook_id = playbook_id
        if previous_roles is not None:
            self.previous_roles = previous_roles
        if read_only is not None:
            self.read_only = read_only
        if recurrent is not None:
            self.recurrent = recurrent
        if reputation_size is not None:
            self.reputation_size = reputation_size
        if reputations is not None:
            self.reputations = reputations
        if roles is not None:
            self.roles = roles
        if scheduled is not None:
            self.scheduled = scheduled
        if sort_values is not None:
            self.sort_values = sort_values
        if start_date is not None:
            self.start_date = start_date
        if system is not None:
            self.system = system
        if tags is not None:
            self.tags = tags
        if tags_raw is not None:
            self.tags_raw = tags_raw
        if task_id is not None:
            self.task_id = task_id
        if times is not None:
            self.times = times
        if timezone_offset is not None:
            self.timezone_offset = timezone_offset
        if type is not None:
            self.type = type
        if user is not None:
            self.user = user
        if version is not None:
            self.version = version

    @property
    def shard_id(self):
        """Gets the shard_id of this Entry.  # noqa: E501


        :return: The shard_id of this Entry.  # noqa: E501
        :rtype: int
        """
        return self._shard_id

    @shard_id.setter
    def shard_id(self, shard_id):
        """Sets the shard_id of this Entry.


        :param shard_id: The shard_id of this Entry.  # noqa: E501
        :type: int
        """

        self._shard_id = shard_id

    @property
    def brand(self):
        """Gets the brand of this Entry.  # noqa: E501


        :return: The brand of this Entry.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this Entry.


        :param brand: The brand of this Entry.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def category(self):
        """Gets the category of this Entry.  # noqa: E501


        :return: The category of this Entry.  # noqa: E501
        :rtype: EntryCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Entry.


        :param category: The category of this Entry.  # noqa: E501
        :type: EntryCategory
        """

        self._category = category

    @property
    def contents(self):
        """Gets the contents of this Entry.  # noqa: E501

        The contents of the entry that is actually indexed - should not be used  # noqa: E501

        :return: The contents of this Entry.  # noqa: E501
        :rtype: object
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this Entry.

        The contents of the entry that is actually indexed - should not be used  # noqa: E501

        :param contents: The contents of this Entry.  # noqa: E501
        :type: object
        """

        self._contents = contents

    @property
    def contents_size(self):
        """Gets the contents_size of this Entry.  # noqa: E501

        ContentsSize the total size of the contents  # noqa: E501

        :return: The contents_size of this Entry.  # noqa: E501
        :rtype: int
        """
        return self._contents_size

    @contents_size.setter
    def contents_size(self, contents_size):
        """Sets the contents_size of this Entry.

        ContentsSize the total size of the contents  # noqa: E501

        :param contents_size: The contents_size of this Entry.  # noqa: E501
        :type: int
        """

        self._contents_size = contents_size

    @property
    def created(self):
        """Gets the created of this Entry.  # noqa: E501

        When it was taken  # noqa: E501

        :return: The created of this Entry.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Entry.

        When it was taken  # noqa: E501

        :param created: The created of this Entry.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def cron(self):
        """Gets the cron of this Entry.  # noqa: E501


        :return: The cron of this Entry.  # noqa: E501
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        """Sets the cron of this Entry.


        :param cron: The cron of this Entry.  # noqa: E501
        :type: str
        """

        self._cron = cron

    @property
    def cron_view(self):
        """Gets the cron_view of this Entry.  # noqa: E501


        :return: The cron_view of this Entry.  # noqa: E501
        :rtype: bool
        """
        return self._cron_view

    @cron_view.setter
    def cron_view(self, cron_view):
        """Sets the cron_view of this Entry.


        :param cron_view: The cron_view of this Entry.  # noqa: E501
        :type: bool
        """

        self._cron_view = cron_view

    @property
    def deleted(self):
        """Gets the deleted of this Entry.  # noqa: E501


        :return: The deleted of this Entry.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Entry.


        :param deleted: The deleted of this Entry.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def ending_date(self):
        """Gets the ending_date of this Entry.  # noqa: E501


        :return: The ending_date of this Entry.  # noqa: E501
        :rtype: datetime
        """
        return self._ending_date

    @ending_date.setter
    def ending_date(self, ending_date):
        """Sets the ending_date of this Entry.


        :param ending_date: The ending_date of this Entry.  # noqa: E501
        :type: datetime
        """

        self._ending_date = ending_date

    @property
    def ending_type(self):
        """Gets the ending_type of this Entry.  # noqa: E501


        :return: The ending_type of this Entry.  # noqa: E501
        :rtype: EndingType
        """
        return self._ending_type

    @ending_type.setter
    def ending_type(self, ending_type):
        """Sets the ending_type of this Entry.


        :param ending_type: The ending_type of this Entry.  # noqa: E501
        :type: EndingType
        """

        self._ending_type = ending_type

    @property
    def entry_task(self):
        """Gets the entry_task of this Entry.  # noqa: E501


        :return: The entry_task of this Entry.  # noqa: E501
        :rtype: EntryTask
        """
        return self._entry_task

    @entry_task.setter
    def entry_task(self, entry_task):
        """Sets the entry_task of this Entry.


        :param entry_task: The entry_task of this Entry.  # noqa: E501
        :type: EntryTask
        """

        self._entry_task = entry_task

    @property
    def error_source(self):
        """Gets the error_source of this Entry.  # noqa: E501

        Source of the error  # noqa: E501

        :return: The error_source of this Entry.  # noqa: E501
        :rtype: str
        """
        return self._error_source

    @error_source.setter
    def error_source(self, error_source):
        """Sets the error_source of this Entry.

        Source of the error  # noqa: E501

        :param error_source: The error_source of this Entry.  # noqa: E501
        :type: str
        """

        self._error_source = error_source

    @property
    def file(self):
        """Gets the file of this Entry.  # noqa: E501

        Filename of associated content  # noqa: E501

        :return: The file of this Entry.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this Entry.

        Filename of associated content  # noqa: E501

        :param file: The file of this Entry.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def file_id(self):
        """Gets the file_id of this Entry.  # noqa: E501

        FileID is the file name when saved in the server  # noqa: E501

        :return: The file_id of this Entry.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this Entry.

        FileID is the file name when saved in the server  # noqa: E501

        :param file_id: The file_id of this Entry.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def file_metadata(self):
        """Gets the file_metadata of this Entry.  # noqa: E501


        :return: The file_metadata of this Entry.  # noqa: E501
        :rtype: FileMetadata
        """
        return self._file_metadata

    @file_metadata.setter
    def file_metadata(self, file_metadata):
        """Sets the file_metadata of this Entry.


        :param file_metadata: The file_metadata of this Entry.  # noqa: E501
        :type: FileMetadata
        """

        self._file_metadata = file_metadata

    @property
    def format(self):
        """Gets the format of this Entry.  # noqa: E501

        Holds information on how content is formatted  # noqa: E501

        :return: The format of this Entry.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Entry.

        Holds information on how content is formatted  # noqa: E501

        :param format: The format of this Entry.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def has_role(self):
        """Gets the has_role of this Entry.  # noqa: E501

        Internal field to make queries on role faster  # noqa: E501

        :return: The has_role of this Entry.  # noqa: E501
        :rtype: bool
        """
        return self._has_role

    @has_role.setter
    def has_role(self, has_role):
        """Sets the has_role of this Entry.

        Internal field to make queries on role faster  # noqa: E501

        :param has_role: The has_role of this Entry.  # noqa: E501
        :type: bool
        """

        self._has_role = has_role

    @property
    def history(self):
        """Gets the history of this Entry.  # noqa: E501

        Edit history  # noqa: E501

        :return: The history of this Entry.  # noqa: E501
        :rtype: list[EntryHistory]
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this Entry.

        Edit history  # noqa: E501

        :param history: The history of this Entry.  # noqa: E501
        :type: list[EntryHistory]
        """

        self._history = history

    @property
    def human_cron(self):
        """Gets the human_cron of this Entry.  # noqa: E501


        :return: The human_cron of this Entry.  # noqa: E501
        :rtype: HumanCron
        """
        return self._human_cron

    @human_cron.setter
    def human_cron(self, human_cron):
        """Sets the human_cron of this Entry.


        :param human_cron: The human_cron of this Entry.  # noqa: E501
        :type: HumanCron
        """

        self._human_cron = human_cron

    @property
    def id(self):
        """Gets the id of this Entry.  # noqa: E501


        :return: The id of this Entry.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Entry.


        :param id: The id of this Entry.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def instance(self):
        """Gets the instance of this Entry.  # noqa: E501


        :return: The instance of this Entry.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this Entry.


        :param instance: The instance of this Entry.  # noqa: E501
        :type: str
        """

        self._instance = instance

    @property
    def investigation_id(self):
        """Gets the investigation_id of this Entry.  # noqa: E501

        The id of the investigation it belongs to  # noqa: E501

        :return: The investigation_id of this Entry.  # noqa: E501
        :rtype: str
        """
        return self._investigation_id

    @investigation_id.setter
    def investigation_id(self, investigation_id):
        """Sets the investigation_id of this Entry.

        The id of the investigation it belongs to  # noqa: E501

        :param investigation_id: The investigation_id of this Entry.  # noqa: E501
        :type: str
        """

        self._investigation_id = investigation_id

    @property
    def modified(self):
        """Gets the modified of this Entry.  # noqa: E501


        :return: The modified of this Entry.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Entry.


        :param modified: The modified of this Entry.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def note(self):
        """Gets the note of this Entry.  # noqa: E501

        Note  # noqa: E501

        :return: The note of this Entry.  # noqa: E501
        :rtype: bool
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this Entry.

        Note  # noqa: E501

        :param note: The note of this Entry.  # noqa: E501
        :type: bool
        """

        self._note = note

    @property
    def parent_content(self):
        """Gets the parent_content of this Entry.  # noqa: E501

        ParentEntry content - for reference  # noqa: E501

        :return: The parent_content of this Entry.  # noqa: E501
        :rtype: object
        """
        return self._parent_content

    @parent_content.setter
    def parent_content(self, parent_content):
        """Sets the parent_content of this Entry.

        ParentEntry content - for reference  # noqa: E501

        :param parent_content: The parent_content of this Entry.  # noqa: E501
        :type: object
        """

        self._parent_content = parent_content

    @property
    def parent_entry_truncated(self):
        """Gets the parent_entry_truncated of this Entry.  # noqa: E501

        ParentEntryTruncated - indicates weather entry content was truncated  # noqa: E501

        :return: The parent_entry_truncated of this Entry.  # noqa: E501
        :rtype: bool
        """
        return self._parent_entry_truncated

    @parent_entry_truncated.setter
    def parent_entry_truncated(self, parent_entry_truncated):
        """Sets the parent_entry_truncated of this Entry.

        ParentEntryTruncated - indicates weather entry content was truncated  # noqa: E501

        :param parent_entry_truncated: The parent_entry_truncated of this Entry.  # noqa: E501
        :type: bool
        """

        self._parent_entry_truncated = parent_entry_truncated

    @property
    def parent_id(self):
        """Gets the parent_id of this Entry.  # noqa: E501

        ParentId is the ID of the parent entry  # noqa: E501

        :return: The parent_id of this Entry.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this Entry.

        ParentId is the ID of the parent entry  # noqa: E501

        :param parent_id: The parent_id of this Entry.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def pinned(self):
        """Gets the pinned of this Entry.  # noqa: E501

        Mark entry as pinned = evidence  # noqa: E501

        :return: The pinned of this Entry.  # noqa: E501
        :rtype: bool
        """
        return self._pinned

    @pinned.setter
    def pinned(self, pinned):
        """Sets the pinned of this Entry.

        Mark entry as pinned = evidence  # noqa: E501

        :param pinned: The pinned of this Entry.  # noqa: E501
        :type: bool
        """

        self._pinned = pinned

    @property
    def playbook_id(self):
        """Gets the playbook_id of this Entry.  # noqa: E501

        PlaybookID - if the entry is assigned as note to a playbook task, it will hold the playbook  # noqa: E501

        :return: The playbook_id of this Entry.  # noqa: E501
        :rtype: str
        """
        return self._playbook_id

    @playbook_id.setter
    def playbook_id(self, playbook_id):
        """Sets the playbook_id of this Entry.

        PlaybookID - if the entry is assigned as note to a playbook task, it will hold the playbook  # noqa: E501

        :param playbook_id: The playbook_id of this Entry.  # noqa: E501
        :type: str
        """

        self._playbook_id = playbook_id

    @property
    def previous_roles(self):
        """Gets the previous_roles of this Entry.  # noqa: E501

        PreviousRoleName - do not change this field manually  # noqa: E501

        :return: The previous_roles of this Entry.  # noqa: E501
        :rtype: list[str]
        """
        return self._previous_roles

    @previous_roles.setter
    def previous_roles(self, previous_roles):
        """Sets the previous_roles of this Entry.

        PreviousRoleName - do not change this field manually  # noqa: E501

        :param previous_roles: The previous_roles of this Entry.  # noqa: E501
        :type: list[str]
        """

        self._previous_roles = previous_roles

    @property
    def read_only(self):
        """Gets the read_only of this Entry.  # noqa: E501

        ReadOnly  # noqa: E501

        :return: The read_only of this Entry.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this Entry.

        ReadOnly  # noqa: E501

        :param read_only: The read_only of this Entry.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def recurrent(self):
        """Gets the recurrent of this Entry.  # noqa: E501


        :return: The recurrent of this Entry.  # noqa: E501
        :rtype: bool
        """
        return self._recurrent

    @recurrent.setter
    def recurrent(self, recurrent):
        """Sets the recurrent of this Entry.


        :param recurrent: The recurrent of this Entry.  # noqa: E501
        :type: bool
        """

        self._recurrent = recurrent

    @property
    def reputation_size(self):
        """Gets the reputation_size of this Entry.  # noqa: E501

        ReputationSize the total size of the reputation  # noqa: E501

        :return: The reputation_size of this Entry.  # noqa: E501
        :rtype: int
        """
        return self._reputation_size

    @reputation_size.setter
    def reputation_size(self, reputation_size):
        """Sets the reputation_size of this Entry.

        ReputationSize the total size of the reputation  # noqa: E501

        :param reputation_size: The reputation_size of this Entry.  # noqa: E501
        :type: int
        """

        self._reputation_size = reputation_size

    @property
    def reputations(self):
        """Gets the reputations of this Entry.  # noqa: E501

        EntryReputations the reputations calculated by regex match  # noqa: E501

        :return: The reputations of this Entry.  # noqa: E501
        :rtype: list[EntryReputation]
        """
        return self._reputations

    @reputations.setter
    def reputations(self, reputations):
        """Sets the reputations of this Entry.

        EntryReputations the reputations calculated by regex match  # noqa: E501

        :param reputations: The reputations of this Entry.  # noqa: E501
        :type: list[EntryReputation]
        """

        self._reputations = reputations

    @property
    def roles(self):
        """Gets the roles of this Entry.  # noqa: E501

        The role assigned to this investigation  # noqa: E501

        :return: The roles of this Entry.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this Entry.

        The role assigned to this investigation  # noqa: E501

        :param roles: The roles of this Entry.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def scheduled(self):
        """Gets the scheduled of this Entry.  # noqa: E501

        is it scheduled  # noqa: E501

        :return: The scheduled of this Entry.  # noqa: E501
        :rtype: bool
        """
        return self._scheduled

    @scheduled.setter
    def scheduled(self, scheduled):
        """Sets the scheduled of this Entry.

        is it scheduled  # noqa: E501

        :param scheduled: The scheduled of this Entry.  # noqa: E501
        :type: bool
        """

        self._scheduled = scheduled

    @property
    def sort_values(self):
        """Gets the sort_values of this Entry.  # noqa: E501


        :return: The sort_values of this Entry.  # noqa: E501
        :rtype: list[str]
        """
        return self._sort_values

    @sort_values.setter
    def sort_values(self, sort_values):
        """Sets the sort_values of this Entry.


        :param sort_values: The sort_values of this Entry.  # noqa: E501
        :type: list[str]
        """

        self._sort_values = sort_values

    @property
    def start_date(self):
        """Gets the start_date of this Entry.  # noqa: E501


        :return: The start_date of this Entry.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Entry.


        :param start_date: The start_date of this Entry.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def system(self):
        """Gets the system of this Entry.  # noqa: E501

        The name of the system associated with this entry  # noqa: E501

        :return: The system of this Entry.  # noqa: E501
        :rtype: str
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this Entry.

        The name of the system associated with this entry  # noqa: E501

        :param system: The system of this Entry.  # noqa: E501
        :type: str
        """

        self._system = system

    @property
    def tags(self):
        """Gets the tags of this Entry.  # noqa: E501

        Tags  # noqa: E501

        :return: The tags of this Entry.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Entry.

        Tags  # noqa: E501

        :param tags: The tags of this Entry.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def tags_raw(self):
        """Gets the tags_raw of this Entry.  # noqa: E501

        TagsRaw  # noqa: E501

        :return: The tags_raw of this Entry.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags_raw

    @tags_raw.setter
    def tags_raw(self, tags_raw):
        """Sets the tags_raw of this Entry.

        TagsRaw  # noqa: E501

        :param tags_raw: The tags_raw of this Entry.  # noqa: E501
        :type: list[str]
        """

        self._tags_raw = tags_raw

    @property
    def task_id(self):
        """Gets the task_id of this Entry.  # noqa: E501

        TaskID - used if the entry is assigned as note to a playbook task  # noqa: E501

        :return: The task_id of this Entry.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this Entry.

        TaskID - used if the entry is assigned as note to a playbook task  # noqa: E501

        :param task_id: The task_id of this Entry.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def times(self):
        """Gets the times of this Entry.  # noqa: E501


        :return: The times of this Entry.  # noqa: E501
        :rtype: int
        """
        return self._times

    @times.setter
    def times(self, times):
        """Sets the times of this Entry.


        :param times: The times of this Entry.  # noqa: E501
        :type: int
        """

        self._times = times

    @property
    def timezone_offset(self):
        """Gets the timezone_offset of this Entry.  # noqa: E501


        :return: The timezone_offset of this Entry.  # noqa: E501
        :rtype: int
        """
        return self._timezone_offset

    @timezone_offset.setter
    def timezone_offset(self, timezone_offset):
        """Sets the timezone_offset of this Entry.


        :param timezone_offset: The timezone_offset of this Entry.  # noqa: E501
        :type: int
        """

        self._timezone_offset = timezone_offset

    @property
    def type(self):
        """Gets the type of this Entry.  # noqa: E501


        :return: The type of this Entry.  # noqa: E501
        :rtype: EntryType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Entry.


        :param type: The type of this Entry.  # noqa: E501
        :type: EntryType
        """

        self._type = type

    @property
    def user(self):
        """Gets the user of this Entry.  # noqa: E501

        The user who created  the entry  # noqa: E501

        :return: The user of this Entry.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Entry.

        The user who created  the entry  # noqa: E501

        :param user: The user of this Entry.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def version(self):
        """Gets the version of this Entry.  # noqa: E501


        :return: The version of this Entry.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Entry.


        :param version: The version of this Entry.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(Entry, dict):
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
        if not isinstance(other, Entry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other