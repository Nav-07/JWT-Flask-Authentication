import markdown2

# This Class Handles Markdown2 to Html5
class HTMLParser:
	# This Method Converts Markdown2 to HTML5
	def convert_to_html(self, app_path, file):
		with open(app_path+'/pages/'+file+'.md') as markdown_file:
			return markdown2.markdown(markdown_file.read())