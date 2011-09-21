import nltk 
import re 
from nltk.tokenize.api import * 

from libpyICTCLASCore import ICTCLASSegmenterCore
import os

class ICTCLASTokenizer(TokenizerI):

	def __init__(self):
		cur_file_path = __file__;
		cur_dir_path = os.path.dirname(cur_file_path) + os.path.sep;
		print cur_dir_path
		self.ICTCLASCore = ICTCLASSegmenterCore(cur_dir_path)
		
	def tokenize(self, text):
		return self.ICTCLASCore.Segment(text)
		
		
		
if __name__ == '__main__':
	
	seg = ICTCLASTokenizer()
	