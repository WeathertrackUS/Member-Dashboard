import React, { useState, useEffect } from 'react';

const FileManager = () => {
    const [files, setFiles] = useState([]);

    useEffect(() => {
        // Fetch files from the backend
        const fetchFiles = async () => {
            try {
                const response = await fetch('/api/assets');
                const data = await response.json();
                setFiles(data);
            } catch (error) {
                console.error('Error fetching files:', error);
            }
        };

        fetchFiles();
    }, []);

    const handleDownload = (fileName) => {
        // Logic to download the file
        const link = document.createElement('a');
        link.href = `/api/assets/download/${fileName}`;
        link.setAttribute('download', fileName);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };

    return (
        <div className="file-manager">
            <h2>File Manager</h2>
            <ul>
                {files.map((file) => (
                    <li key={file.name}>
                        {file.name}
                        <button onClick={() => handleDownload(file.name)}>Download</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default FileManager;