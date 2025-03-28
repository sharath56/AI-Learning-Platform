import React, { useState } from 'react';
import axios from '../services/api';

function CreateUser() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await axios.post('/users/create', { name, email });
        console.log(response.data);
    };

    return (
        <div>
            <h1>Create User</h1>
            <form onSubmit={handleSubmit}>
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" />
                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
                <button type="submit">Create</button>
            </form>
        </div>
    );
}

export default CreateUser;
