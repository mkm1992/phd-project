from services.utility.utility_service import UtilityService
from services.carpettingImage.main_service import MainService

class CarpettingService:
	@classmethod
	def check_image(cls, content_type, buf):
		print(content_type, "the content tope")
		if len(list(filter(lambda item: content_type == item, ["application/octet-stream", "image/jpg", "image/png", "image/jpeg"]))) !=0:
			return buf
		else:
			return "Wrong image!"

	
	def carpetting_process(url):
		content_type, buf = UtilityService.url_downloader(url)
		print(type(buf), "the buffer type")
		return CarpettingService.check_image(content_type, buf)


	def carpetting_process(url, type):
    		return MainService.shaping_carpet(url, type)
        
