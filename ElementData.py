class ElementData:
    __slots__ = '__title', '__artist', '__album', '__genre', '__duration', '__filename'
    
    def __init__(self, title="", artist="", album="", genre="", duration=0, filename=""):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__genre = genre
        self.__duration = duration
        self.__filename = filename

    def __eq__(self, elemdata) -> bool:
        return self.__filename == elemdata.__filename

    def __ne__(self, elemdata) -> bool:
        return self.__filename != elemdata.__filename

    def __lt__(self, elemdata) -> bool:
        return self.__filename < elemdata.__filename

    def __repr__(self) -> str:
        return "Title: " + str(self.__title) + "\nArtits: " + str(self.__artist) + "\nAlbum: " + str(self.__album) + "\nGenre: " + str(self.__genre) + "\nDuration: " + str(self.__duration) + "\nFilename: " + str(self.__filename)

    def __hash__(self) -> int:
        return hash(self.__title) + hash(self.__artist) + hash(self.__album) + hash(self.__genre) + hash(self.__duration) + hash(self.__filename)

    @property
    def title(self) -> str:
        return self.__title
    
    @title.setter
    def title(self, new: str) -> None:
        self.__title = new

    @property
    def artist(self) -> str:
        return self.__artist
    
    @artist.setter
    def artist(self, new: str) -> None:
        self.__artist = new

    @property
    def album(self) -> str:
        return self.__album
    
    @album.setter
    def album(self, new: str) -> None:
        self.__album = new

    @property
    def genre(self) -> str:
        return self.__genre
    
    @genre.setter
    def genre(self, new: str) -> None:
        self.__genre = new

    @property
    def duration(self) -> int:
        return self.__duration
    
    @duration.setter
    def duration(self, new: int) -> None:
        self.__duration = new

    @property
    def filename(self) -> str:
        return self.__filename
    
    @filename.setter
    def filename(self, new: str) -> None:
        self.__filename = new
