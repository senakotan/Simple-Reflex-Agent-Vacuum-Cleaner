# 📌 Simple Reflex Vacuum Agent

This project implements a **Simple Reflex AI Agent** that controls a vacuum-cleaning robot operating in a two-room environment.  
The agent perceives the environment, takes actions based on simple rules, and reacts to dynamic changes such as rooms becoming dirty again over time.

---

## 🚀 Overview

- The system contains **one robot** and **two rooms** (“Left” and “Right”).  
- The agent checks whether the current room is **Clean** or **Dirty**.  
- If the room is **Dirty**, the agent cleans it.  
- If the room is **Clean**, the agent moves to the **other room**.  
- Movements follow a simple rule:  
  **Left → Right** or **Right → Left**.  
- Rooms may become dirty again due to random external factors.  
- The simulation runs for a fixed number of steps using a timer.  
- During execution, the system displays both the **percept sequence** (what the agent senses) and the **action list** (what the agent decides to do).

---

## 🧠  AI Agent Type

This project demonstrates a **Simple Reflex Agent**, one of the fundamental agent types in AI:

- Acts only based on the **current percept**  
- No memory  
- No internal model of the world  
- Uses condition–action rules  
- Ideal for simple, deterministic tasks  

---

## 📂 Project Structure

- `Environment` class → manages room states  
- `SimpleReflexAgent` → perceives & acts  
- `run_simulation()` → runs the full agent–environment loop  
- Random environment changes simulate external events  

---

## ▶️ Run the Simulation

```bash
python vacuum_agent.py

