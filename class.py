class camera:

    def __init__ (self, scan, record, takepic):
        self.scan = scan
        self.record = record
        self.takepic = savepic

class arduino:

    def __init__ (self, left, right, up, down):
        self.left = left
        self.right = right
        self.up = up
        self.down = down

class ping:

    def __init__(self, sentsignal, timeout, receivedsignal):
        self.sentsignal = sentsignal
        self.timeout = timeout
        self.receivedsignal = receivedsignal

    def areyoualive(self, ):
        print("Are you alive? : " + self.receivedsignal)

