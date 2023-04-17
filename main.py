import random

import math

class SecureRandomNumberGenerator:

    def __init__(self, seed=None):

        if seed is None:

            self.seed = random.randint(0, 2**32)

        else:

            self.seed = seed

    def generate_random_number(self, n):

        """Generates a random number between 0 and n-1.

        Args:

            n: The maximum value of the random number.

        Returns:

            A random number between 0 and n-1.

        """

        # Generate a cryptographically secure random number.

        random_number = random.SystemRandom().randint(0, 2**n)

        # XOR the random number with the seed.

        random_number ^= self.seed

        # Return the random number.

        return random_number

    def generate_random_bytes(self, n):

        """Generates n random bytes.

        Args:

            n: The number of bytes to generate.

        Returns:

            A bytearray of n random bytes.

        """

        # Generate a cryptographically secure random number.

        random_number = random.SystemRandom().randint(0, 2**(8*n))

        # Convert the random number to a bytearray.

        random_bytes = bytearray(random_number.to_bytes(n, "big"))

        # Return the random bytes.

        return random_bytes
        def generate_random_string(self, length):

        """Generates a random string of length characters.

        Args:

            length: The length of the random string.

        Returns:

            A random string of length characters.

        """

        # Generate a random bytearray of length bytes.

        random_bytes = self.generate_random_bytes(length)

        # Convert the random bytearray to a string.

        random_string = bytes(random_bytes).decode("utf-8")

        # Return the random string.

        return random_string

    def set_seed(self, seed):

        """Sets the seed for the random number generator.

        Args:

            seed: The seed for the random number generator.

        """

        self.seed = seed

    def get_seed(self):

        """Gets the seed for the random number generator.

        Returns:

            The seed for the random number generator.

        """

        return self.seed

    def save_state(self):

        """Saves the state of the random number generator.

        Returns:

            A dictionary containing the state of the random number generator.

        """

        state = {

            "seed": self.seed,

        }

        return state
        

    def restore_state(self, state):

        """Restores the state of the random number generator.

        Args:

            state: A dictionary containing the state of the random number generator.

        """

        self.seed = state["seed"]

    def __repr__(self):

        return "SecureRandomNumberGenerator(seed={!r})".format(self.seed)

    def __eq__(self, other):

        if not isinstance(other, SecureRandomNumberGenerator):

            return NotImplemented

        return self.seed == other.seed

    def __hash__(self):

        return hash(self.seed)

    def __str__(self):

        return "SecureRandomNumberGenerator(seed={!r})".format(self.seed)
