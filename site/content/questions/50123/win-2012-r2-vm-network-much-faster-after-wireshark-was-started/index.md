+++
type = "question"
title = "Win 2012 R2 VM - Network much faster after Wireshark was started..."
description = '''Dear WireShark Team, I have a very interesting behavior on some VM&#x27;s installed with plain Windows 2012 R2 Server using PVSCSI and VMXNET3 drivers on vSphere 6. Using a database client application it takes a x amount of time to load the data from the db to the VM. For troubleshooting reasons I instal...'''
date = "2016-02-12T02:13:00Z"
lastmod = "2016-02-13T12:21:00Z"
weight = 50123
keywords = [ "windows2012r2", "application", "vmxnet3", "wireshark" ]
aliases = [ "/questions/50123" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Win 2012 R2 VM - Network much faster after Wireshark was started...](/questions/50123/win-2012-r2-vm-network-much-faster-after-wireshark-was-started)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50123-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Dear WireShark Team, I have a very interesting behavior on some VM's installed with plain Windows 2012 R2 Server using PVSCSI and VMXNET3 drivers on vSphere 6.</p><p>Using a database client application it takes a x amount of time to load the data from the db to the VM. For troubleshooting reasons I installed WireShark as the loading performance was not sufficient.</p><p>Now the cool thing is that starting WireShark and closing it again and then using the database client application suddenly everything is very fast! This performance improvement stays there until the VM is restarted. Opening and closing WireShark again is then bringing the VM network speed back to it's high performance.</p><p>It seems that during the start of WireShark something is changed/reinitialized on the Windows networking parameters. Since I'm not very fund of reading source code I was wondering if any of you guys can tell me what is done on the Windows network side while starting WireShark or if you might have any hints regarding this.</p><p>Regards LC</p></div><div id="question-tags" class="tags-container tags">windows2012r2 application vmxnet3 wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '16, 02:13</strong></p><img src="https://secure.gravatar.com/avatar/4c23d1bd79be44f32c9156c798b41213?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Linuxcrash&#39;s gravatar image" /><p>Linuxcrash<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Linuxcrash has no accepted answers">0%</span></p></div></div><div id="comments-container-50123" class="comments-container"><span id="50175"></span><div id="comment-50175" class="comment"><div id="post-50175-score" class="comment-score"></div><div class="comment-text"><p>we have exactly the same problem! and we thought we're getting nuts here. you have some news on this?</p></div><div id="comment-50175-info" class="comment-info"><span class="comment-age">(13 Feb '16, 06:50)</span> p199y</div></div><span id="50176"></span><div id="comment-50176" class="comment"><div id="post-50176-score" class="comment-score"></div><div class="comment-text"><p>i wanted to post this question, since i saw someone already has the same problem i post this here, maybe some usefull information:</p><p>We have a performance issue with our intranet website. we checked network settings on our Cisco switches, web server configuration, SQL server configuration, OS settings, logs and so on but we could not grip where the problem is coming from. so we tried if we can find something by capturing some LAN traffic with Wireshark, then something unexpected happened: when we start Wireshark on the web server (Win 2012 R2), the performance issue instantly disappears. We can close Wireshark, restart the IIS Webservice, disable / enable the network connection, the performance issues does not appear anymore until we restart the OS of the Webserver. now we found out, that when we only start dumpcap in a cmd window the same effect happens: no performance issues.</p><p>you can imagine this leaves us kind of buffeled since we cant understand how starting wireshark to debug a problem actually solves it. is there anyone who can explain what exactly happens on OS level when dumpcap starts?</p><p>BTW: also starting windump.exe has the same effect.</p><p>also to mention: the NPF service / winpcap Driver starts automatically with the OS.</p><p>We run our webserver on a ESXi 6.0 Update 1 (newest Patch releases) Windows Server 2012 R2 Guest OS, VMXNET3 Drivers.</p></div><div id="comment-50176-info" class="comment-info"><span class="comment-age">(13 Feb '16, 07:00)</span> p199y</div></div></div><div id="comment-tools-50123" class="comment-tools"></div><div class="clear"></div><div id="comment-50123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50178"></span>

<div id="answer-container-50178" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50178-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Good news, we found a solution that worked for us:</p><p>try this: disable LRO aka RSC on your VM:</p><p><a href="http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=2129176">http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=2129176</a></p><p>good luck</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '16, 12:21</strong></p><img src="https://secure.gravatar.com/avatar/cb36cdbb64882ae510fb4dec1c43c9ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="p199y&#39;s gravatar image" /><p>p199y<br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="p199y has one accepted answer">100%</span></p></div></div><div id="comments-container-50178" class="comments-container"><span id="50204"></span><div id="comment-50204" class="comment"><div id="post-50204-score" class="comment-score"></div><div class="comment-text"><p>Hi All, After digging around with the VMXNET3 options I can now confirm the answer post.</p><p>There are two settings called Recv Segment Coalescing (IPv4) and Recv Segment Coalescing (IPv6) in the advanced network card settings that are enabled and for some reason have a very negative impact on MSSQL TCP traffic. As soon as these two settings were disabled the loading times on all VM’s have dropped from 25s to 3s and it seems to stay there constantly.</p><p>Thanks for the help everyone!</p></div><div id="comment-50204-info" class="comment-info"><span class="comment-age">(15 Feb '16, 01:28)</span> Linuxcrash</div></div></div><div id="comment-tools-50178" class="comment-tools"></div><div class="clear"></div><div id="comment-50178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

