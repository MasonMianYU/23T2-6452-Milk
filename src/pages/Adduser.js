import React from 'react';
import { Input, Layout, theme , Space } from 'antd';
import Menubar from '../components/Menubar';
const { Header, Content, Footer, Sider } = Layout;

const { Search } = Input;
const Adduser = () => {
  const [addr, setAddr] = React.useState('');
  const {
    token: { colorBgContainer },
  } = theme.useToken();
  const jsonstring = JSON.stringify({
    user_address: addr,
  });

  const requestoption = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: jsonstring,
  };

  
  const onSearch = () => {
    // fetch('http://127.0.0.1:5000/addAdmin', requestoption)
    // .then((r) => {
    //   if (r.status === 200) {
    //     r.json().then((data) => {
    //       console.log(data);
    //       alert('success');
    //       navigate('/input');
    //     });
       
    //   } else {
    //     r.json().then((data) => {
    //     alert(data['message']);  
    //     });
    //   }
    // })
  };
  return (
    <Layout hasSider>
      <Sider
        style={{
          overflow: 'auto',
          height: '100vh',
          position: 'fixed',
          left: 0,
          top: 0,
          bottom: 0,
        }}
      >
        <div className="demo-logo-vertical" />
        <Menubar />
      </Sider>
      <Layout
        className="site-layout"
        style={{
          marginLeft: 200,
        }}
      >
        <Header
          style={{
            padding: 0,
            background: colorBgContainer,
          }}
        />
        <Content
          style={{
            margin: '24px 16px 0',
            height:"1000px",
            overflow: 'initial',
          }}
        >
          <h1>add new user who can acess the chain</h1>
          <div
            style={{
              padding: 60,
              textAlign: 'center',
              background: colorBgContainer,
            }}
          >
            <Space direction="vertical">
                <Search
                placeholder="input user ad6ress"
                allowClear
                enterButton="Add"
                size="large"
                onSearch={onSearch}
                onChange = {e => setAddr(e.target.value)}
                />
            </Space>
          </div>
        </Content>
        <Footer
          style={{
            textAlign: 'center',
          }}
        >
        UNSW ©2023 Created by group 14
        </Footer>
      </Layout>
    </Layout>
  );
};
export default Adduser;