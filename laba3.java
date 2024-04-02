
// Метод простых итераций
class Result {
    public static List<Double> solve_by_fixed_point_iterations(int system_id,
    int number_of_unknowns, List<Double> initial_approximations) {
        List<Function<List<Double>, Double>> funcs = SNAEFunctions.get_functions(system_id);
        double tol = 1e-5;
        int max_iterations = 100;

        List<Double> x0 = new ArrayList<>(initial_approximations);
        for (int iter = 0; iter < max_iterations; iter++) {
            List<Double> x1 = new ArrayList<>();
            for (int i = 0; i < number_of_unknowns; i++) {
                double value = x0.get(i) - 0.0001 * funcs.get(i).apply(x0);
                x1.add(value);
            }
            for (int i = 0; i < number_of_unknowns; i++) {
                if (Math.abs(x1.get(i) - x0.get(i)) < tol) {
                    break;
                }
            }

            x0 = x1;
        }
        return x0;
    }
}