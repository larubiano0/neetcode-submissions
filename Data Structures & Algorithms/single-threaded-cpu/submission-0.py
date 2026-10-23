class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        order = []
        augment_tasks = [tasks[i]+[i] for i in range(len(tasks))]
        augment_tasks = sorted(augment_tasks, key = lambda k: k[0])
        available = []
        t = 1
        while augment_tasks or available:
            last = -1
            for i in range(len(augment_tasks)):
                if augment_tasks[i][0]<=t:
                    last = i
                else:
                    break
            if last>=0:
                available += augment_tasks[:last+1]
                augment_tasks = augment_tasks[last+1:]
            # choose 
            if not available:
                t=augment_tasks[0][0]
                continue
            else:
                # pick min 
                available = sorted(available, key = lambda k: k[1])
                min_time = available[0][1]
                min_time_ind = []
                for i in range(len(available)):
                    if available[i][1] == min_time:
                        min_time_ind.append(available[i])
                    else:
                        break
                # sort by ind
                min_time_ind = sorted(min_time_ind, key = lambda k: k[2])
                index_of_element = available.index(min_time_ind[0])
                available.pop(index_of_element)
                t+=min_time_ind[0][1]
                order.append(min_time_ind[0][2])
        return order

                        
