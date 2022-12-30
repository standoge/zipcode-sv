import os

from bing_image_urls import bing_image_urls
from serpapi import GoogleSearch

G_KEY = os.environ.get("G_KEY")

class Image:
	
	def __init__(self, endpoint:str):
		self.departament = self.__switcher(endpoint)
	
	def __switcher(self, endpoint:str):
		switch={
			"ah":"ahuchapan",
			"so":"sonsonate",
			"sa":"santa ana",
			"ca":"cabañas",
			"ch":"chalatenango",
			"cu":"cuscatlan",
			"li":"la libertad",
			"pa":"la paz",
			"ss":"san salvador",
			"sv":"san vicente",
			"mo":"morazan",
			"sm":"san miguel",
			"us":"usulutan",
			"un":"la union"
		}
		return switch.get(endpoint, "Invalid value")
	

class ImageBing(Image):

	def __init__(self,endpoint:str):
		super().__init__(endpoint)

	@property
	def images(self, image_limit:int=18):
		return bing_image_urls(f"El Salvador departamento {self.departament}",limit=image_limit)
	
class ImageGoogle(Image):

	def __init__(self,endpoint:str):
		super().__init__(endpoint)

	@property
	def images(self):
		params = {
			"q": f"El Salvador departamento {self.departament}",
			"gl": "us",
			"hl": "en",
			"tbm": "isch",
			"ijn": "0",
			"api_key": G_KEY
		}

		search = GoogleSearch(params)
		results = search.get_dict()["images_results"]
		return results