from cffi import FFI
ffibuilder = FFI()


ffibuilder.cdef("""
    int process(int);
""")

ffibuilder.set_source("_process_cffi", "",
                      library_dirs=('.',),
                      libraries=['process'],
                      extra_link_args=['-Wl,-rpath=.'])

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)