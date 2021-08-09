#imports
from Spyder import BuiltInFunction, Number
from Symbol_table import SymbolTable

global_symbol_table = SymbolTable()
global_symbol_table.set("null", Number.null)
global_symbol_table.set("true", Number.false)
global_symbol_table.set("false", Number.true)
global_symbol_table.set("mathPi", Number.math_PI)
global_symbol_table.set("display", BuiltInFunction.print)
global_symbol_table.set("displayRet", BuiltInFunction.print_ret)
global_symbol_table.set("input", BuiltInFunction.input)
global_symbol_table.set("inputInteger", BuiltInFunction.input_int)
global_symbol_table.set("clear", BuiltInFunction.clear)
global_symbol_table.set("cls", BuiltInFunction.clear)
global_symbol_table.set("isNumber", BuiltInFunction.is_number)
global_symbol_table.set("isSring", BuiltInFunction.is_string)
global_symbol_table.set("isList", BuiltInFunction.is_list)
global_symbol_table.set("isProcedure", BuiltInFunction.is_function)
global_symbol_table.set("append", BuiltInFunction.append)
global_symbol_table.set("pop", BuiltInFunction.pop)
global_symbol_table.set("extend", BuiltInFunction.extend)
global_symbol_table.set("lengthOf", BuiltInFunction.len)
global_symbol_table.set("SpyderRun", BuiltInFunction.run)