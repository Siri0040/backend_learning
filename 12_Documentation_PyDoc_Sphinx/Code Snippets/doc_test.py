from docutils import core
def reST_to_html_fragment(a_str):
	parts = core.publish_parts(
							source=a_str,
							writer_name='html')
	return parts['body_pre_docinfo']+parts['fragment']