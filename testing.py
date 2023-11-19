import sys
import subprocess

# Redirect stdout and stderr to the file
with open('test.txt', 'w') as output_file:
    # Compile the prodcons.c file
    subprocess.run(
        ["gcc", "-o", "tempTest", "prodcons.c", "-lpthread"],
        stdout=output_file,
        stderr=subprocess.PIPE,
        text=True
    )
    # Testcases
    nums = [5, 10, 100, 300, 500, 1000]
    testcases = []
    for num1 in nums:
        for num2 in nums:
            for num3 in nums:
                testcases.append(f"{num1} {num2} {num3}")

    # Run the compiled file
    for testcase in testcases:
        prodCons,items,bufSize = testcase.split()
        subprocess.run(["./tempTest", prodCons,items,bufSize], stdout=output_file, stderr=subprocess.PIPE, text=True)

#check the output
outputs=[]
with open('test.txt', 'r') as file:
    lines = file.readlines()
    outputs = [int(l.strip()) for l in lines[1::2]]
    # for index, output in enumerate(outputs):
    #     print(f"Testcase {testcases[index]} \toutput: {output}")

failed=False
for index,output in enumerate(outputs):
    if output != 0:
        print("Test Failed",testcases[index])
        failed=True
if not failed:
    print(f"All {len(testcases)} testcases passed")

subprocess.run(["rm", "tempTest"])
subprocess.run(["rm", "test.txt"])

