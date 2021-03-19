+++
type = "question"
title = "NPF driver Problem in Windows 7"
description = '''I am using Windows 7 64bit edition; when i first installed Wireshark it worked, but after restart its constantly telling me NPF driver is not running error and therefore I cannot see any of my network cards. Please help'''
date = "2010-12-07T23:42:00Z"
lastmod = "2014-12-23T22:25:00Z"
weight = 1281
keywords = [ "windows7", "npf", "driver" ]
aliases = [ "/questions/1281" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [NPF driver Problem in Windows 7](/questions/1281/npf-driver-problem-in-windows-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1281-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Windows 7 64bit edition; when i first installed Wireshark it worked, but after restart its constantly telling me NPF driver is not running error and therefore I cannot see any of my network cards. Please help</p></div><div id="question-tags" class="tags-container tags">windows7 npf driver</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '10, 23:42</strong></p><img src="https://secure.gravatar.com/avatar/c95c425d2d1ab125d82f867e11d63e12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Engr%20Mansoor%20Habib&#39;s gravatar image" /><p>Engr Mansoor...<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Engr Mansoor Habib has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jan '11, 12:11</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-1281" class="comments-container"><span id="8022"></span><div id="comment-8022" class="comment"><div id="post-8022-score" class="comment-score"></div><div class="comment-text"><p>Hi all, I have the exact same symptoms but without the NPF driver error and also I get the proper output from the SC command. Any ideas?</p></div><div id="comment-8022-info" class="comment-info"><span class="comment-age">(16 Dec '11, 14:07)</span> Jim Willows</div></div></div><div id="comment-tools-1281" class="comment-tools"></div><div class="clear"></div><div id="comment-1281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="1282"></span>

<div id="answer-container-1282" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1282-score" class="post-score" title="current number of votes">13</div></div></td><td><div class="item-right"><div class="answer-body"><p>I am using Wireshark on the 64-bit edition of Windows 7 without problem.</p><p>The npf driver is not visible in your regular "Computer Management" WMI-interface. The npf status is best checked with the command line.</p><p>Run a cmd.exe as administrator and run the command <strong>sc qc npf</strong>.</p><p>You should get some output like this:</p><pre><code>C:\Windows\system32&gt;sc qc npf
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: npf
        TYPE               : 1  KERNEL_DRIVER
        START_TYPE         : 2   AUTO_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : system32\drivers\npf.sys
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : NetGroup Packet Filter Driver
        DEPENDENCIES       :
        SERVICE_START_NAME :</code></pre><p>If your driver is not properly started, activate it with the command <strong>sc start npf</strong></p><p>Finally, to start the service automatically, use the command <strong>sc config npf start=auto</strong></p><p>Remember to run your cmd.exe as administrator when issuing these command.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '10, 01:26</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-1282" class="comments-container"><span id="1824"></span><div id="comment-1824" class="comment"><div id="post-1824-score" class="comment-score"></div><div class="comment-text"><p>I am running Windows 7 and I have the same issue with the NPF file not running. I tried your command line stuff. I am set as the administrator on this machine and I get an Access Denied error when I try the sc start npf. Any suggestions?</p></div><div id="comment-1824-info" class="comment-info"><span class="comment-age">(19 Jan '11, 21:11)</span> Joshua</div></div><span id="1838"></span><div id="comment-1838" class="comment not_top_scorer"><div id="post-1838-score" class="comment-score"></div><div class="comment-text"><p>I have also activated NPF fow windows 7. And wireshark 1.4.3 still says it is not active. And also says there are no interfaces that a capture can be done. I'm running an HP Desktop and Windows 7 Home Premium.</p></div><div id="comment-1838-info" class="comment-info"><span class="comment-age">(20 Jan '11, 17:39)</span> yate4899</div></div><span id="2261"></span><div id="comment-2261" class="comment"><div id="post-2261-score" class="comment-score">1</div><div class="comment-text"><p>try to run cmd.exe as an administrator (i mean right click it then choose run as administrator) and then use the command <strong>sc start npf</strong></p></div><div id="comment-2261-info" class="comment-info"><span class="comment-age">(09 Feb '11, 13:23)</span> EssAm</div></div><span id="5415"></span><div id="comment-5415" class="comment"><div id="post-5415-score" class="comment-score">4</div><div class="comment-text"><p>There must be a space after equal sign, i.e.</p><p><strong>sc config npf start= auto</strong></p><p>The rest is perfect:</p><blockquote><p><strong>sc qc npf</strong><br />
Run as Administrator:<br />
<strong>sc start npf</strong></p></blockquote></div><div id="comment-5415-info" class="comment-info"><span class="comment-age">(02 Aug '11, 22:54)</span> Champion</div></div><span id="6938"></span><div id="comment-6938" class="comment not_top_scorer"><div id="post-6938-score" class="comment-score"></div><div class="comment-text"><p>Thank you packethunter, your answer enabled me to get working with Wireshark. One thing though, I can't find the npf service - whose DISPLAY_NAME is given as "NetGroup Packet Filter Driver" listed in the Windows Services. Can anyone enlighten me please?</p></div><div id="comment-6938-info" class="comment-info"><span class="comment-age">(17 Oct '11, 16:56)</span> pcwizard</div></div><span id="6940"></span><div id="comment-6940" class="comment"><div id="post-6940-score" class="comment-score">2</div><div class="comment-text"><p>You can find the NPF driver under Non-Plug and Play Drivers<br />
To open the Computer Management console go to:<br />
Start | Run<br />
type: compmgmt.msc and hit OK<br />
Select:<br />
Computer Management (Local) | System tools | Device Manager<br />
Pull-down menu View | Show Hidden Devices<br />
Non-Plug and Play Drivers | NetGroup Packet Filter Driver</p></div><div id="comment-6940-info" class="comment-info"><span class="comment-age">(17 Oct '11, 21:14)</span> joke</div></div><span id="8337"></span><div id="comment-8337" class="comment not_top_scorer"><div id="post-8337-score" class="comment-score"></div><div class="comment-text"><p>Great!! it is working...BIG THANKS to you. Back to business!</p></div><div id="comment-8337-info" class="comment-info"><span class="comment-age">(12 Jan '12, 07:35)</span> deo</div></div><span id="8338"></span><div id="comment-8338" class="comment not_top_scorer"><div id="post-8338-score" class="comment-score"></div><div class="comment-text"><p>Sorry: I meant for the above "Great ..." to have been converted to a comment under answer #1 (not this answer).</p></div><div id="comment-8338-info" class="comment-info"><span class="comment-age">(12 Jan '12, 08:05)</span> Bill Meier ♦♦</div></div><span id="10912"></span><div id="comment-10912" class="comment not_top_scorer"><div id="post-10912-score" class="comment-score"></div><div class="comment-text"><p>I had to go into the non-plug and play how do I get it to start once I get there?</p></div><div id="comment-10912-info" class="comment-info"><span class="comment-age">(10 May '12, 20:01)</span> angelar</div></div><span id="10915"></span><div id="comment-10915" class="comment not_top_scorer"><div id="post-10915-score" class="comment-score"></div><div class="comment-text"><p>right-click NetGroup Packet Filter Driver<br />
select Properties<br />
select tab Driver<br />
Current status: hit Start<br />
BTW<br />
Here you can read more about <a href="http://technet.microsoft.com/en-us/library/cc756775%28v=ws.10%29.aspx">Startup - Type</a></p></div><div id="comment-10915-info" class="comment-info"><span class="comment-age">(10 May '12, 21:18)</span> joke</div></div><span id="14835"></span><div id="comment-14835" class="comment"><div id="post-14835-score" class="comment-score">2</div><div class="comment-text"><p>This solution also works for Windows 8.</p></div><div id="comment-14835-info" class="comment-info"><span class="comment-age">(09 Oct '12, 13:41)</span> SamsonSF</div></div><span id="19096"></span><div id="comment-19096" class="comment not_top_scorer"><div id="post-19096-score" class="comment-score"></div><div class="comment-text"><p>Tanx alot, was really helpfull.</p></div><div id="comment-19096-info" class="comment-info"><span class="comment-age">(02 Mar '13, 13:28)</span> s_atayi379</div></div><span id="22048"></span><div id="comment-22048" class="comment not_top_scorer"><div id="post-22048-score" class="comment-score"></div><div class="comment-text"><p>You need to add a space between "<code>start=</code>" and "<code>auto</code>".</p></div><div id="comment-22048-info" class="comment-info"><span class="comment-age">(14 Jun '13, 03:10)</span> Mladen B</div></div><span id="34622"></span><div id="comment-34622" class="comment not_top_scorer"><div id="post-34622-score" class="comment-score"></div><div class="comment-text"><p>run as administrator, sc config npf start= auto is the exact command. Space is required after "=".</p></div><div id="comment-34622-info" class="comment-info"><span class="comment-age">(13 Jul '14, 05:09)</span> Utkal Barik</div></div><span id="37629"></span><div id="comment-37629" class="comment not_top_scorer"><div id="post-37629-score" class="comment-score"></div><div class="comment-text"><p>very good , i study network from belém PA, thanks great!</p></div><div id="comment-37629-info" class="comment-info"><span class="comment-age">(06 Nov '14, 15:53)</span> Marciel Rodr...</div></div><span id="59035"></span><div id="comment-59035" class="comment not_top_scorer"><div id="post-59035-score" class="comment-score"></div><div class="comment-text"><p>I created a 'shortcut icon' in Windows 10 to do this. Just make shore that the shortcut properties has 'Run as Admin' selected. The command line in the shortcut target is: %windir%\system32\cmd.exe /K sc start npf</p></div><div id="comment-59035-info" class="comment-info"><span class="comment-age">(24 Jan '17, 16:19)</span> pcarew</div></div></div><div id="comment-tools-1282" class="comment-tools"><span class="comments-showing"> showing 5 of 16 </span> <a href="#" class="show-all-comments-link">show 11 more comments</a></div><div class="clear"></div><div id="comment-1282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38690"></span>

<div id="answer-container-38690" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38690-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Find the file called <em>npf.sys</em> which is located at</p><ul><li>C:\Windows\System32\Drivers\</li></ul><p>in Windows 7. Then make sure that you have installed winpcap, if you didn't install it, just go to its official site and download it for installation: <a href="http://www.winpcap.org"></a><a href="http://www.winpcap.org">http://www.winpcap.org</a></p><p>Next, find cmd.exe which is located at</p><ul><li>C:\Windows\System32</li></ul><p>in Windows 7, right click and "Run as administrator". When it opened, input <em>net start npf</em>, then the NPF driver is successfully opened. That is,the file npf.sys is opened.</p><p>At last, restart Wireshark, it will be OK now.</p><p>BTW, if you have other driver problems or want to update, backup or restore drivers, the free program <strong>DriveTheLife</strong> (official site: <a href="http://www.drivethelife.com"></a><a href="http://www.drivethelife.com">http://www.drivethelife.com</a>) is a perfect one.</p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '14, 22:25</strong></p><img src="https://secure.gravatar.com/avatar/0bc6696cb16a86e51f6ae1fd661a3bac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OliviaLewis&#39;s gravatar image" /><p>OliviaLewis<br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OliviaLewis has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-38690" class="comments-container"></div><div id="comment-tools-38690" class="comment-tools"></div><div class="clear"></div><div id="comment-38690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5482"></span>

<div id="answer-container-5482" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5482-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just run the shark under administrator and it will work as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '11, 00:44</strong></p><img src="https://secure.gravatar.com/avatar/b0484f4a1ae8903955337928f90d0f04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="projek7r&#39;s gravatar image" /><p>projek7r<br />
<span class="score" title="15 reputation points">15</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="projek7r has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-5482" class="comments-container"><span id="5485"></span><div id="comment-5485" class="comment"><div id="post-5485-score" class="comment-score">1</div><div class="comment-text"><p>While this may well "work" it isn't really recommended.</p><p>There is a huge amount of code in Wireshark that attempts to interpret network data, and allowing that code to run as administrator does open a window (albeit quite small) to "bad stuff" gaining access to the host system as the administrator.</p></div><div id="comment-5485-info" class="comment-info"><span class="comment-age">(04 Aug '11, 01:18)</span> grahamb ♦</div></div></div><div id="comment-tools-5482" class="comment-tools"></div><div class="clear"></div><div id="comment-5482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

