from json import loads
from sys import path

from flask import Blueprint, render_template, request
from sqlalchemy import and_

path.insert(0, '..')
from auth import auth
from db import *
from db import engine
from db.models import ( material_artefact as m_a,
                        artefact_collection_reward as a_c_r,
                        reward_collection as r_c
                      )
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

            return {
                'success': True,
                'msg': f'Succesfully updated {artefact_name}'
            }, 200

        return {
            'success': False,
            'error': 'No materials specified'
        }, 400

    return render_template('add-artefact-materials.html')


@admin_blueprint.route('/add/collection-info', methods=['GET', 'POST'])
def add_collection_info():
    if request.method == 'POST':
        r = request.form
        artefact_rewards = loads(r.get('artefactRewards', '[]'))
        collection_rewards = loads(r.get('collectionRewards', '[]'))

        try:
            for artefact_reward in artefact_rewards:
                session = Session()

                collection = session.query(Collection).filter_by(id=r['collectionId']).first()
                if collection is None:
                    raise Exception(f'No Collection with id={r["collectionId"]} found')
                collection_name = collection.name

                artefact = session.query(Artefact).filter_by(id=artefact_reward['artefactId']).first()
                if artefact is None:
                    raise Exception(f'No Artefact with id={artefact_reward["artefactId"]} found')
                    
                reward = session.query(Reward).filter_by(id=artefact_reward['rewardId']).first()
                if reward is None:
                    raise Exception(f'No Reward with id={artefact_reward["rewardId"]} found')
                    
                if artefact not in collection.artefacts:
                    collection.artefacts.append(artefact)
                
                session.commit()

                sql_statement = a_c_r.update() \
                                    .where(and_(
                                        a_c_r.c.artefact_id==artefact.id,
                                        a_c_r.c.collection_id==collection.id
                                        )) \
                                    .values(reward_id=reward.id, amount=artefact_reward['rewardAmt'])
                                    
                session.close() #have to close this session because

                engine.execute(sql_statement) #SQLite is too wimpy to have two concurrent processes
                
            for collection_reward in collection_rewards:
                session = Session()

                collection = session.query(Collection).filter_by(id=r['collectionId']).first()
                if collection is None:
                    raise Exception(f'No Collection with id={r["collectionId"]} found')
                collection_name = collection.name

                reward = session.query(Reward).filter_by(id=collection_reward['rewardId']).first()
                if reward is None:
                    raise Exception(f'No Reward with id={collection_reward["rewardId"]} found')
                
                if reward not in collection.rewards:
                    collection.rewards.append(reward)
                    session.commit()

                sql_statement = r_c.insert() \
                                    .values(
                                        collection_id=collection.id,
                                        reward_id=reward.id,
                                        amount=collection_reward['rewardAmt']
                                    )

                session.close() #have to close this session because

                engine.execute(sql_statement) #SQLite is too wimpy to have two concurrent processes

        except Exception as e:
                session.close()
                print(e)
                return {
                    'success': False,
                    'error': str(e)
                    }
        
        return {
            'success': True,
            'msg': f'Succesfully updated {collection_name}'
        }, 200


    return render_template('add-collection-info.html')
