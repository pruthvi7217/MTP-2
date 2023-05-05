"""
# class Batcher:
#     def __init__(self,
#                     folder='/home/rs/19CS91R05/DarKSkuLL/BI/Anguli_200k_1M',
#                     ext='*.tiff',
#                     batch_size=1000
#                 ) -> iter:
#         self.folder=folder
#         self.ext=ext
#         self.batch_size=1000
#         self.proc_count=cpu_count()-1
#         self.batch = iter()

#     # def
#     def __call__(self, ) -> iter:
#         return next(self.batch)
"""
from multiprocessing import Pool
from os import cpu_count
from time import strftime


def dprint(func):
    def wrapped_func(*args, **kwargs):
        return func(strftime("%H:%M:%S - "),*args,**kwargs)
    return wrapped_func

print = dprint(print)

class Parallel:
    def __init__(self) -> object:
        print("Parallel Instance Created")
    def __call__(
        self, atomic_function, paths, batch=100, chunksize=10, free_core=1
    ) -> dict:
        ctr = done = 0
        doc_list = []
        with Pool(cpu_count() - free_core - 1) as p:
            try:
                for doc in p.imap(atomic_function, paths, chunksize):
                    try:
                        if doc:
                            try:
                                # db_client.insert_one(doc)
                                doc_list.append(doc)
                            except Exception as e:
                                print(str(e))
                            ctr += 1
                            done += 1
                            if ctr == batch:
                                yield doc_list
                                print(f"{done}/{len(paths)} documents processed")
                                ctr = 0
                                doc_list = []
                    except Exception as e:
                        print(str(e))
                        
                if len(doc_list):
                    yield doc_list
            except Exception as e:
                print(str(e))
