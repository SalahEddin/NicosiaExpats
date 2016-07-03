import datetime

class event(object):
    m_time = datetime.date(1990,1,1)
    m_place = "Nicosia"
    m_imgUrl = "#"
    m_detailsUrl = "#"
    m_description = ""
    m_title = ""
    m_genre = ""
    def __init__(self, title, when, where, img = None, moreURL = None, desc = None, genre = None):
        self.m_title = title
        self.m_time = when
        self.m_place = where
        if img is not None:
            self.m_imgUrl = img
        if desc is not None:
            self.m_description = desc
        if genre is not None:
            self.m_genre = genre
        if moreURL is not None:
            self.m_detailsUrl = moreURL