"""
Author: Cristian M. Moreno Rodriguez
Project: Selecciona al azar un texto en una lista creada
"""
import random
import subprocess #Para ejecutar sentencias en la linea de comandos
import time #Para generar un sleep
from datetime import datetime

subprocess.call('clear', shell=True)

frases = ["¿Por qué esta magnífica tecnología científica, que ahorra trabajo y nos hace la vida más fácil nos aporta tan poca felicidad? La respuesta es esta, simplemente: porque aún no hemos aprendido a usarla con tino. (Albert Einstein)", " Ahora incorporamos un control cada vez mayor en la propia tecnología. El control está integrado. Si observas un ordenador moderno, en la mayoría de los casos, ni siquiera lo puedes abrir para conocer todos sus componentes. (Julian Assange)"," Vivimos en una sociedad profundamente dependiente de la ciencia y la tecnología y en la que nadie sabe nada de estos temas. Ello constituye una fórmula segura para el desastre. (Carl Sagan)"," El progreso tecnológico se permite sólo cuando sus productos pueden aplicarse de algún modo a disminuir la libertad humana. (George Orwell)"," El futuro de la tecnología amenaza destruir todo lo que es humano en el hombre, pero la tecnología no alcanza a la locura, y en ella es donde lo humano del hombre se refugia. (Clarice Lispector)"," Todos los grandes inventos tecnológicos creados por el hombre – el avión, el automóvil, el ordenador – dicen poco acerca de su inteligencia, pero dicen mucho de su pereza. (Mark Kennedy)"," Una máquina puede hacer el trabajo de cincuenta hombres ordinarios. Ninguna máquina puede hacer el trabajo de un hombre extraordinario. (Elbert Hubbard)"," En otras palabras, los ordenadores super rápidos del futuro serán como sabios autistas, es decir, podrán memorizar amplias cantidades de información, pero no podrán hacer mucho más y serán incapaces de sobrevivir por sus propios medios en el mundo real. (Michio Kaku)"," Creo que las novelas que dejan de lado la tecnología malinterpretan la vida tan mal como los victorianos tergiversaron la vida, dejando fuera el sexo. (Kurt Vonnegut)"," La tecnología hizo posible las grandes poblaciones; ahora las grandes poblaciones hacen que la tecnología sea indispensable. (José Krutch)"," ¿Cuál es el truco mágico que nos hace inteligentes? El truco es que no hay truco. El poder de la inteligencia emana de nuestra vasta diversidad, no de un único y perfecto principio. (Marvin Minsky)"," Cualquier imagen tridimensional contiene una enorme cantidad de información: un montón de veces, la información almacenada en una imagen bidimensional. (Michio Kaku)", " ¿Qué somos las personas sino máquinas muy evolucionadas? (Marvin Minsky)"," Algunos críticos afirman también que un verdadero detector de mentiras, como un verdadero telépata, podría hacer que las relaciones sociales ordinarias resultasen muy incómodas, puesto que cierta cantidad de mentira es un «lubricante social» que engrasa las ruedas de la sociedad en movimiento. (Michio Kaku)"," Si tu negocio no está en Internet, tu negocio no existe. (Bill Gates)"," No se puede dotar ni siquiera a la mejor máquina de iniciativa; la apisonadora más alegre jamás podrá plantar flores. (Walter Lippmann)"," Que algo no haya salido como hayas querido, no significa que sea inútil. (Thomas Edison)"," La ciencia y la tecnología revolucionan nuestras vidas, pero la memoria, la tradición y el mito cercan nuestra respuesta. (Arthur Schlesinger)"," El hito siguiente en la historia de la IA: aplicar una ingeniería inversa al cerebro humano. (Michio Kaku)"," Estaremos realmente atrapados con la tecnología cuando todo lo que realmente queramos sean sólo cosas que funcionen. (Douglas Adams)"," Hasta la fecha, no se ha diseñado un ordenador que sea consciente de lo que está haciendo; pero, la mayor parte del tiempo, nosotros tampoco lo somos. (Marvin Minsky)"," Cuando se produce un conflicto entre la tecnología moderna y los deseos de nuestros primitivos antepasados, los deseos primitivos siempre ganan. Este es el Principio del Hombre de las Cavernas. (Michio Kaku)", " Los entornos tecnológicos no son meramente, pasivos recipientes de personas, son procesos activos que reconfigurar a las personas y otras tecnologías similares. (Herbert Marshall Mcluhan)", " El gran motor del cambio es la tecnología. (Alvin Toffler)", " El reconocimiento de patrones, como ya hemos visto, es uno de los principales obstáculos para la inteligencia artificial. (Michio Kaku)", " Todo individuo considera que los límites de su propia visión son los límites del mundo. (Arthur Schopenhauer)", " Alrededor de 2020, o poco después, la ley de Moore dejará gradualmente de ser válida, y es posible que Silicon Valley se convierta poco a poco en un simple cinturón industrial, salvo que se encuentre una tecnología sustitutiva. (Michio Kaku)", " Algún día seremos capaces de alcanzar la inmortalidad. Haremos copias de nuestros cerebros. Puede que los creemos en un laboratorio o que, simplemente, descarguemos su contenido en un ordenador. (Marvin Minsky)", " La tecnología y la robótica están avanzando y reducirán la necesidad de trabajadores en el futuro. (Jan C. Ting)", " La tecnología y las redes sociales han traído el poder a la gente. (Marcos McKinnon)", " La máquina tecnológicamente más eficiente que el hombre ha inventado es el libro. (Northrop Frye)", " La tecnología es importante, pero lo único que realmente importa es qué hacemos con ella. (Muhammad Yunus)", " Cada aspecto de la tecnología humana tiene un lado oscuro, incluyendo el arco y la flecha. (Margaret Atwood)", " Toda esta tecnología moderna sólo hace que la gente trate de hacer todo a la vez. (Bill Watterson)", " La biología es la mejor tecnología. Siendo el ADN el software, las proteínas el hardware, y la células las fábricas. (Arvind Gupta)", " Nuestro mundo está creado en la biología y una vez que la entendamos, se convierte en tecnología. (Ryan Bethencourt)", " La tecnología ya está ahí, su éxito vendrá condicionado en gran medida por la cantidad, utilidad e interés de las aplicaciones que se desarrollen para ellos; y como en cualquier otro dispositivo electrónico, por la sencillez de instalación, conexión y uso. (Nuria Higuera Ruiz)", " La tecnología nos está enseñando a ser humanos de nuevo. (Simon Mainwaring)", " El progreso tecnológico sólo nos ha proporcionado medios más eficientes para ir hacia atrás. (Aldous Huxley)", " Si la ciencia ficción es la mitología de la tecnología moderna, entonces su mito es trágico. (Ursula K. Le Guin)", " Incluso cuando te tomas unas vacaciones de la tecnología, la tecnología no se toma un descanso de ti. (Douglas Coupland)", " Las redes sociales no son para explotar la tecnología, sino para servir a la sociedad. (Simon Mainwaring)", " Los ordenadores son como los bikinis. Ahorran a la gente un montón de conjeturas. (Sam Ewing)", " El gran mito de nuestro tiempo es que la tecnología es la comunicación. (Libby Larsen)", " La tecnología nueva no es buena o mala. Tiene que ver con cómo las personas eligen usarla. (David Wong)", " Si piensas que la tecnología puede solucionar tus problemas de seguridad, está claro que ni entiendes los problemas ni entiendes la tecnología. (Bruce Schneier)", " Siempre llega una nueva herramienta. La tecnología es neutral, depende de cómo se use. (Rick Smolan)", " La tecnología es siempre un arma de doble filo. Traerá muchos beneficios, pero también muchos desastres. (Alan Moore)", " La tecnología moderna debe a la ecología una disculpa. (Alan M. Eddison)", " La tecnología tiene que ser inventada o adoptada. (Jared Diamond)", " La tecnología es una palabra que describe algo que no funciona todavía. (Douglas Adams)", " La tecnología nos facilita reducir las barreras de la distancia y el tiempo. (Emily Greene Balch)", " El propósito de la tecnología no es confundir al cerebro, es ayudar al cuerpo. (William S. Burroughs)", " Las cámaras digitales son un gran invento, porque nos permiten recordar grandes momentos. (Demetri Martin)", " Toda nuestra tecnología es completamente innecesaria para una vida feliz. (Tom Hodgkinson)", " La humanidad ha adquirido toda la tecnología correcta por los motivos incorrectos. (R. Buckminster Fuller)", " Es sólo cuando las cosas salen mal que las máquinas te recuerdan lo poderosas que son. (Clive James)", " Incluso la tecnología, que debería unirnos, nos divide. Todos estamos conectados, pero aun así nos sentimos solos. (Dan Brown)", " Eventualmente no diremos «me están espiando desde mi teléfono, sino “mi teléfono me está espiando”. (Phillip K. Dick)", " Primero creamos las herramientas, luego las herramientas nos crean. (Marshall McLuhan)", " Por esto amo la tecnología; si la usas bien, puede darte poder y privacidad. (Cory Doctorow)", " El mayor daño que puede hacer la inteligencia artificial es que la gente crea que la puede comprender. (Eliezer Yudkowsky)", " Errar es humano, pero las máquinas, por más que lo intenten, son incapaces de errar como el humano. (Agatha Christie)", " Mientras las ciudades crecen, y la tecnología se esparce por el mundo, la creencia y la imaginación se desvanece con nosotros. (Julie Kagawa)", " La promesa definitiva de la tecnología es volvernos los maestros de un mundo que podemos controlar presionando un botón. (Volker Grassmuck)", " Cada vez que llega una nueva tecnología, tiene que estar acompañada de demandas por nuevas habilidades, nuevos idiomas. (Richard Kadrey)", " En estos días, hay cámaras hechas para ver la diferencia entre una ardilla y una bomba. (George W. Bush)", " Debemos abordar, individual y colectivamente, las cuestiones morales y éticas planteadas por la investigación de vanguardia en inteligencia artificial y biotecnología, lo que permitirá la extensión de nuevas formas de vida, como los bebés de diseño y la extracción de memoria. (Klaus Schwab)", " La tecnología hace posibles grandes masas, las grandes masas hacen a la tecnología indispensable. (Joseph Wood Krutch)", " Vamos, hay que crear el mañana, y no preocuparse por el ayer. (Steve Jobs)", " Algunas personas denominan a esta tecnología inteligencia artificial, cuando en realidad lo que va a permitir es que aumente la nuestra propia. (Gin Rometti)", " No podemos controlar lo que crece en internet, pero tampoco tenemos que mirarlo. (Tiffany Madison)", " El hombre es un pensador lento, sentimental, pero brillante. Las máquinas son rápidas, precisas y estúpidas. (John Pfeiffer)", " No es que usemos la tecnología, vivimos con la tecnología. (Godfrey Reggio)", " El hombre se ha vuelto la herramienta de sus herramientas. (Henry David Thoreau)", " La tecnología por sí sola no basta. También tenemos que poner el corazón. (Jane Goodall)", " No, no fallé. Sólo encontré diez mil formas que no funcionarán. (Thomas Edison)", " A veces una tecnología es tan imponente que la imaginación vuela con ella, a menudo, muy muy lejos de la realidad. Con los robots es así. Desde muy temprano, se hicieron muchas promesas grandes en robótica basadas en éxitos preliminares y, en última instancia, no se cumplieron. (Daniel H. Wilson)", " Nosotros, los humanos, tenemos una relación de amor-odio con nuestra tecnología. Amamos cada nuevo avance y odiamos cuán rápido está cambiando nuestro mundo. Los robots realmente expresan esa relación de amor-odio que tenemos con la tecnología. (Daniel H. Wilson)", " La cosa no es como se usa la herramienta, sino cómo ella nos usa. (Nick Joaquin)", " Cualquier tecnología suficientemente avanzada es equivalente a la magia (Arthur C. Clarke)", " Como tecnólogo, veo cómo la IA y la cuarta revolución industrial afectarán todos los aspectos de la vida de las personas. (Fei-Fei Li)", " Cuando me preguntaron sobre algún arma capaz de contrarrestar el poder de la bomba atómica yo sugerí la mejor de todas: La paz (Albert Einstein)", " Los hombres construimos demasiados muros y no suficientes puentes (Isaac Newton)", "Crear un ser artificial ha sido el sueño del hombre desde que nació la ciencia. Uno de los intereses más habituales de la tecnología actual"," Habrá seres humanos con minirrobots en el cerebro. (Raymond Kurzweil)"," Primero el Señor creó el tipo más bajo, los humanos, formados más fácilmente. Poco a poco fue reemplazándolos por robots, el siguiente paso, y finalmente me creó a mí, para ocupar el sitio de los últimos humanos. A partir de ahora, yo sirvo al Señor. (Isaac Asimov)"," Nunca uses a un humano para hacer el trabajo de una máquina. (Agente Smith)"," Se ha vuelto terriblemente obvio que nuestra tecnología ha superado nuestra humanidad. (Albert Einstein)"," Los países con la mayor densidad de robots tienen también las tasas de desempleo más bajas. La combinación correcta de tecnología y humanos impulsarán la prosperidad. (Ulrich Spiesshofer)","Un día las inteligencias artificiales nos verán como a simios que caminaban erguidos condenados sin remedio a la extinción."," Con mucha diferencia, el mayor peligro de la Inteligencia Artificial es que las personas concluyen demasiado pronto que la entienden. (Eliezer Yudkowsky)"," La conectividad es un derecho humano. (Mark Zuckerberg)"," El arte se opone a la tecnología y la tecnología inspira el arte (John Lasseter)"," El mundo se puede cambiar en 140 caracteres. (Jack Dorsey)"," Si continuamos desarrollando nuestra tecnología sin sabiduría o prudencia, nuestro servidor se convertirá en nuestro verdugo. (Omar Bradley)"," No construimos servicios para hacer dinero; hacemos dinero para construir mejores servicios (Mark Zuckerberg)"," Todo lo que hagamos planteará problemas en el futuro, pero eso no debería echarnos atrás (Mark Zuckerberg)"," Si decides hacer solo las cosas que sabes que van a funcionar, dejarás un montón de oportunidades encima de la mesa. (Mark Zuckerberg)"," La ciencia de hoy es la tecnología del mañana. (Edward Teller)"," La robótica está empezando a cruzar esa línea que separa al movimiento absolutamente primitivo del movimiento que se asemeja al comportamiento animal. (J.J. Abrams)"," Parte de la inhumanidad de la computadora es que, una vez que está programada de forma correcta y funciona sin problemas, es completamente honesta. (Isaac Asimov)"," Creo que cuando los ordenadores asuman ciertas tareas, eso será difícil para nosotros. Pasará mucho tiempo antes de que las máquinas igualen a los humanos con el tipo de juicio que ejercemos en muchas áreas diferentes (Bill Gates)"," Vaya, mi propio robot gigante, soy el niño con más suerte de toda América. Esto es increíble, es el mayor descubrimiento, desde, no sé, la televisión. (El gigante de hierro)"," Un robot no hará daño a un ser humano o, por inacción, permitirá que un ser humano sufra daño. (Isaac Asimov)"," Ya no requiere un presupuesto multimillonario para que la IA funcione en su empresa. Representa una oportunidad para nivelar el campo de juego para las empresas más pequeñas. (Nichole Jordan)"," No sé con qué armas se combatirá la tercera guerra mundial, pero la cuarta será con palos y piedras. (Albert Einstein)"," Es el impulso de la ciencia para tratar de entender la naturaleza, y el impulso de la tecnología para tratar de manipularla. (Siddhartha Mukherjee)"," La tecnología y las redes sociales han traído el poder a la gente. (Marcos McKinnon)"," Un robot debe cumplir las órdenes dadas por los seres humanos, a excepción de aquellas que entrasen en conflicto con la primera ley. (Isaac Asimov)","Siempre he estado convencido de que la única forma de hacer que funcione la inteligencia artificial es hacer el cálculo de manera similar al cerebro humano. Ese es el objetivo que he estado persiguiendo. (Geoffrey Hinton)"," No me dan miedo los ordenadores. Temo la falta de ellos. (Isaac Asimov)"," Me alegro de que inventaran la bomba atómica: así si necesitan voluntarios para ponerse debajo cuando la lancen, puedo presentarme el primero. (J. D. Salinger)"," Un robot debe proteger su propia existencia, hasta donde esta protección no entre en conflicto con la primera o segunda Leyes. (Yo, robot.)"," La sociedad tecnológica ha logrado multiplicar las ocasiones de placer, pero encuentra muy difícil engendrar la alegría. (Papa Francisco)"," El ordenador nació para resolver problemas que antes no existían. (Bill Gates)"," Internet debe ser un medio de comunicación entre los pueblos que contribuya a la paz mundial y que el principal objetivo de la alta tecnología es mejorar el nivel de vida de las personas. (Larry Ellison)"," La humanidad está desarrollando la tecnología correcta por las razones equivocadas. (Richard Buckminster)"," Internet se está convirtiendo en la plaza del pueblo de la aldea global del mañana. (Bill Gates)"," El Internet puede ser un paso muy positivo hacia la educación, la organización y la participación en una sociedad significativa (Noam Chomsky)"]


def initialise():

    def start():

        print(" ** Bienvendio al primer programa ** ")
        #print("  🙋 >>: Tenemos una longitud de "+str(len(frases))+" frases en total.\n")

        _hour_now = 0

        while _hour_now != 13:  
            date = datetime.now()
            _hour_now = date.time().hour
            _time_now = date.time().strftime("%H:%M:%S")
            print(" 🕰  >> ", _time_now)
            time.sleep(1)

        if _hour_now == 13:
            i= 0
            while i != 3000:
                i +=1
                if i % 10 == 0:
                    print(" ** Reproduciendo el texto **")
                    subprocess.call('espeak -ves+f4 -s 170 '+'"Chicos, la comida esta lista!!"', shell=True)
                time.sleep(1)
        print("Ha terminado el proceso de iniciar el reloj despertador")

    start()

initialise()

