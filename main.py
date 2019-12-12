import pygame
import csv

pygame.init()

screen = pygame.display.set_mode((1366, 768))

pygame.display.set_caption("Dinâmica Molecular")

playerImg = pygame.image.load('molecule6.png')


def player(*args):
    for x, y in args[0]:
        screen.blit(playerImg, (x * 1000000000000, y * 190000000000))
    pygame.display.update()
    screen.fill((0, 0, 0))

with open('position.csv') as atom_file:
    atoms = csv.reader(atom_file, delimiter=';')

    atom_name_list = ['ATOM: {}'.format(i) for i in range(400)]
    atom_dict = dict()

    [atom_dict.update({name: list()})for name in atom_name_list]

    for atom in atoms:
        if atom[1] in atom_name_list:
            atom_dict[atom[1]].append((float(atom[2].replace('posX: ', '')),
                                      float(atom[3].replace('posY: ', ''))))

    atom_matrix = atom_dict.values()

    while True:
        for i in range(500):
            atom_list = list()
            for atom in atom_matrix:
                atom_list.append(atom[i])

            player(atom_list)