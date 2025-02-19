from flask import Blueprint, request, jsonify
from backend.app.models.schedule import Schedule

schedule_bp = Blueprint('schedule', __name__)

@schedule_bp.route('/schedules', methods=['GET'])
def get_schedules():
    # Logic to retrieve all schedules
    schedules = Schedule.get_all_schedules()
    return jsonify(schedules), 200

@schedule_bp.route('/schedules/<int:user_id>', methods=['GET'])
def get_user_schedule(user_id):
    # Logic to retrieve a specific user's schedule
    user_schedule = Schedule.get_schedule_by_user(user_id)
    return jsonify(user_schedule), 200

@schedule_bp.route('/schedules', methods=['POST'])
def create_schedule():
    # Logic to create a new schedule
    data = request.json
    new_schedule = Schedule.create_schedule(data)
    return jsonify(new_schedule), 201

@schedule_bp.route('/schedules/<int:schedule_id>', methods=['PUT'])
def update_schedule(schedule_id):
    # Logic to update an existing schedule
    data = request.json
    updated_schedule = Schedule.update_schedule(schedule_id, data)
    return jsonify(updated_schedule), 200

@schedule_bp.route('/schedules/<int:schedule_id>', methods=['DELETE'])
def delete_schedule(schedule_id):
    # Logic to delete a schedule
    Schedule.delete_schedule(schedule_id)
    return jsonify({'message': 'Schedule deleted successfully'}), 204