from agent import Agent

if __name__ == "__main__":
    goal = input("Enter your goal: ")
    agent = Agent(goal)
    agent.run()
