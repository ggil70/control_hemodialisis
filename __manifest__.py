# -*- coding: utf-8 -*-

{
        'name': "Control de Hemodialisis",
        'version' : "1.0",
        'author' : "Gheylert A. Gil / Beatriz Coronel",
        'website' : "",
        'category' : "Servicio Medico",
        
        'description': """
                 Control de Hemodialisis
         """,
        'depends' : ['base'],
        'data' : [
            'security/groups.xml',
            'security/ir.model.access.csv',
            'views/menu_action_view.xml',
            'views/paciente_view.xml',
            'views/medico_view.xml',
            'views/tratamiento_view.xml',
            'wizard/reporte_historial_paciente_wizard.xml',
            
            'report/hemodialisis_encabezado_hemodialisis_template.xml',
            'report/listado_historial_paciente_template.xml',
            'report/listado_paciente_medico_template.xml',
            #'report/resultado_bienes_inventario_template.xml',


            #'wizard/listado_bien_grupo_reporte_wizard.xml',
            #'wizard/listado_bien_clasificacion_marca_reporte_wizard.xml',
            #'wizard/listado_bienes_sedes_reporte_wizard.xml'
            #'views/views.xml',
            #'report/report.xml',
            #'report/inventario_bienes_template.xml',
            #'report/action_report_personalizado_estudiante.xml',        
        ], 
        
        'installable': True,
        'auto_install': False
        
} 
