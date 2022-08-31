## Trabajo Práctico 1: Fundamentos

A partir del capitulo 26 de AIMA, se deberá desarrollar un resumen sobre los conceptos más importantes volcados en el capítulo. El mismo deberá contener al menos 200 palabras y ser escrito utilizando el formato markdown provisto por github.

1. ### **El documento debe incluir:**

    a. Al menos 3 secciones correspondientes a las tres partes principales:

          i.      Inteligencia Artificial débil.
         ii.      Inteligencia Artificial fuerte.
        iii.      La ética y los riesgos de desarrollar Inteligencia Artificial.

    b. Un mapa mental de los conceptos y sus relaciones (Para esto es posible utilizar una herramienta como **Xmind**, **Freemind**, o alguna otra aplicación en línea).

    c. Una sección de discusión donde se indique una opinión personal sobre los enfoques tratados en el capítulo, su alcance, su viabilidad, etc. Se debe justificar las opiniones vertidas en esta sección.

2. ### Forma de entrega:

    1.  Crear un repositorio en github con el nombre de **ia-uncuyo-2022** y dentro del mismo crear una carpeta con el nombre **tp1-fundamentos**.
    2.  Dentro de dicha carpeta colocar un archivo con el nombre **tp1-fundamentos.md** con el texto de acuerdo a lo especificado en la sección 1.
    3.  Incluir en dicha carpeta las imágenes que considere necesarias.


---

### **Respuestas**

1.  
    ### **FUNDAMENTOS FILOSÓFICOS**

Los filósofos existen desde mucho tiempo antes que las computadoras y han tratado de responder algunas preguntas respecto a la Inteligencia Artificial: ¿Cómo funcionan las mentes?¿Es posible para las máquinas actuar con la inteligencia con la que actúan las personas?¿Cuáles son las implicaciones éticas de las máquinas inteligentes?
Primero, algo de terminología: la afirmación de que las máquinas podrían actuar como si fueran inteligentes es llamada la hipótesis de la inteligencia artificial débil, y la afirmación de que las máquinas lo hacen, que en realidad están pensando(no solo simular pensar) es llamada hipótesis de la inteligencia artificial fuerte.

#### **INTELIGENCIA ARTIFICIAL DÉBIL ¿PUEDEN LAS MÁQUINAS ACTUAR DE FORMA INTELIGENTE?**

La propuesta para el taller de verano de 1956 que definió el campo de la Inteligencia Artificial (McCarthy et al. 1955) afirmó que “Cada aspecto del aprendizaje o cualquier otra característica de la inteligencia se puede describir con tanta precisión que se puede hacer una máquina para simularla”. De este modo, la Inteligencia Artificial se fundó bajo el supuesto de que es posible una IA débil. Otros afirmaron que la IA débil es imposible: “La inteligencia artificial perseguida dentro del culto del computacionalismo se mantiene ni siquiera a la sombra de una posibilidad de producir resultados duraderos” (Sayre, 1993). Claramente, si la IA es posible o no, depende de cómo se la defina.

El científico en computación Edsger Dijkstra (1984) dijo que “La pregunta de si las máquinas pueden pensar es tan relevante como la pregunta de si los submarinos pueden nadar”. Alan turing en su famoso paper “Computer machinery and Intelligence” (1950), sugirió que en vez de preguntarse si las máquinas pueden pensar, deberíamos preguntarnos si las máquinas podían pasar una prueba de comportamiento inteligente, que se llamó test de Turing. La prueba consiste en un programa que tiene que mantener una conversación con un interrogador durante 5 minutos. El interrogador tiene que adivinar si la conversación se está realizando con un programa o una persona. El programa pasa la prueba si engaña a la persona el 30% del tiempo.
Turing examinó una amplia variedad de objeciones a la posibilidad de máquinas inteligentes, algunas de ellas son:

##### **El argumento de la incapacidad** 
Afirma que una máquina no puede hacer “X”. Como ejemplo de X, turing lista lo siguiente:
Ser amable, ingenioso, hermoso, amistoso, tener iniciativa, tener sentido del humor, distinguir el bien del mal, cometer errores, enamorarse, disfrutar de las fresas con crema, enamorar a alguien, aprender de la experiencia, usar correctamente las palabras, ser el sujeto de su propio pensamiento, tener tanta diversidad de comportamiento como el hombre, hacer algo realmente nuevo.

##### **La objeción matemática**
 Es bien conocido, a través del trabajo de Turing (1936) y Gödel (1931), que ciertas preguntas matemáticas son en principio imposibles de responder por sistemas formales particulares. El teorema de incompletitud de Gödel es el ejemplo más famoso de esto. Brevemente, para cualquier sistema axiomático formal F suficientemente poderoso para hacer aritmética, es posible construir un llamada oración de Gödel G(F) con las siguientes propiedades:

- G(F ) es una oración de F, pero no puede probarse dentro de F.
- Si F es consistente, entonces G(F) es verdadera.

Filósofos como J. R. Lucas (1961) han afirmado que este teorema demuestra que las máquinas son mentalmente inferiores a los humanos, porque las máquinas son sistemas formales que están limitados por la teorema de incompletitud—no pueden establecer la verdad de su propia oración de Gödel—mientras que los humanos no tenemos esa limitación

**El argumento de la informalidad**: Turing planteó una de las críticas más influyentes y persistentes a la IA como empresa como el "argumento de la informalidad del comportamiento". Esencialmente, esta es la afirmación de que el comportamiento de los seres humanos es demasiado complejo para ser capturado por un simple conjunto de reglas y que debido a que las computadoras no pueden hacer más que seguir un conjunto de reglas, no pueden generar un comportamiento tan inteligente como el de los humanos. La incapacidad de capturar todo en un conjunto de reglas lógicas se denomina problema de cualificación en IA.

#### **INTELIGENCIA ARTIFICIAL FUERTE ¿PUEDEN LAS MÁQUINAS PENSAR REALMENTE?**

Muchos filósofos claman que una máquina que pasa el test de Turing aún no estaría realmente pensando, sino que sólo sería una simulación del pensamiento. Otra vez, la objeción fue prevista por Turing, citando un discurso del profesor Geoffrey Jefferson (1949):

> Hasta que una máquina pueda escribir un soneto o componer un concierto por pensamientos y emociones que sienta, y no por la casualidad de leer símbolos, podríamos acordar que las máquinas igualan al cerebro

Turing llama a este el argumento de la **conciencia**, la máquina tiene que ser consciente de su propio estado mental y acciones. Mientras que la conciencia es un tema importante, el punto de vista de Jefferson era de la **fenomenología** o el estudio de la experiencia directa: la máquina tiene que sentir emociones. Otros se enfocan en la **intencionalidad**, esto es la pregunta de si las máquinas tienen creencias, deseos y otras representaciones acerca de cosas del mundo real.


##### **Estados mentales y el cerebro en una balde**

Los filósofos fisicalistas han intentado explicar qué significa decir que una persona y, por extensión, una computadora se encuentra en un estado mental particular. Ellos se han centrado en particular en los **estados intencionales**. Estos son estados, como creer, saber, desear, temer, etc., que se refieren a algún aspecto del mundo externo. Si el fisicalismo es correcto, debe darse el caso de que la descripción adecuada del estado mental de una persona esté determinada por el estado cerebral de esa persona. El punto clave es que el mismo estado cerebral no podría corresponder a un estado mental fundamentalmente distinto, como el conocimiento de que uno está haciendo algo.

La simplicidad de este punto de vista es desafiada por experimentos de pensamiento simple. Imagina que tu cerebro es removido de tu cuerpo en el momento del nacimiento y es puesto en una cubeta maravillosa creada por ingeniería. La cubeta mantiene el cerebro, lo que le permite crecer y desarrollarse. Al mismo tiempo señales electrónicas alimentan al cerebro desde una simulación por computadora de un mundo enteramente ficticio, y las señales motoras del cerebro son interceptadas y utilizadas para modificar la simulación según corresponda. De hecho, la vida simulada que vive el cerebro replica exactamente la vida que habría vivido si el cerebro no hubiera sido colocado en la cuba, incluida la acción simulada de hacer algo. Así, esta persona podría tener un estado mental idéntico al de alguien que realmente está haciendo esa acción, pero sería literalmente falso decir que esta persona tiene el estado mental "saber que uno está haciendo algo". Esta persona no está realizando esa acción, nunca experimentó hacer eso, y no podría por lo tanto, tener ese estado mental.

Este ejemplo parece contradecir el punto de vista de que los estados cerebrales determinan los estados mentales. Una forma de resolver este dilema es decir que el contenido de los estados mentales puede ser interpretado desde dos puntos de vista.
El lado del “contenido amplio” lo interpreta desde el punto de vista de un observador externo omnisciente con acceso a toda la situación, que puede distinguir las diferencias en el mundo. Bajo este punto de vista, el contenido de los estados mentales involucra tanto el estado del cerebro como la historia del entorno.
El “contenido estrecho”, por otro lado, considera solo el estado del cerebro. El contenido limitado de los estados cerebrales de una persona real realizando cierta acción y un cerebro en un recipiente que “realiza la acción” es el mismo en ambos casos.

El contenido amplio es completamente apropiado si los objetivos de uno son atribuir estados mentales a otros que comparten el mundo de uno, predecir su comportamiento probable y sus efectos, etc. Este es el entorno en el que ha evolucionado nuestro lenguaje ordinario sobre el contenido mental. Por otro lado, si a uno le preocupa la cuestión de si los sistemas de IA realmente están pensando y realmente tienen estados mentales, entonces el contenido restringido es apropiado; simplemente no tiene sentido decir que si un sistema de IA realmente está pensando o no depende de las condiciones fuera de ese sistema. El contenido limitado también es relevante si estamos pensando en diseñar sistemas de IA o comprender su funcionamiento, porque es el contenido limitado de un estado cerebral lo que determina cuál será el (contenido limitado del) próximo estado cerebral.

##### **El funcionalismo y el experimento del reemplazo cerebral**

La teoría del funcionalismo dice que un estado mental es cualquier condición causal intermedia entre la entrada y la salida. Según la teoría funcionalista, dos sistemas cualesquiera con procesos causales isomórficos tendrían los mismos estados mentales. Por lo tanto, un programa de computadora podría tener los mismos estados mentales que una persona. Por supuesto, todavía no hemos dicho qué significa realmente "isomorfo", pero se supone que existe cierto nivel de abstracción por debajo del cual el la implementación específica no importa.

Las afirmaciones del funcionalismo se ilustran más claramente con el experimento de reemplazo cerebral: supongamos que la neurofisiología se ha desarrollado hasta el punto en que el comportamiento de entrada-salida y la conectividad de todas las neuronas del cerebro humano se entienden perfectamente. Supongamos además que podemos construir dispositivos electrónicos microscópicos que imitan este comportamiento y pueden interconectarse sin problemas con el tejido neural. Por último, supongamos que alguna técnica quirúrgica milagrosa puede reemplazar neuronas individuales con los dispositivos electrónicos correspondientes sin interrumpir el funcionamiento del cerebro como un todo. 

El experimento consiste en reemplazar gradualmente todas las neuronas de la cabeza de alguien con dispositivos electrónicos. Nos preocupamos tanto del comportamiento externo como de la experiencia interna del sujeto, durante y después de la operación. Por la definición del experimento, el comportamiento externo del sujeto debe permanecer sin cambios en comparación con lo que se observaría si la operación no se llevara a cabo. Ahora bien, aunque la presencia o ausencia de conciencia no puede ser fácilmente determinada por un tercero, el sujeto del experimento debe por lo menos ser capaz de registrar cualquier cambio en su propia experiencia consciente.

Aparentemente, hay un choque directo de intuiciones sobre lo que sucedería. Moravec, investigador de robótica y funcionalista, está convencido de que su conciencia no se vería afectada. Searle, un filósofo y naturalista biológico, está igualmente convencido de que su conciencia se desvanecería. Uno no puede hacer más que argumentar desde la intuición.

##### **El naturalismo biológico y la Sala China**

El naturalismo biológico de John Searle (1980) ha planteado un fuerte desafío al funcionalismo, según el cual los estados mentales BIOLÓGICOS son características emergentes de alto nivel que son causadas por procesos físicos de bajo nivel en las neuronas, y son las propiedades (no especificadas) de las neuronas las que importan. Por lo tanto, los estados mentales no se pueden duplicar solo sobre la base de algún programa
teniendo la misma estructura funcional con el mismo comportamiento de entrada-salida; requeriríamos que el programa se ejecutara en una arquitectura con el mismo poder causal que las neuronas.

Para apoyar su punto de vista, Searle describe un sistema hipotético. El sistema consta de un humano, que sólo entiende inglés, equipado con un libro de reglas, escrito en inglés, y varias pilas de papel, algunas en blanco, otras con inscripciones indescifrables. (Por lo tanto, el ser humano desempeña el papel de la CPU, el libro de reglas es el programa y las pilas de papel son el dispositivo de almacenamiento). El sistema está dentro de una habitación con una pequeña abertura hacia el exterior. Por la abertura aparecen papelitos con símbolos indescifrables. El humano encuentra símbolos coincidentes en el libro de reglas y sigue las instrucciones. Las instrucciones pueden incluir escribir símbolos en nuevas tiras de papel, encontrar símbolos en las pilas, reorganizar las pilas, etc. Eventualmente, las instrucciones harán que uno o más símbolos se transcriban en una hoja de papel que se devuelve al mundo exterior.

Hasta aquí todo bien. Pero desde el exterior, vemos un sistema que toma información en forma de oraciones chinas y genera respuestas en chino que son tan "inteligentes" como las de la conversación imaginada por Turing. Searle luego argumenta: la persona en la habitación no entiende chino (dado). El libro de reglas y las pilas de papel, al ser solo pedazos de papel, no entienden chino. Por lo tanto, no hay comprensión del chino. Por lo tanto, según Searle, ejecutar el programa correcto no genera necesariamente comprensión.
Si se le pregunta a la Sala China si entiende chino, la respuesta sería afirmativa (en chino fluido). Según la cortés convención de Turing, esto debería ser suficiente. La respuesta de Searle es reiterar el punto de que la comprensión no está en lo humano y no puede estar en el papel, por lo que no puede haber ninguna comprensión. Parece confiar en el argumento de que una propiedad del todo debe residir en una de las partes. Sin embargo, el agua es mojada, aunque ni el H ni el O2 lo sean. La afirmación real hecha por Searle se basa en la
siguientes cuatro axiomas (Searle, 1990):

1. Los programas de computadora son formales (sintácticos).
2. Las mentes humanas tienen contenidos mentales (semántica).
3. La sintaxis por sí misma no es constitutiva ni suficiente para la semántica.
4. Los cerebros causan mentes.

De los primeros tres axiomas Searle concluye que los programas no son suficientes para las mentes. Del cuarto axioma concluye: “Cualquier otro sistema capaz de causar mentes tendría que tener poderes causales (al menos) equivalentes a los de los cerebros”. De allí infiere que cualquier cerebro artificial tendría que duplicar los poderes causales de los cerebros, no simplemente ejecutar un programa en particular, y que los cerebros humanos no producen fenómenos mentales únicamente en virtud de ejecutar un programa.

En el caso de la Habitación China, Searle se basa en la intuición, no en la prueba: basta con mirar la habitación; ¿Qué demuestra ahí que hay una mente? Pero uno podría hacer el mismo argumento sobre el cerebro: basta con mirar esta colección de células (o de átomos), operando ciegamente de acuerdo con las leyes de la bioquímica (o de la física): ¿Qué demuestra ahí que hay una mente? ¿Por qué un trozo de cerebro puede ser una mente mientras que un trozo de hígado no puede? Ese sigue siendo el gran misterio.

##### **Conciencia, qualia y la brecha explicativa**

A través de todos los debates sobre la IA fuerte está el tema de la conciencia. La conciencia a menudo se divide en aspectos como la comprensión y la autoconciencia. El aspecto en el que nos centraremos es el de la experiencia subjetiva: por qué se siente como algo tener ciertos estados cerebrales (por ejemplo, mientras se come una hamburguesa), mientras que presumiblemente no se siente como algo tener otros estados físicos (por ejemplo,  siendo una roca). El término técnico para la naturaleza intrínseca de las experiencias es qualia (de la palabra latina que significa, más o menos, "tales cosas").

Los qualia presentan un desafío para las explicaciones funcionalistas de la mente porque diferentes qualia podrían estar involucrados en lo que de otro modo serían procesos causales isomórficos. Considere, por ejemplo, el experimento mental del espectro invertido, según el cual la experiencia subjetiva de la persona X al ver objetos rojos es la misma experiencia que experimentamos el resto de nosotros al ver objetos verdes, y viceversa. X todavía llama a los objetos rojos “rojos”, se detiene ante los semáforos en rojo y está de acuerdo en que el rojo de los semáforos en rojo es un rojo más intenso que el rojo del sol poniente. Sin embargo, la experiencia subjetiva de X es simplemente diferente.

El propio Turing reconoce que la cuestión de la conciencia es difícil, pero niega que tenga mucha relevancia para la práctica de la IA: “No quiero dar la impresión de que creo que la conciencia no tiene ningún misterio. . . Pero no creo que estos misterios necesariamente deban ser resueltos antes de que podamos responder la pregunta que nos ocupa en este artículo”.


#### **LA ÉTICA Y LOS RIESGOS DEL DESARROLLO DE LA INTELIGENCIA ARTIFICIAL**

Hasta ahora, nos hemos concentrado en si podemos desarrollar IA, pero también debemos considerar si debemos hacerlo. Si es más probable que los efectos de la tecnología de IA sean negativos que positivos, entonces sería responsabilidad moral de los trabajadores en el campo redirigir su investigación. Todos los científicos e ingenieros enfrentan consideraciones éticas sobre cómo deben actuar en el trabajo, qué proyectos deben o no deben realizarse y cómo deben manejarse. Sin embargo, la IA parece plantear algunos problemas nuevos más allá de, por ejemplo, construir puentes que no se caen:

- Las personas podrían perder sus trabajos debido a la automatización.
- Las personas pueden tener demasiado (o muy poco) tiempo libre.
- Las personas pueden perder su sentido de ser únicas.
- Los sistemas de IA pueden usarse para fines no deseados.
- El uso de sistemas de IA podría resultar en una pérdida de responsabilidad.
- El éxito de la IA podría significar el fin de la raza humana.

Veremos cada tema por separado.

**Las personas podrían perder sus trabajos debido a la automatización**. La economía industrial moderna se ha vuelto dependiente de las computadoras en general y de ciertos programas de inteligencia artificial en particular. Hasta ahora, la automatización a través de la tecnología de la información en general y la IA en particular ha creado más empleos de los que ha eliminado, y ha creado empleos más interesantes y mejor pagados. Ahora que el programa canónico de IA es un "agente inteligente" diseñado para ayudar a un humano, la pérdida de empleos es menos preocupante que cuando la IA se enfocaba en "sistemas expertos" diseñados para reemplazar a los humanos.

**Las personas pueden tener demasiado (o muy poco) tiempo libre**. Alvin Toffler escribió en Future Shock (1970): “La semana laboral se ha reducido en un 50 por ciento desde el cambio de siglo. No está fuera de lugar predecir que se reducirá a la mitad nuevamente para el año 2000”. Arthur C. Clarke (1968b) escribió que las personas en 2001 podrían “enfrentarse a un futuro de absoluto aburrimiento, donde el principal problema en la vida es decidir cuál de varios cientos de canales de televisión seleccionar”.
La única de estas predicciones que ha estado cerca de cumplirse es la cantidad de canales de televisión. En cambio, las personas que trabajan en industrias intensivas en conocimiento se han encontrado a sí mismas como parte de un sistema computarizado integrado que opera las 24 horas del día; para mantenerse al día, se han visto obligados a trabajar más horas. La IA aumenta el ritmo de la innovación tecnológica y, por lo tanto, contribuye a esta tendencia general, pero la IA también promete permitirnos tomarnos un tiempo libre y dejar que nuestros agentes automatizados se encarguen de las cosas por un tiempo.

**Las personas pueden perder su sentido de ser únicas**. Weizenbaum (1976), autor del programa ELIZA, señala algunas de las amenazas potenciales que la IA representa para la sociedad. Uno de los principales argumentos de Weizenbaum es que la investigación de la IA hace posible la idea de que los humanos son autómatas, una idea que resulta en una pérdida de autonomía o incluso de humanidad. La IA, si bien tiene un gran éxito, puede ser tan amenazante para los supuestos morales de la sociedad del siglo XXI como lo fue la teoría de la evolución de Darwin para los del siglo XIX.

**Los sistemas de IA podrían usarse para fines no deseados**. Los poderosos a menudo han utilizado tecnologías avanzadas para reprimir a sus rivales. Los sistemas autónomos de IA ahora son comunes en el campo de batalla. Una teoría moral sostiene que los robots militares son como armaduras medievales llevadas a su extremo lógico: nadie tendría objeciones morales a que un soldado quisiera usar un casco cuando es atacado por enemigos grandes, enojados y armados con hachas, y un robot teleoperado es como una forma muy segura de armadura. Por otro lado, las armas robóticas presentan riesgos adicionales. En la medida en que la toma de decisiones humanas se elimine del circuito de disparos, los robots pueden terminar tomando decisiones que conduzcan a la muerte de civiles inocentes.
Weizenbaum (1976) también señaló que la tecnología de reconocimiento de voz podría conducir a escuchas telefónicas generalizadas y, por lo tanto, a una pérdida de libertades civiles. Su predicción se ha hecho realidad en parte: el Reino Unido ahora tiene una extensa red de cámaras de vigilancia, y otros países monitorean rutinariamente el tráfico web y las llamadas telefónicas.

**El uso de sistemas de IA podría resultar en una pérdida de responsabilidad**. Hasta donde sabemos, a ningún programa se le ha otorgado estatus legal como individuo para fines de transacciones financieras; en la actualidad, parece irrazonable hacerlo. Los programas tampoco se consideran "impulsores" a los efectos de hacer cumplir las normas de tránsito en carreteras reales. En la ley de California, al menos, no parece haber ninguna sanción legal para evitar que un vehículo automatizado exceda los límites de velocidad, aunque el diseñador del mecanismo de control del vehículo sería responsable en caso de accidente. Al igual que con la tecnología reproductiva humana, la ley todavía tiene que ponerse al día con los nuevos desarrollos.

**El éxito de la IA podría significar el fin de la raza humana**. Casi cualquier tecnología tiene el potencial de causar daño en las manos equivocadas, pero con la IA y la robótica, tenemos el nuevo problema de que las manos equivocadas pueden pertenecer a la misma tecnología. La pregunta es si un sistema de IA plantea un riesgo mayor que el software tradicional. Examinaremos tres fuentes de riesgo.
Primero, la estimación del estado del sistema de IA puede ser incorrecta, lo que hace que haga lo incorrecto. La forma correcta de mitigar estos riesgos es diseñar un sistema con controles y equilibrios para que un solo error de estimación de estado no se propague a través del sistema sin control.
En segundo lugar, especificar la función de utilidad correcta para que un sistema de IA maximice no es tan fácil. Entonces, con los sistemas de IA, debemos tener mucho cuidado con lo que pedimos, mientras que los humanos no tendrían problemas para darse cuenta de que la función de utilidad propuesta no se puede tomar literalmente.
En tercer lugar, la función de aprendizaje del sistema de IA puede hacer que se convierta en un sistema con un comportamiento no deseado. No podemos simplemente darle a un programa una función de utilidad estática, porque las circunstancias y nuestro deseo
las respuestas a las circunstancias, cambian con el tiempo.

2. 

El mapa mental se encuentra en el archivo "Fundamentos Filosóficos.xmind"


3. 

#### **Conclusión personal**

En este capítulo se definen dos puntos de vista bien definidos acerca de la inteligencia artificial, como también los riesgos y ética que hay que considerar al desarrollarla.
En cuanto a la inteligencia artificial fuerte, hay varios aspectos filosóficos importantes que entran en juego y que considero que hacen que no sea posible que exista como tal la idea de máquinas con mentes propiamente dichas, capaces de sentir y pensar al nivel que lo hacen los humanos, el más importante creo que es el hecho de la conciencia en sí, las máquinas no son conscientes de su propia existencia, siguen reglas e infieren a partir de una base dada por los desarrolladores, se podría decir que no tienen la singularidad que nos caracteriza. Como se habla en el experimento del cerebro en el recipiente, suponiendo que en algún momento se pueda construir una máquina idéntica al cerebro, la máquina puede tener ciertos “estados mentales” pero carece de una experiencia real de la vida. Además, fuera de estos pensamientos filosóficos, no le veo realmente una funcionalidad a una máquina que simule una mente, creo que el objetivo del desarrollo de la IA tiene un enfoque más parecido al de la hipótesis de la IA débil, es decir, máquina capaces de actuar inteligentemente, otra vez esta hipótesis queda atada a la definición de lo que se considera inteligente, por lo que yo opino, con que sea capaz de realizar una tarea automáticamente, o sea una herramienta para analizar información de montones de datos y ayudar a la toma de decisiones de los humanos se podría considerar inteligente.
En cuanto a los riesgos que puede tener desarrollar IA, no veo mucha diferencia al riesgo que tiene cualquier innovación tecnológica, desde el uso del fuego en la prehistoria, pasando por las armas de destrucción masiva como lo son las bombas nucleares, hasta los inventos en la actualidad, cada invención creada por humanos ha sido una potencial causa de terminar con la vida y como toda herramienta, puede ser un peligro según quien la utilice y para que fines, pero eso supongo que ha pasado y va a pasar con todo lo que desarrollamos. En cuanto a la amenaza para el trabajo, ninguna invención ha despojado a los seres humanos de realizar tareas, más bien creo que cambia el paradigma de lo que es un trabajo. Si coincido en que habría que analizar ciertos vacíos legales que trae esta tecnología pero lejos está de ser la razón del fin de la raza humana.
