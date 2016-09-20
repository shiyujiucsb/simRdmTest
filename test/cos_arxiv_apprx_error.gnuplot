set terminal postscript eps font 'Helvetica, 24'
set output 'cos_arxiv_apprx_error.eps'

set xlabel '# samples'
set yrange [0:2000]
set ytic 200
plot 'cos_arxiv_apprx_error_34551.txt' using 1:2 title 'MaxError' with linespoints pt 3, \
	'cos_arxiv_apprx_error_34551.txt' using 1:3 title 'Improved' with linespoints pt 4, \
	'cos_arxiv_apprx_error_34551.txt' using 1:4 title 'Delta' with linespoints pt 5
	
set term x11
set output
