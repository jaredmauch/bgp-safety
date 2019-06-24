#!/usr/bin/python3


def block_majornets(peer_asn)

    # adjust this as appropriate for your use case
    major_network = [209, 2914, 701, 7018, 2828, 3356, 
        174, 1239, 1668, 3561, 3549, 3320, 5511,
        6461, 6453, 1299, 3257, 3491, 7922,
        7015, 7016, 7725, 13367, 20214, 21508, 22258, 22909, 
        33287, 33489, 33490, 33491, 33650, 33651, 33652, 33653, 
        33654, 33655, 33656, 33657, 33659, 33660, 33661, 33662, 
        33664, 33665, 33666, 33667, 33668, 36732, 36733]
    #
    for temp_asn in major_network:
        if temp_asn != peer_asn:
            print(" deny as-path _%d_" % temp_asn)
    #
    


    


