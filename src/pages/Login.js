import React from 'react';
import { UserOutlined } from '@ant-design/icons';
import { Layout, theme , Avatar, Space} from 'antd';
import Adressiput from '../components/Adressiput';
const { Header, Content, Footer } = Layout;


const Login = () => {


  const {
    token: { colorBgContainer },
  } = theme.useToken();
  return (
    <Layout className="layout">
      <Header
        style={{
          display: 'flex',
          alignItems: 'center',
          color: '#00FFFF',
        }}
      >
        <div className="demo-logo" />
        <h1>6452 Milk Trace to source</h1>
      </Header>
      <Content

        style={{
          padding: '0 50px',
          
        }}
      >
        <div
          className="site-layout-content"
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: 50,
            minHeight: 50,
            background: colorBgContainer,
          }}
        >
        <Space wrap size={16}>
            <Avatar
            shape="square" size={200} 
            icon={<UserOutlined />} 
            />
        </Space>
        </div>

        <div
          className="site-layout-content"
          style={{
            padding: 50,
            minHeight: 50,
            background: colorBgContainer,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          <Adressiput />
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
  );
};
export default Login;