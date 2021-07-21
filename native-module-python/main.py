# from cffi import F
import ctypes
import pathlib
# Import process function from pre-built cffi module

from _pi_cffi import ffi, lib
# libname = pathlib.Path().absolute() / "libprocess.so"
# lib = ctypes.CDLL(libname)
# process = lib.process()

if __name__=="__main__":
	for i in range(1, 101):
		print("Call with", i, "results in", lib.process(i))

