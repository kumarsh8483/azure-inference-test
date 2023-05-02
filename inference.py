from nnunet.inference.predict import predict_from_folder
from nnunet.paths import default_plans_identifier, default_cascade_trainer, default_trainer
import os
from time import time
import shutil 
import base64

network_dir = "network_dir"
input_folder = "inputs"
output_folder = "outputs"
part_id = 0 # used when parallelization
num_parts = 1 # used when parallelization
folds = None # automatically detected if none
save_npz = False # used when ensembling with other models
lowres_segmentations = None
num_threads_preprocessing = 6
num_threads_nifti_save = 2
disable_tta = False
step_size = 0.5
overwrite_existing = False
mode = "normal"
all_in_gpu = None
model = "2d"
trainer_class_name = default_trainer
cascade_trainer_class_name = default_cascade_trainer

task_name = "Task005_Prostate" #default_plans_identifier

if model == "3d_cascade_fullres":
    trainer = cascade_trainer_class_name
else:
    trainer = trainer_class_name


if not task_name.startswith("Task"):
    task_id = int(task_name)
    task_name = convert_id_to_task_name(task_id)


model_folder_name = os.path.join(network_dir, model, task_name, trainer + "__" +
                              default_plans_identifier)
print("using model stored in ", model_folder_name)
assert os.path.isdir(model_folder_name), "model output folder not found. Expected: %s" % model_folder_name

st = time()
predict_from_folder(model_folder_name, input_folder, output_folder, folds, save_npz, num_threads_preprocessing,
                    num_threads_nifti_save, lowres_segmentations, part_id, num_parts, not disable_tta,
                    overwrite_existing=overwrite_existing, mode=mode, overwrite_all_in_gpu=all_in_gpu,
                    mixed_precision=False,
                    step_size=step_size, checkpoint_name="model_best")
end = time()
print("prediction_time :", end - st)