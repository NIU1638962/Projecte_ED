import cfg
import uuid


class MusicID:
    __slots__ = '__diccionari_uuid','__diccionari_remove','__len'

    def __init__(self):
        """
        Iniclitza la classe.

        Returns
        -------
        None.

        """
        self.__diccionari_uuid = {}

    def __len__(self) -> int:
        return len(self.__diccionari_uuid)

    def __str__(self) -> str:
        return self.__diccionari_uuid.__str__()

    def generate_uuid(self, file: str) -> str:
        """


        Parameters
        ----------
        file : str
            File generic path from root directory.

        Returns
        -------
        str
            UUID del file generat si no hi estaba previament sense haberse eliminat.
        None
            L'UUID ja existeix i no ha estat esborrat.

        """
        print("File rebut: " + file)
        # Generem UUID.
        uuid_generat = uuid.uuid5(uuid.NAMESPACE_URL, file)

        if uuid_generat in self.__diccionari_uuid:
            print("ERROR : Aquest UUID ya existeix")
            return None
        else:
            path = cfg.get_canonical_pathfile(file)
            self.__diccionari_uuid[uuid_generat] = path
            return uuid_generat

    def get_uuid(self, file: str) -> str:
        """
        Retorna l'uuid ja generat d'un file.

        Parameters
        ----------
        file : str
            File generic path from root directory.

        Returns
        -------
        str
            UUID del file generat si no hi estaba previament sense haberse eliminat.
        None
            L'UUID ja existeix i no ha estat esborrat.

        """
        try:
            path =  cfg.get_canonical_pathfile(file)
            uuids = self.__diccionari_uuid.keys()
            paths = self.__diccionari_uuid.values()
            uuid = list(uuids)[list(paths).index(path)] #Obtenim la posicio del arxiu i accedim per obtindre el respectiu uuid
            return uuid
        except:
            return None
    

    def remove_uuid(self, file_uuid: str) -> str:
        """
        Elimina l'uuid generat d'un file.

        Parameters
        ----------
        file_uuid : str
            UUID del file.

        Returns
        -------
        str
            UUID eliminat o None si ja estaba eliminat.

        """
        try:
            del self.__diccionari_uuid[file_uuid]
        except:
            return None
        
    def __iter__(self):
        return tuple(self.__diccionari_uuid.values()).__iter__()
    
    def __hash__(self): 
        return hash(tuple(self.__diccionari_uuid.keys()))
    
    def __eq__(self, other):
        return self.__diccionari_uuid == other.__uuid_dict
    
    def __ne__(self, other):
        return self.__diccionari_uuid != other.__uuid_dict
    
    def __lt__(self, other):
        return self.__len__() < other.__len__()

    def __repr__(self):
        return self.__diccionari_uuid.__repr__()
        
