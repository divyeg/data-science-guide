import loguru as logger


class CombinationAlgos(object):
    def __init__(self):
        pass

    def generate_string_combinations(self, input_string):
        """
        This function is used to generate combination of upper case and lower case strings

        """

        def helper(input_string, partial_solution, index):
            if index == len(input_string):
                logger.debug(partial_solution)
                return

            if input_string[index].isdigit():
                helper(input_string, partial_solution + input_string[index], index + 1)
            else:
                helper(
                    input_string,
                    partial_solution + input_string[index].lower(),
                    index + 1,
                )
                helper(
                    input_string,
                    partial_solution + input_string[index].upper(),
                    index + 1,
                )

        helper(input_string, "", 0)

    def generate_list_combinations(self):
        """
        This function is used to generated combination of elements in an array

        """
        pass
