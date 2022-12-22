import basic_operations as bo
def main():
    operator = bo.Operations()
    print(operator.sum(5,3))
    print(operator.minus(1, 2, 3, 5))
    print(operator.mul(1, 2, 3, 5))
    print(operator.div(100,2,2,5))

if __name__ == '__main__':
    main()