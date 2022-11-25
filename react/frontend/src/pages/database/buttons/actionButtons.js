// material-ui
import { Grid, Typography, Stack } from '@mui/material';
import { PendingActions } from '@mui/icons-material';
// project import
import DataBaseButtons from './button';
import { gridParameters } from '../styles';

export const ActionButtons = () => {
    return (
        <Grid>
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
                    <DataBaseButtons href={'dbs/actions/actions'} Title={'Actions'} Icon={PendingActions} />
                </Grid>
            </Grid>
        </Grid>
    );
};
