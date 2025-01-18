from dataclasses import dataclass
import re

@dataclass
class TextBox:

    subtitle_cue: str
    timestamp_str: str
    content: str

    @property
    def text(self):
        match = re.search(r'>(.*?)</v>', self.content.replace('\n',' '))
        if match:
            return match.group(1)
        
    @property
    def speaker(self):
        match = re.search(r'<v(.*?)>', self.content.replace('\n',' '))
        if match:
            return match.group(1).strip()
        
    @property
    def start_time(self):
        return self.timestamp_str.split(' --> ')[0]
    
    @property
    def end_time(self):
        return self.timestamp_str.split(' --> ')[1]