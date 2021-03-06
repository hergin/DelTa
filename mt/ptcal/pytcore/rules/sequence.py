'''*****************************************************************************
AToMPM - A Tool for Multi-Paradigm Modelling

Copyright (c) 2011 Eugene Syriani

This file is part of AToMPM.

AToMPM is free software: you can redistribute it and/or modify it under the
terms of the GNU Lesser General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later 
version.

AToMPM is distributed in the hope that it will be useful, but WITHOUT ANY 
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along
with AToMPM.  If not, see <http://www.gnu.org/licenses/>.
*****************************************************************************'''

from ..tcore.composer import Composer


class Sequence(Composer):
    '''
        Applies each rule in the order provided.
    '''
    def __init__(self, rules):
        '''
            Applies each rule in the order provided.
            @param rules: The rules to apply.
        '''
        super(Sequence, self).__init__()
        self.rules = rules
    
    def packet_in(self, packet):
        self.exception = None
        self.is_success = False
        for rule in self.rules:
            packet = rule.packet_in(packet)
            packet.clean()
            if not rule.is_success:
                if rule.exception is not None:
                    self.exception = rule.exception
                return packet
        self.is_success = True
        return packet
