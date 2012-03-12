# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.mapper import Mapper


class CompositePolyDataMapper(Mapper):
    """
    CompositePolyDataMapper - a class that renders hierarchical
    polygonal data
    
    Superclass: Mapper
    
    This class uses a set of PolyDataMappers to render input data
    which may be hierarchical. The input to this mapper may be either
    PolyData or a CompositeDataSet built from polydata. If
    something other than PolyData is encountered, an error message
    will be produced.
    
    See Also:
    
    PolyDataMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCompositePolyDataMapper, obj, update, **traits)
    
    _updateable_traits_ = \
    (('immediate_mode_rendering', 'GetImmediateModeRendering'),
    ('scalar_mode', 'GetScalarMode'), ('reference_count',
    'GetReferenceCount'), ('static', 'GetStatic'),
    ('resolve_coincident_topology', 'GetResolveCoincidentTopology'),
    ('force_compile_only', 'GetForceCompileOnly'),
    ('resolve_coincident_topology_z_shift',
    'GetResolveCoincidentTopologyZShift'), ('scalar_visibility',
    'GetScalarVisibility'), ('color_mode', 'GetColorMode'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('interpolate_scalars_before_mapping',
    'GetInterpolateScalarsBeforeMapping'), ('progress_text',
    'GetProgressText'), ('use_lookup_table_scalar_range',
    'GetUseLookupTableScalarRange'), ('abort_execute', 'GetAbortExecute'),
    ('scalar_material_mode', 'GetScalarMaterialMode'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('progress', 'GetProgress'), ('render_time', 'GetRenderTime'),
    ('global_immediate_mode_rendering',
    'GetGlobalImmediateModeRendering'), ('scalar_range',
    'GetScalarRange'),
    ('resolve_coincident_topology_polygon_offset_faces',
    'GetResolveCoincidentTopologyPolygonOffsetFaces'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_immediate_mode_rendering',
    'global_warning_display', 'immediate_mode_rendering',
    'interpolate_scalars_before_mapping', 'release_data_flag',
    'scalar_visibility', 'static', 'use_lookup_table_scalar_range',
    'color_mode', 'resolve_coincident_topology', 'scalar_material_mode',
    'scalar_mode', 'force_compile_only', 'progress_text', 'render_time',
    'resolve_coincident_topology_polygon_offset_faces',
    'resolve_coincident_topology_z_shift', 'scalar_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CompositePolyDataMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CompositePolyDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_immediate_mode_rendering',
            'immediate_mode_rendering', 'interpolate_scalars_before_mapping',
            'scalar_visibility', 'static', 'use_lookup_table_scalar_range'],
            ['color_mode', 'resolve_coincident_topology', 'scalar_material_mode',
            'scalar_mode'], ['force_compile_only', 'render_time',
            'resolve_coincident_topology_polygon_offset_faces',
            'resolve_coincident_topology_z_shift', 'scalar_range']),
            title='Edit CompositePolyDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CompositePolyDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
