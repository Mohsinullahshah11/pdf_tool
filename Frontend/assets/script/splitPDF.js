async function fetchData() {
    try {
      const response = await fetch('http://127.0.0.1:5500/api/greet?name=Mohsin', {
        method: 'GET', // or 'POST', etc.
        // headers: {
        //   'Content-Type': 'application/json',
        // }
      });
  
    //   if (!response.ok) {
    //     throw new Error(`HTTP error! status: ${response.status}`);
    //   }
  
      const data = await response.json();
      console.log('Success:', data);
    } catch (error) {
      console.error('Error:', error);
    }
  }
  
  fetchData();
  