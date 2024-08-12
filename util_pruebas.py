def verificar_funcion(test_case, funcion, casos):
    for a, b, resultado in casos:
        with test_case.subTest(a=a, b=b, resultado=resultado):
            test_case.assertEqual(funcion(a, b), resultado)
