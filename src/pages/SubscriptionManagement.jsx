import React, { useState } from 'react';
import { TextField, Button, List, ListItem, ListItemText } from '@mui/material';

const SubscriptionManagement = () => {
  const [subscriptionUrl, setSubscriptionUrl] = useState('');
  const [subscriptionUrls, setSubscriptionUrls] = useState([]);
  const [sshKey, setSshKey] = useState('');

  const handleAddUrl = () => {
    if (subscriptionUrl.trim()) {
      setSubscriptionUrls([...subscriptionUrls, subscriptionUrl]);
      setSubscriptionUrl('');
    }
  };

  const handleSaveSshKey = () => {
    if (sshKey.trim()) {
      // 这里可以添加保存 SSH 密钥的逻辑
      console.log('保存的 SSH 密钥:', sshKey);
      setSshKey('');
    }
  };

  return (
    <div>
      <TextField
        label="订阅地址"
        value={subscriptionUrl}
        onChange={(e) => setSubscriptionUrl(e.target.value)}
        fullWidth
        margin="normal"
      />
      <TextField
        label="GitHub SSH 密钥"
        value={sshKey}
        onChange={(e) => setSshKey(e.target.value)}
        fullWidth
        margin="normal"
        multiline
        rows={4}
      />
      <Button variant="contained" color="primary" onClick={handleSaveSshKey}>保存 SSH 密钥</Button>
      <Button variant="contained" color="primary" onClick={handleAddUrl}>添加</Button>
      <List>
        {subscriptionUrls.map((url, index) => (
          <ListItem key={index}>
            <ListItemText primary={url} />
          </ListItem>
        ))}
      </List>
    </div>
  );
};

export default SubscriptionManagement;