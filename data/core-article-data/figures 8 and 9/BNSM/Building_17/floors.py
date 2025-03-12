import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 2.75)
    ops.node(11002, 3.15, 0.0, 2.75)
    ops.node(11003, 8.5, 0.0, 2.75)
    ops.node(11004, 13.85, 0.0, 2.75)
    ops.node(11005, 0.0, 4.2, 2.75)
    ops.node(11006, 3.15, 4.2, 2.75)
    ops.node(11007, 8.5, 4.2, 2.75)
    ops.node(11008, 13.85, 4.2, 2.75)
    ops.node(11009, 0.0, 8.4, 2.75)
    ops.node(11010, 3.15, 8.4, 2.75)
    ops.node(11011, 8.5, 8.4, 2.75)
    ops.node(11012, 13.85, 8.4, 2.75)
    ops.node(11013, 0.0, 12.6, 2.75)
    ops.node(11014, 3.15, 12.6, 2.75)
    ops.node(11015, 8.5, 12.6, 2.75)
    ops.node(11016, 13.85, 12.6, 2.75)
    ops.node(11017, 0.0, 16.8, 2.75)
    ops.node(11018, 3.15, 16.8, 2.75)
    ops.node(11019, 8.5, 16.8, 2.75)
    ops.node(11020, 13.85, 16.8, 2.75)
    ops.node(11021, 0.0, 21.0, 2.75)
    ops.node(11022, 3.15, 21.0, 2.75)
    ops.node(11023, 8.5, 21.0, 2.75)
    ops.node(11024, 13.85, 21.0, 2.75)
    ops.node(11025, 0.0, 25.2, 2.75)
    ops.node(11026, 3.15, 25.2, 2.75)
    ops.node(11027, 8.5, 25.2, 2.75)
    ops.node(11028, 13.85, 25.2, 2.75)
    # Retained floor node
    ops.node(91000, 7.13744858, 12.78089218, 2.75)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018, 11019, 11020, 11021, 11022, 11023, 11024, 11025, 11026, 11027, 11028)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 5.5)
    ops.node(12002, 3.15, 0.0, 5.5)
    ops.node(12003, 8.5, 0.0, 5.5)
    ops.node(12004, 13.85, 0.0, 5.5)
    ops.node(12005, 0.0, 4.2, 5.5)
    ops.node(12006, 3.15, 4.2, 5.5)
    ops.node(12007, 8.5, 4.2, 5.5)
    ops.node(12008, 13.85, 4.2, 5.5)
    ops.node(12009, 0.0, 8.4, 5.5)
    ops.node(12010, 3.15, 8.4, 5.5)
    ops.node(12011, 8.5, 8.4, 5.5)
    ops.node(12012, 13.85, 8.4, 5.5)
    ops.node(12013, 0.0, 12.6, 5.5)
    ops.node(12014, 3.15, 12.6, 5.5)
    ops.node(12015, 8.5, 12.6, 5.5)
    ops.node(12016, 13.85, 12.6, 5.5)
    ops.node(12017, 0.0, 16.8, 5.5)
    ops.node(12018, 3.15, 16.8, 5.5)
    ops.node(12019, 8.5, 16.8, 5.5)
    ops.node(12020, 13.85, 16.8, 5.5)
    ops.node(12021, 0.0, 21.0, 5.5)
    ops.node(12022, 3.15, 21.0, 5.5)
    ops.node(12023, 8.5, 21.0, 5.5)
    ops.node(12024, 13.85, 21.0, 5.5)
    ops.node(12025, 0.0, 25.2, 5.5)
    ops.node(12026, 3.15, 25.2, 5.5)
    ops.node(12027, 8.5, 25.2, 5.5)
    ops.node(12028, 13.85, 25.2, 5.5)
    # Retained floor node
    ops.node(92000, 7.1293816, 12.78083104, 5.5)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020, 12021, 12022, 12023, 12024, 12025, 12026, 12027, 12028)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 8.25)
    ops.node(13002, 3.15, 0.0, 8.25)
    ops.node(13003, 8.5, 0.0, 8.25)
    ops.node(13004, 13.85, 0.0, 8.25)
    ops.node(13005, 0.0, 4.2, 8.25)
    ops.node(13006, 3.15, 4.2, 8.25)
    ops.node(13007, 8.5, 4.2, 8.25)
    ops.node(13008, 13.85, 4.2, 8.25)
    ops.node(13009, 0.0, 8.4, 8.25)
    ops.node(13010, 3.15, 8.4, 8.25)
    ops.node(13011, 8.5, 8.4, 8.25)
    ops.node(13012, 13.85, 8.4, 8.25)
    ops.node(13013, 0.0, 12.6, 8.25)
    ops.node(13014, 3.15, 12.6, 8.25)
    ops.node(13015, 8.5, 12.6, 8.25)
    ops.node(13016, 13.85, 12.6, 8.25)
    ops.node(13017, 0.0, 16.8, 8.25)
    ops.node(13018, 3.15, 16.8, 8.25)
    ops.node(13019, 8.5, 16.8, 8.25)
    ops.node(13020, 13.85, 16.8, 8.25)
    ops.node(13021, 0.0, 21.0, 8.25)
    ops.node(13022, 3.15, 21.0, 8.25)
    ops.node(13023, 8.5, 21.0, 8.25)
    ops.node(13024, 13.85, 21.0, 8.25)
    ops.node(13025, 0.0, 25.2, 8.25)
    ops.node(13026, 3.15, 25.2, 8.25)
    ops.node(13027, 8.5, 25.2, 8.25)
    ops.node(13028, 13.85, 25.2, 8.25)
    # Retained floor node
    ops.node(93000, 7.12118377, 12.78076891, 8.25)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018, 13019, 13020, 13021, 13022, 13023, 13024, 13025, 13026, 13027, 13028)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 11.0)
    ops.node(14002, 3.15, 0.0, 11.0)
    ops.node(14003, 8.5, 0.0, 11.0)
    ops.node(14004, 13.85, 0.0, 11.0)
    ops.node(14005, 0.0, 4.2, 11.0)
    ops.node(14006, 3.15, 4.2, 11.0)
    ops.node(14007, 8.5, 4.2, 11.0)
    ops.node(14008, 13.85, 4.2, 11.0)
    ops.node(14009, 0.0, 8.4, 11.0)
    ops.node(14010, 3.15, 8.4, 11.0)
    ops.node(14011, 8.5, 8.4, 11.0)
    ops.node(14012, 13.85, 8.4, 11.0)
    ops.node(14013, 0.0, 12.6, 11.0)
    ops.node(14014, 3.15, 12.6, 11.0)
    ops.node(14015, 8.5, 12.6, 11.0)
    ops.node(14016, 13.85, 12.6, 11.0)
    ops.node(14017, 0.0, 16.8, 11.0)
    ops.node(14018, 3.15, 16.8, 11.0)
    ops.node(14019, 8.5, 16.8, 11.0)
    ops.node(14020, 13.85, 16.8, 11.0)
    ops.node(14021, 0.0, 21.0, 11.0)
    ops.node(14022, 3.15, 21.0, 11.0)
    ops.node(14023, 8.5, 21.0, 11.0)
    ops.node(14024, 13.85, 21.0, 11.0)
    ops.node(14025, 0.0, 25.2, 11.0)
    ops.node(14026, 3.15, 25.2, 11.0)
    ops.node(14027, 8.5, 25.2, 11.0)
    ops.node(14028, 13.85, 25.2, 11.0)
    # Retained floor node
    ops.node(94000, 7.17595445, 12.79824897, 11.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018, 14019, 14020, 14021, 14022, 14023, 14024, 14025, 14026, 14027, 14028)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
