const getData = async (url : string, query: string) => {
    const data = {
        query: query
    }
    try {
        const response = await fetch(url, {
          method: 'POST', // Specifies the request method
          headers: {
            'Content-Type': 'application/json', // Specify that we are sending JSON
          },
          body: JSON.stringify(data), // Convert data to JSON string
          cache: 'no-store'
        });
    
        console.log('hi')
        // Check if response is OK
        if (response.ok) {
          const jsonResponse = await response.json(); // Parse the JSON response
          // console.log('Success:', jsonResponse); // Log the successful response
          return jsonResponse; // Optionally return the response for further use
        } else {
          console.error('HTTP Error:', response.status); // Log the error status
        }
      } catch (error) {
        console.error('Error:', error); // Catch and log any errors
      }
  }
const Check = async () => {
    const jj = await getData('https://44.204.195.204/chat', 'hey');
    console.log(jj)
    console.log('hi')
  return (
    <div>Check</div>
  )
}

export default Check