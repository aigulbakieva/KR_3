from utils import load_file, get_executed, get_sorted_by_date, get_five_operations, prepare_to_output


def main():
    all_operations = load_file('operations.json')
    executed_only = get_executed(all_operations)
    sorted_operations = get_sorted_by_date(executed_only)
    only_five_operations = get_five_operations(sorted_operations)
    for operation in only_five_operations:
        print(prepare_to_output(operation))
        print()


if __name__ == '__main__':
    main()
