## 39. Lyft: How do you uniformly sample points at random from a circle with radious R?

```
Inverse Transform method
- define the cdf: y = r2/R2 (ratio of areas) [Side note: to get pdf differentiate w.r.t. r to get 2r/R2] 
- derive r = sqrt(R2 * y)
- We can sample Y ~ U(0, 1) and corresponding r with the above eqn.
- Sample theta uniformly from [0, 2*pi]
- Finally x = r cos(theta) and y = r sin(theta)
```
