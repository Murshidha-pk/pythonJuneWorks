class vehicle:

    def start(self):

        print("vehicle start method")

    def accelerate(self):

        print("vehicle accelarate method")

class swift(vehicle):

    pass

swift_instance=swift()

swift_instance.accelerate()

swift_instance.start()