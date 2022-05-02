##
## EPITECH PROJECT, 2021
## B-MAT-500-COT-5-1-301dannon-mohamed.mazu
## File description:
## Makefile
##

NAME	=	304pacman

all:	$(NAME)

$(NAME):
		ln -s 304pacman.py $(NAME)
		chmod +x $(NAME)

clean:
		rm -rf *~
		rm -rf __pycache__

fclean:	clean
		rm -rf $(NAME)

re:	fclean all
