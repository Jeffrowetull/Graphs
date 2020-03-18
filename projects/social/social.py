import itertools, random
from util import Queue
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        
        # Add users
        for x in range(num_users):
            self.add_user(f'User {x+1}')
        # Create friendships
        possible_friendships = list(itertools.combinations(range(1,num_users+1),2))
        random.shuffle(possible_friendships)
        friend_num = num_users*avg_friendships//2
        print(friend_num)
        new_friends = possible_friendships[:friend_num]
        print('hi',new_friends)
        for bond in new_friends:
            self.add_friendship(bond[0],bond[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        #definitely a searchy sort of thing, probably bfs because we want the shortest paths
        q = Queue()
        q.enqueue([user_id])
        bisited = set()
        while q.size() > 0:
            path = q.dequeue()
            checker = path[-1]
            if checker not in bisited:
                bisited.add(checker)
                if checker != user_id:
                    visited.update({f'{checker}':path})
                for connection in self.friendships[checker]:
                    new_path = path.copy()
                    new_path.append(connection)
                    q.enqueue(new_path)
        return visited



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
