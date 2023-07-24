import React from 'react';
import { Button, Form, Input, Select } from 'antd';
const { Option } = Select;
const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 16,
  },
};
const tailLayout = {
  wrapperCol: {
    offset: 8,
    span: 16,
  },
};
const Form_ = () => {

  const [productId, setproductId] = React.useState('null');
//   const [password, setPassword] = React.useState('');
//   const [passwordCheck, setPasswordCheck] = React.useState('');
  const [info, setInfo] = React.useState('null');
  const [role, setRole] = React.useState('null');

  const formRef = React.useRef(null);

//   const jsonstring = JSON.stringify({
//     address: sessionStorage.getItem('addr');
//     productId: productId
//
//     
//   });

  const onFinish = (values) => {
    console.log(values);
    console.log(info);
    console.log(role);
  };

  const onReset = () => {
    formRef.current?.resetFields();
  };
  return (
    <Form
      {...layout}
      ref={formRef}
      name="control-ref"
      onFinish={onFinish}
      style={{
        maxWidth: 600,
        justifyContent: 'center',
      }}
    >
      <Form.Item
        name="Character"
        label="character"
        rules={[
          {
            required: true,
          },
        ]}
      >
        <Select
          allowClear
          onChange = {e => setRole(e)}
        >
          <Option value="Dairy farmer">Dairy farmer</Option>
          <Option value="Packergers and Distributors">Packergers and Distributor</Option>
          <Option value="Retailers">Retailers</Option>
          <Option value="Processor">Processor</Option>
        </Select>
      </Form.Item>

      {/* <Form.Item
        noStyle
        shouldUpdate={(prevValues, currentValues) => prevValues.Character !== currentValues.Character}
      >
        {({ getFieldValue }) =>
          getFieldValue('Character') !== 'Dairy farmer' ? (
            <Form.Item
              name="Product ID"
              label="Product ID"
              rules={[
                {
                  required: true,
                },
              ]}
            >
              <Input />
            </Form.Item>
          ) : null
        }
      </Form.Item> */}
      <Form.Item
        name="Product ID"
        label="Product ID"
        rules={[
          {
            required: true,
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        name="status"
        label="Milk status"
        rules={[
          {
            required: true,
          },
        ]}
      >
        <Select
          //onChange={onGenderChange}
          allowClear
        >
          <Option value="producing">Producing</Option>
          <Option value="processing">Processing</Option>
          <Option value="packing">Packing</Option>
          <Option value="delivered">Delivered</Option>
          <Option value="dispatching">Dispatching</Option>
        </Select>
      </Form.Item>
      <Form.Item
        name="expiry"
        label="expiry date"
        rules={[
          {
            required: true,
          },
        ]}
      >
        <Input />
      </Form.Item>
      <Form.Item
        name="infomation"
        label="other infomation"
        rules={[
          {
            required: true,
          },
        ]}
      >
        <Input.TextArea onChange = {e => setInfo(e.target.value)}/>
      </Form.Item>
      <Form.Item {...tailLayout}>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
        <Button htmlType="button" onClick={onReset}>
          Reset
        </Button>
      </Form.Item>
    </Form>
  );
};
export default Form_;