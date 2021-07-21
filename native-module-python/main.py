# Import process function from pre-built cffi module
from _process_cffi import ffi, lib


process = lib.process

if __name__=="__main__":
	for i in range(1, 101):
		print("Call with", i, "results in", process(i))

