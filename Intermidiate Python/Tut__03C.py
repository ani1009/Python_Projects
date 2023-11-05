try:
    print("It Will Try This Code and Will Throw Exception, If There is Any Problem.")
except Exception as e:
    print("It Will Run Only if 'try block' Fails.")
else:
    print("It Will Run Only if there is no Exception." 
          "Use This to Run Code Which Should Only Execute if there is no Exception")
finally:
    print("This Will be Printed in Every Case.")

