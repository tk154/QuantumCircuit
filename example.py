from QuantumCircuit import QuantumCircuit


initial_qubits = (1, 0, 1)

circuit = QuantumCircuit(initial_qubits, 
    comment=f"Create circuit with {len(initial_qubits)} qubits")

circuit.qft()

circuit.comment("Measure the qubits")
circuit.measure()

with open("qft.qs", 'w') as file:
    circuit.write(file)
