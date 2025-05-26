select f3.serial, dateadd(s,f1.timestamp,'19700101'), concat('https://v9.footfallcam.com/FootfallCam/VerifyStudyReport?VerifyStudyReportId=' ,f1.id, '&sendReport=0'), OverallAccuracyIn,OverallAccuracyOut,OverallSampleSizeIn,OverallSampleSizeOut from FFVerificationStudyReports f1 
right join
(select max(timestamp) latesttimestamp,ffcameraid from FFVerificationStudyReports where ffcameraid in (select id from ffcameras where serial in (
'0000000072e82548'
)) group by ffcameraid) f2
on f1.timestamp = f2.latesttimestamp and f1.ffcameraid = f2.ffcameraid
left join ffcameras f3 on f1.ffcameraid = f3.id

--check who upload setting(param)
select * from offlinesimsettings where serial in (
'1000000081a8cdec'
)

--Check IP
select IP,* from FFCameras where serial = '10000000c7c06af3'


--check online or not
Select lastheartbeatdatetime,Serial,server, * from CounterHealthChecks where Serial in
(				
'10000000994afbb8'
)


-- check heartbeat trend --
SELECT DATEADD(second, Timestamp, CAST('1970-01-01 00:00:00' AS datetime)) AS UTCDateTime, DateTime AS LocalDateTime, LastBoot, Wifi,
Version, PatchVersion, Raspicam, Memory, Storage, DStorage, cameraError, CountingData, Name as CounterName, BranchName, ExternalIP, SoftetherIP, Temp, * FROM FFCounterCameraHCs 
WHERE serial LIKE '%10000000fc5b4da1%' ORDER BY ID DESC


--if running, wait for 15 minutes
Update FFCameraSettings set Softether = 1 where CameraId in(select id from ffcameras where Serial in
(
'10000000464a5a44'
))


--run(check softether IP)
Select TOP 200 Softether, SoftetherIP, Serial,DateTime,counterCurrentDateTimeTimezone,* from FFCounterCameraHCs  
where serial in
( 
'10000000464a5a44'
)
order by id desc;

--check Device IP
SELECT chc.server, chc.Verification_Tuner, chc.Serial, chc.ip, chc.CompanyName, chc.BranchName, chc.CameraName, chc.CompanySerial, chc.PatchVersion  FROM CounterHealthChecks AS chc
--JOIN DeviceTrackers AS dt on (chc.Serial = dt.Serial)
WHERE chc.serial in (
'000000008b07d7b2',
'00000000c490ef31',
'000000009231ce5e',
'0000000099231b59',
'0000000017386a84'
)

--Check certified report
select
	concat('https://v9.footfallcam.com/FootfallCam/VerifyStudyReport?VerifyStudyReportId=' , id, '&sendReport=0'), dateadd(s,timestamp,'1970-01-01'),*
from
	RetailCamControlPanel.dbo.FFVerificationStudyReports
where
	ffcameraid in (
	select
			id
	from
		RetailCamControlPanel.dbo.FFCameras
	where

		serial in ('10000000335f3a6d'))


--Check param upload status 6848 (can check if force param show no setting):
select * from offlinesimsettings where serial in (
'100000006a64bc88'
)

select CameraFirmwareVersion,count(CameraFirmwareVersion) as TotalAmount from ffcameras group by CameraFirmwareVersion


select FC.IP, FC.CounterCameraType, FC.serial, FC.companySerial, FC.BranchName, FC.BranchCode, FC.CameraName, FC.PatchVersion, CHC.CompanyName, CHC.CounterVerifiedDateTime, CHC.Server, CHC.IP as DeviceIP, OSS.Email as UploadSetting from FFCameras FC, CounterHealthChecks CHC, offlinesimsettings OSS
where FC.Serial = CHC.Serial and 
OSS.Serial = CHC.Serial and
FC.Serial in ('10000000ccb8f909')

--Check all device in this side
WITH SerialInfo AS (
    SELECT companyname, BranchName 
    FROM CounterHealthChecks 
    WHERE CompanySerial = ('15F010248414')
)
SELECT * 
FROM CounterHealthChecks 
WHERE companyname IN (SELECT companyname FROM SerialInfo)
AND BranchName IN (SELECT BranchName FROM SerialInfo) Order by CameraName;


--find data integrity report
SELECT * FROM FFCameraHourlyValues WHERE CameraID in (select id from ffcameras where serial in (
'10000000e16200d3'
)) 
ORDER BY ValueDateTime desc




--Change video download status--
 

select filename,status,RecordingType, * from ffvideoschedules where filename like '%100000003017a998%'


update ffvideoschedules set status =2 where filename like '%.zip' and filename like '%100000003017a998%' and status = 19

update ffvideoschedules set status =2 where filename like '%.zip' and filename like '%1000000005a0b4f9%' and status = 16
update ffvideoschedules set status =2 where filename like '%.zip' and filename like '%1000000005a0b4f9_OfflineSim_19-07-2024 16-30-00.zip%' and status = 19

begin tran
commit tran
rollback tran


--modify ticket query
--take ticket id
select * from supportportal.dbo.supporttickets where id = 72582
select * from supportportal.dbo.supporttickets where TicketSupportPerson = 'Guan Hao'
				



--take msg content id and msg content
select messagecontent, * from supportportal.dbo.TicketChats where ticketid = '878E26E4-968E-45B0-99F1-75CA49802A36' order by messagedatetime desc

begin tran
delete from supportportal.dbo.TicketChats where ChatID= 'FCAEDB98-4759-EF11-AE78-D05099FE293D'
			
			



--update msg content
update supportportal.dbo.TicketChats set messagecontent = '
<div>Hi,</div><div><br></div><div>Hope you are well.</div><div><br></div><div>The [15F010249099] [100000007d111a35] (Site [Khafji Othaim Mall]) has been tuned and it is ready for business use. You can see the latest param here (https://prnt.sc/sPWroHqcSxMw). As part of our FootfallCam process, we would continue to monitor the accuracy of the site.</div><div><br></div><div>Many Thanks</div>'
where chatid = 'EFB79079-2997-EF11-AE78-D05099FE293D'


select
	concat('https://v9.footfallcam.com/FootfallCam/VerifyStudyReport?VerifyStudyReportId=' , id, '&sendReport=0'), dateadd(s,timestamp,'1970-01-01'),*
from
	RetailCamControlPanel.dbo.FFVerificationStudyReports
where
	ffcameraid in (
	select
			id
	from
		RetailCamControlPanel.dbo.FFCameras
	where

		serial in ('00000000c5b05e23'))
		
begin tran





--update RetailCamControlPanel.dbo.FFVerificationStudyReports (dunno 6848 or 218)
set AdditionalComment = 'Param settings have been tuned with confidence for this device so that it is able to track people''s movements properly within the tracking zone. However, as this device is mainly used for counting on OUT value, the number of IN counts is significantly lower than the OUT counts. (https://imgur.com/a/heAKuO6)<br/><br/>For now, we have reviewed the accuracy on 1 video to achieve a higher sample size and more precise accuracy which is a total of 263 In and 1 Out count (video can achieve In 98.86% and Out 100%). FootfallCam has optimized the best settings according to this device and no further action is required.<br/>'
where ID = 176287





--218
update workspace.dbo.VerificationAssignationWorkspace set TuningStartDateTime = '2024-09-27 00:00:00.000' where ChipsetCode = '100000003254af2c'
update workspace.dbo.VerificationAssignationWorkspace set TuningEndDateTime = '2024-10-15 18:00:00.000' where ChipsetCode in ('1000000059f819bf')

select auditstage, assignee, CompanySerial, chipsetcode, TuningStartDateTime, TuningEndDateTime, VerificationEndDateTime from workspace.dbo.verificationassignationworkspace where ChipsetCode in (
'00000000d317d2da'
) 

update workspace.dbo.VerificationAssignationWorkspace set AuditStage = '8' where ChipsetCode in (
'00000000d317d2da'
)



select serial, AuditStage from CounterHealthChecks where CompanyCode in (
'WatsonMsia') and AuditStage = '8'


--Check all certified device after (Date)
select AuditStage,CompanyCode, serial, CounterVerifiedDateTime, * from CounterHealthChecks where CounterVerifiedDateTime > '2024-10-23 00:00:00.000' and AuditStage = '8' and Server != 'http://footfallcounter.com' and Server != 'https://footfallcounter.com' and Server != 'https://login.footfallcounts.com/' order by Server

-- 6848
select IsVerified, verification_tuner, AuditStage,serial, Verification_EndDateTime, CounterVerifiedDateTime, * from CounterHealthChecks where Serial in (
'100000004efd1536',
'10000000b26c4f48',
'00000000582b6fa9',
'000000006472a5b3',
'000000006dbc7475',
'10000000375766d3',
'100000007b765cdd',
'1000000084c44464',
'10000000b6ecf671',
'10000000a8161dec',
'100000002809a956',
'00000000b5e9e2af',
'000000003259ff61',
'100000000533640c',
'10000000baff306e',
'1000000012c99fbe',
'10000000652d2af4',
'100000007f085468',
'10000000a413d75f'
)


update CounterHealthChecks set AuditStage = '8' where serial in (
'100000004efd1536',
'10000000b26c4f48',
'00000000582b6fa9',
'000000006472a5b3',
'000000006dbc7475',
'10000000375766d3',
'100000007b765cdd',
'1000000084c44464',
'10000000b6ecf671',
'10000000a8161dec',
'100000002809a956',
'00000000b5e9e2af',
'000000003259ff61',
'100000000533640c',
'10000000baff306e',
'1000000012c99fbe',
'10000000652d2af4',
'100000007f085468',
'10000000a413d75f'
)

begin tran
commit tran
rollback tran



--Check OdooID 218:
select * from SupportPortal.dbo.MetaUser where OdooUserName like '%Ansel%'
select * from SupportPortal.dbo.MetaUser where OdooUserId?=?700

--per tuner check traffic light 
select assignee,chipsetcode, auditstage, tuningstartdatetime,
case when datediff(day, tuningstartdatetime, GETUTCDATE()) <= 3 then 'Green (<3)'
	 when datediff(day, tuningstartdatetime, GETUTCDATE()) >7 then 'Red (>7)'
	 else 'Yellow (4-7)' end as DeviceSLA
from Workspace.dbo.verificationassignationworkspace where Assignee = 804 and auditstage = 9
order by TuningStartDateTime


-------------bulk schedule---------------------------------
 
select filename,status,RecordingType, * from ffvideoschedules where filename like '%10000000464a5a44%'

--bulk schedule video
select concat('insertVSchedule(', id, ')') from ffcameras where serial in (
'10000000464a5a44'
)

delete from FFVideoSchedules where ffcameraid in (
select id from ffcameras where serial in (
'10000000fc5b4da1')
and RecordingType in ('0') and ScheduleDateTime in ('2024-11-16 12:00:00.000', '2024-11-16 13:00:00.000', '2024-11-16 14:00:00.000'))

--check able to schedule or not
select RecordingType, * from FFVideoSchedules where ffcameraid in (
select id from ffcameras where serial in (
'10000000464a5a44'
)
and DATEDIFF(day, scheduledatetime, GETDATE()) <= 2) and RecordingType = '3'
order by scheduledatetime 

select * from ffcameras where serial in ('000000002152d134');

insertVSchedule(69548)
insertVSchedule(69549)
insertVSchedule(69510)
insertVSchedule(69511)

function insertVSchedule(cameraId) {		
		$.ajax({
		url: "/FootfallCam/InsertVerificationSchedule3D?cameraID=" + cameraId,
		data: '[{"recordingOne":{"StartTime":15,"StartTime_Min":00,"Duration":30},"recordingTwo":{"StartTime":17,"StartTime_Min":00,"Duration":30},"recordingThree":{"StartTime":20,"StartTime_Min":00,"Duration":30},"recordingStartDate":"01/11/2024","recordingType":"3","counterLocalTime":"2022-05-11T05:50:10.000Z","isIndividualRecordingTypeTurnOn":false},{},{}]',
		type: "POST",
	dataType: "json",	
	contentType: "application/json; charset=utf-8",	
		success: function (data) {
		},
		error: function (data){
		}
		});
}



-- check everyday
select
	chc.serial,
	vaw.auditstage as vaw_auditstage,
	chc.auditstage as chc_auditstage,
	vaw.verificationenddatetime as vaw_verifieddatetime,
	chc.counterverifieddatetime as chc_verifieddatetime,
	chc.CameraName,
	chc.branchname ,
	chc.companyname,
	vaw.tuningenddatetime
from
	dbo.rccp_counterhealthchecks chc
left join dbo.workspace_verificationassignationworkspace vaw on
	vaw.chipsetcode = chc.serial
	where vaw.auditstage = 8 and chc.auditstage != 8
	and vaw.verificationenddatetime >= '2010-01-01 00:00:00'
	order by vaw.verificationenddatetime desc




--Email to contact
select dateadd(s,lastlogintimestamp, '1970-01-01') as LastLoginTime, * from users where companycode in
(Select CompanyCode from retailcamcontrolpanel.dbo.CounterHealthChecks c  where Serial in(
'000000007f2afe37') 
 )
Order by LastLoginTime DESC 


--Camera Scaling Factor
select serial, camerascalingfactor from ffcameras where serial = '10000000335f3a6d'

update ffcameras set camerascalingfactor=1.1 where serial = '10000000335f3a6d'





