from xmlrpc.server import SimpleXMLRPCServer

class Forecast(object):
    """
    Reprezentuje predpoved. V instancnich promennych jsou reprezentovany hodnoty
    predpovedi.
    """

    def __init__(self, description, wind_force, temperature):
        """
        TODO [0.5 b] Konstuktor predpovedi. Instancni promenne reprezentuji predana data.
        """
        self.description = description; self.wind_force = wind_force; self.temperature = temperature

    def get_list(self):
        """
        TODO [0.5 b] Vraci trojici reprezentujici predpoved.
        """
        return (self.description,self.wind_force,self.temperature)
        

class ForecastCalendar(object):
    """
    Reprezentuje predpovedi pro nekolik dni. Data predpovedi jsou ulozena ve
    slovniku. Klicem je datum, hodnotou pak instance tridy Forecast. Vkladani
    predpovedi metodou update_forecast je chraneno heslem, ktere je predano v
    konstruktoru. Startovaci data jsou tektez predana v konstruktoru.
    """
    
    def __init__(self, initial_values, password):
        """
        TODO [1 b] Konstruktor kalendare predpovedi. Instancni promenne reprezentuji predana data.
        Provedte kontrolu zda initial_values je datovy typ slovnik (dict), pokud neni, tak nastavit
        prazdny slovnik.
        TODO [0.5. b] Provedte kontrolu prvku v initial_values, ze jsou jeho prvky skutecne 
        datoveho typu Forecast. Ty co nejsou, tak nebudou vlozeny do instance (odfiltruji se).
        """

        if(type(initial_values) is dict):
            for item in list(initial_values):
                if(type(initial_values[item]) is not Forecast):
                    initial_values.pop(item)
            self.initial_values = initial_values    
        else:
            self.initial_values = dict()
        self.password = password
        

    def get_forecast(self, date):
        """
        TODO [1 b] Vrati predpoved pro zadane datum jako retezec. V pripade, ze pro dane
        datum neexistuje predpoved. Vrati se retezec "No focecast".
        """
        return self.initial_values.get(date, "No forecast")

    def update_forecast(self, password, date, description, wind_force, temperature):
        """
        TODO [1 b] Aktualizuje predpoved pro zadane datum. Akce je chranena heslem. Pokud
        heslo nesouhlasi s heslem, ktere je zadano v konstruktoru, neni mozno
        aktualizovat predpoved. v takovm priapde metoda vrati retezec "No
        update". Metoda muze aktualizovat stavajici predpoved nebo pridat novou.
        """
        if(password == self.password):
            self.initial_values[date] = Forecast(description, wind_force, temperature)
            return "Updated"
        else:
            return "No update"
        
def main():

    """
    TODO [0.5 b] Pridat do initial_state data predpovedi tak, aby je mohl klient
    precist.
    """
    initial_state = {}
    initial_state["20017-11-05"] = Forecast("raining",30,13)
    initial_state["20017-11-06"] = Forecast("snowing",7.12,15)
    initial_state["20017-11-08"] = Forecast("sunny",8.33,22)

    fcalendar = ForecastCalendar(initial_state, password = "master-of-weather")

    #fcalendar.update_forecast("master-of-weather","20017-11-05","raining",30,13)
    #fcalendar.update_forecast("master-of-weather","20017-11-06","foggy",27.3,15)
    #fcalendar.update_forecast("master-of-weather","20017-11-07","snowing",7,12.9)
    #fcalendar.update_forecast("master-of-weather","20017-11-08","sunny",3.55,22)

    server_address = ('localhost', 10001)
    server = SimpleXMLRPCServer(server_address)
    server.register_instance(fcalendar)
    server.register_introspection_functions()
    print("Starting Weather XML-RPC server, use <Ctrl-C> to stop")
    server.serve_forever()

if __name__ == "__main__":
    main()
