set terminal postscript eps font 'Helvetica, 24'
set output 'cos_normal_apprx_error.eps'

set xlabel '# samples'
set yrange [0:1000]
set ytic 100
plot 'cos_normal_apprx_error.txt' using 1:2 title 'MaxError' with linespoints pt 3, \
	'cos_normal_apprx_error.txt' using 1:3 title 'Improved' with linespoints pt 4, \
	'cos_normal_apprx_error.txt' using 1:4 title 'Delta' with linespoints pt 5
	
set term x11
set output
