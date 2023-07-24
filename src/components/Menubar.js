import React from 'react';
import {
  ConsoleSqlOutlined,
  EuroCircleOutlined,
  PoweroffOutlined,
  AliwangwangOutlined,
  FileAddOutlined
} from '@ant-design/icons';
import { Menu } from 'antd';
import { useNavigate } from 'react-router-dom';

const item1 = [
  {
    key: '1',
    icon: React.createElement(EuroCircleOutlined),
    label: `input`,
    path: '/input',
  },
  {
    key: '2',
    icon: React.createElement(ConsoleSqlOutlined),
    label: `query`,
    path: '/info',
  },
  {
    key: '3',
    icon: React.createElement(AliwangwangOutlined),
    label: `add user`,
    path: '/add',
  },
  {
    key: '4',
    icon: React.createElement(FileAddOutlined),
    label: `add product`,
    path: '/product',
  },
  {
    key: '5',
    icon: React.createElement(PoweroffOutlined),
    label: `exit`,
    action: 'clearLocalStorage',
  }
];

// Helper function to modify item1 based on the "is admin" session storage value
const getModifiedItem1 = () => {
  const isAdmin = sessionStorage.getItem('is_manager') === 'true';
  if (isAdmin) {
    // If "is admin" is true, include item 3 in the array
    return item1;
  } else {
    // If "is admin" is false, exclude item 3 from the array
    return item1.filter(item => item.key !== '3');
  }
};

const Menubar = () => {
  const navigate = useNavigate();

  const handleMenuItemClick = (item) => {
    if (item.path) {
      navigate(item.path);
    }

    if (item.action === 'clearLocalStorage') {
      sessionStorage.clear();
      navigate('/');
    }
  };

  // Get the modified item1 array based on the "is admin" session storage value
  const modifiedItem1 = getModifiedItem1();

  return (
    <Menu theme="dark" mode="inline" >
      {modifiedItem1.map(item => (
        <Menu.Item key={item.key} icon={item.icon} onClick={() => handleMenuItemClick(item)} defaultSelectedKeys={[item.key]}>
          {item.label}
        </Menu.Item>
      ))}
    </Menu>
  );
};

export default Menubar;
