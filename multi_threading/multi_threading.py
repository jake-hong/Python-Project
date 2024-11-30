"""
Multithreading 
스레드와 프로세스의 차이, GIL

1) 프로세스
- 운영체제에서 할당받는 자원의 단위(실행중인 프로그램)
- CPU 동작 시간, 주소공간은 독립적이다.
- code, data, stack, heap 영역이 독립적이다.
- 최소 1개의 메인 스레드를 보유한다. 
- 파이프, 파일, 소켓 등을 사용해서 프로세스 간 통신이 가능하다.(cost가 높음)
- Context Switching 비용에 대한 고려필요.

2) 스레드
 - 프로세스 내에서 실행 흐름 단위 
 - 프로세스의 자원을 사용한다. 
 - stack만 별도로 할당하고, 나머지는 공유한다.(code, data, heap)
 - 메모리를 공유한다(변수를 공유)
 - 한 스레드의 결과가 다른 스레드의 영향을 끼친다.
 - 동기화 문제는 주의해야한다. (디버깅이 어려움)

3) 멀티 스레드
- 한 개의 단일 어플리케이션은 여러스레드로 구성 후 작업 처리 
- 시스템 자원 소모가 감소된다.(효울성), 처리량이 증가됨.(cost 감소)
- 통신 부담이 감소되고, 디버깅은 어려워진다.단일 프로세스에는 효과가 약함.
- 자원 공유 문제가 발생한다.(교착상태)
- 프로세스에 영향을 줄 수 있다. 

4) 멀티 프로세스
- 한 개의 단일 어플리케이션을 여러 프로세스로 구성 후 작업 처리 
- 한 개의 프로세스 문제 발생은 확산이 없다. (process kill)
- 캐시 체인지를 활용함(cost 비용이 매우 높음- overhead)
- 복잡한 통신 방식

5) GIL(Global Interpreter Lock)
- Cpython이 python(bytecode) 실행 시 여러 thread를 사용할 경우 하나의 단일 스레드만 python object에 접근하도록 or 사용하도록 제한을 건 것. 
- Cpython 메모리 관리가 취약해서..(thread-safe를 위해 GIL을 검)
- 단일 스레드도 충분히 빠르다. 
- 멀티 프로세스도 사용 가능(Numpy/scipy) 
- 병렬 처리는 multiprocessing을 쓰면 됨. asyncio를 써도 됨.
- thread 동시성을 완벽하게 처리하기 위한 Jython, IronPython, stackelss python 등이 있음.
"""

"""
Python Thread

thread는 main area와 상관 없이 sub thread의 일이 끝나야 끝남.
"""
import logging
import threading
import time


def thread_func(name):
    logging.info(f"Sub-Thread {name}: start")
    time.sleep(2)
    logging.info(f"Sub-Thread {name}: finish")
    
# main area
if __name__ == "__main__":
    # logging format
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-thread: before create thread")
    
    thread = threading.Thread(target=thread_func, args= ("First",))
    logging.info("Main-Thread: before run thread")
    
    # start sub-thread 
    thread.start()
    
    #join()을 추가하면 sub thread가 먼저 끝날때까지 기다림
    thread.join()
    
    logging.info("Main-Thread: wait for the thread to finish")
    logging.info("Main-Thread: all done")
