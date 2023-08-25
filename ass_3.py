class FlightProcess:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority

class FlightTable:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def sort_by_p_id(self):
        self.processes.sort(key=lambda x: x.p_id)

    def sort_by_start_time(self):
        self.processes.sort(key=lambda x: x.start_time)

    def sort_by_priority(self):
        priority_order = {"High": 3, "MID": 2, "Low": 1}
        self.processes.sort(key=lambda x: priority_order[x.priority], reverse=True)

    def print_table(self):
        print("P_ID  Process   Start Time (ms)  Priority")
        print("-----------------------------------------")
        for process in self.processes:
            print(f"{process.p_id:<6} {process.process:<9} {process.start_time:<17} {process.priority}")

def main():
    flight_table = FlightTable()

    flight_table.add_process(FlightProcess("P1", "VSCode", 100, "MID"))
    flight_table.add_process(FlightProcess("P23", "Eclipse", 234, "MID"))
    flight_table.add_process(FlightProcess("P93", "Chrome", 189, "High"))
    flight_table.add_process(FlightProcess("P42", "JDK", 9, "High"))
    flight_table.add_process(FlightProcess("P9", "CMD", 7, "High"))
    flight_table.add_process(FlightProcess("P87", "NotePad", 23, "Low"))

    print("Select sorting parameter:")
    print("1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority")
    choice = int(input())

    if choice == 1:
        flight_table.sort_by_p_id()
    elif choice == 2:
        flight_table.sort_by_start_time()
    elif choice == 3:
        flight_table.sort_by_priority()
    else:
        print("Invalid choice")

    flight_table.print_table()

if __name__ == "__main__":
    main()
