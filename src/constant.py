import typing

class __const_access_error(Exception):
  def __init__(self, message = "writing to constant is not allowed") -> None:
    super().__init__(message)

class Constant:
  def __init__(self, value, locked: bool = True) -> None:
    self.__locked = locked
    self.__value = value
  
  def lock(self) -> None:
    self.__locked = True
  
  def unlock(self) -> None:
    self.__locked = False

  def is_locked(self) -> bool:
    return self.__locked

  @property
  def val(self):
    return self.__value
  
  @val.setter
  def val(self, value):
    if (self.__locked):
      raise __const_access_error()
    else:
      self.__value = value
  
  @val.getter
  def val(self):
    return self.__value
    