from cffi import FFI
ffibuilder = FFI()

# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef("""
    int process(int);
""")

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("_pi_cffi", "",
                      library_dirs=('.',),
                      #include_dirs=('.',),
                      libraries=['process'],
                      extra_link_args=['-Wl,-rpath=.'])
                      #sources=['./libprocess'])   # library name, for the linker

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)