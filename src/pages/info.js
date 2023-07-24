import React from 'react';
import { Input, Layout, theme , Space , Descriptions} from 'antd';
import Menubar from '../components/Menubar';
const { Header, Content, Footer, Sider } = Layout;

const { Search } = Input;
const If = () => {
  const [addr, setAddr] = React.useState('');
  const {
    token: { colorBgContainer },
  } = theme.useToken();
  const jsonstring = JSON.stringify({
    batch_id: addr,
  });

  const requestoption = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: jsonstring,
  };

  const onSearch = () => {
    
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
          <h1>search for all record</h1>
          <div
            style={{
              padding: 24,
              textAlign: 'center',
              background: colorBgContainer,
            }}
          >
            <Space direction="vertical">
                <Search
                placeholder="input product Id"
                allowClear
                enterButton="Search"
                size="large"
                onSearch={onSearch}
                onChange = {e => setAddr(e.target.value)}
                />
            </Space>
          </div>
          <div
            style={{
              padding: 50,
              textAlign: 'center',
              background: colorBgContainer,
            }}
          >
            <Descriptions title="User Info">
                <Descriptions.Item label="UserName">Zhou Maomao</Descriptions.Item>
                <Descriptions.Item label="Telephone">1810000000</Descriptions.Item>
                <Descriptions.Item label="Live">Hangzhou, Zhejiang</Descriptions.Item>
                <Descriptions.Item label="Remark">empty</Descriptions.Item>
                <Descriptions.Item label="Address">
                No. 18, Wantang Road, Xihu District, Hangzhou, Zhejiang, China
                </Descriptions.Item>
            </Descriptions>
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
export default If;