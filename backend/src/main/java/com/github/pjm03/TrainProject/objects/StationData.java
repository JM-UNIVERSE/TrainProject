package com.github.pjm03.TrainProject.objects;

import com.google.gson.annotations.SerializedName;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.ToString;

import java.util.List;

@RequiredArgsConstructor
@ToString
@Getter
public class StationData {
    @SerializedName("stationName")
    private final String name;
    @SerializedName("stationCode")
    private final String code;
    @SerializedName("stationLines")
    private final List<String> lines;
    @SerializedName("stationAddress")
    private final String address;
    @SerializedName("stationLongitude")
    private final double longitude;
    @SerializedName("stationLatitude")
    private final double latitude;
}
