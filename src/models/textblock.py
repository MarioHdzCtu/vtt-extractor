from dataclasses import dataclass
import re

@dataclass
class TextBox:

    subtitle_cue: str
    timestamp_str: str
    content: str

    @property
    def text(self):
        match = re.search(r'>(.*?)</v>', self.content)
        if match:
            return match.group(1)
        
    @property
    def speaker(self):
        match = re.search(r'<v(.*?)>', self.content)
        if match:
            return match.group(1).strip()