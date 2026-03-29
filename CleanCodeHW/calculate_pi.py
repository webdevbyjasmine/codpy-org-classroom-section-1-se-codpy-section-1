import random


RADIUS = 1.0
NUM_SAMPLES = 1_000_000


def is_inside_unit_circle(x: float, y: float) -> bool:
    return x**2 + y**2 <= RADIUS**2


def sample_random_point() -> tuple[float, float]:
    x = random.uniform(-RADIUS, RADIUS)
    y = random.uniform(-RADIUS, RADIUS)
    return x, y


def estimate_pi(num_samples: int) -> float:
    hits = sum(
        1 for _ in range(num_samples)
        if is_inside_unit_circle(*sample_random_point())
    )
    return (hits / num_samples) * 4


def main() -> None:
    pi_estimate = estimate_pi(NUM_SAMPLES)
    print(f"Estimated value of pi: {pi_estimate}")


if __name__ == "__main__":
    main()
