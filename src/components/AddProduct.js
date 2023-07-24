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
const AddP = () => {

  const [product, setProduct] = React.useState('null');

  const formRef = React.useRef(null);

  const jsonstring = JSON.stringify({
    user_address: sessionStorage.getItem('addr'),
    product_type: product
  });

  const requestoption = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: jsonstring,
  };

  const onFinish = () => {
    // fetch('http://127.0.0.1:5000/createBatch', requestoption)
    // .then((r) => {
    //   if (r.status === 200) {
    //     r.json().then((data) => {
    //       console.log(data);
    //       alert('success');
    //       navigate('/info');
    //     });
    //   } else {
    //     r.json().then((data) => {
    //       alert(data.message);  
    //     });
    //   }
    // })
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
        name="expiry"
        label="product Name"
        rules={[
          {
            required: true,
          },
        ]}
        onChange = {e => setProduct(e.target.value)}
      >
        <Input />
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
export default AddP;