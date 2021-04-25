try:
   from termcolor import colored
except ImportError:
    import pip
    failed = pip.main(["install", 'colored'])
    
import random



def unreliable_transmission(frame, prob):
    original_frame = frame
    count_error_bit = 0
    print('Original frame {:<40}'.format(original_frame))
    for i in range(100):
        frame = list(original_frame)
        for j in range(len(frame)):
            p = random.uniform(0,1)
            #p more then prob then no bit error
            if p > prob:
                pass
            else: #
                if frame[j] == '1':
                    frame[j] = colored('0','red')
                else:
                    frame[j] = colored('1','red')
                count_error_bit += 1
        
        print('Sending bit.. ',''.join(frame));
    print("** NOTE bit red is change bit")
    print("total error bit occur",count_error_bit)
        
