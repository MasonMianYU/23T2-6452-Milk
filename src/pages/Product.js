import React from 'react';
import { Layout, theme } from 'antd';
import Menubar from '../components/Menubar';
import Inputarea from '../components/AddProduct';
const { Header, Content, Footer, Sider } = Layout;

const Addproduct = () => {
  const [addr, setAddr] = React.useState('');
  const {
    token: { colorBgContainer },
  } = theme.useToken();
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
            overflow: 'initial',
            height:'1000px'
          }}
        >
          <div
            style={{
              padding: 24,
              background: colorBgContainer,
            }}
          >
          <h1>Product creation</h1>
          </div>

          <div
            style={{
              padding: 24,
              textAlign: 'center',
              background: colorBgContainer,
            }}
          >
            <Inputarea />
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
export default Addproduct;