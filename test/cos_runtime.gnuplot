set terminal postscript eps font 'Helvetica, 24'
set output 'cos_runtime.eps'

set xlabel '# samples'
#set yrange [0:2000]
#set ytic 200
plot 'cos_arxiv_runtime.txt' using 1:2 title 'Cit-HepPh' with linespoints pt 3, \
	'cos_email_runtime.txt' using 1:2 title 'Email-Enron' with linespoints pt 4
	
set term x11
set output
