class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        # f(5) = 5 - 0.01 * 2(5)

        # theta := theta - alpha * nabla theta * loss function

        minimizer = init # Set x = init = minimizer | f(minimizer) = f(5) = x^2
        
        for _ in range(iterations):
            gradient = 2 * minimizer
            minimizer = minimizer - learning_rate * gradient 
        return round(minimizer, 5)



        

    