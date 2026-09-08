from time import perf_counter


# Problem 9a: Rekursiv LCS
def lcs_recursive(x, y, i, j):
    """Returnerer lengda på LCS for x[:i] og y[:j]."""

    # Base case: Ein tom streng har ingen felles subsekvens.
    if i == 0 or j == 0:
        return 0

    # Dei siste teikna er like. Ta teiknet med og kort ned begge.
    if x[i - 1] == y[j - 1]:
        return 1 + lcs_recursive(x, y, i - 1, j - 1)

    # Dei siste teikna er ulike. Prøv å korte ned kvar streng.
    return max(
        lcs_recursive(x, y, i - 1, j),
        lcs_recursive(x, y, i, j - 1),
    )


# Problem 9b: Dynamisk LCS
def lcs_dynamic(x, y):
    """Returnerer lengda på LCS ved hjelp av ein DP-tabell."""

    rows = len(x) + 1
    columns = len(y) + 1
    dp = [[0] * columns for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, columns):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(x)][len(y)]


def measure_time(function, *arguments):
    """Køyrer ein funksjon og returnerer resultat og tidsbruk."""

    start_time = perf_counter()
    result = function(*arguments)
    elapsed_time = perf_counter() - start_time
    return result, elapsed_time


# Problem 9c: Eksperiment med ulike strenglengder
def run_experiment():
    # Vi gjentar strengane frå oppgåve 8 og tek lengre prefiks.
    x_full = "babbabab" * 5
    y_full = "bbabbaaab" * 5

    lengths = [8, 12, 16, 20, 24, 28, 30, 32, 34, 36]
    slow_limit = 5.0

    print("\nProblem 9c - samanlikning av tidsbruk")
    print(f"{'Lengd':>6} {'Rekursiv':>12} {'Dynamisk':>12} {'LCS':>6}")
    print("-" * 42)

    for length in lengths:
        x = x_full[:length]
        y = y_full[:length]

        # Skriv ut lengda først, slik at vi ser kva test som køyrer.
        print(f"Testar lengd {length} ...", flush=True)

        recursive_result, recursive_time = measure_time(
            lcs_recursive, x, y, len(x), len(y)
        )
        dynamic_result, dynamic_time = measure_time(lcs_dynamic, x, y)

        # Begge algoritmane skal gi same LCS-lengd.
        assert recursive_result == dynamic_result

        print(
            f"{length:>6} "
            f"{recursive_time:>11.6f}s "
            f"{dynamic_time:>11.6f}s "
            f"{recursive_result:>6}"
        )

        # Stopp etter den første testen som bruker mykje tid.
        if recursive_time >= slow_limit:
            print(
                f"\nDen rekursive versjonen blei tydeleg treg "
                f"ved omtrent {length} teikn."
            )
            break


if __name__ == "__main__":
    # Kontroller oppgåve 9a og 9b med strengane frå oppgåve 8.
    first_string = "babbabab"
    second_string = "bbabbaaab"

    recursive_answer = lcs_recursive(
        first_string,
        second_string,
        len(first_string),
        len(second_string),
    )
    dynamic_answer = lcs_dynamic(first_string, second_string)

    print("Problem 9a - rekursivt svar:", recursive_answer)
    print("Problem 9b - dynamisk svar:", dynamic_answer)

    run_experiment()
