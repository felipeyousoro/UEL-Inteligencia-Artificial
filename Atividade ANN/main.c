#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define INPUTS 2
#define HIDDEN 2
#define OUTPUTS 1

#define THRESHOLD 0.5

#define EPOCHS 2
#define ITERATIONS 4

double weights_ih [INPUTS][HIDDEN];
double weights_ho [HIDDEN][OUTPUTS];

double sigmoid(int x) {
    return 1/(1+exp(-x));
}

double sigmoid_derivative(double x) {
    double sigmoid_x = sigmoid(x);
    return sigmoid_x * (1 - sigmoid_x);
}

void start_weights() {
    printf("Starting weights for input-hidden layer\n");
    for (int i = 0; i < INPUTS; i++) {
        for (int j = 0; j < HIDDEN; j++) {
            weights_ih[i][j] = (double)rand()/RAND_MAX - 0.5;
            printf("%f ", weights_ih[i][j]);
        }
    }

    printf("\nStarting weights for hidden-output layer\n");
    for (int i = 0; i < HIDDEN; i++) {
        for (int j = 0; j < OUTPUTS; j++) {
            weights_ho[i][j] = (double)rand()/RAND_MAX - 0.5;
            printf("%f ", weights_ho[i][j]);
        }
    }

    printf("\n");
}

int main() {
    int inputs [4][2] = {{0,0},{0,1},{1,0},{1,1}};
    int outputs [4] = {0,1,1,0};

    start_weights();

    for (int epoch = 0; epoch < EPOCHS; epoch++) {
        printf("\nEpoch %d\n\n", epoch + 1);
        for (int iteration = 0; iteration < ITERATIONS; iteration++) {
            // Feedforward
            printf("Iteration %d\n", iteration + 1);
            int input [INPUTS];
            for (int i = 0; i < INPUTS; i++) {
                input[i] = inputs[iteration][i];
                printf("%d ", input[i]);
            }
            printf("\n");

            double hidden [HIDDEN];
            for (int i = 0; i < HIDDEN; i++) {
                double sum = 0;
                for (int j = 0; j < INPUTS; j++) {
                    sum += input[j] * weights_ih[j][i];
                }
                hidden[i] = sigmoid(sum);
                printf("%f ", hidden[i]);
            }
            printf("\n");

            double output [OUTPUTS];
            for (int i = 0; i < OUTPUTS; i++) {
                double sum = 0;
                for (int j = 0; j < HIDDEN; j++) {
                    sum += hidden[j] * weights_ho[j][i];
                }
                output[i] = sigmoid(sum);
                printf("%f ", output[i]);
            }

            // Backpropagation
            printf("\n");
            double error = outputs[iteration] - output[0];
            printf("Error: %f\n", error);
            double delta_output = error * sigmoid_derivative(output[0]);
            printf("Delta output: %f\n", delta_output);
            double delta_hidden [HIDDEN];
            for (int i = 0; i < HIDDEN; i++) {
                delta_hidden[i] = delta_output * weights_ho[i][0] * sigmoid_derivative(hidden[i]);
                printf("Delta hidden %d: %f\n", i, delta_hidden[i]);
            }
            printf("\n");

            // Update weights
            for (int i = 0; i < HIDDEN; i++) {
                for (int j = 0; j < OUTPUTS; j++) {
                    weights_ho[i][j] += delta_output * hidden[i];
                    printf("Weight hidden-output %d-%d: %f\n", i, j, weights_ho[i][j]);
                }
            }

            for (int i = 0; i < INPUTS; i++) {
                for (int j = 0; j < HIDDEN; j++) {
                    weights_ih[i][j] += delta_hidden[j] * input[i];
                    printf("Weight input-hidden %d-%d: %f\n", i, j, weights_ih[i][j]);
                }
            }
            printf("\n");


        }

    }




}
