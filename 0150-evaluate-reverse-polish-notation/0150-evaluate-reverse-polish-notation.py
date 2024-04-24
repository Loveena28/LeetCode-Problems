class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = ['+','-','*','/']
        for i in tokens:
            if i not in operators:
                st.append(i)
            else:
                num1 = int(st.pop())
                num2 = int(st.pop())
                if i == '+':
                    st.append(str(num1+num2))
                elif i == '-':
                    st.append(str(num2-num1))
                elif i == '*':
                    st.append(str(num1*num2))
                else:
                    st.append(str(int(num2/num1)))
        return int(st[0])
        