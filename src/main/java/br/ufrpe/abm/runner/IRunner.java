package br.ufrpe.abm.runner;

/**
 * <p>
 * Interface that defines a runner.
 * </p>
 *
 * <p>
 * Every runner abstracts the idea of using an algorithm for solving a problem.
 * </p>
 *
 * @version 1.0
 */
public interface IRunner {

  /**
   * Executes the runner.
   */
  void run();

  /**
   * Returns the runner results. Returns null if it hasn't been run.
   *
   * @return an object that implements {@link IRunnerResult}.
   */
  IRunnerResult getResult();

  /**
   * Returns the runner configuration.
   *
   * @return an object that implements {@link IRunnerConfig}.
   */
  IRunnerConfig getConfig();
}
