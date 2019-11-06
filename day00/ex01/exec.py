# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fgaribot <fgaribot@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 14:49:43 by fgaribot          #+#    #+#              #
#    Updated: 2019/11/06 15:13:53 by fgaribot         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#argecho.py

import sys

def usage():
	print("Merci")

def main(argv):
	grammar = "exec.py"
	try:
		opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)

if __name__ == "__main__":
	main(sys.argv[1:])
