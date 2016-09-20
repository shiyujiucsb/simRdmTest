set terminal postscript eps font 'Helvetica, 24'
set output 'simrank_runtime.eps'

set xlabel '# samples'
#set yrange [0:2000]
#set ytic 200
plot 'simrank_gplus_runtime.txt' using 1:2 title 'ego-Gplus' with linespoints pt 3, \
	'simrank_twitter_runtime.txt' using 1:2 title 'ego-Twitter' with linespoints pt 4
	
set term x11
set output
