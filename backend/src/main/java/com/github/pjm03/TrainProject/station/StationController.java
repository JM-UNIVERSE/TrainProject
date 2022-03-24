package com.github.pjm03.TrainProject.station;

import com.github.pjm03.TrainProject.objects.StationData;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.stream.Collectors;

@RequiredArgsConstructor
@RestController
@RequestMapping("station")
public class StationController {
    private final StationService stationService;

    @GetMapping("/all")
    public List<StationData> allStationPosition() {
        return stationService.getAllStationNames().stream()
                .map(stationService::getStationData)
                .collect(Collectors.toList());
    }

    @GetMapping("/{name}")
    public StationData stationPosition(@PathVariable String name) {
        return stationService.getStationData(name);
    }
}
