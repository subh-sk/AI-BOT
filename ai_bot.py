import json
from difflib import get_close_matches

def load_knowladge_base(file_path: str) -> dict:
    with open(file_path, "r") as f:
        data: dict = json.load(f)
        # print(data)
        return data

def save_knowlagde_base(file_path: str,data:dict):
    with open(file_path,'w') as f:
        json.dump(data, f,indent=2)

def find_bast_match(user_question:str,questions:list[str]) -> str|None:
    matches : list = get_close_matches(user_question,questions,n=1,cutoff=.6) #n=1 mean will give one answer  .6 means 60% similer q. 
    return matches[0] if matches else None


def get_ans_for_question(question:str,knoladge_base:dict) -> str|None:
    for q in knoladge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
        
def chat_bot():
    knowladge_base : dict = load_knowladge_base('knowladge_base.json')

    while True:
        user_input : str = input("YOU : ")
        
        if user_input.lower() == "quit" or user_input.lower() == "exit":
            break
        best_match : str |None = find_bast_match(user_input,[q["question"] for q in knowladge_base['questions']])

        if best_match:
            answer : str = get_ans_for_question(best_match,knowladge_base)
            print(f"BOT : {answer}")
        else:
            print("I don't know the answer can you tech me?")
            new_answer : str =input('Type the answer or ("skip","no") to skip : ')
            if new_answer.lower() != 'skip' or new_answer.lower() != 'no':
                knowladge_base["questions"].append({"question":user_input,"answer":new_answer})
                save_knowlagde_base('knowladge_base.json',knowladge_base)
                print("Bot : Thankyou! i learned a new response!\n")

if __name__ == "__main__":
    chat_bot()
    # load_knowladge_base()