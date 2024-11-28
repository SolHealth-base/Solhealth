// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// import { getAnalytics } from "firebase/analytics";
import { getFirestore } from "firebase/firestore";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCA9YBJde4dpMpu1A6BodlK83_lE5mQfbs",
  authDomain: "solhealth-e2647.firebaseapp.com",
  projectId: "solhealth-e2647",
  storageBucket: "solhealth-e2647.appspot.com",
  messagingSenderId: "77238429345",
  appId: "1:77238429345:web:5e959918c59b3f8136b2e0",
  measurementId: "G-3RGQPNBCFF"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
// const analytics = getAnalytics(app);
export const db = getFirestore(app)