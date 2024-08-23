import time
import random

# Initialize the traffic lights states
traffic_lights = [{"light": i, "state": "red"} for i in range(8)]

# Define the timing for each light state
yellow_duration = 2  # duration in seconds
green_duration = 8  # base duration in seconds

def simulate_traffic_density():
    # Simulate random traffic density for each light
    return [random.randint(1, 100) for _ in range(8)]

def update_traffic_lights(traffic_lights, active_light):
    # Set all lights to red
    for light in traffic_lights:
        light["state"] = "red"
    
    # Set the active light to green, and the next one to yellow
    traffic_lights[active_light]["state"] = "green"
    traffic_lights[(active_light + 1) % 8]["state"] = "yellow"

def display_traffic_lights(traffic_lights):
    for light in traffic_lights:
        print(f"Light {light['light']}: {light['state']}")
    print("-" * 40)

def run_traffic_system():
    while True:
        traffic_density = simulate_traffic_density()
        print("Traffic Density: ", traffic_density)
        
        # Find the light with the highest traffic density
        active_light = traffic_density.index(max(traffic_density))
        
        # Set the green light duration based on traffic density
        current_green_duration = green_duration + traffic_density[active_light] // 10
        
        # Update and display the traffic lights
        update_traffic_lights(traffic_lights, active_light)
        display_traffic_lights(traffic_lights)
        
        # Green light duration
        time.sleep(current_green_duration)
        
        # Yellow light duration
        update_traffic_lights(traffic_lights, active_light)
        display_traffic_lights(traffic_lights)
        time.sleep(yellow_duration)

if __name__ == "__main__":
    run_traffic_system()
