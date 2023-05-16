#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - print the infor about python list
 * @p: pointer to the python list
 * Return: Always Nothing
 */

void print_python_list_info(PyObject *p)
{
	int j;
	PyListObject *obj = (PyListObject *)p;
	long int size = PyList_Size(p);

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (j = 0; j < size; j++)
		printf("Element %i: %s\n", j, Py_TYPE(obj->ob_item[j])->tp_name);
}
