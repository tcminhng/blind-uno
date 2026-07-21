# BUNO (Blind UNO) — Assistive Gaming Device

> **An accessible Raspberry Pi & Computer Vision system enabling visually impaired individuals to play UNO independently through real-time card recognition, state tracking, and audio/haptic feedback.**

<p align="center">
  <img src="images/overview.JPG" alt="BUNO Hardware Setup Overview" width="550"/>
</p>

---

## 📌 Project Overview

**BUNO** bridges the accessibility gap in tabletop card games. By combining custom 3D-printed hardware, computer vision processing, and dual-button state logic, BUNO reads and tracks cards for visually impaired players without compromising game privacy or requiring third-party assistance.

### Key Features
* 📷 **Fixed Optical Scanning Box:** Custom enclosure provides consistent camera focus, framing, and light isolation.
* 🧠 **Real-Time Color & Symbol CV:** Preprocesses frames (HSV color masking, filtering) to detect colors (Red, Blue, Yellow, Green) and card numbers/actions.
* 🎧 **Private Audio Feedback:** Reads card identities directly to the user via Bluetooth/3.5mm audio.
* 📳 **Haptic Feedback:** Vibrates via a tactile motor to confirm successful actions or prompt retries.
* 🧠 **Smart Hand Inventory Tracking:** Maintains an active list of cards currently held in the user's hand.

---

## 🔄 System Logic & Workflow

The core state machine handles scanning, card verification, and inventory management using dual-button interaction.

<p align="center">
  <img src="images/flow_chart.jpeg" alt="BUNO State Machine Flowchart" width="450"/>
</p>

### User Interaction Model
* **Button A (Action / Scan):**
  * **Single Click:** Scans a new card to add to the player's active hand or updates table status.
  * **Double Click:** Confirms playing a card from the hand, removing it from the stored inventory.
* **Button B (Status Check):**
  * **Single Click:** Reads out the current cards held in hand (e.g., *"You have 4 cards: Red 3, Blue Skip, Yellow 2, and Wild"*).

---

## 🛠️ Hardware Setup & Electronics

The hardware consists of a top scanning enclosure resting on an electronics housing base containing the Raspberry Pi, power source, and breadboard.

<div align="center">

| Top View (Card Slot) | Internal Electronics & Wiring | Complete Assembly |
| :---: | :---: | :---: |
| <img src="images/top.JPG" width="250"/> | <img src="images/inside.JPG" width="250"/> | <img src="images/overview.JPG" width="250"/> |

</div>

### Enclosure Iterations (Autodesk Fusion 360)
The chassis evolved through physical testing to optimize ambient light entry and ease of card insertion.

---

## 📷 Computer Vision & Sample Captures

The internal camera captures high-contrast, framed views of the card face when inserted into the slot.

<div align="center">
<table width="100%">
  <tr>
    <td align="center" width="33.33%"><b>Blue 4 Card</b></td>
    <td align="center" width="33.33%"><b>Yellow 0 Card</b></td>
    <td align="center" width="33.33%"><b>Red 0 Card</b></td>
  </tr>
  <tr>
    <td align="center"><img src="images/captured_image.jpg" width="85%"/></td>
    <td align="center"><img src="images/captured_image%201.jpg" width="85%"/></td>
    <td align="center"><img src="images/captured_image%202.jpg" width="85%"/></td>
  </tr>
  <tr>
    <td align="center"><i>Captured Frame (Blue 4)</i></td>
    <td align="center"><i>Captured Frame (Yellow 0)</i></td>
    <td align="center"><i>Captured Frame (Red 0)</i></td>
  </tr>
</table>
</div>

---

## 💻 Tech Stack & Dependencies

* **Hardware:** Raspberry Pi, USB Webcam Module, Vibration Motor, Push Buttons, Power Bank.
* **Languages & Frameworks:** Python 3, OpenCV (Computer Vision), `RPi.GPIO` (Hardware Interface), `pyttsx3` (Text-to-Speech).
* **CAD Software:** Autodesk Fusion 360.
