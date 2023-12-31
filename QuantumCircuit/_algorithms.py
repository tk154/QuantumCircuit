from ._base import Base
from ._gates import Gates


# An abstract class containing predefined algrorithms resp. circuits
class Algorithms(Gates, Base):
    def __qft_swap_gates(self, qubits: tuple[int], qubits_len: int):
        "Swaps the gates for the QFT"

        for i in reversed(range(qubits_len // 2)):
            self.swap(qubits[i], qubits[qubits_len - i - 1])


    def __qft(self, qubits: tuple[int]):
        """
        Builds the QFT for the given qubits.\n
        Raises a ValueError exception if a qubit is not part of the circuit or if there are duplicates.
        """

        # Retrieve the count of given qubits
        qubits_len = len(qubits)

        # Start the circuit with the last given qubit
        for i in reversed(range(qubits_len)):
            qubit = qubits[i]

            # Create a Hadamard-Gate for all qubits
            self.hadamard(qubit)

            # Controlled-Phase-Shift-Gates
            # qubit_count - 1 for the first qubit, 0 for the last
            for j in range(i):
                cqubit = qubits[i - j - 1]
                self.cphase(qubit, cqubit, f"pi / {2 ** (j + 1)}")

            # Only append a new line if there is more than one iteration
            if qubits_len >= 2:
                self.empty_line()

        if qubits_len >= 2:
            # Swap the Gates
            self.__qft_swap_gates(qubits, qubits_len)


    def __iqft(self, qubits: tuple[int]):
        """
        Builds the QFT for the given qubits.\n
        Raises a ValueError exception if a qubit is not part of the circuit or if there are duplicates.
        """

        # Retrieve the count of given qubits
        qubits_len = len(qubits)

        if qubits_len >= 2:
            # Swap the gates
            self.__qft_swap_gates(qubits, qubits_len)

        # Start the circuit with the first given qubit
        for i in range(qubits_len):
            # Only append a new line if there is more than one iteration
            if qubits_len >= 2:
                self.empty_line()

            qubit = qubits[i]

            # Create a Hadamard-Gate for all qubits
            self.hadamard(qubit)

            # Controlled-Phase-Shift-Gates
            # qubit_count - 1 for the first qubit, 0 for the last
            for j in range(qubits_len - i - 1):
                cqubit = qubits[i + j + 1]
                self.cphase(qubit, cqubit, f"-pi / {2 ** (j + 1)}")


    def qft(self, qubits: tuple[int] = (), inverse: bool = False):
        """
        Builds the Quantum Fourier Transform for the given qubits.\n
        Raises a ValueError exception if a qubit is not part of the circuit or if there are duplicates.

        :param tuple[int] qubits: (optional) A tuple containing the IDs of the qubits.
            If no qubits are given, defaults to all qubits of the circuit.
        :param bool inverse: (optional) If set to True, the inverse QFT will be built.
            Defaults to False.
        """

        qubits = self._check_qubits(qubits)

        # Build the QFT or inverse QFT
        self.__iqft(qubits) if inverse else self.__qft(qubits)
