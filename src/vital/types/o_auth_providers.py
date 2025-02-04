# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OAuthProviders(str, enum.Enum):
    """
    An enumeration.
    """

    OURA = "oura"
    FITBIT = "fitbit"
    GARMIN = "garmin"
    STRAVA = "strava"
    WAHOO = "wahoo"
    IHEALTH = "ihealth"
    WITHINGS = "withings"
    GOOGLE_FIT = "google_fit"
    DEXCOM_V_3 = "dexcom_v3"
    POLAR = "polar"
    CRONOMETER = "cronometer"
    OMRON = "omron"

    def visit(
        self,
        oura: typing.Callable[[], T_Result],
        fitbit: typing.Callable[[], T_Result],
        garmin: typing.Callable[[], T_Result],
        strava: typing.Callable[[], T_Result],
        wahoo: typing.Callable[[], T_Result],
        ihealth: typing.Callable[[], T_Result],
        withings: typing.Callable[[], T_Result],
        google_fit: typing.Callable[[], T_Result],
        dexcom_v_3: typing.Callable[[], T_Result],
        polar: typing.Callable[[], T_Result],
        cronometer: typing.Callable[[], T_Result],
        omron: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OAuthProviders.OURA:
            return oura()
        if self is OAuthProviders.FITBIT:
            return fitbit()
        if self is OAuthProviders.GARMIN:
            return garmin()
        if self is OAuthProviders.STRAVA:
            return strava()
        if self is OAuthProviders.WAHOO:
            return wahoo()
        if self is OAuthProviders.IHEALTH:
            return ihealth()
        if self is OAuthProviders.WITHINGS:
            return withings()
        if self is OAuthProviders.GOOGLE_FIT:
            return google_fit()
        if self is OAuthProviders.DEXCOM_V_3:
            return dexcom_v_3()
        if self is OAuthProviders.POLAR:
            return polar()
        if self is OAuthProviders.CRONOMETER:
            return cronometer()
        if self is OAuthProviders.OMRON:
            return omron()
