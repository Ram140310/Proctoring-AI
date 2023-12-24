from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute_all')
def execute_all():
    files = [
        'person_and_phone.py',
        'mouth_opening_detector.py',
        'head_pose_estimation.py',
        'face_spoofing.py',
        'face_landmarks.py',
        'face_detector.py',
        'eye_tracker.py',
        'audio_part.py'
    ]
    
    try:
        processes = []
        for file_name in files:
            command = f"python {file_name}"
            process = subprocess.Popen(command, shell=True, 
stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            processes.append(process)
        
        outputs = []
        for process in processes:
            output, error = process.communicate()
            if error:
                outputs.append({"status": "Error", "message": 
error.decode('utf-8')})
            else:
                outputs.append({"status": "Success", "output": 
output.decode('utf-8')})

        return jsonify({"status": "All files executed", "outputs": 
outputs})
    
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000,debug=True)

