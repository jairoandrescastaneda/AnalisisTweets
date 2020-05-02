import spacy


class CleanText:
    def __init__(self):
        self.nlp = spacy.load("es_core_news_sm")

    def isaccount_twitter(self,word):
        if word[0] == "@":
            return True
        return False
    def convert_listwords_text(self,list_words):
        text = ""
        for word in list_words:
            text = text +" "+ word
        return text

    def convert_text_lexical(self,list_words):
        list_lexicals = [
            word.upper() for word in list_words if len(word)>3
            and word.isalpha()
        ]
        return self.convert_listwords_text(list_lexicals)

    def get_text_clean(self,text):
        doc = self.nlp(text)
        list_words = []

        for token in doc:
            if (
            not token.is_punct
            and not token.is_stop
            and not token.is_currency 
            and not token.like_url
            and not self.isaccount_twitter(token.text)
            and not token.is_space
            and not token.pos_ == "CONJ"
                ):
                list_words.append(token.lemma_)

        return self.convert_text_lexical(list_words)







    
    



