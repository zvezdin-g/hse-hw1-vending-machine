# Higher School of Economics: course Programming part 1
Assignment 1: Vending machine. This task was completed 23.03.2019 as a home work in HSE. Grade: 10/10

# Task information from [hw1.pdf](https://github.com/zvezdin-g/hse-hw1-vending-machine/blob/master/hw1.pdf)
## General information

Deadline:March 24th, 23:59:
Submission:through the Canvas LMS as a zip archive (even if you have just a single .py file).

## Introduction

In the first graded homework assignment you will implement a simplified logic of a vending machine.
Today vending machines (VMs) are used to provide a broad range of operatorless services, from selling
snacks, drinks or transport tickets to printing instagram pictures.
Writing a complete application for a real vending machine requires physical hardware (motors, coin
acceptors, bill validators, etc). In your solution many of the functions of a real vending terminal will be
emulated by console input and output. For example, payment acceptal will be done by the user entering the
banknote denomination, while product or change dispensing will be performed by console output.

## General requirements

- Use proper coding style, follow PEP-8 guidelines. Strict PEP-8 validation like the one in PyJudge
    won’t be performed, however, if the code becomes hard to read because of multiple PEP-8 violations,
    your grade can be lowered
- Use constants instead of “magic numbers”
- Use functions (and optionally modules) to modularize your program, don’t put all logic in the main
    program
- Protect against possible program crashes that come as a result of incorrect user actions, e.g. entering
    a non-valid number and others
- Make sure you submit your own work. All solutions will be checked for plagiarism by an automated
    service

## Description of tasks

### Vending machine capabilities

- The VM accepts the following banknotes: 50RUB, 100RUB, 200RUB and 500RUB. However, you have
    to design the program code in such a way that the list can be easily extended to other bill types.
- Change is given only in 10RUB, 5RUB, 2RUB and 1RUB coins listed in order of decreasing priority.
- The terminal is capable of physically storing up to 15 items of each product.
- The change dispensing module is capable of physically holding up to 400 coins of each denomination.

### Basic task (6 points max)

Start by creating an assortment of products for your vending machine. Hardcode it in a data structure in
your program (the user does not need to enter this information!). In particular, the following information
needs to be stored:

- Products: name, price (integer) and remaining quantity of each product


- Accepted cash: number of accepted banknotes of each denomination since the beginning of operation
    (or for the advanced task - since the last service operation)
- Number of remaining coins of each denomination used to give change

Your VM application should operate in an loop giving the user a choice of the following options on each
iteration:

1. Insert a banknote
2. Show available products
3. Select a product
4. Get the change

When the user enters a banknote value, check that it is supported and increase the corresponding counter,
give an error message otherwise.
In the second option (show available products) print information about all products that are currently
present (quantity>0).
In the third menu option provide a choice of only those products that are present and can be bought
with the current credit. If the user makes a selection, print information about the product and decrease its
quantity.
When the “Get change” option is selected, dispense the change using 10,5,2 and 1 RUB coins (print the
distribution of coins on the screen). 10RUB coins have the highest priority, followed by 5 RUB, then 2RUB
and finally 1RUB. For the basic task you don’t need to consider the number of remaining coins (assume it
to be infinite).

### Additional tasks (+4 points max)

1. + 2 points. Write an advanced algorithm of calculating change that takes into account the remaining
    number of each coin denomination, i.e. if there are no 10RUB coins left in the terminal, dispense the
    change using other coin types.
    Additionally make several verifications that will guarantee that the user can get the full change at any
    time. This is about two scenarios:

```
(a) When the user inserts a banknote, check that there is at least one product that can be bought
with the full change. If there are no such products, do not accept the banknote.
(b) When the user selects a product, check that the change can be dispensed with available coins,
otherwise do not sell the product.
```
2. + 2 points. Implement the VM maintenance logic. If in the main menu instead of choosing an option, a
    secret password ’srvop17’ is entered, the service operation is performed. The service operation consists
    of the following steps:
       - Set the remaining quantity of all products to maximum (see above)
       - Set the remaining amount of each coin denomination to maximum (see above)
       - Print the number of banknotes in the cash accepting module and reset their counters (make them
          0),
       - Request a key press, then return back to main menu

```
After the end of each vending operation (when credit reaches 0) check whether service is required. This
can happen in the following two cases:
```
- No products are left in the vending machine


- No change is left in the terminal

In any of the two cases stated above disable selling products - only the service password (see previous
step) can be entered.


