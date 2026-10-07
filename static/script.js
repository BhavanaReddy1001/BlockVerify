```javascript
/* ================================
   BLOCKVERIFY - FRONTEND JAVASCRIPT
   ================================ */


/* ================================
   TAMPER DEMO
   ================================ */

const tamperButton = document.getElementById("tamper-button");
const resetButton = document.getElementById("reset-button");
const tamperResult = document.getElementById("tamper-result");
const cgpaInput = document.getElementById("new-cgpa");


/*
 * Show the tampering result when
 * the user modifies a blockchain block.
 */

if (tamperButton) {

    tamperButton.addEventListener("click", function () {

        if (!cgpaInput) {
            return;
        }


        const originalCgpa = "9.12";
        const newCgpa = cgpaInput.value;


        /*
         * Check whether the user actually
         * changed the CGPA.
         */

        if (newCgpa === originalCgpa) {

            alert("Please change the CGPA before modifying the block.");

            return;
        }


        /*
         * Show the tampering result.
         */

        if (tamperResult) {
            tamperResult.style.display = "flex";
        }


        /*
         * Change the button text so the
         * user knows the demo was triggered.
         */

        tamperButton.textContent = "Block Modified";

        tamperButton.disabled = true;

    });

}


/* ================================
   RESET TAMPER DEMO
   ================================ */

if (resetButton) {

    resetButton.addEventListener("click", function () {

        /*
         * Hide the tampering result.
         */

        if (tamperResult) {
            tamperResult.style.display = "none";
        }


        /*
         * Restore the original CGPA.
         */

        if (cgpaInput) {
            cgpaInput.value = "9.12";
        }


        /*
         * Restore the Modify Block button.
         */

        if (tamperButton) {

            tamperButton.textContent = "Modify Block";

            tamperButton.disabled = false;

        }

    });

}
```
