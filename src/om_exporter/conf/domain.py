from typing import Dict

from ..grid import GridSpec

DOMAIN_GRIDS: Dict[str, Dict[str, GridSpec]] = {
    "CdsDomain": {
        "era5": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.25,
                "dy": 0.25,
            },
        },
        "era5_daily": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.25,
                "dy": 0.25,
            },
        },
        "era5_ocean": {
            "type": "RegularGrid",
            "params": {
                "nx": 720,
                "ny": 361,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.5,
                "dy": 0.5,
            },
        },
        "era5_ensemble": {
            "type": "RegularGrid",
            "params": {
                "nx": 720,
                "ny": 361,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.5,
                "dy": 0.5,
            },
        },
        "era5_land": {
            "type": "RegularGrid",
            "params": {
                "nx": 3600,
                "ny": 1801,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.1,
                "dy": 0.1,
            },
        },
        "era5_land_daily": {
            "type": "RegularGrid",
            "params": {
                "nx": 3600,
                "ny": 1801,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.1,
                "dy": 0.1,
            },
        },
        "cerra": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 1069,
                "ny": 1069,
                "latitude": (20.29228, 63.769516),
                "longitude": (-17.485962, 74.10509),
                "projection": {
                    "type": "LambertConformalConicProjection",
                    "params": {
                        "lambda0": 8.0,
                        "phi0": 50.0,
                        "phi1": 50.0,
                        "phi2": 50.0,
                        "radius": 6371229,
                    },
                },
            },
        },
        "ecmwf_ifs": {"type": "GaussianGrid", "params": {"grid_type": "o1280"}},
        "ecmwf_ifs_analysis": {
            "type": "GaussianGrid",
            "params": {"grid_type": "o1280"},
        },
        "ecmwf_ifs_analysis_long_window": {
            "type": "GaussianGrid",
            "params": {"grid_type": "o1280"},
        },
        "ecmwf_ifs_long_window": {
            "type": "GaussianGrid",
            "params": {"grid_type": "o1280"},
        },
    },
    "EcmwfDomain": {
        "ifs04": {
            "type": "RegularGrid",
            "params": {
                "nx": 900,
                "ny": 451,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 360 / 900,
                "dy": 180 / 450,
            },
        },
        "ifs04_ensemble": {
            "type": "RegularGrid",
            "params": {
                "nx": 900,
                "ny": 451,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 360 / 900,
                "dy": 180 / 450,
            },
        },
        "ifs025": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 360 / 1440,
                "dy": 180 / (721 - 1),
            },
        },
        "ifs025_ensemble": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 360 / 1440,
                "dy": 180 / (721 - 1),
            },
        },
        "wam025": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 360 / 1440,
                "dy": 180 / (721 - 1),
            },
        },
        "wam025_ensemble": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 360 / 1440,
                "dy": 180 / (721 - 1),
            },
        },
        "aifs025": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 360 / 1440,
                "dy": 180 / (721 - 1),
            },
        },
        "aifs025_single": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 360 / 1440,
                "dy": 180 / (721 - 1),
            },
        },
        "aifs025_ensemble": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 360 / 1440,
                "dy": 180 / (721 - 1),
            },
        },
    },
    "EcmwfEcpdsDomain": {
        "ifs": {"type": "GaussianGrid", "params": {"grid_type": "o1280"}},
        "wam": {"type": "GaussianGrid", "params": {"grid_type": "o1280"}},
    },
    "EcmwfSeasDomain": {
        "seas5": {"type": "GaussianGrid", "params": {"grid_type": "o320"}},
        "seas5_daily": {"type": "GaussianGrid", "params": {"grid_type": "o320"}},
        "seas5_monthly": {"type": "GaussianGrid", "params": {"grid_type": "o320"}},
        "ec46": {"type": "GaussianGrid", "params": {"grid_type": "o320"}},
        "ec46_weekly": {"type": "GaussianGrid", "params": {"grid_type": "o320"}},
        "seas5_12hourly": {"type": "GaussianGrid", "params": {"grid_type": "n160"}},
        "seas5_monthly_upper_level": {
            "type": "GaussianGrid",
            "params": {"grid_type": "n160"},
        },
    },
    "KnmiDomain": {
        "harmonie_arome_europe": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 676,
                "ny": 564,
                "latitude": (39.740627, 62.619324),
                "longitude": (-25.162262, 38.75702),
                "projection": {
                    "type": "RotatedLatLonProjection",
                    "params": {"latitude": -35.0, "longitude": -8.0},
                },
            },
        },
        "harmonie_arome_netherlands": {
            "type": "RegularGrid",
            "params": {
                "nx": 390,
                "ny": 390,
                "latMin": 49.0,
                "lonMin": 0.0,
                "dx": 0.029,
                "dy": 0.018,
            },
        },
    },
    "KmaDomain": {
        "gdps": {
            "type": "RegularGrid",
            "params": {
                "nx": 2560,
                "ny": 1920,
                "latMin": -90 + 180 / 1920 / 2,
                "lonMin": -180 + 360 / 2560 / 2,
                "dx": 360 / 2560,
                "dy": 180 / 1920,
            },
        },
        "ldps": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 602,
                "ny": 781,
                "latitude": 32.2569,
                "longitude": 121.834,
                "dx": 1500,
                "dy": 1500,
                "projection": {
                    "type": "LambertConformalConicProjection",
                    "params": {
                        "lambda0": 126.0,
                        "phi0": 38.0,
                        "phi1": 30.0,
                        "phi2": 60.0,
                        "radius": 6371229,
                    },
                },
            },
        },
    },
    "JaxaHimawariDomain": {
        "himawari_10min": {
            "type": "RegularGrid",
            "params": {
                "nx": 2401,
                "ny": 2401,
                "latMin": -60.0,
                "lonMin": 80.0,
                "dx": 0.05,
                "dy": 0.05,
            },
        },
        "himawari_70e_10min": {
            "type": "RegularGrid",
            "params": {
                "nx": 2801,
                "ny": 2401,
                "latMin": -60.0,
                "lonMin": 70.0,
                "dx": 0.05,
                "dy": 0.05,
            },
        },
        "mtg_fci_10min": {
            "type": "RegularGrid",
            "params": {
                "nx": 2801,
                "ny": 2401,
                "latMin": -60.0,
                "lonMin": -70.0,
                "dx": 0.05,
                "dy": 0.05,
            },
        },
    },
    "CmaDomain": {
        "grapes_global": {
            "type": "RegularGrid",
            "params": {
                "nx": 2880,
                "ny": 1440,
                "latMin": -89.9375,
                "lonMin": -180.0,
                "dx": 0.125,
                "dy": 0.125,
            },
        },
    },
    "DmiDomain": {
        "harmonie_arome_europe": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 1906,
                "ny": 1606,
                "latitude": 39.671,
                "longitude": -25.421997,
                "dx": 2000,
                "dy": 2000,
                "projection": {
                    "type": "LambertConformalConicProjection",
                    "params": {
                        "lambda0": 352.0,
                        "phi0": 55.5,
                        "phi1": 55.5,
                        "phi2": 55.5,
                        "radius": 6371229,
                    },
                },
            },
        },
    },
    "IconDomains": {
        "icon": {
            "type": "RegularGrid",
            "params": {
                "nx": 2879,
                "ny": 1441,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.125,
                "dy": 0.125,
            },
        },
        "iconEu": {
            "type": "RegularGrid",
            "params": {
                "nx": 1377,
                "ny": 657,
                "latMin": 29.5,
                "lonMin": -23.5,
                "dx": 0.0625,
                "dy": 0.0625,
            },
        },
        "iconD2": {
            "type": "RegularGrid",
            "params": {
                "nx": 1215,
                "ny": 746,
                "latMin": 43.18,
                "lonMin": -3.94,
                "dx": 0.02,
                "dy": 0.02,
            },
        },
        "iconD2_15min": {
            "type": "RegularGrid",
            "params": {
                "nx": 1215,
                "ny": 746,
                "latMin": 43.18,
                "lonMin": -3.94,
                "dx": 0.02,
                "dy": 0.02,
            },
        },
        "iconEps": {
            "type": "RegularGrid",
            "params": {
                "nx": 1439,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.25,
                "dy": 0.25,
            },
        },
        "iconEuEps": {
            "type": "RegularGrid",
            "params": {
                "nx": 689,
                "ny": 329,
                "latMin": 29.5,
                "lonMin": -23.5,
                "dx": 0.125,
                "dy": 0.125,
            },
        },
        "iconD2Eps": {
            "type": "RegularGrid",
            "params": {
                "nx": 1214,
                "ny": 745,
                "latMin": 43.18,
                "lonMin": -3.94,
                "dx": 0.02,
                "dy": 0.02,
            },
        },
    },
    "MetNoDomain": {
        "nordic_pp": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 1796,
                "ny": 2321,
                "latitude": (52.30272, 72.18527),
                "longitude": (1.9184653, 41.764282),
                "projection": {
                    "type": "LambertConformalConicProjection",
                    "params": {
                        "lambda0": 15.0,
                        "phi0": 63.0,
                        "phi1": 63.0,
                        "phi2": 63.0,
                        "radius": 6371229,
                    },
                },
            },
        },
    },
    "NbmDomain": {
        "nbm_conus": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 2345,
                "ny": 1597,
                "latitude": 19.229,
                "longitude": 233.723 - 360,
                "dx": 2539.7,
                "dy": 2539.7,
                "projection": {
                    "type": "LambertConformalConicProjection",
                    "params": {
                        "lambda0": 265 - 360,
                        "phi0": 0.0,
                        "phi1": 25.0,
                        "phi2": 25.0,
                        "radius": 6371200,
                    },
                },
            },
        },
        "nbm_alaska": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 1649,
                "ny": 1105,
                "latitude": (40.53, 63.97579),
                "longitude": (181.429 - 360, -93.689514),
                "projection": {
                    "type": "StereographicProjection",
                    "params": {"latitude": 90.0, "longitude": 210.0, "radius": 6371200},
                },
            },
        },
    },
    "MfWaveDomain": {
        "mfwave": {
            "type": "RegularGrid",
            "params": {
                "nx": 4320,
                "ny": 2041,
                "latMin": -80 + 1 / 24,
                "lonMin": -180 + 1 / 24,
                "dx": 1 / 12,
                "dy": 1 / 12,
                "searchRadius": 2,
            },
        },
        "mfcurrents": {
            "type": "RegularGrid",
            "params": {
                "nx": 4320,
                "ny": 2041,
                "latMin": -80 + 1 / 24,
                "lonMin": -180 + 1 / 24,
                "dx": 1 / 12,
                "dy": 1 / 12,
                "searchRadius": 2,
            },
        },
        "mfsst": {
            "type": "RegularGrid",
            "params": {
                "nx": 4320,
                "ny": 2041,
                "latMin": -80 + 1 / 24,
                "lonMin": -180 + 1 / 24,
                "dx": 1 / 12,
                "dy": 1 / 12,
                "searchRadius": 2,
            },
        },
    },
    "ItaliaMeteoArpaeDomain": {
        "icon_2i": {
            "type": "RegularGrid",
            "params": {
                "nx": 761,
                "ny": 761,
                "latMin": 33.7,
                "lonMin": 3.0,
                "dx": 0.025,
                "dy": 0.02,
            },
        },
    },
    "MeteoSwissDomain": {
        "icon_ch1": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 1089,
                "ny": 705,
                "latitudeProjectionOrigin": -4.06,
                "longitudeProjectionOrigin": -6.46,
                "dx": 0.01,
                "dy": 0.01,
                "projection": {
                    "type": "RotatedLatLonProjection",
                    "params": {"latitude": 43.0, "longitude": 190.0},
                },
            },
        },
        "icon_ch1_ensemble": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 1089,
                "ny": 705,
                "latitudeProjectionOrigin": -4.06,
                "longitudeProjectionOrigin": -6.46,
                "dx": 0.01,
                "dy": 0.01,
                "projection": {
                    "type": "RotatedLatLonProjection",
                    "params": {"latitude": 43.0, "longitude": 190.0},
                },
            },
        },
        "icon_ch2": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 545,
                "ny": 353,
                "latitudeProjectionOrigin": -4.06,
                "longitudeProjectionOrigin": -6.46,
                "dx": 0.02,
                "dy": 0.02,
                "projection": {
                    "type": "RotatedLatLonProjection",
                    "params": {"latitude": 43.0, "longitude": 190.0},
                },
            },
        },
        "icon_ch2_ensemble": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 545,
                "ny": 353,
                "latitudeProjectionOrigin": -4.06,
                "longitudeProjectionOrigin": -6.46,
                "dx": 0.02,
                "dy": 0.02,
                "projection": {
                    "type": "RotatedLatLonProjection",
                    "params": {"latitude": 43.0, "longitude": 190.0},
                },
            },
        },
    },
    "UkmoDomain": {
        "global_deterministic_10km": {
            "type": "RegularGrid",
            "params": {
                "nx": 2560,
                "ny": 1920,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 360 / 2560,
                "dy": 180 / 1920,
            },
        },
        "global_ensemble_20km": {
            "type": "RegularGrid",
            "params": {
                "nx": 1280,
                "ny": 960,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 360 / 1280,
                "dy": 180 / 960,
            },
        },
        "uk_deterministic_2km": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 1042,
                "ny": 970,
                "latitudeProjectionOrigin": -1036000,
                "longitudeProjectionOrigin": -1158000,
                "dx": 2000,
                "dy": 2000,
                "projection": {
                    "type": "LambertAzimuthalEqualAreaProjection",
                    "params": {"lambda0": -2.5, "phi1": 54.9, "radius": 6371229},
                },
            },
        },
        "uk_ensemble_2km": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 1042,
                "ny": 970,
                "latitudeProjectionOrigin": -1036000,
                "longitudeProjectionOrigin": -1158000,
                "dx": 2000,
                "dy": 2000,
                "projection": {
                    "type": "LambertAzimuthalEqualAreaProjection",
                    "params": {"lambda0": -2.5, "phi1": 54.9, "radius": 6371229},
                },
            },
        },
    },
    "GfsGraphCastDomain": {
        "graphcast025": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.25,
                "dy": 0.25,
            },
        },
        "aigfs025": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.25,
                "dy": 0.25,
            },
        },
        "aigefs025": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.25,
                "dy": 0.25,
            },
        },
        "hgefs025_stats": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.25,
                "dy": 0.25,
            },
        },
    },
    "GfsDomain": {
        "gfs05_ens": {
            "type": "RegularGrid",
            "params": {
                "nx": 720,
                "ny": 361,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.5,
                "dy": 0.5,
            },
        },
        "gfs013": {
            "type": "RegularGrid",
            "params": {
                "nx": 3072,
                "ny": 1536,
                "latMin": -0.11714935 * (1536 - 1) / 2,
                "lonMin": -180.0,
                "dx": 360 / 3072,
                "dy": 0.11714935,
            },
        },
        "gfs025": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.25,
                "dy": 0.25,
            },
        },
        "gfs025_ens": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.25,
                "dy": 0.25,
            },
        },
        "gfswave025": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.25,
                "dy": 0.25,
            },
        },
        "gfswave025_ens": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.25,
                "dy": 0.25,
            },
        },
        "nam_conus": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 1799,
                "ny": 1059,
                "latitude": (21.138, 47.8424),
                "longitude": (-122.72, -60.918),
                "projection": {
                    "type": "LambertConformalConicProjection",
                    "params": {
                        "lambda0": -97.5,
                        "phi0": 0.0,
                        "phi1": 38.5,
                        "phi2": 38.5,
                        "radius": 6371229,
                    },
                },
            },
        },
        "gfswave016": {
            "type": "RegularGrid",
            "params": {
                "nx": 2160,
                "ny": 406,
                "latMin": -15.0,
                "lonMin": -180.0,
                "dx": 360 / 2160,
                "dy": (52.5 + 15) / (406 - 1),
            },
        },
        "hrrr_conus": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 1799,
                "ny": 1059,
                "latitude": (21.138, 47.8424),
                "longitude": (-122.72, -60.918),
                "projection": {
                    "type": "LambertConformalConicProjection",
                    "params": {
                        "lambda0": -97.5,
                        "phi0": 0.0,
                        "phi1": 38.5,
                        "phi2": 38.5,
                        "radius": 6371229,
                    },
                },
            },
        },
        "hrrr_conus_15min": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 1799,
                "ny": 1059,
                "latitude": (21.138, 47.8424),
                "longitude": (-122.72, -60.918),
                "projection": {
                    "type": "LambertConformalConicProjection",
                    "params": {
                        "lambda0": -97.5,
                        "phi0": 0.0,
                        "phi1": 38.5,
                        "phi2": 38.5,
                        "radius": 6371229,
                    },
                },
            },
        },
    },
    "BomDomain": {
        "access_global": {
            "type": "RegularGrid",
            "params": {
                "nx": 2048,
                "ny": 1536,
                "latMin": -89.941406,
                "lonMin": -179.912109,
                "dx": 360 / 2048,
                "dy": 180 / 1536,
            },
        },
        "access_global_ensemble": {
            "type": "RegularGrid",
            "params": {
                "nx": 800,
                "ny": 600,
                "latMin": -89.85,
                "lonMin": -179.775,
                "dx": 360 / 800,
                "dy": 180 / 600,
            },
        },
    },
    "EumetsatSarahDomain": {
        "sarah3_30min": {
            "type": "RegularGrid",
            "params": {
                "nx": 2600,
                "ny": 2600,
                "latMin": -65.0,
                "lonMin": -65.0,
                "dx": 0.05,
                "dy": 0.05,
            },
        },
    },
    "EumetsatLsaSafDomain": {
        "msg": {
            "type": "RegularGrid",
            "params": {
                "nx": 3201,
                "ny": 3201,
                "latMin": -80.0,
                "lonMin": -80.0,
                "dx": 0.05,
                "dy": 0.05,
            },
        },
        "iodc": {
            "type": "RegularGrid",
            "params": {
                "nx": 3201,
                "ny": 3201,
                "latMin": -80.0,
                "lonMin": -40.0,
                "dx": 0.05,
                "dy": 0.05,
            },
        },
    },
    "GemDomain": {
        "gem_global": {
            "type": "RegularGrid",
            "params": {
                "nx": 2400,
                "ny": 1201,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.15,
                "dy": 0.15,
            },
        },
        "gem_regional": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 935,
                "ny": 824,
                "latitude": (18.14503, 45.405453),
                "longitude": (217.10745, 349.8256),
                "projection": {
                    "type": "StereographicProjection",
                    "params": {"latitude": 90.0, "longitude": 249.0, "radius": 6371229},
                },
            },
        },
        "gem_hrdps_continental": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 2540,
                "ny": 1290,
                "latitude": (39.626034, 47.876457),
                "longitude": (-133.62952, -40.708557),
                "projection": {
                    "type": "RotatedLatLonProjection",
                    "params": {"latitude": -36.0885, "longitude": 245.305},
                },
            },
        },
        "gem_hrdps_west": {
            "type": "ProjectionGrid",
            "params": {
                "nx": 1330,
                "ny": 1180,
                "latitudeProjectionOrigin": 5.308595 + (1180 * -0.00899),
                "longitudeProjectionOrigin": -22.18489,
                "dx": 0.00899,
                "dy": 0.00899,
                "projection": {
                    "type": "RotatedLatLonProjection",
                    "params": {"latitude": 33.443381, "longitude": 86.463574},
                },
            },
        },
        "gem_global_ensemble": {
            "type": "RegularGrid",
            "params": {
                "nx": 720,
                "ny": 361,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.5,
                "dy": 0.5,
            },
        },
    },
    "MeteoFranceDomain": {
        "arpege_europe": {
            "type": "RegularGrid",
            "params": {
                "nx": 741,
                "ny": 521,
                "latMin": 20.0,
                "lonMin": -32.0,
                "dx": 0.1,
                "dy": 0.1,
            },
        },
        "arpege_europe_probabilities": {
            "type": "RegularGrid",
            "params": {
                "nx": 741,
                "ny": 521,
                "latMin": 20.0,
                "lonMin": -32.0,
                "dx": 0.1,
                "dy": 0.1,
            },
        },
        "arpege_world": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.25,
                "dy": 0.25,
            },
        },
        "arpege_world_probabilities": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 721,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.25,
                "dy": 0.25,
            },
        },
        "arome_france": {
            "type": "RegularGrid",
            "params": {
                "nx": 1121,
                "ny": 717,
                "latMin": 37.5,
                "lonMin": -12.0,
                "dx": 0.025,
                "dy": 0.025,
            },
        },
        "arome_france_hd": {
            "type": "RegularGrid",
            "params": {
                "nx": 2801,
                "ny": 1791,
                "latMin": 37.5,
                "lonMin": -12.0,
                "dx": 0.01,
                "dy": 0.01,
            },
        },
        "arome_france_15min": {
            "type": "RegularGrid",
            "params": {
                "nx": 1121,
                "ny": 717,
                "latMin": 37.5,
                "lonMin": -12.0,
                "dx": 0.025,
                "dy": 0.025,
            },
        },
        "arome_france_hd_15min": {
            "type": "RegularGrid",
            "params": {
                "nx": 2801,
                "ny": 1791,
                "latMin": 37.5,
                "lonMin": -12.0,
                "dx": 0.01,
                "dy": 0.01,
            },
        },
    },
    "IconWaveDomain": {
        "gwam": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 699,
                "latMin": -85.25,
                "lonMin": -180.0,
                "dx": 0.25,
                "dy": 0.25,
            },
        },
        "ewam": {
            "type": "RegularGrid",
            "params": {
                "nx": 526,
                "ny": 721,
                "latMin": 30.0,
                "lonMin": -10.5,
                "dx": 0.1,
                "dy": 0.05,
            },
        },
    },
    "CamsDomain": {
        "cams_global": {
            "type": "RegularGrid",
            "params": {
                "nx": 900,
                "ny": 451,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.4,
                "dy": 0.4,
            },
        },
        "cams_global_greenhouse_gases": {
            "type": "RegularGrid",
            "params": {
                "nx": 3600,
                "ny": 1801,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.1,
                "dy": 0.1,
            },
        },
        "cams_europe": {
            "type": "RegularGrid",
            "params": {
                "nx": 700,
                "ny": 420,
                "latMin": 71.95,
                "lonMin": -24.95,
                "dx": 0.1,
                "dy": -0.1,
            },
        },
        "cams_europe_reanalysis_interim": {
            "type": "RegularGrid",
            "params": {
                "nx": 700,
                "ny": 420,
                "latMin": 30.05,
                "lonMin": -24.95,
                "dx": 0.1,
                "dy": 0.1,
            },
        },
        "cams_europe_reanalysis_validated": {
            "type": "RegularGrid",
            "params": {
                "nx": 700,
                "ny": 420,
                "latMin": 30.05,
                "lonMin": -24.95,
                "dx": 0.1,
                "dy": 0.1,
            },
        },
        "cams_europe_reanalysis_validated_pre2020": {
            "type": "RegularGrid",
            "params": {
                "nx": 701,
                "ny": 421,
                "latMin": 30.0,
                "lonMin": -25.0,
                "dx": 0.1,
                "dy": 0.1,
            },
        },
        "cams_europe_reanalysis_validated_pre2018": {
            "type": "RegularGrid",
            "params": {
                "nx": 701,
                "ny": 401,
                "latMin": 30.0,
                "lonMin": -25.0,
                "dx": 0.1,
                "dy": 0.1,
            },
        },
    },
    "JmaDomain": {
        "gsm": {
            "type": "RegularGrid",
            "params": {
                "nx": 720,
                "ny": 361,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.5,
                "dy": 0.5,
            },
        },
        "msm": {
            "type": "RegularGrid",
            "params": {
                "nx": 481,
                "ny": 505,
                "latMin": 22.4,
                "lonMin": 120.0,
                "dx": 0.0625,
                "dy": 0.05,
            },
        },
        "msm_upper_level": {
            "type": "RegularGrid",
            "params": {
                "nx": 241,
                "ny": 253,
                "latMin": 22.4,
                "lonMin": 120.0,
                "dx": 0.125,
                "dy": 0.1,
            },
        },
    },
    "Cmip6Domain": {
        "CMCC_CM2_VHR4": {
            "type": "RegularGrid",
            "params": {
                "nx": 1152,
                "ny": 768,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.3125,
                "dy": 180 / 768,
            },
        },
        "FGOALS_f3_H": {
            "type": "RegularGrid",
            "params": {
                "nx": 1440,
                "ny": 720,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.25,
                "dy": 0.25,
            },
        },
        "HiRAM_SIT_HR": {
            "type": "RegularGrid",
            "params": {
                "nx": 1536,
                "ny": 768,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 360 / 1536,
                "dy": 180 / 768,
            },
        },
        "MRI_AGCM3_2_S": {
            "type": "RegularGrid",
            "params": {
                "nx": 1920,
                "ny": 960,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 0.1875,
                "dy": 0.1875,
            },
        },
        "EC_Earth3P_HR": {
            "type": "RegularGrid",
            "params": {
                "nx": 1024,
                "ny": 512,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 360 / 1024,
                "dy": 180 / 512,
            },
        },
        "MPI_ESM1_2_XR": {
            "type": "RegularGrid",
            "params": {
                "nx": 768,
                "ny": 384,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 360 / 768,
                "dy": 180 / 384,
            },
        },
        "NICAM16_8S": {
            "type": "RegularGrid",
            "params": {
                "nx": 1280,
                "ny": 640,
                "latMin": -90.0,
                "lonMin": -180.0,
                "dx": 360 / 1280,
                "dy": 180 / 640,
            },
        },
    },
    "GloFasDomain": {
        "forecast": {
            "type": "RegularGrid",
            "params": {
                "nx": 7200,
                "ny": 3000,
                "latMin": -59.975,
                "lonMin": -180.025,
                "dx": 0.05,
                "dy": 0.05,
            },
        },
        "consolidated": {
            "type": "RegularGrid",
            "params": {
                "nx": 7200,
                "ny": 3000,
                "latMin": -59.975,
                "lonMin": -180.025,
                "dx": 0.05,
                "dy": 0.05,
            },
        },
        "seasonal": {
            "type": "RegularGrid",
            "params": {
                "nx": 7200,
                "ny": 3000,
                "latMin": -59.975,
                "lonMin": -180.025,
                "dx": 0.05,
                "dy": 0.05,
            },
        },
        "intermediate": {
            "type": "RegularGrid",
            "params": {
                "nx": 7200,
                "ny": 3000,
                "latMin": -59.975,
                "lonMin": -180.025,
                "dx": 0.05,
                "dy": 0.05,
            },
        },
        "forecastv3": {
            "type": "RegularGrid",
            "params": {
                "nx": 3600,
                "ny": 1500,
                "latMin": -60.0,
                "lonMin": -180.0,
                "dx": 0.1,
                "dy": 0.1,
            },
        },
        "consolidatedv3": {
            "type": "RegularGrid",
            "params": {
                "nx": 3600,
                "ny": 1500,
                "latMin": -60.0,
                "lonMin": -180.0,
                "dx": 0.1,
                "dy": 0.1,
            },
        },
        "seasonalv3": {
            "type": "RegularGrid",
            "params": {
                "nx": 3600,
                "ny": 1500,
                "latMin": -60.0,
                "lonMin": -180.0,
                "dx": 0.1,
                "dy": 0.1,
            },
        },
        "intermediatev3": {
            "type": "RegularGrid",
            "params": {
                "nx": 3600,
                "ny": 1500,
                "latMin": -60.0,
                "lonMin": -180.0,
                "dx": 0.1,
                "dy": 0.1,
            },
        },
    },
    "SatelliteDomain": {
        "imerg_daily": {
            "type": "RegularGrid",
            "params": {
                "nx": 3600,
                "ny": 1800,
                "latMin": -89.95,
                "lonMin": -179.95,
                "dx": 0.1,
                "dy": 0.1,
            },
        },
    },
}
