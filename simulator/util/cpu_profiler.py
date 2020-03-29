import os
import sys


_profiler = None



def profiler_start(profile_threads=True):
    global _profiler
    import yappi

    if _profiler is not None:
        _profiler.clear_stats()
        _profiler.stop()

    _profiler = yappi

    yappi.start(profile_threads=profile_threads)


# noinspection PyProtectedMember,SpellCheckingInspection
def profiler_print(n=25, out=sys.stdout):
    writeLn = lambda s : (out.write(s), out.write(os.linesep))

    yappi_ = _profiler
    from yappi import YFuncStats
    func_stats: YFuncStats = yappi_.get_func_stats()
    columns = {0: ("name", 42), 1: ("ncall", 5), 2: ("tsub", 8), 3: ("ttot", 8), 4: ("tavg", 8)}

    writeLn('CPU profile by ttot:')
    func_stats.sort('ttot')._print_header(out, columns)
    for stat in func_stats[0:n]:
        stat._print(out, columns)
    writeLn('')

    writeLn('CPU profile by tsub:')
    func_stats.sort('tsub')._print_header(out, columns)
    for stat in func_stats[0:n]:
        stat._print(out, columns)
    writeLn('')

    out.flush()


def profiler_clear(print_stats=False):
    if _profiler is not None:
        if print_stats:
            profiler_print()
        _profiler.clear_stats()
        # logger.info('CPU profiler cleared!')
