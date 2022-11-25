import { useState } from 'react';

// material-ui
import { Grid, Box, Typography, Stack } from '@mui/material';
import {
    TireRepair,
    BatteryCharging90,
    BatterySaver,
    QrCode2,
    Explore,
    GpsFixed,
    Route,
    PendingActions,
    AdminPanelSettings,
    SettingsRemote
} from '@mui/icons-material';
// project import
import DataBaseButtons from './buttons/button';
import { SmartToy } from '../../../node_modules/@mui/icons-material/index';

// ==============================|| DASHBOARD - DEFAULT ||============================== //
const gridParameters = {
    xs: 'span 60',
    sm: 'span 30',
    md: 'span 20',
    lg: 'span 15',
    xl: 'span 12',
    direction: 'row',
    justifyContent: 'flex-start',
    alignItems: 'center',
    columnSpacing: '2rem',
    columns: '60'
};

const stackParameters = {
    direction: 'column',
    justifyContent: 'space-evenly',
    alignItems: 'flex-start',
    spacing: 2
};

const DataBase = () => {
    return (
        <Grid container rowSpacing={3} columnSpacing={1.25}>
            {/* Main block */}
            <Stack
                direction={stackParameters.direction}
                justifyContent={stackParameters.justifyContent}
                alignItems={stackParameters.alignItems}
                spacing={stackParameters.spacing}
            >
                {/*Spacing*/}
                <Typography variant="h3" color="textSecondary"></Typography>
                {/*Position databases*/}
                <Typography variant="h3" color="textSecondary">
                    Position databases
                </Typography>
                <Grid
                    container
                    columnSpacing={gridParameters.columnSpacing}
                    justifyContent={gridParameters.justifyContent}
                    direction={gridParameters.direction}
                    alignItems={gridParameters.alignItems}
                    columns={gridParameters.columns}
                >
                    <Grid
                        item
                        xs={gridParameters.xs}
                        sm={gridParameters.sm}
                        md={gridParameters.md}
                        lg={gridParameters.lg}
                        xl={gridParameters.xl}
                    >
                        <DataBaseButtons href={'dbs/position/odometry'} Title={'Odometry'} Icon={TireRepair} />
                    </Grid>
                    <Grid
                        item
                        xs={gridParameters.xs}
                        sm={gridParameters.sm}
                        md={gridParameters.md}
                        lg={gridParameters.lg}
                        xl={gridParameters.xl}
                    >
                        <DataBaseButtons href={'dbs/position/fiducialmark'} Title={'Fiducial marks'} Icon={QrCode2} />
                    </Grid>
                    <Grid
                        item
                        xs={gridParameters.xs}
                        sm={gridParameters.sm}
                        md={gridParameters.md}
                        lg={gridParameters.lg}
                        xl={gridParameters.xl}
                    >
                        <DataBaseButtons href={'dbs/position/gyroscope'} Title={'Gyroscope'} Icon={Explore} />
                    </Grid>
                    <Grid
                        item
                        xs={gridParameters.xs}
                        sm={gridParameters.sm}
                        md={gridParameters.md}
                        lg={gridParameters.lg}
                        xl={gridParameters.xl}
                    >
                        <DataBaseButtons href={'dbs/position/globalPosition'} Title={'Global position'} Icon={GpsFixed} />
                    </Grid>
                </Grid>
                {/*Battery databases*/}
                <Typography variant="h3" color="textSecondary">
                    Battery databases
                </Typography>
                <Grid
                    container
                    columnSpacing={gridParameters.columnSpacing}
                    justifyContent={gridParameters.justifyContent}
                    direction={gridParameters.direction}
                    alignItems={gridParameters.alignItems}
                    columns={gridParameters.columns}
                >
                    <Grid
                        item
                        xs={gridParameters.xs}
                        sm={gridParameters.sm}
                        md={gridParameters.md}
                        lg={gridParameters.lg}
                        xl={gridParameters.xl}
                    >
                        <DataBaseButtons href={'dbs/battery/physical'} Title={'Physical'} Icon={BatterySaver} />
                    </Grid>
                    <Grid
                        item
                        xs={gridParameters.xs}
                        sm={gridParameters.sm}
                        md={gridParameters.md}
                        lg={gridParameters.lg}
                        xl={gridParameters.xl}
                    >
                        <DataBaseButtons href={'dbs/battery/status'} Title={'Status'} Icon={BatteryCharging90} />
                    </Grid>
                </Grid>
                {/*Actions databases*/}
                <Typography variant="h3" color="textSecondary">
                    Actions databases
                </Typography>
                <Grid
                    container
                    columnSpacing={gridParameters.columnSpacing}
                    justifyContent={gridParameters.justifyContent}
                    direction={gridParameters.direction}
                    alignItems={gridParameters.alignItems}
                    columns={gridParameters.columns}
                >
                    <Grid
                        item
                        xs={gridParameters.xs}
                        sm={gridParameters.sm}
                        md={gridParameters.md}
                        lg={gridParameters.lg}
                        xl={gridParameters.xl}
                    >
                        <DataBaseButtons href={'dbs/battery/physical'} Title={'Actions'} Icon={PendingActions} />
                    </Grid>
                </Grid>
                {/*Route databases*/}
                <Typography variant="h3" color="textSecondary">
                    Route databases
                </Typography>
                <Grid
                    container
                    columnSpacing={gridParameters.columnSpacing}
                    justifyContent={gridParameters.justifyContent}
                    direction={gridParameters.direction}
                    alignItems={gridParameters.alignItems}
                    columns={gridParameters.columns}
                >
                    <Grid
                        item
                        xs={gridParameters.xs}
                        sm={gridParameters.sm}
                        md={gridParameters.md}
                        lg={gridParameters.lg}
                        xl={gridParameters.xl}
                    >
                        <DataBaseButtons href={'dbs/routes/routes'} Title={'Routes'} Icon={Route} />
                    </Grid>
                </Grid>
                {/*Decisions databases*/}
                <Typography variant="h3" color="textSecondary">
                    Decisions databases
                </Typography>
                <Grid
                    container
                    columnSpacing={gridParameters.columnSpacing}
                    justifyContent={gridParameters.justifyContent}
                    direction={gridParameters.direction}
                    alignItems={gridParameters.alignItems}
                    columns={gridParameters.columns}
                >
                    <Grid
                        item
                        xs={gridParameters.xs}
                        sm={gridParameters.sm}
                        md={gridParameters.md}
                        lg={gridParameters.lg}
                        xl={gridParameters.xl}
                    >
                        <DataBaseButtons href={'dbs/decisions/administrator'} Title={'Administrator'} Icon={AdminPanelSettings} />
                    </Grid>
                    <Grid
                        item
                        xs={gridParameters.xs}
                        sm={gridParameters.sm}
                        md={gridParameters.md}
                        lg={gridParameters.lg}
                        xl={gridParameters.xl}
                    >
                        <DataBaseButtons href={'dbs/decisions/remote'} Title={'Remote'} Icon={SettingsRemote} />
                    </Grid>
                    <Grid
                        item
                        xs={gridParameters.xs}
                        sm={gridParameters.sm}
                        md={gridParameters.md}
                        lg={gridParameters.lg}
                        xl={gridParameters.xl}
                    >
                        <DataBaseButtons href={'dbs/decisions/robot'} Title={'Robot'} Icon={SmartToy} />
                    </Grid>
                </Grid>
            </Stack>
        </Grid>
    );
};

export default DataBase;
