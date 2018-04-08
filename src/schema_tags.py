"""Collection of schema related tags."""


class Tags:
    """List of tags available."""
    BINARY_NAME_TAG = 'binary_name'
    BUILD_TYPE_TAG = 'build_type'
    EXERCISES_TAG = 'exercises'
    FOLDER_TAG = 'folder'
    HOMEWORKS_TAG = 'homeworks'
    INPUT_TAG = 'input_args'
    LANGUAGE_TAG = 'language'
    NAME_TAG = 'name'
    OUTPUT_TAG = 'expected_output'
    OUTPUT_TYPE_TAG = 'output_type'
    TESTS_TAG = 'tests'


class OutputTags:
    """Define tags for output types."""
    STRING = 'string'
    NUMBER = 'number'
    ALL = [STRING, NUMBER]


class BuildTags:
    """Define tags for build types."""
    CMAKE = 'cmake'
    SIMPLE = 'simple'
    ALL = [CMAKE, SIMPLE]


class LangTags:
    """Define tags for build types."""
    CPP = 'cpp'
    ALL = [CPP]


class OneOf:
    """Check that an item is one of the list."""

    def __init__(self, some_list):
        """Set the list to choose from."""
        self.__items = some_list

    def __call__(self, item):
        """Check that the list contains what is needed."""
        return item in self.__items

    def __str__(self):
        """Override str for this class."""
        return "Possible values: {}".format(self.__items)