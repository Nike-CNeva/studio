export const getUrgencyOptions = () => {
  return [
    { value: 'LOW', label: 'Low' },
    { value: 'MEDIUM', label: 'Medium' },
    { value: 'HIGH', label: 'High' },
  ];
};

export const getStatusOptions = () => {
  return [
    { value: 'NEW', label: 'New' },
    { value: 'IN_WORK', label: 'In Work' },
    { value: 'COMPLETED', label: 'Completed' },
    { value: 'CANCELED', label: 'Canceled' },
    { value: 'ON_HOLD', label: 'On Hold' },
  ];
};
