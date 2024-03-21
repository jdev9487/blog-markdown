---
title: The Quadratic Formula
date: "2024-03-08T11:49:00.000Z"
description: "A derivation of the quadratic formula using the 'completing the square' method"
featuredAnimation: "completingTheSquare.mp4"
user: "jdev9487"
---

## Overview

The quadratic formula is used to solve *any* quadratic equation. It is derived by a process called "completing the square" whose name often goes unexplained. What is the "square" and how is it completed? The above animation should provide some geometric intuition.

## Derivation

We can write any quadratic equation in this form:

$$
    ax^2 + bx + c = 0\,.
$$

Dividing by $a$ gives us an "easier" equation to work with: 

$$
x^2 + \frac{b}{a}x + \frac{c}{a} = 0\,.
$$

We now want to split up the middle term and "place" them on either side of the $x^2$ term (see animation):

$$
x^2 + \frac{b}{2a}x + \frac{b}{2a}x + \frac{c}{a} = 0\,.
$$

Arranged carefully, the first three terms almost produce a square; now to complete it.

### Completion

What can often seem like an arbitrary insertion, $\frac{b^2}{4a^2}$, is added and immediately taken away to ensure the equation still holds:

$$
x^2 + \frac{b}{2a}x + \frac{b}{2a}x + \frac{b^2}{4a^2} - \frac{b^2}{4a^2} + \frac{c}{a} = 0\,.
$$

These first four terms make up the square. But what is the length of this square? The animation provides a better explanation than words can but you can verify that these terms factorise nicely:

$$
\left(x + \frac{b}{2a}\right)^2 - \frac{b^2}{4a^2} + \frac{c}{a} = 0\,.
$$

### Algebra clean up

This section is devoted to the "$\dots$" in the animation. But no more quadratic magic is needed; just algebra that an attentive teenager is comfortable with:

$$
\begin{align*}
\left(x + \frac{b}{2a}\right)^2 &= \frac{b^2}{4a^2} - \frac{c}{a} \\
\left(x + \frac{b}{2a}\right)^2 &= \frac{b^2-4ac}{4a^2} \\
x + \frac{b}{2a} &= \frac{\pm\sqrt{b^2-4ac}}{2a} \\
x &= \frac{-b\pm\sqrt{b^2-4ac}}{2a}\,.
\end{align*}
$$

## Conclusion

For those who have not seen this derivation before it may seem like a lot of steps. Whilst that may be true, each one is simple (if not obvious). Anyone looking to study maths beyond compulsory level (A Levels upward in the UK) should look to derive the quadratic formula as proof of the required algebraic manipulations that are taken for granted later on.