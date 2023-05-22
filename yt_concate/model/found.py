from model.yt import YT


class Found:
    def __init__(self, yt: YT, caption: str,  time: str):
        self.yt = yt
        self.caption = caption
        self.time = time

    def __str__(self):
        return f'<Foundobj~ {self.yt} >'

    def __repr__(self):
        content = ' : '.join([
            'yt = ' + str(self.yt),
            'caption = ' + str(self.caption),
            'time = ' + str(self.time),
        ])
        return f"<Foundobj~ {content}>"
