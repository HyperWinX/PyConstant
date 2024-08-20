import src.constant as const

def test_const_set_get() -> None:
  var = const.Constant(5, False)
  try:
    var.val = 10
  except const.__const_access_error:
    pass
  assert(var.val == 10)

def test_const_locked_set() -> None:
  var = const.Constant(5, True)
  try:
    var.val = 10
  except:
    pass
  
  assert(var.val == 5)