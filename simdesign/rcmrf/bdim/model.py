from .baselib.building import TaxonomyData, BuildingBase
from .eu_cdn.building import Building as EUCDN
from .eu_cdl.building import Building as EuCDL
from .eu_cdm.building import Building as EuCDM
from .eu_cdh.building import Building as EuCDH


class BDIM:
    """
    Factory class to dynamically create a BDIM instance of the corresponding
    design class based on taxonomy data.
    """

    _design_classes = {
        "eu_cdn": EUCDN,
        "eu_cdl": EuCDL,
        "eu_cdm": EuCDM,
        "eu_cdh": EuCDH
    }
    """Design class mapper."""

    def __new__(cls, taxonomy: TaxonomyData) -> BuildingBase:
        """
        Dynamically creates a BDIM instance based on the design class.

        Parameters
        ----------
        taxonomy : TaxonomyData
            Building taxonomy data.

        Returns
        -------
        BuildingBase
            A BDIM instance of the corresponding design class.

        Raises
        ------
        TypeError
            If taxonomy is not an instance of TaxonomyData.
        ValueError
            If taxonomy.design_class is invalid.
        """
        # Type checking for taxonomy
        if not isinstance(taxonomy, TaxonomyData):
            raise TypeError(
                "Expected taxonomy to be an instance of TaxonomyData"
            )
        # Get appropriate bdim class
        bdim_class = cls._design_classes.get(taxonomy.design_class)
        # Check if the design_class in taxonomy is valid
        if bdim_class is None:
            valid_classes = ", ".join(cls._design_classes.keys())
            raise ValueError(
                f"Invalid design class: {taxonomy.design_class}."
                f"Valid options are: {valid_classes}."
            )
        # Instantiate and return the appropriate class
        return bdim_class(taxonomy)
