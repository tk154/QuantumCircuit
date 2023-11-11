from . import QuantumCircuit

import errno, sys
from functools import partial


# Maps a string to the corresponding circuit function and arguments
__str2func = { 
    "qft":  partial(QuantumCircuit.qft, inverse=False), 
    "iqft": partial(QuantumCircuit.qft, inverse=True) 
}

def __checkCmdArgs():
    # Retrieve the argument count
    argc = len(sys.argv)

    # Check if the circuit type is given
    if argc < 2:
        print("Error: Missing circuit type argument.", file=sys.stderr)
        sys.exit(errno.EINVAL)

    # Check if the circuit type function exists
    func = __str2func.get(sys.argv[1])
    if func == None:
        print(f"Error: Unknown circuit type '{sys.argv[1]}'. Allowed are: {list(__str2func.keys())}", file=sys.stderr)
        sys.exit(errno.EINVAL)

    # Check if initial qubits are given
    if argc < 3:
        print("Error: Missing initial qubits argument.", file=sys.stderr)
        sys.exit(errno.EINVAL)

    # Convert the initial qubit string to an integer list
    try:
        initial_qubits = [int(q) for q in reversed(sys.argv[2])]
    except ValueError:
        print("Error: Initial qubits should only contain 0s and 1s.", file=sys.stderr)
        sys.exit(errno.EINVAL)

    return func, initial_qubits


if __name__ == "__main__":
    func, initial_qubits = __checkCmdArgs()

    # Create the circuit
    circuit = QuantumCircuit(initial_qubits)
    
    # Apply the given circuit/algorithm
    func(circuit)

    # Measure all qubits
    circuit.measure()

    # Print the circuit to stdout
    circuit.write()
