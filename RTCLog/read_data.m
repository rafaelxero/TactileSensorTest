filename = "TactileSensorTest.tactileInfoRaw";

fid = fopen(filename);

i = 1;
while (!feof(fid))

  line = fgetl(fid);
  data_cells = strsplit(strtrim(line));
  
  data_raw(i).time = str2num(data_cells{1});
  ind = 2;
  
  for j = 1 : (length(data_cells) - 1) / 5
    data_raw(i).points(j, 1) = str2num(data_cells{ind}); ind = ind + 1;
    data_raw(i).points(j, 2) = str2num(data_cells{ind}); ind = ind + 1;
    data_raw(i).forces(j, 1) = str2num(data_cells{ind}); ind = ind + 1;
    data_raw(i).forces(j, 2) = str2num(data_cells{ind}); ind = ind + 1;
    data_raw(i).forces(j, 3) = str2num(data_cells{ind}); ind = ind + 1;
  end
  
  i = i + 1;

end

fclose(fid);

%%%

filename = "TactileSensorTest.tactileInfoProc";

fid = fopen(filename);

i = 1;
while (!feof(fid))

  line = fgetl(fid);
  data_cells= strsplit(strtrim(line));
  
  data_proc(i).time = str2num(data_cells{1});
  ind = 2;
  
  for j = 1 : (length(data_cells) - 1) / 2
    data_proc(i).points(j, 1) = str2num(data_cells{ind}); ind = ind + 1;
    data_proc(i).points(j, 2) = str2num(data_cells{ind}); ind = ind + 1;
  end
  
  i = i + 1;

end

fclose(fid);