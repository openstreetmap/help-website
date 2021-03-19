+++
type = "question"
title = "How to capture network traffic of Genymotion on host using wireshark?"
description = '''I have multiple android devices (simulated with Genymotion on top off virtualBox) on my host computer.  What is the best network setting for devices? and which interface I should capture to have both incoming and outgoing traffic of android devices? in all android devices I run same application and ...'''
date = "2017-03-10T10:02:00Z"
lastmod = "2017-03-10T10:02:00Z"
weight = 59992
keywords = [ "android", "networking", "virtualbox", "wireshark" ]
aliases = [ "/questions/59992" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture network traffic of Genymotion on host using wireshark?](/questions/59992/how-to-capture-network-traffic-of-genymotion-on-host-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59992-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59992-score" class="post-score" title="current number of votes">0</div><span id="post-59992-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have multiple android devices (simulated with Genymotion on top off virtualBox) on my host computer. What is the best network setting for devices? and which interface I should capture to have both incoming and outgoing traffic of android devices? in all android devices I run same application and I want to be able to differentiate between their traffic in my .pcap file.</p><p>I have try following but I only have outgoing traffic of devices:</p><p>In Genymotion:</p><blockquote><p>Network mode: Bridge</p></blockquote><p>In virtualBox:</p><blockquote><p>Adaptor 1: attach to : Host-only Adaptor</p><p>Adaptor 2: attach to : Bridged Adaptor</p></blockquote><p>and listen on Local area connection (since I connected to internet via LAN)</p><p>I also try following:</p><blockquote><p>C:\Program Files\Oracle\VirtualBox&gt;VBoxManage modifyvm "HTC_Mine" --nictrace1 on --nictracefile1 file.pcap VBoxManage.exe: error: The machine 'HTC_Mine' is already locked for a session (o r being unlocked) VBoxManage.exe: error: Details: code VBOX_E_INVALID_OBJECT_STATE (0x80bb0007), c omponent MachineWrap, interface IMachine, callee IUnknown VBoxManage.exe: error: Context: "LockMachine(a-&gt;session, LockType_Write)" at lin e 507 of file VBoxManageModifyVM.cpp</p></blockquote></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-networking" rel="tag" title="see questions tagged &#39;networking&#39;">networking</span> <span class="post-tag tag-link-virtualbox" rel="tag" title="see questions tagged &#39;virtualbox&#39;">virtualbox</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '17, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/1595a24111dff7d0376d456e91895399?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zahra&#39;s gravatar image" /><p><span>Zahra</span><br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zahra has no accepted answers">0%</span></p></div></div><div id="comments-container-59992" class="comments-container"></div><div id="comment-tools-59992" class="comment-tools"></div><div class="clear"></div><div id="comment-59992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

