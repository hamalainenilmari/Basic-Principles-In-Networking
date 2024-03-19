# Exercise 3 Authentication

## 1. Goals of the experiment

- **Understanding and Implementing Endpoint Authentication**: The primary objective is to help students understand the concept of endpoint authentication, a crucial security mechanism in networking. This involves ensuring that only authorized devices, such as laptops, smartphones, tablets, and other TCP/IP network-connected hardware, can access a specific network, site, or service. The experiment aims to provide hands-on experience with the practical aspects of securing network endpoints, which is increasingly important in the realms of machine-to-machine (M2M) communications and the Internet of Things (IoT).

- **Exploring Authentication Methods in Networking**: A significant part of the experiment is exploring and understanding various authentication methods used in 802.11 (Wi-Fi) networks. This includes not only identifying these methods but also describing them in detail, thereby enhancing our knowledge of how different authentication mechanisms work and their applications in real-world scenarios.

- **Practical Application and Analysis**: Through the creation of a sketch (a program written for microcontrollers like those in Arduino boards) that performs specific tasks such as printing the board's MAC address, scanning for encrypted Wi-Fi networks, and connecting to a network via authentication, we get to apply theoretical knowledge in a practical setting. This hands-on approach helps in solidifying understanding and encourages problem-solving and analytical skills.

- **Security Analysis**: The bonus task of attempting to brute force a Wi-Fi password, although ethically questionable, is designed to give students insight into the vulnerabilities and security aspects of Wi-Fi networks. By experimenting with different password complexities, we can observe the importance of strong, secure passwords and learn about methods to safeguard networks against such attacks.

## 2. Experimental Setup

Connecting to a network

- Installing WiFINiNA library to Arduino IDE
- Creating the sketch for printing network info and connecting to a network
- Testing the sketch

Brute force

- 

## 3. Results & Conclusion



## 4. Answer to the given questions

### 4.1 Which authentication methods did you find for 802.11?

We found three of them:

1. Open System Authentication (OSA)

2. Shared Key Authentication (SKA), a method using a pre-shared key (WEP key)

3. Wi-Fi Protected Access (WPA and WPA2/WPA3)

### 4.2 Please describe three authentication methods in detail

- OSA is the simplest form of authentication for 802.11 networks. In this method, any device can request authentication from another device and will be authenticated without any identity verification. Essentially, it's a null authentication process where the authentication step is bypassed, leading directly to association with the access point (AP).

- SKA is a more secure method compared to OSA. It uses a pre-shared key (WEP key) that both the client and the AP must know in advance. During authentication, the AP sends a challenge text to the client, which encrypts it using the shared key and sends it back. The AP then decrypts the message to verify the client's identity. However, due to vulnerabilities in the WEP encryption, this method is considered insecure by modern standards.

- WPA and its successors, WPA2 and WPA3, are security protocols developed to address the vulnerabilities in previous authentication methods. WPA uses the Temporal Key Integrity Protocol (TKIP) for encryption, which dynamically changes keys to prevent unauthorized access. WPA2 enhances security by introducing the Advanced Encryption Standard (AES) and is mandatory for all new devices to be Wi-Fi certified. WPA3, the latest, provides more robust protections through features like individualized data encryption, protection against brute-force attacks, and easier secure setup for devices without displays.

### 4.3 Describe briefly applications scenarios for these methods

- OSA is commonly used in networks where data security is not a concern, such as in public Wi-Fi hotspots or guest networks. It facilitates easy connectivity but should be used with caution due to the lack of security measures, making it suitable for environments where ease of access is prioritized over network security.
- Initially, SKA was used in environments where a higher level of security than OSA was required, such as small offices or private networks. However, due to its vulnerabilities, it's now largely obsolete and replaced by more secure standards like WPA and WPA2.
- WPA/WPA2 is widely used in both personal and enterprise settings, offering a strong level of security suitable for home networks, businesses, and sensitive environments. WPA3, being the latest, is gradually being adopted for its enhanced security features and is expected to become the standard for securing Wi-Fi connections, especially in environments where data security and privacy are of paramount importance.

## 5. Annex

```C

```