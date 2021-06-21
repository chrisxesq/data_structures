class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def process_queries(queries, contacts):
    res=''  
    if q.type == 'add':
      contacts[q.number] = q.name
    elif q.type == 'del':
      try:
        del contacts[q.number]
      except:
        pass
    elif q.type == 'find':
        if q.number in contacts.keys():
          res = contacts[q.number]
        else:
          res = 'not found'
    return res

if __name__ == '__main__':
    contacts={}
    n_queries = int(input())
    for _ in range(n_queries):
      q = Query(input().split())
      ans =process_queries(q, contacts)
      if ans != '':
        print(ans)