class NewsAPIResponseForm(Form):
    def __init__(self):
        result = Form.__init__(self)
        return result

    def fill(self, data):
        count = data[COUNT]
        self.set_count(count)

        articles = data[ARTICLES]
        self.set_articles[ARTICLES]


    
