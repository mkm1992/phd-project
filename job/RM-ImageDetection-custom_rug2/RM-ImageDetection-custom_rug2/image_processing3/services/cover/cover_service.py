from services.utility.utility_service import UtilityService
from services.coverRug.main_service import MainService

class CoverService:
	@classmethod
	def check_image(cls, content_type, buf):
		print(content_type, "the content tope")
		if len(list(filter(lambda item: content_type == item, ["application/octet-stream", "image/jpg", "image/png", "image/jpeg"]))) !=0:
			return buf
		else:
			return "Wrong image!"

	
	def cover_process(url):
		content_type, buf = UtilityService.url_downloader(url)
		print(type(buf), "the buffer type")
		return CoverService.check_image(content_type, buf)


        
