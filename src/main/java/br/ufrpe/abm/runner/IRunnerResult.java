package br.ufrpe.abm.runner;

import java.util.List;
import java.util.Map;
import tech.tablesaw.api.Table;
import tech.tablesaw.plotly.components.Figure;

public interface IRunnerResult {

  /**
   * <p>
   * Returns a Table containing solutions and their fitness. Solutions are stored in a String column
   * (i.e., {@link tech.tablesaw.api.StringColumn}) named 'solutions'. Fitness values are store in
   * Double column (i.e., {@link tech.tablesaw.api.DoubleColumn}) named 'fitness'.
   * </p>
   *
   * <p>
   * Specifics of the solutions representation in String is implementation-dependent.
   * </p>
   *
   * @return a {@link Table} relating solutions and their fitness.
   */
  Table solutionFitnessTable();

  /**
   * Returns a list of figures. Results contain at least one {@link Figure}. Callers can plot those
   * figures using {@link tech.tablesaw.plotly.Plot#show(Figure) Plot.show(Figure)} on each figure
   * in the list.
   *
   * @return a {@link String}.
   */
  List<Figure> figures();

  /**
   * Returns the full results description as a Map. Every key is a result variable (e.g., mean, max,
   * min, best solution).
   *
   * @return a {@link Map} from a String to an Object.
   */
  Map<String, Object> asMap();

  /**
   * Stringifies the full results in a human-readable text.
   *
   * @return a {@link String}.
   */
  String stringify();
}
