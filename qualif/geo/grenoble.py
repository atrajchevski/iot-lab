# geo.grenoble.py: geo(graphy|metry) for GRE nodes

"""
    To get the physical coordinates of nodes on a site,
    use "experiment-cli info".  Utility parse_json.py helps
    getting this (static) piece of information back into python.

    Nodes in Grenoble are arranged in a flat setup.  The following
    command provides xy coordinates together with node's short name.

        $  experiment-cli info --site devgrenoble -l | ./parse_json.py '
	[
		[
			node["network_address"].split(".")[0],
			float(node["x"]),
			float(node["y"])
		]
		for node in x["items"]
	]'

    The result of this command is copy/pasted below in variable "nodes"
    and can then be processed as needed in python.

"""
nodes=[[u'm3-1', 20.1, 26.76], [u'm3-2', 20.7, 26.76], [u'm3-3', 21.3, 26.76], [u'm3-4', 21.9, 26.76], [u'm3-5', 22.5, 26.76], [u'm3-6', 23.1, 26.76], [u'm3-7', 24.55, 26.76], [u'm3-8', 25.15, 26.76], [u'm3-9', 25.75, 26.76], [u'm3-10', 26.35, 26.76], [u'm3-11', 26.95, 26.76], [u'm3-12', 27.55, 26.76], [u'm3-13', 28.15, 26.76], [u'm3-14', 28.75, 26.76], [u'm3-15', 29.35, 26.76], [u'm3-16', 29.95, 26.76], [u'm3-17', 30.55, 26.76], [u'm3-18', 31.15, 26.76], [u'm3-19', 31.75, 26.76], [u'm3-20', 32.35, 26.76], [u'm3-21', 32.95, 26.76], [u'm3-22', 33.55, 26.76], [u'm3-23', 34.15, 26.76], [u'm3-24', 34.75, 26.76], [u'm3-25', 35.35, 26.76], [u'm3-26', 35.95, 26.76], [u'm3-27', 36.55, 26.76], [u'm3-28', 37.15, 26.76], [u'm3-29', 37.75, 26.76], [u'm3-30', 38.35, 26.76], [u'm3-31', 38.95, 26.76], [u'm3-32', 39.55, 26.76], [u'm3-33', 40.15, 26.76], [u'm3-34', 40.75, 26.76], [u'm3-35', 41.35, 26.76], [u'm3-36', 41.95, 26.76], [u'm3-37', 42.55, 26.76], [u'm3-38', 43.15, 26.76], [u'm3-39', 43.75, 26.76], [u'm3-40', 44.35, 26.76], [u'm3-41', 44.95, 26.76], [u'm3-42', 45.55, 26.76], [u'm3-43', 46.15, 26.76], [u'm3-44', 46.75, 26.76], [u'm3-45', 47.35, 26.76], [u'm3-46', 47.95, 26.76], [u'm3-47', 48.55, 26.76], [u'm3-48', 49.15, 26.76], [u'm3-49', 49.75, 26.76], [u'm3-50', 50.35, 26.76], [u'm3-51', 50.95, 26.76], [u'm3-52', 51.55, 26.76], [u'm3-53', 52.15, 26.76], [u'm3-54', 52.75, 26.76], [u'm3-55', 53.35, 26.76], [u'm3-56', 53.95, 26.76], [u'm3-57', 54.55, 26.76], [u'm3-58', 55.15, 26.76], [u'm3-59', 55.75, 26.76], [u'm3-60', 56.35, 26.76], [u'm3-61', 56.95, 26.76], [u'm3-62', 57.55, 26.76], [u'm3-63', 58.15, 26.76], [u'm3-64', 58.75, 26.76], [u'm3-65', 59.35, 26.76], [u'm3-66', 59.95, 26.76], [u'm3-67', 60.55, 26.76], [u'm3-68', 61.15, 26.76], [u'm3-69', 61.75, 26.76], [u'm3-70', 17.02, 26.76], [u'm3-71', 16.42, 26.76], [u'm3-72', 15.82, 26.76], [u'm3-73', 15.22, 26.76], [u'm3-74', 14.62, 26.76], [u'm3-75', 14.02, 26.76], [u'm3-76', 13.42, 26.76], [u'm3-77', 12.82, 26.76], [u'm3-78', 12.22, 26.76], [u'm3-79', 11.62, 26.76], [u'm3-80', 11.02, 26.76], [u'm3-81', 10.42, 26.76], [u'm3-82', 9.82, 26.76], [u'm3-83', 9.22, 26.76], [u'm3-84', 8.62, 26.76], [u'm3-85', 8.02, 26.76], [u'm3-86', 7.42, 26.76], [u'm3-87', 6.82, 26.76], [u'm3-88', 6.22, 26.76], [u'm3-89', 5.62, 26.76], [u'm3-90', 5.02, 26.76], [u'm3-91', 4.42, 26.76], [u'm3-92', 3.82, 26.76], [u'm3-93', 3.22, 26.76], [u'm3-94', 2.62, 26.76], [u'm3-95', 0.4, 26.52], [u'm3-96', 1.0, 26.52], [u'm3-97', 0.4, 25.92], [u'm3-98', 1.0, 25.92], [u'm3-99', 0.4, 25.23], [u'm3-100', 1.0, 25.23], [u'm3-101', 0.4, 24.63], [u'm3-102', 1.0, 24.63], [u'm3-103', 0.4, 24.03], [u'm3-104', 1.0, 24.03], [u'm3-105', 0.4, 23.43], [u'm3-106', 1.0, 23.43], [u'm3-107', 0.4, 22.83], [u'm3-108', 1.0, 22.83], [u'm3-109', 0.4, 22.23], [u'm3-110', 1.0, 22.23], [u'm3-111', 0.4, 21.63], [u'm3-112', 1.0, 21.63], [u'm3-113', 0.4, 21.03], [u'm3-114', 1.0, 21.03], [u'm3-115', 0.4, 20.43], [u'm3-116', 1.0, 20.43], [u'm3-117', 0.4, 19.83], [u'm3-118', 1.0, 19.83], [u'm3-119', 0.4, 19.23], [u'm3-120', 1.0, 19.23], [u'm3-121', 0.4, 18.63], [u'm3-122', 1.0, 18.63], [u'm3-123', 0.4, 18.03], [u'm3-124', 1.0, 18.03], [u'm3-125', 0.4, 17.43], [u'm3-126', 1.0, 17.43], [u'm3-127', 0.4, 16.83], [u'm3-128', 1.0, 16.83], [u'm3-129', 0.4, 16.23], [u'm3-130', 1.0, 16.23], [u'm3-131', 0.4, 15.63], [u'm3-132', 1.0, 15.63], [u'm3-133', 0.4, 15.03], [u'm3-134', 1.0, 15.03], [u'm3-135', 0.4, 14.43], [u'm3-136', 1.0, 14.43], [u'm3-137', 0.4, 13.83], [u'm3-138', 1.0, 13.83], [u'm3-139', 0.4, 13.23], [u'm3-140', 1.0, 13.23], [u'm3-141', 0.4, 12.63], [u'm3-142', 1.0, 12.63], [u'm3-143', 0.4, 12.03], [u'm3-144', 1.0, 12.03], [u'm3-145', 0.4, 11.43], [u'm3-146', 1.0, 11.43], [u'm3-147', 0.4, 10.83], [u'm3-148', 1.0, 10.83], [u'm3-149', 0.4, 10.23], [u'm3-150', 1.0, 10.23], [u'm3-151', 0.4, 9.63], [u'm3-152', 1.0, 9.63], [u'm3-153', 0.4, 9.03], [u'm3-154', 1.0, 9.03], [u'm3-155', 0.4, 8.43], [u'm3-156', 1.0, 8.43], [u'm3-157', 0.4, 7.83], [u'm3-158', 1.0, 7.83], [u'm3-159', 0.4, 7.23], [u'm3-160', 1.0, 7.23], [u'm3-161', 0.4, 6.63], [u'm3-162', 1.0, 6.63], [u'm3-163', 0.4, 6.03], [u'm3-164', 1.0, 6.03], [u'm3-165', 0.4, 5.43], [u'm3-166', 1.0, 5.43], [u'm3-167', 0.4, 4.83], [u'm3-168', 1.0, 4.83], [u'm3-169', 0.4, 4.23], [u'm3-170', 1.0, 4.23], [u'm3-171', 0.4, 3.63], [u'm3-172', 1.0, 3.63], [u'm3-173', 0.4, 3.03], [u'm3-174', 1.0, 3.03], [u'm3-175', 0.4, 2.43], [u'm3-176', 1.0, 2.43], [u'm3-177', 0.4, 1.85], [u'm3-178', 1.0, 1.85], [u'm3-179', 2.75, 0.94], [u'm3-180', 3.35, 0.94], [u'm3-181', 3.95, 0.94], [u'm3-182', 4.55, 0.94], [u'm3-183', 5.15, 0.94], [u'm3-184', 5.75, 0.94], [u'm3-185', 6.35, 0.94], [u'm3-186', 6.95, 0.94], [u'm3-187', 7.55, 0.94], [u'm3-188', 8.15, 0.94], [u'm3-189', 8.75, 0.94], [u'm3-190', 9.35, 0.94], [u'm3-191', 9.95, 0.94], [u'm3-192', 10.55, 0.94], [u'm3-193', 11.15, 0.94], [u'm3-194', 11.75, 0.94], [u'm3-195', 12.35, 0.94], [u'm3-196', 12.95, 0.94], [u'm3-197', 13.55, 0.94], [u'm3-198', 14.15, 0.94], [u'm3-199', 14.75, 0.94], [u'm3-200', 15.35, 0.94], [u'm3-201', 15.95, 0.94], [u'm3-202', 16.55, 0.94], [u'm3-203', 17.15, 0.94], [u'm3-204', 18.95, 0.75], [u'm3-205', 18.35, 0.75], [u'm3-206', 18.95, 1.83], [u'm3-207', 18.35, 1.83], [u'm3-208', 18.95, 2.43], [u'm3-209', 18.35, 2.43], [u'm3-210', 18.95, 3.03], [u'm3-211', 18.35, 3.03], [u'm3-212', 18.95, 3.63], [u'm3-213', 18.35, 3.63], [u'm3-214', 18.95, 4.23], [u'm3-215', 18.35, 4.23], [u'm3-216', 18.95, 4.83], [u'm3-217', 18.35, 4.83], [u'm3-218', 18.95, 5.43], [u'm3-219', 18.35, 5.43], [u'm3-220', 18.95, 6.03], [u'm3-221', 18.35, 6.03], [u'm3-222', 18.95, 6.63], [u'm3-223', 18.35, 6.63], [u'm3-224', 18.95, 7.23], [u'm3-225', 18.35, 7.23], [u'm3-226', 18.95, 7.83], [u'm3-227', 18.35, 7.83], [u'm3-228', 18.95, 8.43], [u'm3-229', 18.35, 8.43], [u'm3-230', 18.95, 9.03], [u'm3-231', 18.35, 9.03], [u'm3-232', 18.95, 9.63], [u'm3-233', 18.35, 9.63], [u'm3-234', 18.95, 10.23], [u'm3-235', 18.35, 10.23], [u'm3-236', 18.95, 10.83], [u'm3-237', 18.35, 10.83], [u'm3-238', 18.95, 11.43], [u'm3-239', 18.35, 11.43], [u'm3-240', 18.95, 12.03], [u'm3-241', 18.35, 12.03], [u'm3-242', 18.95, 12.63], [u'm3-243', 18.35, 12.63], [u'm3-244', 18.95, 13.23], [u'm3-245', 18.35, 13.23], [u'm3-246', 18.95, 13.83], [u'm3-247', 18.35, 13.83], [u'm3-248', 18.95, 14.43], [u'm3-249', 18.35, 14.43], [u'm3-250', 18.95, 15.03], [u'm3-251', 18.35, 15.03], [u'm3-252', 18.95, 15.63], [u'm3-253', 18.35, 15.63], [u'm3-254', 18.95, 16.23], [u'm3-255', 18.35, 16.23], [u'm3-256', 18.95, 16.83], [u'm3-257', 18.35, 16.83], [u'm3-258', 18.95, 17.43], [u'm3-259', 18.35, 17.43], [u'm3-260', 18.95, 18.03], [u'm3-261', 18.35, 18.03], [u'm3-262', 18.95, 18.63], [u'm3-263', 18.35, 18.63], [u'm3-264', 18.95, 19.23], [u'm3-265', 18.35, 19.23], [u'm3-266', 18.95, 19.83], [u'm3-267', 18.35, 19.83], [u'm3-268', 18.95, 20.43], [u'm3-269', 18.35, 20.43], [u'm3-270', 18.95, 21.03], [u'm3-271', 18.35, 21.03], [u'm3-272', 18.95, 21.63], [u'm3-273', 18.35, 21.63], [u'm3-274', 18.95, 22.23], [u'm3-275', 18.35, 22.23], [u'm3-276', 18.95, 22.83], [u'm3-277', 18.35, 22.83], [u'm3-278', 18.95, 23.43], [u'm3-279', 18.35, 23.43], [u'm3-280', 18.95, 24.03], [u'm3-281', 18.35, 24.03], [u'm3-282', 18.95, 24.63], [u'm3-283', 18.35, 24.63], [u'm3-284', 18.95, 25.23], [u'm3-285', 18.35, 25.23], [u'm3-286', 18.95, 26.0], [u'm3-287', 18.35, 26.0], [u'm3-288', 18.95, 26.52], [u'm3-289', 18.35, 26.52], [u'm3-290', 20.05, 0.94], [u'm3-291', 20.65, 0.94], [u'm3-292', 21.25, 0.94], [u'm3-293', 21.85, 0.94], [u'm3-294', 22.45, 0.94], [u'm3-295', 23.05, 0.94], [u'm3-296', 24.62, 0.94], [u'm3-297', 25.22, 0.94], [u'm3-298', 25.85, 0.94], [u'm3-299', 26.42, 0.94], [u'm3-300', 27.02, 0.94], [u'm3-301', 28.22, 0.94], [u'm3-302', 28.71, 0.94], [u'm3-303', 29.36, 0.94], [u'm3-304', 29.96, 0.94], [u'm3-305', 30.56, 0.94], [u'm3-306', 31.16, 0.94], [u'm3-307', 31.76, 0.94], [u'm3-308', 32.36, 0.94], [u'm3-309', 32.96, 0.94], [u'm3-310', 33.56, 0.94], [u'm3-311', 34.16, 0.94], [u'm3-312', 34.76, 0.94], [u'm3-313', 35.36, 0.94], [u'm3-314', 35.96, 0.94], [u'm3-315', 36.56, 0.94], [u'm3-316', 37.16, 0.94], [u'm3-317', 37.76, 0.94], [u'm3-318', 38.36, 0.94], [u'm3-319', 38.96, 0.94], [u'm3-320', 39.56, 0.94], [u'm3-321', 40.16, 0.94], [u'm3-322', 40.76, 0.94], [u'm3-323', 41.36, 0.94], [u'm3-324', 41.96, 0.94], [u'm3-325', 42.56, 0.94], [u'm3-326', 43.16, 0.94], [u'm3-327', 43.76, 0.94], [u'm3-328', 44.36, 0.94], [u'm3-329', 44.96, 0.94], [u'm3-330', 45.56, 0.94], [u'm3-331', 46.16, 0.94], [u'm3-332', 46.76, 0.94], [u'm3-333', 47.36, 0.94], [u'm3-334', 47.96, 0.94], [u'm3-335', 48.56, 0.94], [u'm3-336', 49.16, 0.94], [u'm3-337', 49.76, 0.94], [u'm3-338', 50.36, 0.94], [u'm3-339', 50.96, 0.94], [u'm3-340', 51.56, 0.94], [u'm3-341', 52.16, 0.94], [u'm3-342', 52.76, 0.94], [u'm3-343', 53.36, 0.94], [u'm3-344', 53.96, 0.94], [u'm3-345', 54.56, 0.94], [u'm3-346', 55.16, 0.94], [u'm3-347', 55.76, 0.94], [u'm3-348', 56.36, 0.94], [u'm3-349', 56.96, 0.94], [u'm3-350', 57.56, 0.94], [u'm3-351', 58.16, 0.94], [u'm3-352', 58.76, 0.94], [u'm3-353', 59.36, 0.94], [u'm3-354', 59.96, 0.94], [u'm3-355', 60.56, 0.94], [u'm3-356', 61.16, 0.94], [u'm3-357', 61.76, 0.94], [u'm3-358', 62.26, 0.94], [u'm3-359', 34.75, 25.75], [u'm3-360', 35.35, 25.75], [u'm3-361', 35.95, 25.75], [u'm3-362', 36.55, 25.75], [u'm3-363', 37.75, 24.92], [u'm3-364', 37.75, 24.92], [u'm3-365', 38.95, 25.75], [u'm3-366', 39.55, 25.75], [u'm3-367', 40.15, 25.75], [u'm3-368', 40.75, 25.75], [u'm3-369', 41.35, 25.75], [u'm3-370', 46.15, 25.75], [u'm3-371', 46.75, 25.75], [u'm3-372', 47.35, 25.75], [u'm3-373', 47.95, 25.75], [u'm3-374', 48.55, 25.75], [u'm3-375', 49.15, 25.75], [u'm3-376', 52.15, 25.75], [u'm3-377', 52.75, 25.75], [u'm3-378', 53.35, 25.75], [u'm3-379', 53.95, 25.75], [u'm3-380', 54.55, 25.75], [u'a8-1', 20.33, 25.28], [u'a8-2', 20.33, 25.28], [u'a8-3', 20.93, 25.28], [u'a8-4', 21.53, 25.33], [u'a8-5', 21.53, 25.33], [u'a8-6', 22.13, 25.33], [u'a8-7', 22.13, 25.33], [u'a8-8', 22.73, 25.33], [u'a8-9', 23.33, 25.33], [u'a8-10', 23.33, 25.33], [u'a8-11', 23.93, 25.8], [u'a8-12', 23.93, 25.8], [u'a8-13', 24.53, 25.75], [u'a8-14', 25.13, 25.75], [u'a8-15', 25.73, 25.75], [u'a8-16', 26.33, 25.75], [u'a8-17', 26.93, 25.75], [u'a8-18', 27.55, 25.75], [u'a8-19', 28.15, 25.75], [u'a8-20', 28.75, 25.75], [u'a8-21', 29.35, 25.75], [u'a8-22', 29.95, 25.75], [u'a8-23', 30.55, 25.75], [u'a8-24', 31.15, 25.75], [u'a8-25', 31.75, 25.75], [u'a8-26', 32.35, 25.75], [u'a8-27', 32.35, 25.75], [u'a8-28', 32.95, 25.75], [u'a8-29', 33.55, 25.75], [u'a8-30', 34.15, 25.75], [u'a8-31', 38.35, 24.92], [u'a8-32', 38.35, 24.92], [u'a8-33', 41.95, 25.75], [u'a8-34', 41.95, 25.75], [u'a8-35', 43.15, 25.75], [u'a8-36', 43.15, 25.75], [u'a8-37', 44.35, 25.75], [u'a8-38', 44.95, 25.75], [u'a8-39', 44.95, 25.75], [u'a8-40', 46.15, 25.75], [u'a8-41', 49.75, 24.9], [u'a8-42', 50.35, 24.9], [u'a8-43', 50.95, 24.9], [u'a8-44', 51.55, 25.75], [u'a8-45', 55.15, 25.75], [u'a8-46', 55.75, 25.75], [u'a8-47', 56.35, 25.75], [u'a8-48', 56.95, 25.75], [u'a8-49', 57.55, 25.75], [u'a8-50', 58.15, 24.9], [u'a8-51', 58.75, 24.9], [u'a8-52', 59.35, 24.9], [u'a8-53', 59.95, 25.75], [u'a8-54', 59.95, 25.75], [u'a8-55', 60.55, 25.75], [u'a8-56', 61.15, 25.75], [u'a8-57', 61.75, 25.75], [u'a8-58', 62.35, 25.75], [u'a8-59', 15.47, 25.73], [u'a8-60', 14.87, 25.73], [u'a8-61', 14.27, 25.73], [u'a8-62', 13.67, 25.73], [u'a8-63', 13.07, 25.73], [u'a8-64', 12.47, 25.73], [u'a8-65', 11.87, 25.73], [u'a8-66', 11.27, 25.73], [u'a8-67', 10.67, 25.73], [u'a8-68', 10.07, 25.73], [u'a8-69', 9.47, 25.73], [u'a8-70', 8.87, 25.73], [u'a8-71', 8.27, 25.73], [u'a8-72', 7.67, 25.73], [u'a8-73', 7.07, 25.73], [u'a8-74', 6.47, 25.73], [u'a8-75', 5.87, 25.73], [u'a8-76', 5.27, 25.73], [u'a8-77', 4.57, 25.73], [u'a8-78', 5.5, 0.04], [u'a8-79', 6.1, 0.04], [u'a8-80', 6.7, 0.04], [u'a8-81', 7.3, 0.04], [u'a8-82', 7.9, 0.04], [u'a8-83', 8.5, 0.04], [u'a8-84', 9.1, 0.04], [u'a8-85', 9.7, 0.04], [u'a8-86', 10.3, 0.04], [u'a8-87', 10.9, 0.04], [u'a8-88', 11.5, 0.04], [u'a8-89', 12.1, 0.04], [u'a8-90', 12.7, 0.04], [u'a8-91', 13.3, 0.04], [u'a8-92', 13.9, 0.04], [u'a8-93', 14.5, 0.04], [u'a8-94', 15.1, 0.04], [u'a8-95', 19.75, 2.1], [u'a8-96', 19.75, 2.1], [u'a8-97', 19.75, 2.7], [u'a8-98', 19.75, 2.7], [u'a8-99', 19.75, 3.3], [u'a8-100', 19.75, 3.9], [u'a8-101', 19.75, 4.5], [u'a8-102', 19.75, 4.5], [u'a8-103', 19.75, 5.1], [u'a8-104', 19.75, 5.7], [u'a8-105', 19.75, 5.7], [u'a8-106', 19.75, 6.3], [u'a8-107', 19.75, 6.3], [u'a8-108', 19.75, 6.9], [u'a8-109', 19.75, 7.5], [u'a8-110', 19.75, 8.1], [u'a8-111', 20.45, 8.7], [u'a8-112', 20.45, 8.7], [u'a8-113', 20.45, 9.3], [u'a8-114', 20.45, 9.9], [u'a8-115', 20.45, 10.5], [u'a8-116', 19.75, 11.1], [u'a8-117', 19.75, 11.7], [u'a8-118', 19.75, 11.7], [u'a8-119', 19.75, 12.3], [u'a8-120', 19.75, 12.9], [u'a8-121', 19.75, 13.5], [u'a8-122', 19.75, 13.5], [u'a8-123', 19.75, 14.1], [u'a8-124', 19.75, 14.7], [u'a8-125', 19.75, 14.7], [u'a8-126', 19.75, 15.3], [u'a8-127', 19.75, 15.9], [u'a8-128', 19.75, 16.5], [u'a8-129', 19.75, 17.1], [u'a8-130', 19.75, 17.1], [u'a8-131', 19.75, 17.7], [u'a8-132', 19.75, 18.3], [u'a8-133', 19.75, 18.9], [u'a8-134', 19.75, 18.9], [u'a8-135', 20.65, 20.1], [u'a8-136', 20.65, 20.1], [u'a8-137', 19.91, 20.6], [u'a8-138', 19.91, 21.2], [u'a8-139', 19.91, 21.2], [u'a8-140', 19.91, 21.8], [u'a8-141', 19.91, 22.4], [u'a8-142', 19.91, 22.4], [u'a8-143', 19.91, 23.0], [u'a8-144', 19.91, 23.6], [u'a8-145', 19.91, 24.2], [u'a8-146', 19.91, 24.2], [u'a8-147', 19.91, 24.8], [u'a8-148', 19.91, 25.3], [u'a8-149', 20.09, 1.54], [u'a8-150', 20.09, 1.54], [u'a8-151', 20.69, 1.54], [u'a8-152', 21.29, 1.54], [u'a8-153', 21.29, 1.54], [u'a8-154', 21.89, 1.54], [u'a8-155', 21.89, 1.54], [u'a8-156', 23.09, 1.54], [u'a8-157', 23.09, 1.54], [u'a8-158', 23.82, 1.54], [u'a8-159', 23.82, 1.54], [u'a8-160', 24.17, 1.66], [u'a8-161', 26.49, 1.54], [u'a8-162', 26.49, 1.54], [u'a8-163', 27.29, 1.54], [u'a8-164', 27.29, 1.54], [u'a8-165', 27.89, 1.54], [u'a8-166', 28.49, 1.54], [u'a8-167', 29.09, 1.54], [u'a8-168', 29.69, 2.34], [u'a8-169', 29.69, 2.34], [u'a8-170', 30.29, 2.34], [u'a8-171', 30.29, 2.34], [u'a8-172', 30.89, 2.34], [u'a8-173', 31.49, 1.54], [u'a8-174', 31.49, 1.54], [u'a8-175', 32.09, 1.54], [u'a8-176', 32.09, 1.54], [u'a8-177', 32.69, 1.54], [u'a8-178', 33.29, 1.54], [u'a8-179', 33.89, 1.54], [u'a8-180', 34.49, 1.54], [u'a8-181', 35.09, 1.54], [u'a8-182', 35.69, 1.54], [u'a8-183', 36.29, 1.54], [u'a8-184', 36.89, 2.34], [u'a8-185', 37.49, 2.34], [u'a8-186', 38.09, 2.34], [u'a8-187', 38.69, 2.34], [u'a8-188', 39.29, 1.54], [u'a8-189', 39.29, 1.54], [u'a8-190', 39.89, 1.54], [u'a8-191', 40.49, 1.54], [u'a8-192', 41.09, 1.54], [u'a8-193', 41.69, 1.54], [u'a8-194', 42.29, 1.54], [u'a8-195', 42.36, 1.54], [u'a8-196', 42.89, 2.34], [u'a8-197', 43.49, 2.34], [u'a8-198', 43.49, 2.34], [u'a8-199', 45.96, 1.54], [u'a8-200', 45.9, 1.54], [u'a8-201', 46.49, 1.54], [u'a8-202', 47.09, 1.54], [u'a8-203', 47.69, 1.54], [u'a8-204', 48.29, 1.54], [u'a8-205', 48.29, 1.54], [u'a8-206', 48.89, 1.54], [u'a8-207', 49.49, 2.34], [u'a8-208', 50.09, 2.34], [u'a8-209', 51.29, 1.54], [u'a8-210', 51.29, 1.54], [u'a8-211', 51.89, 1.54], [u'a8-212', 52.49, 1.54], [u'a8-213', 53.09, 1.54], [u'a8-214', 53.69, 1.54], [u'a8-215', 54.29, 1.54], [u'a8-216', 54.89, 1.54], [u'a8-217', 55.49, 1.54], [u'a8-218', 56.09, 1.54], [u'a8-219', 56.69, 1.54], [u'a8-220', 57.29, 2.34], [u'a8-221', 57.89, 2.34], [u'a8-222', 57.89, 1.54], [u'a8-223', 58.49, 1.54], [u'a8-224', 59.09, 1.54], [u'a8-225', 59.69, 1.54], [u'a8-226', 60.29, 1.54], [u'a8-227', 60.89, 1.54], [u'a8-228', 61.49, 1.54]]

def list_nodes(type):
	dict = {}
	type_str = type + "-"
	for n in nodes:
		if n[0][0:len(type_str)] == type_str:
			id = n[0].replace(type_str, "")
			dict[id] = [n[1], n[2]]
	return dict

def dump(nodes_dict):
	for id in nodes_dict:
		x, y = nodes_dict[id]	
		print id, x, y

def test():
	m3 = list_nodes("m3")
	a8 = list_nodes("a8")
	dump(m3)
	dump(a8)

if __name__ == '__main__': # pragma: no cover
	test()
