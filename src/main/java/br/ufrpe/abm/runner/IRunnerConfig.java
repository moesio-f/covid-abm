package br.ufrpe.abm.runner;

import java.util.Map;


/**
 * Interface for runner configuration objects.
 *
 * @version 1.0
 */
public interface IRunnerConfig {

  /**
   * Returns the number of full experiments executed by the runner (i.e., number of instances of the
   * problem solved by the algorithm).
   *
   * @return a {@link String}.
   */
  int numberOfExperiments();

  /**
   * Returns the name of the runner.
   *
   * @return a {@link String}
   */
  String runnerName();

  /**
   * Returns the name of the algorithm associated with the runner.
   *
   * @return a {@link String}.
   */
  String algorithmName();

  /**
   * Returns the name of the problem solved by the algorithm.
   *
   * @return a {@link String}.
   */
  String problemName();

  /**
   * Stringifies the full configuration in a human-readable text.
   *
   * @return a {@link String}.
   */
  String stringify();

  /**
   * Returns the full configuration description as a Map. Every key is a configuration variable.
   *
   * @return a {@link Map} from a String to an Object.
   */
  Map<String, Object> asMap();
}
