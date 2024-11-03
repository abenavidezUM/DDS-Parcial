from repositories.dna_repository import get_dna_record, save_dna_record

async def is_mutant(dna: list[str]) -> bool:
    n = len(dna)
    sequences_found = 0

    dna_sequence = ','.join(dna)

    record = await get_dna_record(dna_sequence)
    if record:
        return record['is_mutant']

    def has_sequence(x, y, dx, dy):
        char = dna[x][y]
        for i in range(1, 4):
            nx, ny = x + i * dx, y + i * dy
            if nx >= n or ny >= n or ny < 0 or dna[nx][ny] != char:
                return False
        return True

    for i in range(n):
        for j in range(n):
            if dna[i][j]:
                if j <= n - 4 and has_sequence(i, j, 0, 1):
                    sequences_found += 1
                if i <= n - 4 and has_sequence(i, j, 1, 0):
                    sequences_found += 1
                if i <= n - 4 and j <= n - 4 and has_sequence(i, j, 1, 1):
                    sequences_found += 1
                if i <= n - 4 and j >= 3 and has_sequence(i, j, 1, -1):
                    sequences_found += 1

            if sequences_found > 1:
                print(f"Se detectaron {sequences_found} secuencias, es mutante.")
                await save_dna_record(dna_sequence, True)
                return True

    print(f"Se detectaron {sequences_found} secuencias, no es mutante.")
    await save_dna_record(dna_sequence, False)
    return False

