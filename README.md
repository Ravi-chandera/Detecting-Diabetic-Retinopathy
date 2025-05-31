# Detecting-Diabetic-Retinopathy
## **Problem Statement**

Diabetic Retinopathy (DR) is one of the causes of vision loss among individuals with diabetes. Manual screening processes are time-consuming, resource-intensive, and often unavailable in underserved or rural areas. There is a need for a scalable, efficient, and reliable solution to detect DR early and accurately .

## **Expected Outcomes**

- AI model that can identify signs of Diabetic Retinopathy from retinal scans.
- Reduced dependency on specialist availability through assistive diagnostics.
- Deployment potential in remote areas through mobile or edge devices.
- A step towards large-scale screening for DR, contributing to early intervention and treatment.

<details>
<summary>More about DR</summary>

    Diabetic retinopathy is an eye condition and a complication of diabetes that damages the blood vessels in the retina—the light-sensitive tissue at the back of the eye responsible for vision. It is a leading cause of vision loss and blindness in adults, particularly in people who have had diabetes for many years
    
    ## Causes
    
    - Diabetic retinopathy is caused by prolonged high blood sugar levels associated with diabetes
    - Over time, high blood sugar damages the tiny blood vessels in the retina, causing them to leak fluid or bleed
    - In response to this damage, the eye may grow new, abnormal blood vessels that are fragile and prone to bleeding, leading to further vision problems
    
    ## Types and Stages
    
    There are two main stages:
    
    - Non proliferative Diabetic Retinopathy (NPDR): The early stage, where blood vessels in the retina weaken, swell, and may leak fluid or blood. This can lead to swelling of the retina (macular edema) and mild vision loss
    - Proliferative Diabetic Retinopathy (PDR): The advanced stage, marked by the growth of new, abnormal blood vessels on the retina’s surface. These vessels can bleed into the eye, cause scar tissue, and may result in severe vision loss or blindness
    
    ## Symptoms
    
    - Early diabetic retinopathy often has no symptoms
    - As the disease progresses, symptoms may include:
        - Blurred or fluctuating vision
        - Dark or empty areas in your vision
        - Spots or floaters
        - Vision loss
    
    ## Risk Factors
    
    - Anyone with type 1 or type 2 diabetes is at risk
    - The risk increases with the duration of diabetes, poor blood sugar control, high blood pressure, high cholesterol, pregnancy, and smoking
    
    ## Complications
    
    - If left untreated, diabetic retinopathy can lead to serious complications such as:
        - Vitreous hemorrhage (bleeding into the gel that fills the eye)
        - Retinal detachment
        - Glaucoma
        - Permanent blindness
    
    ## Prevention and Management
    
    - Good control of blood sugar, blood pressure, and cholesterol can significantly reduce the risk and slow the progression of diabetic retinopathy
    - Regular eye exams are crucial for early detection and treatment
    - Treatments include laser therapy, anti-VEGF injections, and surgery in advanced cases

</details>

## Dataset idea

From background knowledge of DR, I believe we would need data

## Class details

0 - No DR

1 - Mild

2 - Moderate

3 - Severe

4 - Proliferative DR

This is how problem becomes of multi class classification.

## Human observation of images

I believe if we can see some samples for each class, we get more idea of how they differ from each other, so later on during misclassifications we might know that what went wrong. 

Take a look at 100 images of each class.
### class 0
![Class 0](assets/class_0.png)

### class 1
![class 1](assets/class_1.png)

### class 2
![class 2](assets/class_2.png)

### class 3
![class 3](assets/class_3.png)

### class 4
![class 4](assets/class_4.png)

here are some observations. 

As we move from 0 to 4,

## Storing data 
Our data size is large and it can't be stored into local system, so I am using AWS S3. 
While creating bucket, I have enabled versioning so when we do training, all the model checkpoints are versioned.
S3 stores files directly and direcoties can't be made there, but there is workaround, name you file name like it is in diretory and then prase at your end.
<details>
<summary>More about versioning of s3 bucket</summary>
When you enable versioning in an Amazon S3 bucket, every version of an object—including previous versions and delete markers—is retained and stored until you explicitly delete them or set up automated rules to remove them. By default, these versions remain permanent and are not deleted automatically. This allows you to recover from accidental deletions or overwrites, as you can always restore a previous version.

Storage and Charges:

You are charged for every version of an object stored in your bucket. If you have multiple versions of a file (for example, three versions), you are billed for the total storage consumed by all three versions—not just the latest one.

Each version is a full copy of the object, not just a delta or difference from previous versions.

Managing Old Versions:

Old versions will continue to accumulate and incur storage costs unless you delete them manually or use S3 Lifecycle rules to automatically expire (delete) noncurrent versions after a set period
</details>
