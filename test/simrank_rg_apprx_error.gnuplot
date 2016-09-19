set terminal postscript eps font 'Helvetica, 24'
set output 'simrank_rg_apprx_error.eps'

set yrange [0:.4]
set xtic 2000
set xlabel '# samples'
set ytic .05
plot 'simrank_rg_apprx_error.txt' using 1:2 title 'MaxError' with linespoints pt 3, \
	'simrank_rg_apprx_error.txt' using 1:3 title 'Delta' with linespoints pt 5
	
set term x11
set output
