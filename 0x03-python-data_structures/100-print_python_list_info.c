#include <Python.h>
/**
 * print_python_list_info - print the infor about python list
 * @p: pointer to the python list
 * Return: Always Nothing
 */

void print_python_list_info(PyObject *p)
{
	const char *typeName;
	py_ssize_t i;
	PyObject *item;
	Py_ssize_t size = PyList_Size(p);
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		typeName = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", i, typeName);
		Py_DECREF(item);
	}
}
