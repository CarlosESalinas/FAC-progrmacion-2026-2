# Asignación de cariables
x <- 5
y <- 3
z <- x + y

# Muestra el valor de z en la consola escribiendo su nombre:
z

# Tipos de datos primitivos

class(42L)        
class(3.14)       
class("hola")     
class(TRUE)       
class(2 + 3i)     

# Funciones is.*

is.numeric(3.14)  
is.character(42L) 


# Conversión de tipos

as.integer(3.99)    
as.character(100)   
as.numeric("42")    
as.numeric("hola")  

# Vectores

v <- c(1, 2, 3, 4, 5)
length(v)

# En R indexa desde 1, NO desde 0.

v[1]         
v[3]         
v[c(1,3,5)]  

# Operaciones vectorizadas

v * 2
v + c(10, 20, 30, 40, 50)


# Estadística descriptiva

set.seed(42)
calif <- round(rnorm(30, 75, 10), 1)

# Muestra el vector completo:
calif


mean(calif)      # Media:
median(calif)    # Mediana:
var(calif)       # Varianza:
sd(calif)        # Desv. estándar:
range(calif)     # Mínimo y máximo:
table(calif)     # Frecuencias (¿hay valores repetidos?)
summary(calif)   # Resumen completo (los 6 estadísticos)


quantile(calif, c(0.25, 0.5, 0.75))


# Visualización con base R

hist(calif,
     main   = "Distribución",
     col    = "steelblue",
     breaks = 10)

abline(v = mean(calif), col = "red", lwd = 2)


hist(calif, main = "Distribución", col = "green", breaks = 10)
abline(v = mean(calif), col = "red", lwd = 2)


hist(calif, main = "Menos barras",  col = "steelblue", breaks = 10)
hist(calif, main = "Más barras",    col = "steelblue", breaks = 5)


boxplot(calif,
        main = "Boxplot",
        col  = "lightgreen",
        ylab = "Calificación")


boxplot(calif, main = "Boxplot con mediana", col = "lightgreen", ylab = "Calificación")
abline(h = median(calif), col = "blue", lwd = 2, lty = 2)



plot(1:30, calif,
     main = "Por alumno",
     pch  = 19,
     col  = "darkorange")

# pch controla la forma del punto. Prueba estos valores:
# pch = 1  (círculo vacío)
# pch = 3  (cruz +)
# pch = 17 (triángulo sólido)
plot(1:30, calif, main = "pch = 1",  pch = 1,  col = "darkorange")
plot(1:30, calif, main = "pch = 3",  pch = 3,  col = "darkorange")
plot(1:30, calif, main = "pch = 17", pch = 17, col = "purple")
