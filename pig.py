#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Pig Dice Game"""

import random


class Die(object):
    def __init__(self):
        self.die = 0

    def roll(self):
        self.die = random.randint(1, 6)
        return self.die


class Player(object):
    def __init__(self, player):
        self.player = ''
        self.turn_score = 0
        self.turn = True

    def throw(self):
        die = Die()
        rolled = die.roll()
        if rolled != 1:
            self.turn_score += rolled
        else:
            self.turn_score = 0
            self.turn = False
        return rolled

class Game(object):
    def __init__(self, players):
        self.players = players
        self.player_index = {n: Player(n) for n in self.players}
        self.scores = {n: 0 for n in self.players}
        self.max_score = 100
        self.high_score = 0
        self.starter = None
        self.next_player = None
        self.toss()

        while self.max_score > self.high_score:
            print '\n'
            print '{}, your score is {}.'.format(self.next_player, self.scores[self.next_player])
            print '{}, it is now your turn to roll: '.format(self.starter)
            print '{}, your score is {}.'.format(self.starter, self.scores[self.starter])
            choice = raw_input('roll or hold? ( r or h ): ').lower()
            if choice == 'r':
                rolled = self.player_index[self.starter].throw()
                player_total = self.scores[self.starter] + self.player_index[self.starter].turn_score
                round_score = self.player_index[self.starter].turn_score
                player_score = self.scores[self.starter]
                player = self.starter
                if rolled == 1:
                    print '\n'
                    print 'You rolled a 1, you score nothing.'
                    print '{}, it is now your turn to roll: '.format(self.next_player)
                    print '\n'
                    self.turn_score = 0
                    self.turn_pass()
                    print '{} your score is {}.'.format(player, player_total)
                    continue
                elif player_total > self.max_score:
                    print '{} lost your score is {}.'.format(player, player_total)
                    break
                else:
                    print '{} You rolled {}, and round score is {}.'.format(player, rolled, round_score)
                    print '\n'
                    print 'If you hold your score will be {}'.format(player_total)
            elif choice == 'h':
                player_score = self.scores[self.starter]
                player = self.starter
                player_total = player_score + self.player_index[self.starter].turn_score
                if player_total == self.max_score:
                    print 'Congratulations {} you the winner with a score of {}.'.format(player, 100)
                    break
                elif player_total > self.max_score:
                    print 'Sorry {} you lost, with score of {}.'.format(self.starter, player_total)
                    break
                else:
                    self.scores[self.starter] = player_total
                    self.player_index[self.starter].turn_score = 0
                    self.player_index[self.starter].turn = False
                    self.turn_pass()
            else:
                continue

    def toss(self):
        toss = random.choice(self.players)
        toss = self.players.index(toss)
        if toss == 0:
            self.starter = self.players[0]
            self.next_player = self.players[1]
        else:
            self.starter = self.players[1]
            self.next_player = self.players[0]

    def turn(self):
        pass

    def turn_pass(self):
        hold_player = self.starter
        self.starter = self.next_player
        self.next_player = hold_player


if __name__ == '__main__':
    pig = Game(['Player1', 'Player2'])
