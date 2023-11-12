QuantumCircuit
==============

.. autoclass:: QuantumCircuit.circuit.QuantumCircuit
   :members:
   :special-members:

.. autoclass:: QuantumCircuit._base.Base
   :members:


Gates
-----

1-Qubit-Gates
^^^^^^^^^^^^^

.. autoclass:: QuantumCircuit._gates.__OneQubitGates
   :members:


2-Qubit-Gates
^^^^^^^^^^^^^

.. autoclass:: QuantumCircuit._gates.__TwoQubitGates
   :members:


3-Qubit-Gates
^^^^^^^^^^^^^

.. autoclass:: QuantumCircuit._gates.__ThreeQubitGates
   :members:


Algorithms
----------

.. autoclass:: QuantumCircuit._algorithms.Algorithms
   :special-members:

   .. automethod:: qft
   .. note::
      | The following pictures show how the QFT is applied on the given Qubits.
      |
      | ``qft((0, 1, 2), inverse=False)``

      .. image:: _images/qft.svg

      |
      |
      | ``qft((0, 1, 2), inverse=True)``

      .. image:: _images/iqft.svg
