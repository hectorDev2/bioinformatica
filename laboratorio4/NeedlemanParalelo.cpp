#include <iostream>
#include <vector>
#include <omp.h>

using namespace std;

// Devuelve el puntaje para coincidencia o desajuste
int get_score(char a, char b, int match, int mismatch) {
    return (a == b) ? match : mismatch;
}

// Inicializa la matriz de puntuación con penalización de gap
void initialize_matrix(vector<vector<int>>& score_matrix, int n, int m, int gap_penalty) {
    // Inicialización de la primera fila y columna
    for (int i = 1; i <= n; i++) {
        score_matrix[i][0] = gap_penalty * i;
    }
    for (int j = 1; j <= m; j++) {
        score_matrix[0][j] = gap_penalty * j;
    }
}

// Llena la matriz de puntuación
void fill_matrix(const string& seq1, const string& seq2, vector<vector<int>>& score_matrix, int match, int mismatch, int gap_penalty) {
    int n = seq1.size();
    int m = seq2.size();

    // Llenado de la matriz en diagonales
    for (int k = 1; k <= n + m; k++) {
        #pragma omp parallel for
        for (int i = 1; i <= n; i++) {
            int j = k - i;
            if (j >= 1 && j <= m) {
                int match_score = score_matrix[i - 1][j - 1] + get_score(seq1[i - 1], seq2[j - 1], match, mismatch);
                int delete_score = score_matrix[i - 1][j] + gap_penalty;
                int insert_score = score_matrix[i][j - 1] + gap_penalty;
                score_matrix[i][j] = max({match_score, delete_score, insert_score});
            }
        }
    }
}

// Realiza el retroceso desde la esquina inferior derecha para obtener el alineamiento
pair<string, string> backtrack(const string& seq1, const string& seq2, const vector<vector<int>>& score_matrix, int match, int mismatch, int gap_penalty) {
    string alignment_a, alignment_b;
    int i = seq1.size();
    int j = seq2.size();

    // Retroceso
    while (i > 0 && j > 0) {
        int current_score = score_matrix[i][j];
        int score_diagonal = score_matrix[i - 1][j - 1];
        int score_up = score_matrix[i - 1][j];
        int score_left = score_matrix[i][j - 1];

        if (current_score == score_diagonal + get_score(seq1[i - 1], seq2[j - 1], match, mismatch)) {
            alignment_a = seq1[i - 1] + alignment_a;
            alignment_b = seq2[j - 1] + alignment_b;
            i--; j--;
        } else if (current_score == score_up + gap_penalty) {
            alignment_a = seq1[i - 1] + alignment_a;
            alignment_b = "-" + alignment_b;
            i--;
        } else {
            alignment_a = "-" + alignment_a;
            alignment_b = seq2[j - 1] + alignment_b;
            j--;
        }
    }

    // Manejo de gaps restantes
    while (i > 0) {
        alignment_a = seq1[i - 1] + alignment_a;
        alignment_b = "-" + alignment_b;
        i--;
    }

    while (j > 0) {
        alignment_a = "-" + alignment_a;
        alignment_b = seq2[j - 1] + alignment_b;
        j--;
    }

    return {alignment_a, alignment_b};
}

// Algoritmo de Needleman-Wunsch
pair<pair<string, string>, int> needleman_wunsch(const string& seq1, const string& seq2, int match, int mismatch, int gap_penalty) {
    int n = seq1.size();
    int m = seq2.size();
    
    // Matriz de puntuación
    vector<vector<int>> score_matrix(n + 1, vector<int>(m + 1, 0));

    // Inicializar la matriz
    initialize_matrix(score_matrix, n, m, gap_penalty);

    // Llenar la matriz
    fill_matrix(seq1, seq2, score_matrix, match, mismatch, gap_penalty);

    // Realizar el retroceso
    auto alignment = backtrack(seq1, seq2, score_matrix, match, mismatch, gap_penalty);

    // El puntaje final está en la esquina inferior derecha de la matriz
    int final_score = score_matrix[n][m];

    return {alignment, final_score};
}

int main() {
    // Secuencias de ejemplo
    string seq1 = "GCATGCG";
    string seq2 = "GATTACA";

    // Parámetros del alineamiento
    int match = 1;
    int mismatch = -1;
    int gap_penalty = -1;

    // Ejecución del algoritmo Needleman-Wunsch
    auto result = needleman_wunsch(seq1, seq2, match, mismatch, gap_penalty);

    // Imprimir alineamiento y puntaje
    cout << "Alineamiento:" << endl;
    cout << result.first.first << endl;
    cout << result.first.second << endl;
    cout << "Puntaje de alineamiento: " << result.second << endl;

    return 0;
}
