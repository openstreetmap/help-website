+++
type = "question"
title = "TCP window Size"
description = '''Hello, I have made 2 wireshark captures: 1- A text file of size 10 MB 2- A PDF file of size 16MB I repeated both these captures, once on a Cloud Virtual Machine and another on a LAN desktop. I am capturing the file Sync between the device and VM/desktop on a laptop that the mobile device is connecte...'''
date = "2013-09-03T13:57:00Z"
lastmod = "2013-09-04T06:37:00Z"
weight = 24316
keywords = [ "window", "mtu", "mss", "tcp", "size" ]
aliases = [ "/questions/24316" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP window Size](/questions/24316/tcp-window-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24316-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have made 2 wireshark captures: 1- A text file of size 10 MB 2- A PDF file of size 16MB</p><p>I repeated both these captures, once on a Cloud Virtual Machine and another on a LAN desktop. I am capturing the file Sync between the device and VM/desktop on a laptop that the mobile device is connected to.</p><p>What i don't understand is, how should i measure the window size for each environment using WireShark? I understand that since both of the environments are windows 7 and windows 2008 R2 which means the window size changes according to demand.</p><p>Before the file is sync-ed its split into segments and then compressed. Once that is done it is sent over TCP to the device. What i noticed is that for my desktop, the text file is being sent over seperate TCP packets of size 247, while the same file on my CLOUD VM is sent over a larger window with each packet of size 1514.</p><p>Why am i noticing different behavior for each?</p></div><div id="question-tags" class="tags-container tags">window mtu mss tcp size</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Sep '13, 13:57</strong></p><img src="https://secure.gravatar.com/avatar/389ef5755273f1efbae2adbcc75e45cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mustafa%20El-Hilo&#39;s gravatar image" /><p>Mustafa El-Hilo<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mustafa El-Hilo has no accepted answers">0%</span></p></div></div><div id="comments-container-24316" class="comments-container"><span id="24329"></span><div id="comment-24329" class="comment"><div id="post-24329-score" class="comment-score"></div><div class="comment-text"><blockquote><p>being sent over seperate TCP <strong>packets of size 247</strong>, while the same file on my CLOUD VM is sent over a larger window with each <strong>packet of size 1514</strong>.</p></blockquote><p>That sounds like a MTU issue rather than a TCP window size problem.</p><p>Can you please post the capture files somewhere (google docs, dropbox, cloudshark)? Without the capture files it is impossible to give good advice.</p></div><div id="comment-24329-info" class="comment-info"><span class="comment-age">(03 Sep '13, 23:45)</span> Kurt Knochner ♦</div></div><span id="24343"></span><div id="comment-24343" class="comment"><div id="post-24343-score" class="comment-score"></div><div class="comment-text"><p>Here is a link for 2. The file "10MBfileSuncDStoDevice" this is from Cloud to Device. The other is from Desktop to Device. <a href="https://drive.google.com/folderview?id=0B_M_fihdbr8VY1RESmwtZGpDVmM&amp;usp=sharing">https://drive.google.com/folderview?id=0B_M_fihdbr8VY1RESmwtZGpDVmM&amp;usp=sharing</a></p></div><div id="comment-24343-info" class="comment-info"><span class="comment-age">(04 Sep '13, 05:47)</span> Mustafa El-Hilo</div></div></div><div id="comment-tools-24316" class="comment-tools"></div><div class="clear"></div><div id="comment-24316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24346"></span>

<div id="answer-container-24346" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24346-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The small packet size on the LAN is caused by the PUSH (PSH) flag (~78% of the packets from the server). The PUSH flag is handled by the application (real time applications do that). If you add some information about the file sync application, we (and you) might be able to understand why/how the application is doing that (maybe a config option or default behavior).</p><blockquote><p>Why am i noticing different behavior for each?</p></blockquote><p>Because of the use of the PUSH flag on the LAN (78%) versus Internet (10%). The TCP Windows size does not matter here, at least not as a source of the small packets.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '13, 06:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Sep '13, 06:42</p></div></div><div id="comments-container-24346" class="comments-container"><span id="24348"></span><div id="comment-24348" class="comment"><div id="post-24348-score" class="comment-score"></div><div class="comment-text"><p>my task is reverse engineer the file sync application. So i was wondering if you can see something i can't</p></div><div id="comment-24348-info" class="comment-info"><span class="comment-age">(04 Sep '13, 06:52)</span> Mustafa El-Hilo</div></div><span id="24349"></span><div id="comment-24349" class="comment"><div id="post-24349-score" class="comment-score"></div><div class="comment-text"><blockquote><p>my task is reverse engineer the file sync application. So i was wondering if you can see something</p></blockquote><p>what are you interested in, besides the explanation of the small packtes (see my answer)?</p><blockquote><p>So i was wondering if you can see something <strong>i can't</strong></p></blockquote><p>because the data is encrypted with SSL/TLS. There is no way to reverse engineer that, without access to the server keys.</p></div><div id="comment-24349-info" class="comment-info"><span class="comment-age">(04 Sep '13, 06:59)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-24346" class="comment-tools"></div><div class="clear"></div><div id="comment-24346-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

