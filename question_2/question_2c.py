""" Question 2c

    Brief analysis about why use inheritance in this situation:

        In this situation, 
        since we only use a component which is Account it is enough to use inheritance rather than composition.

        The DevAccount are basically similar in many sense to Account class itself, the properties changes and new methods are just extension
        to the Account class

        Testing done on DevAccount class could be adapted to StagingAccount the ProdClass

        No major changes to parent properties or addition to it, just defaulting new created DevAccount instance's balance to 0.

"""