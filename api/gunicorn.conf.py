import multiprocessing

bind            = "0.0.0.0:8000"
reload          = True
#worker_tmp_dir  = '/dev/shm'
workers         = multiprocessing.cpu_count() * 2 + 1
threads         = 4
worker_class    = 'gthread'
accesslog       = '-'
errorlog        = '-'
log_level       = 'info'
