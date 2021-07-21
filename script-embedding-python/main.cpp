#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <iostream>

int main(int argc, const char * argv[]) {
    Py_Initialize();

    PyObject * sys = PyImport_ImportModule("sys");
    PyObject * path = PyObject_GetAttrString(sys, "path");
    PyList_Append(path, PyUnicode_FromString("../"));

    PyObject * pName = PyUnicode_DecodeFSDefault("process");
    PyObject  * pModule = PyImport_Import(pName);
    PyObject * pFunc = PyObject_GetAttrString(pModule, "process");

    Py_DecRef(pName);
    Py_DecRef(pModule);

    if (pFunc &&PyCallable_Check(pFunc)) {

        for (auto i = 0; i <= 100; ++i) {
            PyObject * pArgs = PyTuple_New(1);
            PyObject * pValue = PyLong_FromLong(i);
            PyTuple_SetItem(pArgs, 0, pValue);
            const auto pResult = PyObject_CallObject(pFunc, pArgs);
            const auto result = PyLong_AsLong(pResult);
            std::cout << "Call with " << i << " resulted in " << result << '\n';

            Py_DecRef(pResult);

        }
    }
	
	return Py_FinalizeEx() < 0 ? -1 : 0;
}
