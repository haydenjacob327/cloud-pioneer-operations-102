# -*- coding: utf-8 -*-

# 小龙智脑 (XiaoLong Brain) - 全新原创项目

# 作者 / 版权人: 小龙 (XiaoLong)

# License: MIT。本项目所有代码均为原创，保留署名即可自由使用。



from xiaolong_ai.core.llm import MockLLM

from xiaolong_ai.core.agent import Agent

from xiaolong_ai.tools import calculator





def main():

    agent = Agent(llm=MockLLM(), system_prompt="你是小龙智脑演示助手。")

    print(agent.run("你好，介绍一下你自己"))

    print("计算器:", calculator.calculator("1+2*3"))





if __name__ == "__main__":

    main()

