# Philip Otter 2025
import json
from datetime import datetime

class crier:
    def __init__(self, boolVerbose: bool, boolColoredOutput: bool, boolTimestamping: bool):
        self.verbose = boolVerbose
        self.colorize = boolColoredOutput
        self.colorize = boolTimestamping

        self.depth = 0
        self.primaryPrefix = '='
        self.secondaryPrefix = '>'
        self.prefix = ''

        self.timestampFormat = '%Y-%m-%d %H:%M:%S'
        self.timestampPrefix = '['
        self.timestampSuffix = ']'

        self.color = ''

        self.build_prefix(self.depth)

        self.colorCodes = {
                    "RED": "\033[31m",
                    "GREEN": "\033[32m",
                    "YELLOW": "\033[33m",
                    "BLUE": "\033[34m",
                    "MAGENTA": "\033[35m",
                    "CYAN": "\033[36m",
                    "WHITE": "\033[37m",
                    "RESET": "\033[0m"
                }


    def write_crier_exception(self, e) -> None:
        try:
            exceptionColor = "RED"
            exceptionPrefix = "CRIER ERROR:  "

            if (self.colorize):
                self.set_color(exceptionColor)
                print(f'{self.color}{e}{self.reset_color()}')
            else:
                print(f'{exceptionPrefix}{e}')

        except Exception as ee:
            print(f'CRITICAL CRIER EXCEPTION HANDLING FAILURE\n{ee}')
    

    def write_message(self, stringMessage: str, intDepth: int) -> None:
        try:

            if (not self.colorize):
                self.write_bland_message(stringMessage, intDepth)
                return

            self.check_depth(intDepth)
            
            print(f'{self.color}{self.get_timestamp()}{self.prefix} {stringMessage}{self.reset_color()}')

        except Exception as e:
            self.write_crier_exception(e)
     

    def write_bland_message(self, stringMessage: str, intDepth: int) -> None:
        try:
            self.check_depth(intDepth)
            print(f'{self.get_timestamp()}{self.prefix} {stringMessage}')

        except Exception as e:
            self.write_crier_exception(e)

    
    def set_color(self, color: str) -> None:
        try:
            if (type(color) == str):
                if (color.upper() in self.colorCodes):
                    self.color = self.colorCodes[color.upper()]
                else:
                    raise ValueError(f'Invalid Color Requested! -> "{color}"')

            elif (type(color) == int):
                if (color == 0):
                    self.set_color("GREEN")
                elif ( color == 1):
                    self.set_color("YELLOW")
                elif ( color == 2):
                    self.set_color("BLUE")
                elif ( color == 3):
                    self.set_color("MAGENTA")
                elif ( color == 4):
                    self.set_color("CYAN")
                else:
                    self.set_color("WHITE")
                
        except Exception as e:
            self.write_crier_exception(e)
    

    def reset_color(self) -> str:
        try:
            self.color = self.colorCodes["RESET"]
        except Exception as e:
            self.write_crier_exception(e)
        
        return self.color


    def build_prefix(self, intDepth: int) -> None:
        try:
            self.prefix = (self.primaryPrefix * intDepth) + self.secondaryPrefix
        except Exception as e:
            self.write_crier_exception(e)


    def set_prefix(self, charPrimary: str, charSecondary: str) -> None:
        try:
            self.primaryPrefix = charPrimary
            self.secondaryPrefix = charSecondary
    
        except Exception as e:
            self.write_crier_exception(e)


    def get_timestamp(self) -> str:
        try:
            now = datetime.now()

            return f'[{now.strftime(self.timestampFormat)}]'

        except Exception as e:
            self.write_crier_exception(e)
    

    def check_depth(self, intDepth):
        try:
            if (self.depth != intDepth):
                self.depth = intDepth

                if (self.colorize):
                    self.set_color(intDepth)
                
                self.build_prefix(intDepth)

        except Exception as e:
            self.write_crier_exception(e)
    

    def dump_object(self, object):
        try:
            if (self.colorize):
                print(f'{self.color}Hear Ye! Hear Ye! Behold The Object {object} {json.dumps(self.__dict__, indent=4)}{self.reset_color()}')
            else:
                print(f'Hear Ye! Hear Ye! Behold The Object {object} {json.dumps(self.__dict__, indent=4)}')
        
        except Exception as e:
            self.write_crier_exception(e)
