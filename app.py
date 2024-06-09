from flask import Flask # creating the Flask instance
from flask import render_template # to combine html and css pages in templates directory
from flask import request   # to handle the methods (POST/GET)
from flask import redirect, url_for # to redirect the site for given URL
from flask import session
from datetime import timedelta
import phishingPrediction
import requests
import SQLi
import os
import socket
import sys
import passManager 

USER = "admin"
PASS = "admin"
FirewallStatus = "START"


app = Flask(__name__)
app.secret_key = "this_is_not_real"
app.permanent_session_lifetime = timedelta(minutes=25)

# login page
@app.route("/", methods=["POST", "GET"])
@app.route("/login", methods=["POST", "GET"])
def login_page():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(f"username: {username}, password: {password}")
        detials = SQLi.select_loginSQL(username, password)
        print(detials)
        if len(detials) != 0:
            if (username == detials[0][2]) and (password == detials[0][3]):
                session["username"] = username
                session.permanent = True
                return render_template("index.html")
            else:
                return render_template("login.html")
        else:
            return render_template("register.html")
    else:
        if "username" in session:
            print(session.items())
            return render_template("index.html")
        return render_template("login.html")


# Register page
@app.route("/register", methods=["POST", "GET"])
def register_page():
    if "username" in session:
        return render_template("index.html")
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        password = request.form["password"]
        SQLi.insert_registerSQL(firstname, lastname, email, password)
        return redirect(url_for("login_page"))
    else:
        return render_template("register.html")


# Dashboard page
@app.route("/dashboard", methods=["POST", "GET"])
def dashboard_page():
    publicip = "103.28.246.254"
    privateip = "127.0.0.1"
    city = "Vellore"
    state = "Tamil Nadu"
    country = "IN"
    location = "12.9184,79.1325"
    pincode = "614620"
    timezone = "Asia/Kolkata"
    isp = "AS24186 RailTel Corporation of India Ltd"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        privateip = s.getsockname()[0]
        response = requests.get(" https://ipinfo.io/")
        response = response.json()
        publicip = response["ip"]
        city = response["city"]
        state = response["region"]
        country = response["country"]
        location = response["loc"]
        pincode = response["postal"]
        timezone = response["timezone"]
        isp = response["org"]
    except Exception as e:
        print(e)
        
    if "username" in session:
        return render_template("dashboard.html", publicip=publicip,privateip=privateip,    city=city, state=state, country=country,location=location, pincode=pincode,   timezone=timezone, isp=isp)
    else:
        return redirect(url_for("login_page"))


# Firewall page
@app.route("/firewall", methods=["POST", "GET"])
def firewall_page():
    if request.method == "POST":
        print(f"{FirewallStatus}")
        return render_template("firewall.html", firewall=FirewallStatus)
    else:
        print(f"{FirewallStatus}")
        return render_template("firewall.html", firewall=FirewallStatus)

@app.route("/firewall_status", methods=['POST', "GET"])
def firewall_status():
    global FirewallStatus
    if request.method == "POST":
        status = request.form.get("status")
        print(f"firewall status {status}")
        if status == "START":
            os.system("sudo bash rules/firewall.sh")
            FirewallStatus = "STOP"
        else:
            os.system("sudo bash rules/stop_rule.sh")
            FirewallStatus = "START"
        return ("", 204)


# Domain Blocking Page
@app.route("/domainblocking", methods=["POST", "GET"])
def domain_blocking_page():
    if "username" in session:
        detials = SQLi.select_domainBlockingSQL()
        print(detials)
        domains = []
        host_file = open("hosts/hosts", "w")
        with open("hosts/original_hosts", "r") as file:
            host_file.write(file.read())
        host_file.close()
        host_file = open("hosts/hosts", "a")
        for i in detials:
            domains.append(i[0])
            host_file.writelines(f"127.0.0.1   {i[0]}\n")
        host_file.close()

        os.system("sudo cp hosts/hosts /etc/hosts")
            

        return render_template("domainblocking.html", domains=domains)
    else:
        return redirect(url_for("login_page"))

@app.route("/domain_url_2_block", methods=["POST", "GET"])
def domain_url_2_block():
    if request.method == 'POST':
        domain = request.form.get("url")
        print(domain)
        SQLi.insert_domainBlockingSQL(domain)
        return ("", 204)

@app.route("/domain_url_2_delete", methods=["POST", "GET"])
def domain_url_2_delete():
    if request.method == 'POST':
        domain = request.form.get("url_name")
        print(f"domain to delete {domain}")
        SQLi.delete_domainBlockingSQL(domain)
        return ("", 204)


# password manager
@app.route("/passwordmanager", methods=["POST", "GET"])
def password_manager_page():
    if "username" in session:
        if request.method == "GET":
            detials = SQLi.select_passwordManagerSQL()
            print(detials)
            passwordManagers = []
            for i in detials:
                passwordManagers.append(i)
            return render_template("passwordmanager.html", detials=passwordManagers)
    return redirect(url_for("login_page"))

@app.route("/expansion_panel_detials", methods=["POST", "GET"])
def expansion_panel_detials():
    if request.method == "POST":
        website = request.form.get("website_name");
        username = request.form.get("username");
        password = request.form.get("password");
        description = request.form.get("description");
        print(website, username, password, description)
        enc_password = passManager.encryption(password)
        SQLi.insert_passwordManagerSQL(website, username, enc_password, description)
        return ("", 204)

@app.route("/decrypt_password", methods=["POST", "GET"])
def decrypt_password():
    if request.method == "POST":
        decrypt = request.form.get("decrypt")
        dec_password = passManager.decryption(decrypt)
        print(dec_password)
        detials = SQLi.select_passwordManagerSQL()
        print(detials)
        passwordManagers = []
        for i in detials:
            passwordManagers.append(i)
        return render_template("passwordmanager.html", decrypt=dec_password, password="strong password", detials=passwordManagers)

@app.route("/generate_password", methods=["POST", "GET"])
def generate_password():
    if request.method == "POST":
        strong_password = passManager.strong_password_generator()
        print(f"{strong_password}")
        detials = SQLi.select_passwordManagerSQL()
        print(detials)
        passwordManagers = []
        for i in detials:
            passwordManagers.append(i)
        return render_template("passwordmanager.html", decrypt="decrypt", password=strong_password, detials=passwordManagers)
    
@app.route("/delete_from_manager", methods=['POST', 'GET'])
def delete_from_manager():
    if request.method == 'POST':
        website = request.form.get("url_name")
        print(f"website to delete {website}")
        SQLi.delete_passwordManagerSQL(website)
        return ("", 204)


# for Phishing URL detection
@app.route("/phishingurldetection", methods=["POST", "GET"])
def phishingurl_detection_page():
    if "username" in session:
        phish_percent = str(0) + '%'
        non_phish_percent = str(100) + '%'
        url = "https://google.com"
        return render_template("phishingurldetection.html", url=url, phish=phish_percent, nonphish=non_phish_percent)
    else:
        return redirect(url_for("login_page"))

@app.route("/phishing_urls", methods=["POST", "GET"])
def phishing_urls():
    if request.method == 'POST':
        url = request.form.get("url")
        result, phishing, non_phishing = phishingPrediction.phishPrediction(url)
        if int(phishing) > 10:
            SQLi.insert_phishingDetectionSQL(url)
        return render_template("phishingurldetection.html", url=url, phish=phishing, nonphish=non_phishing)
    

# for Help Page
@app.route("/help", methods=["POST", "GET"])
def help_page():
    return render_template("help.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
