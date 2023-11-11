from ._base import Base


# 1-Qubit-Gates
class __OneQubitGates(Base):
    def ident(self, qubit: int):
        """
        Executes the ident command on the given qubit.\n
        Raises a ValueError exception if the qubit is not part of the circuit.

        :param int qubit: The ID of the qubit.
        """

        self._check_qubit(qubit)
        self._command(f"ident('q{qubit}');")

    def hadamard(self, qubit: int):
        """
        Executes the hadamard command on the given qubit.\n
        Raises a ValueError exception if the qubit is not part of the circuit.

        :param int qubit: The ID of the qubit.
        """

        self._check_qubit(qubit)
        self._command(f"hadamard('q{qubit}');")

    def phase(self, qubit: int, angle: str):
        """
        Executes the phase command on the given qubit.\n
        Raises a ValueError exception if the qubit is not part of the circuit.

        :param int qubit: The ID of the qubit.
        :param str angle: The angle for the shift. 
            Use str so that expressions like 'pi / 2' 
            don't get evaluated here but in the QSFW.
        """

        self._check_qubit(qubit)
        self._command(f"phase('q{qubit}', {angle});")

    def pauliX(self, qubit: int):
        """
        Executes the pauliX command on the given qubit.\n
        Raises a ValueError exception if the qubit is not part of the circuit.

        :param int qubit: The ID of the qubit.
        """

        self._check_qubit(qubit)
        self._command(f"pauliX('q{qubit}');")

    def pauliY(self, qubit: int):
        """
        Executes the pauliY command on the given qubit.\n
        Raises a ValueError exception if the qubit is not part of the circuit.

        :param int qubit: The ID of the qubit.
        """

        self._check_qubit(qubit)
        self._command(f"pauliY('q{qubit}');")

    def pauliZ(self, qubit: int):
        """
        Executes the pauliZ command on the given qubit.\n
        Raises a ValueError exception if the qubit is not part of the circuit.

        :param int qubit: The ID of the qubit.
        """

        self._check_qubit(qubit)
        self._command(f"pauliZ('q{qubit}');")

    def sphase(self, qubit: int):
        """
        Executes the sphase command on the given qubit.\n
        Raises a ValueError exception if the qubit is not part of the circuit.

        :param int qubit: The ID of the qubit.
        """

        self._check_qubit(qubit)
        self._command(f"sphase('q{qubit}');")

    def tphase(self, qubit: int):
        """
        Executes the tphase command on the given qubit.\n
        Raises a ValueError exception if the qubit is not part of the circuit.

        :param int qubit: The ID of the qubit.
        """

        self._check_qubit(qubit)
        self._command(f"tphase('q{qubit}');")

    def measure(self, qubits: tuple[int] = ()):
        """
        Executes the measure command for all given qubits.\n
        Raises a ValueError exception if a qubit is not part of the circuit or if there are duplicates.

        :param tuple[int] qubits: (optional) The to-be-measured qubit IDs.
            If no qubits are given, defaults to all qubits of the circuit.
        """

        qubits = self._check_qubits(qubits)

        for qubit in qubits:
            self._command(f"measure('q{qubit}');")


# 2-Qubit-Gates
class __TwoQubitGates(Base):
    def cnot(self, qubit: int, cqubit: int):
        """
        Executes the cnot command on the given qubits.\n
        Raises a ValueError exception if one of the qubits is not part of the circuit.

        :param int qubit: The ID of the qubit.
        :param int cqubit: The ID of the control qubit.
        """

        self._check_qubit(qubit)
        self._check_qubit(cqubit)
        self._command(f"cnot('q{cqubit}', 'q{qubit}');")

    def swap(self, qubit0: int, qubit1: int):
        """
        Executes the swap command on the given qubits.\n
        Raises a ValueError exception if one of the qubits is not part of the circuit.

        :param int qubit0: The ID of the first qubit.
        :param int qubit1: The ID of the second qubit.
        """

        self._check_qubit(qubit0)
        self._check_qubit(qubit1)
        self._command(f"swap('q{qubit0}', 'q{qubit1}');")

    def cz(self, qubit: int, cqubit: int):
        """
        Executes the cz (Controlled-Z) command on the given qubits.\n
        Raises a ValueError exception if one of the qubits is not part of the circuit.

        :param int qubit: The ID of the qubit.
        :param int cqubit: The ID of the control qubit.
        """

        self._check_qubit(qubit)
        self._check_qubit(cqubit)
        self._command(f"cz('q{cqubit}', 'q{qubit}');")

    def cphase(self, qubit: int, cqubit: int, angle: str):
        """
        Executes the cphase command on the given qubits.\n
        Raises a ValueError exception if one of the qubits is not part of the circuit.

        :param int qubit: The ID of the qubit.
        :param int cqubit: The ID of the control qubit.
        :param str angle: The angle for the shift. 
            Use str so that expressions like 'pi / 2' don't get evaluated here.
        """

        self._check_qubit(qubit)
        self._check_qubit(cqubit)
        self._command(f"cphase('q{cqubit}', 'q{qubit}', {angle});")


# 3-Qubit-Gates
class __ThreeQubitGates(Base):
    def toffoli(self, qubit0: int, qubit1: int, qubit2: int):
        """
        Executes the toffoli command on the given qubits.\n
        Raises a ValueError exception if one of the qubits is not part of the circuit.

        :param int qubit0: The ID of the first qubit.
        :param int qubit1: The ID of the second qubit.
        :param int qubit2: The ID of the third qubit.
        """

        self._check_qubit(qubit0)
        self._check_qubit(qubit1)
        self._check_qubit(qubit2)
        self._command(f"toffoli('q{qubit0}', 'q{qubit1}, 'q{qubit2}');")

    def cswap(self, qubit0: int, qubit1: int, qubit2: int):
        """
        Executes the cswap command on the given qubits.\n
        Raises a ValueError exception if one of the qubits is not part of the circuit.

        :param int qubit0: The ID of the first qubit.
        :param int qubit1: The ID of the second qubit.
        :param int qubit2: The ID of the third qubit.
        """

        self._check_qubit(qubit0)
        self._check_qubit(qubit1)
        self._check_qubit(qubit2)
        self._command(f"cswap('q{qubit0}', 'q{qubit1}, 'q{qubit2}');")


# An abstract class containing the quantum circuit gates
class Gates(__OneQubitGates, __TwoQubitGates, __ThreeQubitGates):
    pass
