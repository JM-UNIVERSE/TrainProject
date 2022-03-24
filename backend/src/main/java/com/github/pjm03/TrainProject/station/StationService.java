package com.github.pjm03.TrainProject.station;

import com.github.pjm03.TrainProject.objects.StationData;
import com.github.pjm03.TrainProject.objects.StationPosition;
import com.google.gson.Gson;
import com.google.gson.JsonArray;
import lombok.NonNull;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

@Service
public class StationService {
    private final Map<String, StationData> stationDataMap;
    private final Gson gson;

    @Autowired
    public StationService(Gson gson) {
        this.stationDataMap = new HashMap<>();
        this.gson = gson;
        try {
            ClassPathResource resource = new ClassPathResource("data/station_data.json");
            String json = Files.readString(Paths.get(resource.getURI()));
            JsonArray array = gson.fromJson(json, JsonArray.class);
            array.forEach(element -> {
                StationData data = this.gson.fromJson(element, StationData.class);
                stationDataMap.put(data.getName(), data);
            });
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public StationData getStationData(@NonNull String name) {
        return stationDataMap.get(name);
    }

    public Set<String> getAllStationNames() {
        return stationDataMap.keySet();
    }
}
