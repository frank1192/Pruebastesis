import { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import {
  Box,
  Drawer,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  IconButton,
  Typography,
  Divider,
  useMediaQuery,
  useTheme,
} from '@mui/material';
import {
  Menu as MenuIcon,
  Dashboard as DashboardIcon,
  People as PeopleIcon,
  LocationOn as LocationIcon,
  School as SchoolIcon,
  EventNote as EventIcon,
  Category as CategoryIcon,
  Logout as LogoutIcon,
  ChevronLeft as ChevronLeftIcon,
} from '@mui/icons-material';
import useAuthStore from '../store/authStore';

const drawerWidth = 260;

const Sidebar = ({ open, onClose, onToggle }) => {
  const navigate = useNavigate();
  const location = useLocation();
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('md'));
  const logout = useAuthStore((state) => state.logout);
  const user = useAuthStore((state) => state.user);

  const menuItems = [
    { text: 'Dashboard', icon: <DashboardIcon />, path: '/dashboard' },
    { text: 'Usuarios', icon: <PeopleIcon />, path: '/dashboard/users' },
    { text: 'Áreas', icon: <LocationIcon />, path: '/dashboard/areas' },
    { text: 'Sedes', icon: <SchoolIcon />, path: '/dashboard/sedes' },
    { text: 'Campus', icon: <SchoolIcon />, path: '/dashboard/campus' },
    { text: 'Actividades', icon: <EventIcon />, path: '/dashboard/activities' },
    { text: 'Categorías', icon: <CategoryIcon />, path: '/dashboard/categories' },
  ];

  const handleNavigation = (path) => {
    navigate(path);
    if (isMobile) {
      onClose();
    }
  };

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  const drawerContent = (
    <Box sx={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
      {/* Header */}
      <Box
        sx={{
          p: 2,
          backgroundColor: 'primary.main',
          color: 'white',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
        }}
      >
        <Box>
          <Typography variant="h6" sx={{ fontWeight: 600 }}>
            UNIVALLE
          </Typography>
          <Typography variant="caption" sx={{ opacity: 0.9 }}>
            Sistema de Gestión
          </Typography>
        </Box>
        {!isMobile && (
          <IconButton onClick={onToggle} sx={{ color: 'white' }}>
            <ChevronLeftIcon />
          </IconButton>
        )}
      </Box>

      {/* User Info */}
      <Box sx={{ p: 2, backgroundColor: '#f5f5f5' }}>
        <Typography variant="body2" sx={{ fontWeight: 600 }}>
          {user?.name || 'Usuario'}
        </Typography>
        <Typography variant="caption" color="text.secondary">
          {user?.email || 'email@univalle.edu.co'}
        </Typography>
      </Box>

      <Divider />

      {/* Menu Items */}
      <List sx={{ flex: 1, pt: 2 }}>
        {menuItems.map((item) => (
          <ListItem key={item.text} disablePadding sx={{ mb: 0.5 }}>
            <ListItemButton
              onClick={() => handleNavigation(item.path)}
              selected={location.pathname === item.path}
              sx={{
                mx: 1,
                borderRadius: 1,
                '&.Mui-selected': {
                  backgroundColor: 'primary.main',
                  color: 'white',
                  '& .MuiListItemIcon-root': {
                    color: 'white',
                  },
                  '&:hover': {
                    backgroundColor: 'primary.dark',
                  },
                },
              }}
            >
              <ListItemIcon
                sx={{
                  color: location.pathname === item.path ? 'white' : 'primary.main',
                  minWidth: 40,
                }}
              >
                {item.icon}
              </ListItemIcon>
              <ListItemText
                primary={item.text}
                primaryTypographyProps={{
                  fontSize: '0.9rem',
                }}
              />
            </ListItemButton>
          </ListItem>
        ))}
      </List>

      <Divider />

      {/* Logout */}
      <List>
        <ListItem disablePadding>
          <ListItemButton onClick={handleLogout} sx={{ mx: 1, borderRadius: 1 }}>
            <ListItemIcon sx={{ color: 'error.main', minWidth: 40 }}>
              <LogoutIcon />
            </ListItemIcon>
            <ListItemText
              primary="Cerrar Sesión"
              primaryTypographyProps={{
                fontSize: '0.9rem',
              }}
            />
          </ListItemButton>
        </ListItem>
      </List>
    </Box>
  );

  return (
    <Drawer
      variant={isMobile ? 'temporary' : 'persistent'}
      open={open}
      onClose={onClose}
      sx={{
        width: drawerWidth,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: drawerWidth,
          boxSizing: 'border-box',
          borderRight: '1px solid rgba(0, 0, 0, 0.12)',
        },
      }}
    >
      {drawerContent}
    </Drawer>
  );
};

export default Sidebar;
