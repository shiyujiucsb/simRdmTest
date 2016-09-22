set terminal postscript eps font 'Helvetica, 24'
set output 'simrank_gplus_apprx_error.eps'

set xlabel '# samples'
set yrange [0:.4]
#set xtic 2000
plot 'simrank_gplus_apprx_error_n344.txt' using 1:2 title 'MaxError' with linespoints pt 3, \
	'simrank_gplus_apprx_error_n344.txt' using 1:3 title 'Delta' with linespoints pt 5
	
set term windows
set output
