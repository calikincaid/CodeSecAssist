import sys
sys.path.append("../src")
from main import *
import unittest


class TestPromptCrafter(unittest.TestCase):
    
    def test_get_template(self): # test ensures that the loaded prompt is formatted as a python dictionary and its values are accessible
        crafter = PromptCrafter("test")
        crafter.template = "prompt_test.json"
        crafter.get_prompt_template()
    
        self.assertIsInstance(crafter.prompt, dict)
        self.assertIn("role", crafter.prompt)
        self.assertEqual(crafter.prompt["role"], "You are an expert application security analyst specializing in static code analysis and secure coding practices.")

    def test_get_template_file_not_found(self): # test ensures that when the JSON file doesnt exist that the prompt field is empty
        crafter = PromptCrafter("test")
        crafter.template = "missing.json"
        crafter.get_prompt_template()

        self.assertIsNone(crafter.prompt)

    def test_read_user_source_code(self): # test ensures that when the source code file doesnt exist that the source_code field is empty
        crafter = PromptCrafter("test")
        crafter.template = "prompt_test.json"
        crafter.read_user_source_code()

        self.assertIsNone(crafter.source_code)
 

if __name__ == '__main__':
    unittest.main()