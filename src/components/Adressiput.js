import React ,{ useEffect }from 'react';
import { Input, Space, Button } from 'antd';
import { useNavigate } from 'react-router-dom'; // Change from useHistory to useNavigate

const Adressiput = () => {
  const navigate = useNavigate(); // Change from useHistory to useNavigate
  const [addr, setAddr] = React.useState('');
//   const jsonstring = JSON.stringify({
//     address: addr,
//   });

//   const requestoption = {
//     method: 'POST',
//     headers: { 'Content-Type': 'application/json' },
//     body: jsonstring,
//   };

  const handleButtonClick = () => {
    console.log(addr);
    sessionStorage.setItem('is_manager', 'true');
    console.log(sessionStorage);
    // fetch('http://127.0.0.1:5000/account/wallet/create_item', requestoption)
    // .then((r) => {
    //   if (r.status === 200) {
    //     r.json().then((data) => {
    //       console.log(data);
    //       alert('success');
    //       navigate('/input');
          
    //     });
       
    //   } else {
    //     r.json().then((data) => {
    //     });
    //   }
    // })
    navigate('/input'); // Change history.push to navigate
  };

  return (
    <Space.Compact style={{ width: '80%' }}>
      <Input defaultValue="Enter your address" onChange = {e => setAddr(e.target.value)}/>
      <Button type="primary" onClick={handleButtonClick}>
        Submit
      </Button>
    </Space.Compact>
  );
};

export default Adressiput;

