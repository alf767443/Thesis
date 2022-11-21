import { useState } from 'react';

// material-ui
import { Grid } from '@mui/material';

// project import
import debugBoxe from 'graphs/debugBox';
import SalesColumnChart from 'graphs/SalesColumnChart';
import DinamicGrid from 'components/DinamicGrid';
import MonthlyBarChart from './MonthlyBarChart';

// assets
import { GiftOutlined, MessageOutlined, SettingOutlined } from '@ant-design/icons';

// ==============================|| DASHBOARD - DEFAULT ||============================== //

const DashboardDefault = () => {
    const [value, setValue] = useState('today');
    const [slot, setSlot] = useState('week');

    return (
        <Grid container rowSpacing={4.5} columnSpacing={2.75}>
            {/* Main block */}
            <DinamicGrid Itens First={MonthlyBarChart} Second={SalesColumnChart} Third={SalesColumnChart} Fourth={MonthlyBarChart} />
            <DinamicGrid Itens First={MonthlyBarChart} Second={SalesColumnChart} Third={SalesColumnChart} Fourth={MonthlyBarChart} />
        </Grid>
    );
};

export default DashboardDefault;
