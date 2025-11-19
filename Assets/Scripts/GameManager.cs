using UnityEngine;

public class GameManager : MonoBehaviour
{
    public GameObject zombiePrefab;
    public float spawnInterval = 2f;
    public Transform[] spawnPoints;

    private float timer = 0f;

    void Update()
    {
        timer += Time.deltaTime;
        if (timer >= spawnInterval)
        {
            SpawnZombie();
            timer = 0f;
        }
    }

    void SpawnZombie()
    {
        int index = Random.Range(0, spawnPoints.Length);
        Instantiate(zombiePrefab, spawnPoints[index].position, Quaternion.identity);
    }
}
