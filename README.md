<p align="center">
  <img src="assets/overview.jpg" alt="BUNO Hardware Setup Overview" width="550"/>
</p>

# BUNO (Blind UNO) — Assistive Gaming Device

> **An accessible Raspberry Pi & Computer Vision system enabling visually impaired individuals to play UNO independently through real-time card recognition, state tracking, and audio/haptic feedback.**

---

## 📌 Project Overview

**BUNO** bridges the accessibility gap in tabletop card games. By combining custom 3D-printed hardware, computer vision processing, and dual-button state logic, BUNO reads and tracks cards for visually impaired players without compromising game privacy or requiring third-party assistance.

### Key Features
* 📷 **Fixed Optical Scanning Box:** Custom enclosure provides consistent camera focus, framing, and light isolation.
* 🧠 **Real-Time Color & Symbol CV:** Preprocesses frames (HSV color masking, filtering) to detect colors (Red, Blue, Yellow, Green) and card numbers/actions.
* 🎧 **Private Audio Feedback:** Reads card identities directly to the user via Bluetooth/3.5mm audio.
* 📳 **Haptic Feedback:** Vibrates via a tactile motor to confirm successful actions or prompt retries.
* 🧠 **Smart Hand Inventory Tracking:** Maintains an active list of cards currently held in the user's hand[cite: 7].

---

## 🔄 System Logic & Workflow

The core state machine handles scanning, card verification, and inventory management using dual-button interaction[cite: 7].

<p align="center">
  <img src="assets/flow_chart.jpeg" alt="BUNO State Machine Flowchart" width="450"/>
</p>

### User Interaction Model
* **Button A (Action / Scan):**
  * **Single Click:** Scans a new card to add to the player's active hand or updates table status[cite: 7].
  * **Double Click:** Confirms playing a card from the hand, removing it from the stored inventory[cite: 7].
* **Button B (Status Check):**
  * **Single Click:** Reads out the current cards held in hand (e.g., *"You have 4 cards: Red 3, Blue Skip, Yellow 2, and Wild"*)[cite: 7].

---

## 🛠️ Hardware Setup & Electronics

The hardware consists of a top scanning enclosure resting on an electronics housing base containing the Raspberry Pi, power source, and breadboard.

| Top View (Card Slot) | Internal Electronics & Wiring | Complete Assembly |
| :---: | :---: | :---: |
| <img src="assets/top.jpg" width="250"/> | <img src="assets/inside.jpg" width="250"/> | <img src="assets/overview.jpg" width="250"/> |

### Enclosure Iterations (Autodesk Fusion 360)
The chassis evolved through physical testing to optimize ambient light entry and ease of card insertion.

| Initial Design (Solid Shell) | Final Design (Windowed Housing) |
| :---: | :---: |
| <img src="assets/first_design.jpg" width="350"/> | <img src="assets/final_design.jpg" width="350"/> |
| *Original fully enclosed concept.* | *Redesigned with side windows for easier card placement and natural illumination.* |

---

## 📷 Computer Vision & Sample Captures

The internal camera captures high-contrast, framed views of the card face when inserted into the slot.

| Blue 4 Card | Yellow 0 Card | Red 0 Card |
| :---: | :---: | :---: |
| <img src="assets/captured_image.jpg" width="230"/> | <img src="assets/captured_image 1.jpg" width="230"/> | <img src="assets/captured_image 2.jpg" width="230"/> |
| *Captured Frame (Blue 4)* | *Captured Frame (Yellow 0)* | *Captured Frame (Red 0)* |

---

## 💻 Tech Stack & Dependencies

* **Hardware:** Raspberry Pi, USB Webcam Module, Vibration Motor, Push Buttons, Power Bank.
* **Languages & Frameworks:** Python 3, OpenCV (Computer Vision), `RPi.GPIO` (Hardware Interface), `pyttsx3` (Text-to-Speech).
* **CAD Software:** Autodesk Fusion 360.
