import { addDoc, collection, getDocs, query, where } from "firebase/firestore";
import { db } from "./firebase";

export const createAccount = async (address : string) => {
    const docColName = 'users'
    const users = collection(db, docColName);
    const q = query(users, where("walletAddress", "==", address));

    const querySnapshot = await getDocs(q);

    if(querySnapshot.docs.length) return
    
    const docRef = await addDoc(collection(db, docColName), {
        walletAddress: address,
    });
    console.log("Account created for", address);
}
