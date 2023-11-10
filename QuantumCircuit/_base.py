class Base:
    # The count of qubits inside the circuit
    _qubit_count = 0

    # Acts as a output buffer for the circuit
    _output = []

    def _check_qubit(self, qubit_id: int):
        "Check if the given qubit ID is part of the circuit. Raises a ValueError exception if not."

        if qubit_id < 0:
            raise ValueError("Qubit ID cannot be smaller than 0.")
        if qubit_id >= self._qubit_count:
            raise ValueError(f"Qubit q{qubit_id} is not part of the circuit.")

    def _check_qubits(self, qubit_ids: tuple[int]):
        """
        Check if the given qubit IDs are part of the circuit and there are no duplicates.\n
        If yes, the qubit IDs will be returned, raises a ValueError exception otherwise.\n
        If no qubit IDs are given, all qubit IDs of the circuit will be returned.
        """

        if len(qubit_ids) == 0:
            return range(self._qubit_count)

        for qubit in qubit_ids:
            self._check_qubit(qubit)

            # Check for duplicates
            if qubit_ids.count(qubit) > 1:
                raise ValueError(f"Qubit ID q{qubit} is duplicate")
            
        return qubit_ids

    def _command(self, cmd: str):
        "Appends the given command cmd to the output buffer."

        self._output.append(cmd)

    def comment(self, cmt: str, multiline: bool = False):
        """
        Appends the given comment cmt with the prefix '// ' to the output buffer.\n

        :param str cmt: The comment to be appended.
        :param bool multiline: (optional) If set to False, the comment gets '// ' as a prefix.
            If set to True, the comment gets '/* ' as a prefix and ' \*/' as a subfix. Defaults to False.
        """

        self._output.append((f"/* {cmt} */") if (multiline) else (f"// {cmt}"))

    def empty_line(self, count: int = 1):
        """
        Appends empty line(s) to the output buffer.\n
        Raises a ValueError exception if count is smaller than 1.

        :param int count: (optional) Determines the number of empty lines. Defaults to 1.
        """

        if (count < 1):
            raise ValueError("Empty line(s) count must be at least 1.")

        for _ in range(count):
            self._output.append("")
