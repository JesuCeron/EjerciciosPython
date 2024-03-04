
print ("Ingrese tres numero")

n1=int(input("Numero uno:"))
n2=int(input("Numero dos:"))
n3=int(input("Numero tres:"))

def devolver_distintos(nu1,nu2,nu3):

    if nu1+nu2+nu3 > 15:
         
         if nu1 > nu2 and nu3:

            return nu1

         if nu2 > nu3 and nu1:

            return nu2
         
         if nu3 > nu2 and nu1:

            return nu3
    
    elif nu1+nu2+nu3 < 10:
         
         if nu1 < nu2 and nu3:

             return nu1

         if nu2 < nu3 and nu1:

            return nu2
         
         if nu3 < nu2 and nu1:

            return nu3
    
    else:
         
         if nu1 < nu2 and nu1 > nu3 or nu1 > nu2 and nu1 < nu3: 

            return nu1

         if nu2 < nu3 and nu2 > nu1 or nu2 > nu3 and nu1 < nu1:

            return nu2
         
         if nu3 < nu2 and nu3 > nu1 or nu3 > nu1 and nu1 < nu2:

            return nu3


print (devolver_distintos (n1, n2, n3))

        
         
         
         
        


    
