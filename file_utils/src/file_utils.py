import tkinter.filedialog
import tkinter
import os

class FileHandler: 
    def __init__(self): 
        self.file_path = None
        self.file_extension = None

    def select_file(self, filetypes = None): 
        """Allows the user to select a file using a tkinter file dialog popup

        Args:
            filetypes (list, optional): A list of tuples indicating which filetypes the user can select from. Defaults to None which allows
            all file types

        Raises:
            ValueError: If filetypes is not None and not a list
            ValueError: If the element in the filetypes list is not a tuple or not the appropriate length
            ValueError: If the item inside of the tuple are not strings
            ValueError: If the file extension in the tuple does not start with a wildcard *
        """
        try: 
            # Validate the filetypes input if it's provided
            if filetypes is not None:
                if not isinstance(filetypes, list):
                    raise ValueError("filetypes must be a list.")
                
                for element in filetypes:
                    if not isinstance(element, tuple) or len(element) != 2:
                        raise ValueError(f"Each filetype entry must be a tuple of the form (description, extension), but got {element}.")
                    
                    description, extension = element
                    
                    if not isinstance(description, str) or not isinstance(extension, str):
                        raise ValueError(f"Both the description and extension must be strings, but got {element}.")
                    
                    if not extension.startswith("*"):
                        raise ValueError(f"File extension must start with '*', but got {extension} in {element}.")

            # If no filetypes are passed in, allow all
            if filetypes is None:
                filetypes = [("All files", "*.*")]

            self.file_path = tkinter.filedialog.askopenfilename(filetypes=filetypes)

            if self.file_path: 
                self.file_extension = os.path.splitext(self.file_path)[1]

        except ValueError as e: 
            print(f"Invalid filetypes input: {e}")
        except Exception as e: 
            print(f"{e}")

    def get_file_path(self): 
        """Gets the object's related file path

        Returns:
            str: A string representing the file path
        """
        if self.file_path: 
            return self.file_path
        else: 
            return None
    
    def get_file_extension(self): 
        """Gets the object's related file extension with a period

        Returns:
            str: A string representing the file extension
        """
        if self.file_extension: 
            return self.file_extension
        else: 
            return None
    