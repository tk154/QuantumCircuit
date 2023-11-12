from ._base import Base
from ._gates import Gates
from ._algorithms import Algorithms

from typing import TextIO


class QuantumCircuit(Algorithms, Gates, Base):
    """
    A class to build a Quantum Circuit and write it to a file for the QSFW.
    When the various methods of this class are called, the code for the qsfw is generated
    and cached in the object so that it can finally be written to the interface file.
    """

    def __init__(self, initial_qubits: tuple[int], comment: str = None):
        """
        Creates a circuit by executing the circuit command for the given initial qubits.\n
        Raises a ValueError exception if the initial qubits are empty or they include a non-Bit value.

        :param tuple[int] initial_qubits: A tuple containing the initial qubits.
            The index of the qubit inside the tuple determines the qubit ID e.g., initial_qubits[2] has qubit ID 'q2'.
        :param str comment: (optional) Adds the given comment before the circuit command.
        """

        # Get the count of initial qubits
        self._qubit_count = len(initial_qubits)

        # Return if there is no initial qubit
        if self._qubit_count == 0:
            raise ValueError("There must be at least one initial qubit.") 

        # Return if the qubits include a non-Bit value
        if any(q not in (0,1) for q in initial_qubits):
            raise ValueError("Initial qubits should only contain 0s and 1s.")
        
        # If a comment is given, append it to the output buffer
        if comment != None:
            self.comment(comment)

        # Create the circuit
        self.__create_circuit(initial_qubits)

    def __create_circuit(self, initial_qubits: tuple[int]):
        # Build the circuit command string
        circuit = f"circuit(\n\t('q0', {initial_qubits[0]})"
        for qubit in range(1, self._qubit_count):
            circuit += f",\n\t('q{qubit}', {initial_qubits[qubit]})"
        circuit += "\n);"

        self._command(circuit)
        self.empty_line()
    
    def write(self, file: TextIO = None):
        """
        Writes the circuit buffer to the given file. Clears the output buffer afterwards.\n
        Raises an IOError exception if the given file is not writeable.

        :param TextIO file: (optional) The file where to write the circuit buffer.
            Defaults to stdout, if no file is given.
        """

        if file != None:
            # Check if the given file is writeable, raise an exception if not
            if not file.writable():
                raise IOError(f"'{file.name}' is not writable.")

        for line in self._output:
            print(line, file=file)

        self._output.clear()
