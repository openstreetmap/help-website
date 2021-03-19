+++
type = "question"
title = "SMB INVALID DEVICE REQUEST"
description = '''Getting a SMB error during a filetransfer that I don&#x27;t understand.  Anyone able to shed some light on this error?  Here is the trace: https://www.cloudshark.org/captures/7b5be0802a2c '''
date = "2013-04-24T12:56:00Z"
lastmod = "2013-04-24T15:14:00Z"
weight = 20779
keywords = [ "device", "request", "smb", "invalid" ]
aliases = [ "/questions/20779" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [SMB INVALID DEVICE REQUEST](/questions/20779/smb-invalid-device-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20779-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Getting a SMB error during a filetransfer that I don't understand. Anyone able to shed some light on this error? Here is the trace: <a href="https://www.cloudshark.org/captures/7b5be0802a2c">https://www.cloudshark.org/captures/7b5be0802a2c</a> <img src="https://lh4.googleusercontent.com/-7PzFmTZQLiA/UXg4U2nkiKI/AAAAAAAAAdk/XpivGfQKzAA/s720/smb_inv_device_req.pcapng.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">device request smb invalid</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '13, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p>mrEEde2<br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></img></div></div><div id="comments-container-20779" class="comments-container"></div><div id="comment-tools-20779" class="comment-tools"></div><div class="clear"></div><div id="comment-20779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20780"></span>

<div id="answer-container-20780" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20780-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Frame 28 is a response to frame 27, which is an <code>FSCTL_REQUEST_FILTER_OPLOCK</code> ioctl request on file <code>\Eigene Dateien\ind$.txt</code> (which had been opened earlier). According to <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/aa364589(v=vs.85).aspx">Microsoft's documentation for <code>FSCTL_REQUEST_FILTER_OPLOCK</code></a>:</p><pre><code>In Windows 8 and Windows Server 2012, this code is supported by the following technologies.
Technology                                  Supported
Server Message Block (SMB) 3.0 protocol     No
SMB 3.0 Transparent Failover (TFO)          No
SMB 3.0 with Scale-out File Shares (SO)     No
Cluster Shared Volume File System (CsvFS)   Yes
Resilient File System (ReFS)                Yes</code></pre><p>so it sounds as if it's not supported by SMB 3 - which means it's almost certainly not supported by "SMB 1", which is the protocol being used here. You'll have to find out what operation is doing a <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/aa363216(v=vs.85).aspx"><code>DeviceIoControl()</code></a> operation with that code, and fix it not to do so (or not to do so unless it's accessing a local file system that's CsvFS or ReFS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '13, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-20780" class="comments-container"></div><div id="comment-tools-20780" class="comment-tools"></div><div class="clear"></div><div id="comment-20780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20786"></span>

<div id="answer-container-20786" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20786-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>based on the TTL of frame 27 (TTL == 59), I believe the server could be a *NIX or *BSD system running Samba (see <a href="http://www.netresec.com/?page=Blog&amp;month=2011-11&amp;post=Passive-OS-Fingerprinting">default TTL values of several systems</a>) - could be a kind of NAS system. Maybe <a href="http://www.samba.org/samba/docs/man/Samba-HOWTO-Collection/locking.html">OPLOCKs are not enabled</a> on that system (<a href="http://www.samba.org/samba/docs/man/Samba-HOWTO-Collection/locking.html">Samba config</a>).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '13, 15:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Apr '13, 15:40</p></div></div><div id="comments-container-20786" class="comments-container"><span id="20794"></span><div id="comment-20794" class="comment"><div id="post-20794-score" class="comment-score"></div><div class="comment-text"><p>@mrEEde2: What type of system is that server?</p></div><div id="comment-20794-info" class="comment-info"><span class="comment-age">(25 Apr '13, 05:53)</span> Kurt Knochner ♦</div></div><span id="20797"></span><div id="comment-20797" class="comment"><div id="post-20797-score" class="comment-score"></div><div class="comment-text"><p>Don't know for sure but looks like a Linux flavor</p></div><div id="comment-20797-info" class="comment-info"><span class="comment-age">(25 Apr '13, 07:09)</span> mrEEde2</div></div><span id="20798"></span><div id="comment-20798" class="comment"><div id="post-20798-score" class="comment-score"></div><div class="comment-text"><p>O.K. did you check the Samba config?</p></div><div id="comment-20798-info" class="comment-info"><span class="comment-age">(25 Apr '13, 07:20)</span> Kurt Knochner ♦</div></div><span id="20806"></span><div id="comment-20806" class="comment"><div id="post-20806-score" class="comment-score"></div><div class="comment-text"><p>I don't have access to the server's admins, sorry, I'm looking at this from the client's perspective only But I guess from the information I received so far here "I'm off the hook" ;-)</p></div><div id="comment-20806-info" class="comment-info"><span class="comment-age">(25 Apr '13, 11:25)</span> mrEEde2</div></div></div><div id="comment-tools-20786" class="comment-tools"></div><div class="clear"></div><div id="comment-20786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

