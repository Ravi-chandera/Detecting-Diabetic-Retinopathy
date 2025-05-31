# Detecting-Diabetic-Retinopathy
## **Problem Statement**

Diabetic Retinopathy (DR) is one of the causes of vision loss among individuals with diabetes. Manual screening processes are time-consuming, resource-intensive, and often unavailable in underserved or rural areas. There is a need for a scalable, efficient, and reliable solution to detect DR early and accurately .

This is how eyes are examined and need to check fundus of eye manually and make decision. This is time consuming and also we need experts to perform and instrument to check. 
![Eye checking for DR](assets\image.png)

## **Expected Outcomes**

- AI model that can identify signs of Diabetic Retinopathy from retinal scans.
- Reduced dependency on specialist availability through assistive diagnostics.
- Deployment potential in remote areas through mobile or edge devices.
- A step towards large-scale screening for DR, contributing to early intervention and treatment.


## Dataset idea

From background knowledge of DR, I believe we would need data

## Class details

0 - No DR

1 - Mild

2 - Moderate

3 - Severe

4 - Proliferative DR

This is how problem becomes of multi class classification.

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
