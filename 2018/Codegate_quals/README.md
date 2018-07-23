# RSAbaby.

임의의 m에 대해, d, p, g, h의 하위 m비트를 각각 d_partial, p_partial, g_partial, h_partial이라고 하자. XOR, 덧셈, 뺄셈, 곱셈 모두 상위 비트가 하위 비트에 영향을 주지 않는 연산이므로 g_partial = d_partial(p_partial - 0xdeadbeef)과 h_partial = (d_partial+p_partial) ^ (d_partial-p_partial) 이 두 식이 모두 성립한다. 이를 이용해 p와 d를 하위비트부터 복원하고, 이렇게 복원해낸 후보군들에 대해 직접 N을 p로 나눠보면서 올바른 p와 q를 찾아내어 메시지를 얻어낼 수 있다.

For arbitrary m, let least m-bit of d, p, g, h be d_partial, p_partial, g_partial, h_partial. Since XOR, addition, substraction, multiplication are the operation which higher bits are not effected on lower bits, two eqautions g_partial = d_partial(p_partial - 0xdeadbeef) and h_partial = (d_partial+p_partial) ^ (d_partial-p_partial) hold. Using this two equations, recover p, d from lower bit, and for all candidate p, divide N into p. Then you can found right p, q and recover the message.
