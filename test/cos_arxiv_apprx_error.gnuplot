set terminal postscript eps font 'Helvetica, 24'
set output 'cos_arxiv_apprx_error.eps'

set xlabel '# samples'

plot 'cos_arxiv_apprx_error_34551.txt' using 1:2 title 'MaxError' with linespoints pt 3, \
	'cos_arxiv_apprx_error_34551.txt' using 1:3 title 'Delta' with linespoints pt 4, \
	
set term epslatex
set output
