function plot_points_edges(time, data_raw, edges, circle, contact, no_contact)

for i = 1 : size(data_raw, 2)
  if (abs(data_raw(i).time - time) < 1E-6)
    break;
  end
end

foot_points = [-0.10,  0.075;
                0.13,  0.075;
                0.13, -0.055;
               -0.10, -0.055];
foot_points = [foot_points; foot_points(1, :)];
               
t = data_raw(i).time;
disp(t);
disp(i);

convex_hull = [contact(i).points; contact(i).points(1, :)];

figure(1)
clf

hold on

plot(foot_points(:, 1), foot_points(:, 2), 'Color', 'black')
plot(data_raw(i).points(:, 1),  data_raw(i).points(:, 2), 'Color', 'magenta', '*')

y_line = -0.08 : 0.01 : 0.08;
x_line = -edges(i, 4) / edges(i, 3) * y_line - edges(i, 2) / edges(i, 3);

plot(x_line, y_line)

t = linspace(0, 2 * pi, 100);
circx = circle(i, 4) .* cos(t) + circle(i, 2);
circy = circle(i, 4) .* sin(t) + circle(i, 3);
plot(circx, circy, 'Color', 'red')

xlim([-0.2 0.2])
ylim([-0.1 0.1])
axis equal

plot(convex_hull(:, 1), convex_hull(:, 2), 'Color', 'green', '--')
plot(contact(i).points(:, 1), contact(i).points(:, 2), 'Color', 'blue', '*')
plot(no_contact(i).points(:, 1), no_contact(i).points(:, 2), 'Color', 'red', '*')