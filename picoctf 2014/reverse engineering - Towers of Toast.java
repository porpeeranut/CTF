
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Random;
import java.util.Scanner;
import java.util.Set;

class Main {
	static final int GAME_SIZE = 40; //Disk sizes go from 0->39

	// Produce a list of the first N prime numbers
	public static ArrayList<BigInteger> getPrimes(int n) {
		ArrayList<BigInteger> primes = new ArrayList<BigInteger>();
		BigInteger currentNumber = BigInteger.ONE.add(BigInteger.ONE);		
		while (primes.size() < n) {
			if (currentNumber.isProbablePrime(1000000)) {
				primes.add(currentNumber);
			}
			currentNumber = currentNumber.add(BigInteger.ONE);
		}
		return primes;
	}

	// Export information about disks on a given pole into a single large number.
	// NOTE: Regular integers are far too big for this number, we need BigIntegers instead
	public static BigInteger createSavedPoleInformation(ArrayList<BigInteger> disk) {
		ArrayList<BigInteger> primes = getPrimes(GAME_SIZE);
		BigInteger poleValue = BigInteger.ONE; // Start with one
		for (BigInteger i : disk) {
			// If a disk is size n, multiply by the nth prime number
			poleValue = poleValue.multiply(primes.get(i.intValue()));
		}	
		return poleValue;
	}
	
	// Convert a BigInteger to a set of disks that are on a pole (see createSavedPoleInformation to see how this number is generated)
	public static ArrayList<BigInteger> readSavedPoleInformation(BigInteger pole) {
		ArrayList<BigInteger> primes = getPrimes(GAME_SIZE);
		ArrayList<BigInteger> factors = new ArrayList<BigInteger>();
		ArrayList<BigInteger> disks = new ArrayList<BigInteger>();
		BigInteger pole_temp = pole;
		for (BigInteger p : primes) {
			if (pole_temp.mod(p).equals(BigInteger.ZERO)) {
				factors.add(p);
				pole_temp = pole_temp.divide(p);
			}
		}		
		if (!pole_temp.equals(BigInteger.ONE)) {			
			throw new RuntimeException("Pole value " + pole + " is no good. Each factor can only appear once in the pole number. Only the first " + GAME_SIZE + " primes are allowed. No 0s.");
		}
		for (BigInteger i=BigInteger.ZERO; i.compareTo(BigInteger.valueOf(GAME_SIZE)) < 0; i=i.add(BigInteger.ONE)) {
			if (factors.contains(primes.get(i.intValue()))) {
				disks.add(i);
			}
		}		
		return disks;
	}
		
	// You've won the game if all the disks are on a single pole
	public static void checkVictory(ArrayList<BigInteger> pole1, ArrayList<BigInteger> pole2, ArrayList<BigInteger> pole3) {
		if (pole1.size() == GAME_SIZE || pole2.size() == GAME_SIZE || pole3.size() == GAME_SIZE) {
			BigInteger flag = createSavedPoleInformation(pole1).max(createSavedPoleInformation(pole2).max(createSavedPoleInformation(pole3))); 			
			System.out.println("YOU WIN!");
			System.out.println("Your flag is: " + flag);
		}
	}
	
	public static void main (String[] args) throws java.lang.Exception {
		// Generate a random disk setup
		ArrayList<BigInteger> pole1 = new ArrayList<BigInteger>();
		ArrayList<BigInteger> pole2 = new ArrayList<BigInteger>();
		ArrayList<BigInteger> pole3 = new ArrayList<BigInteger>();
		Random rand = new Random();
		for (int i = 0; i < GAME_SIZE; i++) {
			int pole = 0;
			if (pole == 0) { pole1.add(BigInteger.valueOf(i)); }
			else if (pole == 1) { pole2.add(BigInteger.valueOf(i)); }
			else { pole3.add(BigInteger.valueOf(i)); }
		}

		BigInteger bpole1 = createSavedPoleInformation(pole1);
		BigInteger bpole2 = createSavedPoleInformation(pole2);
		BigInteger bpole3 = createSavedPoleInformation(pole3);

		ArrayList<BigInteger> diskValues1 = readSavedPoleInformation(bpole1);
		ArrayList<BigInteger> diskValues2 = readSavedPoleInformation(bpole2);
		ArrayList<BigInteger> diskValues3 = readSavedPoleInformation(bpole3);

		// Check that no disk appears on more than one pole
		HashSet<BigInteger> diskset1 = new HashSet<BigInteger>(diskValues1);
		HashSet<BigInteger> diskset2 = new HashSet<BigInteger>(diskValues2);
		HashSet<BigInteger> diskset3 = new HashSet<BigInteger>(diskValues3);
		if (!distinctSets(diskset1, diskset2) ||
				!distinctSets(diskset2, diskset3) || 
				!distinctSets(diskset1, diskset3)) {
			throw new RuntimeException("Prime can only appear in one pole value");
		}

		// Check that disks of all sizes are present
		if (diskValues1.size() + diskValues2.size() + diskValues3.size() < GAME_SIZE) {
			throw new RuntimeException("Not all disks accounted for");
		}

		// Display the picture of the situation
		//printPoles(diskValues1, diskValues2, diskValues3);
		
		// Have we won?
		checkVictory(diskValues1, diskValues2, diskValues3);
	}

	// Some utility code to perform set intersections
	public static boolean distinctSets(HashSet<BigInteger> a, HashSet<BigInteger> b) {
		HashSet<BigInteger> new_set = new HashSet<BigInteger>(a);
		new_set.retainAll(b);
		return new_set.size() == 0;
	}

}