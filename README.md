# TPOS_MIPT


###Ansible

\documentclass{article}
\usepackage{enumitem}

\begin{document}

\section*{Алгоритм тестирования:}

\begin{enumerate}[label=\arabic*.]
  \item Запустить виртуальную машину с Vagrant и выполнить Ansible-скрипт.
  \item Проверить, что при запросе \texttt{GET /service\_data} получены начальные данные.
  \item Подождать более 1 минуты и проверить обновление \texttt{uptime}.
  \item Повторно выполнить Ansible-скрипт и убедиться, что \texttt{uptime} не сброшен и Nginx не перезапущен.
  \item Изменить первую строку в \texttt{service\_state}, повторно выполнить Ansible и проверить обновление файла и рестарт Nginx.
  \item Подождать более 1 минуты и проверить, что \texttt{uptime} обновлен.
\end{enumerate}

\end{document}

