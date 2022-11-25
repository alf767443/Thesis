import { lazy } from 'react';

// project import
import Loadable from 'components/Loadable';
import MainLayout from 'layout/MainLayout';

// Render - Dashboard
const Dashboard = Loadable(lazy(() => import('pages/dashboard')));

// Render - Databases
const Database = Loadable(lazy(() => import('pages/database')));

const DBActions = Loadable(lazy(() => import('pages/database/actions')));
const DBAdministrator = Loadable(lazy(() => import('pages/database/administrator')));
const DBFiducialmark = Loadable(lazy(() => import('pages/database/fiducialmark')));
const DBGlobalposition = Loadable(lazy(() => import('pages/database/globalposition')));
const DBGyroscope = Loadable(lazy(() => import('pages/database/gyroscope')));
const DBOdometry = Loadable(lazy(() => import('pages/database/odometry')));
const DBPhysical = Loadable(lazy(() => import('pages/database/physical')));
const DBRemote = Loadable(lazy(() => import('pages/database/remote')));
const DBRobot = Loadable(lazy(() => import('pages/database/robot')));
const DBRoute = Loadable(lazy(() => import('pages/database/route')));
const DBStatus = Loadable(lazy(() => import('pages/database/status')));

// render - sample page
const SamplePage = Loadable(lazy(() => import('pages/extra-pages/SamplePage')));

// render - utilities
const Typography = Loadable(lazy(() => import('pages/components-overview/Typography')));
const Color = Loadable(lazy(() => import('pages/components-overview/Color')));
const Shadow = Loadable(lazy(() => import('pages/components-overview/Shadow')));
const AntIcons = Loadable(lazy(() => import('pages/components-overview/AntIcons')));

// ==============================|| MAIN ROUTING ||============================== //

const MainRoutes = {
    path: '/',
    element: <MainLayout />,
    children: [
        {
            path: '/',
            element: <Dashboard />
        },
        {
            path: 'information',
            children: [
                {
                    path: 'dashboard',
                    element: <Dashboard />
                },
                {
                    path: 'dbs',
                    children: [
                        {
                            path: '',
                            element: <Database />
                        },
                        {
                            path: 'position',
                            children: [
                                {
                                    path: 'odometry',
                                    element: <DBOdometry />
                                },
                                {
                                    path: 'globalPosition',
                                    element: <DBGlobalposition />
                                },
                                {
                                    path: 'fiducialmark',
                                    element: <DBFiducialmark />
                                },
                                {
                                    path: 'gyroscope',
                                    element: <DBGyroscope />
                                }
                            ]
                        },
                        {
                            path: 'routes',
                            children: [
                                {
                                    path: 'routes',
                                    element: <DBRoute />
                                }
                            ]
                        },
                        {
                            path: 'battery',
                            children: [
                                {
                                    path: 'status',
                                    element: <DBStatus />
                                },
                                {
                                    path: 'physical',
                                    element: <DBPhysical />
                                }
                            ]
                        },
                        {
                            path: 'decisions',
                            children: [
                                {
                                    path: 'administrator',
                                    element: <DBAdministrator />
                                },
                                {
                                    path: 'remote',
                                    element: <DBRemote />
                                },
                                {
                                    path: 'robot',
                                    element: <DBRobot />
                                }
                            ]
                        },
                        {
                            path: 'actions',
                            children: [
                                {
                                    path: 'actions',
                                    element: <DBActions />
                                }
                            ]
                        }
                    ]
                },
                {
                    path: 'logs',
                    element: <Dashboard />
                }
            ]
        },
        {
            path: 'sample-page',
            element: <SamplePage />
        },
        {
            path: 'shadow',
            element: <Shadow />
        },
        {
            path: 'typography',
            element: <Typography />
        },
        {
            path: 'icons/ant',
            element: <AntIcons />
        },
        {
            path: 'color',
            element: <Color />
        }
    ]
};

export default MainRoutes;
