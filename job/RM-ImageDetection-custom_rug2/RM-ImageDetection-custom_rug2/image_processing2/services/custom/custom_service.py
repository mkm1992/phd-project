from services.utility.utility_service import UtilityService
from services.customRug.main_service import MainService

class CustomService:
	@classmethod
	def check_image(cls, content_type, buf):
		print(content_type, "the content tope")
		if len(list(filter(lambda item: content_type == item, ["application/octet-stream", "image/jpg", "image/png", "image/jpeg"]))) !=0:
			return buf
		else:
			return "Wrong image!"

	
	def custom_process(url):
		content_type, buf = UtilityService.url_downloader(url)
		print(type(buf), "the buffer type")
		return CustomService.check_image(content_type, buf)


        
