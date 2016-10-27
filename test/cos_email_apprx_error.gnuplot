set terminal postscript eps font 'Helvetica, 24'
set output 'cos_email_apprx_error.eps'

set xlabel '# samples'

plot 'cos_email_apprx_error_36697.txt' using 1:2 title 'MaxError' with linespoints pt 3, \
	'cos_email_apprx_error_36697.txt' using 1:3 title 'Delta' with linespoints pt 4	
set term epslatex
set output
