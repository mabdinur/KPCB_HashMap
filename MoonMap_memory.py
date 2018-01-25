from datetime import datetime
class MoonMap:
    """USE  --> test(num_values_to_fill , map_size)     from module map_test to test this class
    This class creates a hash MAP using 2 lists, one to store values and the other to store a key. Whenever this there
    is a conflict between the hash of two strings( ie. two keys produce the same hashcode) the first value to be set
    will be place in the appropriate index while the next value will be place in the smallest empty index.
    Therefore when retrieving or deleting a value the run time will be on average O(1) and O(n) for worst case senarios.
     """

    def __init__(self, size):
        """Sets size of HashMap and initializes all li_key and li_value arrays to None"""
        self.max_size = size
        self.curr_size = 0
        self.li_key = [None]*size
        self.li_value = [None]*size

    def boolean_set(self, key, value):
        """Places keys and values in an index determined by the hash, if conflicts arise, values are placed in the
        first availible Null value """
        if(self.curr_size < self.max_size ):
            i = key.__hash__() % self.max_size
            if self.li_key[i] is None:
                self.li_value[i] = value
                self.li_key[i] = key
            elif key == self.li_key[i] :
                self.li_value[i] = value
            else:
               for j in range(self.max_size) :
                if self.li_key[j] == None :
                    self.li_key[j] = key
                    self.li_value[j] = value
                    break
            self.curr_size += 1
            return True
        else:
            return False

    def get(self, key):
        """Retrieves a specific value in a key-value pair otherwise it returns NONE"""
        i = key.__hash__() % self.max_size
        if self.li_key[i] == key :
            return self.li_value[i]
        else:
            return self.__search_key(key, self.__find_value )

    def delete(self, key):
        """Removes a specified Key by setting the key value at a specified index to Null"""
        i = key.__hash__() % self.max_size
        if self.li_key[i] == key:
            return  self.__remove(i)
        else:
            return self.__search_key(key, self.__remove)

    def __search_key(self, key, func):
        """**USED when hash produces the same index value for 2 strings***,
        this method finds the index of a key-value pair when a value was placed in an index that does not
         correspond to the hashed value of the key"""
        for k in range(self.max_size):
            if key == self.li_key[k]:
                return func(k)
        return None

    def __remove(self, i):
        """Nullifies the Key value at a specific index,
        It is used in the delete method after finding the appropriate key-value pair"""
        self.li_key[i] = None
        self.curr_size -= 1
        return self.li_value[i]

    def __find_value(self, i):
        """Returns a value at a specific index,
        It is used in the get method to retreive an existing value"""
        return self.li_value[i]

    def load(self):
        """Returns the percent of occupided indicies in the key list"""
        if( int(self.max_size) == 0):
            return "This is an empty HASH"
        else:
            return self.curr_size/float(self.max_size)