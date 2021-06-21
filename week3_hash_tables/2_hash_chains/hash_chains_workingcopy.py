# python3
from collections import deque

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count   
        self.elems = [ deque()  for _ in range(self.bucket_count)]
        

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count
 
    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        
        def _check_same_hashed_exist(que):
            if len(self.elems[que])==0:
                return False
            else:
                return True
        if query.type == "check":
            # use reverse order, because we append strings to the end
            if _check_same_hashed_exist(query.ind) == True:
                chain = []
                for _ in self.elems[query.ind]:
                    chain.append(_)
                self.write_chain(chain)
            else:
                print('')
        else:
            cur_h = self._hash_func(query.s)
            if query.type == 'find':
                if _check_same_hashed_exist(cur_h) == True:
                    if query.s in self.elems[cur_h]:
                        print('yes')
                    else:
                        print('no')
                else:
                    print('no')
            elif query.type == 'add':
                if _check_same_hashed_exist(cur_h) == True:
                    if query.s in self.elems[cur_h]:
                        pass
                    else:
                        self.elems[cur_h].appendleft(query.s)
                else:
                    self.elems[cur_h].appendleft(query.s)
            elif query.type =='del':
                if _check_same_hashed_exist(cur_h) == True:
                    if query.s in query.elems[cur_h]:
                        pass
                    else:
                        if self.elems[cur_h][0]==query.s:
                            self.elems[cur_h].popleft()
                        elif self.elems[cur_h][-1]==query.s:
                            self.elems[cur_h].pop()
                        else:
                            newque = deque()
                            for _ in self.elems[cur_h]:
                                if self.elems[cur_h][_]!=query.s:
                                    newque.append(_)
                            self.elems[cur_h] = newque
                else:
                    if self.elems[cur_h][0]==query.s:
                        self.elems[cur_h].popleft()
                    elif self.elems[cur_h][-1]==query.s:
                        self.elems[cur_h].pop()
                    else:
                        newque = deque()
                        for _ in self.elems[cur_h]:
                            if self.elems[cur_h][_]!=query.s:
                                newque.append(_)
                        self.elems[cur_h] = newque
                    
             #cur_h = _hash_func(query.s)
            #if _check_same_hashed(cur_h) == 0:
            #    print('not in db')
            # try:
            #     ind = self.elems.index(query.s)
            # except ValueError:
            #     ind = -1
            # if query.type == 'find':
            #     self.write_search_result(ind != -1)
            # elif query.type == 'add':
            #     if ind == -1:
            #         self.elems.append(query.s)
            # else:
            #     if ind != -1:
            #         self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()