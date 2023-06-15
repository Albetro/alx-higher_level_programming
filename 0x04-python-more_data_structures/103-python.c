python

#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

For Python bytes (print_python_bytes):

c

#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p) {
    Py_ssize_t size;
    char *str;
    Py_ssize_t i;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %ld bytes: ", (size <= 10) ? size : 10);
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x", (unsigned char)str[i]);
        if (i < size - 1 && i < 9) {
            printf(" ");
        }
    }
    printf("\n");
}


