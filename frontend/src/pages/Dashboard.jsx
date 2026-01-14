import {
  Box,
  Grid,
  Paper,
  Typography,
  Card,
  CardContent,
} from '@mui/material';
import {
  People as PeopleIcon,
  LocationOn as LocationIcon,
  EventNote as EventIcon,
  School as SchoolIcon,
} from '@mui/icons-material';

const Dashboard = () => {
  const stats = [
    {
      title: 'Usuarios',
      value: '0',
      icon: <PeopleIcon sx={{ fontSize: 40 }} />,
      color: '#C20E1A',
    },
    {
      title: 'Áreas',
      value: '0',
      icon: <LocationIcon sx={{ fontSize: 40 }} />,
      color: '#599876',
    },
    {
      title: 'Actividades',
      value: '0',
      icon: <EventIcon sx={{ fontSize: 40 }} />,
      color: '#RD5AA2',
    },
    {
      title: 'Campus',
      value: '0',
      icon: <SchoolIcon sx={{ fontSize: 40 }} />,
      color: '#DC911B',
    },
  ];

  return (
    <Box>
      <Typography variant="h4" sx={{ mb: 3, color: 'primary.main', fontWeight: 600 }}>
        Dashboard
      </Typography>

      <Grid container spacing={3}>
        {stats.map((stat, index) => (
          <Grid item xs={12} sm={6} md={3} key={index}>
            <Card
              elevation={2}
              sx={{
                height: '100%',
                transition: 'transform 0.2s',
                '&:hover': {
                  transform: 'translateY(-4px)',
                  boxShadow: 4,
                },
              }}
            >
              <CardContent>
                <Box
                  sx={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                  }}
                >
                  <Box>
                    <Typography color="text.secondary" variant="h6" sx={{ mb: 1 }}>
                      {stat.title}
                    </Typography>
                    <Typography variant="h3" sx={{ fontWeight: 600, color: stat.color }}>
                      {stat.value}
                    </Typography>
                  </Box>
                  <Box sx={{ color: stat.color, opacity: 0.7 }}>{stat.icon}</Box>
                </Box>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>

      <Box sx={{ mt: 4 }}>
        <Paper sx={{ p: 3 }}>
          <Typography variant="h5" sx={{ mb: 2, color: 'primary.main' }}>
            Bienvenido al Sistema de Información
          </Typography>
          <Typography variant="body1" color="text.secondary" paragraph>
            Sección de Cultura, Recreación y Deporte - Universidad del Valle
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Utilice el menú lateral para navegar por las diferentes secciones del sistema.
          </Typography>
        </Paper>
      </Box>
    </Box>
  );
};

export default Dashboard;
