// src/lib/api.ts

const API_BASE_URL = "http://localhost:8000"; // FastAPI backend URL

export async function createTask(taskData: any): Promise<any> {
  const response = await fetch(`${API_BASE_URL}/tasks/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(taskData),
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }

  return await response.json();
}

export async function readTasks(): Promise<any[]> {
  const response = await fetch(`${API_BASE_URL}/tasks/`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }

  return await response.json();
}
