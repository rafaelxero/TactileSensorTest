function plot_points(time, data_raw, data_proc)

for i = 1 : size(data_raw, 2)
  if (abs(data_raw(i).time - time) < 1E-6)
    break;
  end
end

t = data_proc(i).time;
disp(t);
disp(i);

figure(1)
clf

hold on

raw_points  = data_raw(i).points;
proc_points = [data_proc(i).points; data_proc(i).points(1, :)];

plot(raw_points(:, 1),  raw_points(:, 2),  'Color', 'blue', '*')
plot(proc_points(:, 1), proc_points(:, 2), 'Color', 'red')