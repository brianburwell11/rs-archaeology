from sys import path

from flask import Blueprint, render_template, request
from sqlalchemy import and_

path.insert(0, '..')
from auth import auth
from db import *
from db import engine
from db.models import material_artefact as m_a
from create_db import ARTEFACTS


admin_blueprint = Blueprint('admin_blueprint', __name__,
                            template_folder='templates',
                            static_folder='static')

@admin_blueprint.before_request
@auth.login_required()
def before_request():
    """This function is called before every request.

    Putting the login_required decorator on this function protects every
    endpoint in the blueprint, only allowing authenticated users to use this endpoint.
    """

    ...

# ------------------------------ #

@admin_blueprint.route('/add/artefact', methods=['GET', 'POST'])
def add_artefact():
    if request.method == 'POST':
        r = request.form
        
        try:
            data = {
                'id': int(r['id']),
                'name': r['name'],
                'alignment': r['alignment'],
                'level_required': int(r['levelRequired']),
                'xp': float(r['xp'])
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
        
        try:
            session = Session()
            session.add(Artefact(**data))
            session.commit()
            session.close()
        except Exception as e:
            session.close()
            return {
                'success': False,
                'error': str(e)
            }

        idx = ARTEFACTS.index(r['name'])
        return {
            'success': True,
            'next': ARTEFACTS[idx+1]
        }

    return render_template('add-artefact.html')

@admin_blueprint.route('/add/artefact-materials', methods=['GET', 'POST'])
def add_artefact_material():
    if request.method == 'POST':
        r = request.form

        materials = r.get('materials', '')
        if materials != '':
            materials = materials.split(',')
            materials_dict = {int(materials[i]):int(materials[i+1]) for i in range(0,len(materials),2)}
            try:
                for material_id,material_amt in materials_dict.items():
                    session = Session()

                    artefact = session.query(Artefact).filter_by(id=r['artefactId']).first()
                    if artefact is None:
                        raise Exception(f'No Artefact with id={r["artefactId"]} found')
                    artefact_name = artefact.name

                    material = session.query(Material).filter_by(id=material_id).first()
                    if material is None:
                        raise Exception(f'No Material with id={material_id} found')

                    if material not in artefact.materials:
                        artefact.materials.append(material)
                    
                    session.commit()

                    sql_statement = m_a.update() \
                                    .where(and_(
                                        m_a.c.material_id==material_id,
                                        m_a.c.artefact_id==artefact.id
                                        )) \
                                    .values(amount=material_amt)
                    session.close() #have to close this session because

                    engine.execute(sql_statement) #SQLite is too wimpy to have two concurrent processes

            except Exception as e:
                session.close()
                print(e)
                return {
                    'success': False,
                    'error': str(e)
                    }

            session.commit()        
            session.close()

            return {
                'success': True,
                'msg': f'Succesfully updated {artefact_name}'
            }, 200

        return {
            'success': False,
            'error': 'No materials specified'
        }, 400

    return render_template('add-artefact-materials.html')