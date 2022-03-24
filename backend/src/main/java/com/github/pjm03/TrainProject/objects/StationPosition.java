package com.github.pjm03.TrainProject.objects;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@Getter
public class StationPosition {
    private final String name;
    private final double longitude; //경도
    private final double latitude; //위도
}
