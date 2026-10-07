from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import copy

from blockchain.blockchain import Blockchain


app = Flask(__name__)

# Create one blockchain instance for the application
blockchain = Blockchain()

# Keep a copy of original data for tampered blocks
original_student_data = {}


# ================================
# DASHBOARD
# ================================

@app.route("/")
def index():

    chain = blockchain.get_chain()
    chain_valid = blockchain.is_chain_valid()

    student_records = chain[1:]

    return render_template(
        "index.html",
        records=student_records,
        chain=chain,
        chain_valid=chain_valid
    )


# ================================
# STUDENT RECORDS
# ================================

@app.route("/records")
def records():

    chain = blockchain.get_chain()
    student_records = chain[1:]

    return render_template(
        "records.html",
        records=student_records
    )


# ================================
# ADD STUDENT RECORD
# ================================

@app.route("/add-record", methods=["GET", "POST"])
def add_record():

    if request.method == "POST":

        student_id = request.form["student_id"]
        name = request.form["name"]
        course = request.form["course"]
        semester = int(request.form["semester"])
        cgpa = float(request.form["cgpa"])

        student_data = {
            "student_id": student_id,
            "name": name,
            "course": course,
            "semester": semester,
            "cgpa": cgpa
        }

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        blockchain.add_block(student_data, timestamp)

        return redirect(url_for("records"))

    return render_template("add_record.html")


# ================================
# BLOCKCHAIN EXPLORER
# ================================

@app.route("/blockchain")
def blockchain_explorer():

    chain = blockchain.get_chain()
    chain_valid = blockchain.is_chain_valid()

    return render_template(
        "blockchain.html",
        chain=chain,
        chain_valid=chain_valid
    )


# ================================
# BLOCKCHAIN VERIFICATION
# ================================

@app.route("/verify")
def verify():

    is_valid = blockchain.is_chain_valid()

    return render_template(
        "index.html",
        verification_result=is_valid,
        chain_valid=is_valid,
        chain=blockchain.get_chain(),
        records=blockchain.get_chain()[1:]
    )


# ================================
# TAMPER DEMONSTRATION
# ================================

@app.route("/tamper", methods=["GET", "POST"])
def tamper():

    message = None
    tampered = False

    chain = blockchain.get_chain()

    if request.method == "POST":

        block_index = int(request.form["block_index"])
        new_cgpa = float(request.form["new_cgpa"])

        if block_index <= 0 or block_index >= len(chain):

            message = "Please select a valid student record."

        else:

            block = chain[block_index]

            # Save the original student data only once
            if block_index not in original_student_data:

                original_student_data[block_index] = copy.deepcopy(
                    block.student_data
                )

            original_cgpa = block.student_data["cgpa"]

            if new_cgpa == original_cgpa:

                message = "Please enter a different CGPA."

            else:

                # Intentionally modify the actual blockchain data
                block.student_data["cgpa"] = new_cgpa

                # Do not update the stored hash.
                # This makes the blockchain invalid.
                tampered = not blockchain.is_chain_valid()

                if tampered:

                    message = (
                        "Tampering detected. The blockchain is now invalid "
                        "because the block data no longer matches its hash."
                    )

    return render_template(
        "tamper.html",
        chain=chain,
        chain_valid=blockchain.is_chain_valid(),
        message=message,
        tampered=tampered
    )


# ================================
# RESET TAMPERED BLOCKCHAIN
# ================================

@app.route("/tamper/reset", methods=["POST"])
def reset_tamper():

    chain = blockchain.get_chain()

    # Restore every saved original student record
    for block_index, original_data in original_student_data.items():

        if 0 < block_index < len(chain):

            chain[block_index].student_data = copy.deepcopy(
                original_data
            )

    # Rebuild the hashes from the beginning of the chain
    for i in range(1, len(chain)):

        current_block = chain[i]

        current_block.previous_hash = chain[i - 1].hash

        current_block.hash = current_block.calculate_hash()

    # Clear saved tamper data
    original_student_data.clear()

    # Verify that the restored chain is actually valid
    if blockchain.is_chain_valid():

        return redirect(url_for("tamper"))

    return "Blockchain reset failed. The chain is still invalid.", 500


# ================================
# RUN FLASK APPLICATION
# ================================

if __name__ == "__main__":
    app.run(debug=True)