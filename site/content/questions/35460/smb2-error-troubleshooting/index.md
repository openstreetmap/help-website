+++
type = "question"
title = "SMB2 Error Troubleshooting"
description = '''Hello, I&#x27;m new to packet analysis and I&#x27;m looking for some direction on troubleshooting SMB2 errors.  I have a Windows 7 machine on a corporate network. As soon as I booted it up and logged in, I ran a packet capture. Filtering on SMB errors, I have a boat load of NT Status: STATUS_INVALID_PARAMETER...'''
date = "2014-08-13T08:57:00Z"
lastmod = "2014-08-13T14:57:00Z"
weight = 35460
keywords = [ "errors", "smb2", "smb" ]
aliases = [ "/questions/35460" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SMB2 Error Troubleshooting](/questions/35460/smb2-error-troubleshooting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35460-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm new to packet analysis and I'm looking for some direction on troubleshooting SMB2 errors.</p><p>I have a Windows 7 machine on a corporate network. As soon as I booted it up and logged in, I ran a packet capture. Filtering on SMB errors, I have a boat load of NT Status: STATUS_INVALID_PARAMETER (0xc000000d), NT Status: STATUS_NOT_A_REPARSE_POINT (0xc0000275) and NT Status: STATUS_OBJECT_PATH_NOT_FOUND (0xc000003a). Line after line of them in the same stream. All coming from the server back to the PC.<br />
</p><p>I've done a lot of searching on the errors but only seem to get Microsoft developer sites that give me no direction. Since it's a fresh reboot, I'm guessing the PC system is running something but have no idea how to proceed.<br />
</p><p>Does anyone have a troubleshooting methodology, web site, youtube video, etc., for figuring out SMB errors?<br />
</p></div><div id="question-tags" class="tags-container tags">errors smb2 smb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '14, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/89f1bff2baf084744ed4e4650224ba40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tom%20Fury&#39;s gravatar image" /><p>Tom Fury<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tom Fury has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-35460" class="comments-container"></div><div id="comment-tools-35460" class="comment-tools"></div><div class="clear"></div><div id="comment-35460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35471"></span>

<div id="answer-container-35471" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35471-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>The protocol is defined here - <a href="http://msdn.microsoft.com/en-gb/library/cc246482.aspx">http://msdn.microsoft.com/en-gb/library/cc246482.aspx</a></p><p>There's a pdf version; just google [MS-SMB2]</p><p>You'll also find an introductory guide here - <a href="http://www.advance7.com/smb-2-file-server-protocol-overview">http://www.advance7.com/smb-2-file-server-protocol-overview</a></p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '14, 14:57</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span> </br></p></div></div><div id="comments-container-35471" class="comments-container"><span id="35540"></span><div id="comment-35540" class="comment"><div id="post-35540-score" class="comment-score"></div><div class="comment-text"><p>Paul,</p><p>Thanks for the information. The advance7 document really helped with giving me a baseline for how things should work. Unfortunately, I'm still struggling with how to figure out what is not happening correctly.</p></div><div id="comment-35540-info" class="comment-info"><span class="comment-age">(18 Aug '14, 09:58)</span> Tom Fury</div></div><span id="35596"></span><div id="comment-35596" class="comment"><div id="post-35596-score" class="comment-score"></div><div class="comment-text"><p>Hi Tom,</p><p>What's the problem you are investigating?</p><p>Best regards...Paul</p></div><div id="comment-35596-info" class="comment-info"><span class="comment-age">(19 Aug '14, 13:31)</span> PaulOfford</div></div><span id="35634"></span><div id="comment-35634" class="comment"><div id="post-35634-score" class="comment-score"></div><div class="comment-text"><p>Paul,</p><p>On my corporate desktop, I'm being flooded with the repeated SMB errors listed in the original posting above. I've done a lot of searching, but can't find any meaningful information about the errors that would point me in a direction.<br />
</p><p>It looks to me that my workstation is trying to write something to the server that it doesn't like. I'm troubleshooting it a step at a time and posted a separate question on the forum for information about a successful SMB2 Create that the packet gives me no information on what or where was created. Thanks for your answer on that posting too.</p></div><div id="comment-35634-info" class="comment-info"><span class="comment-age">(20 Aug '14, 09:21)</span> Tom Fury</div></div><span id="35641"></span><div id="comment-35641" class="comment"><div id="post-35641-score" class="comment-score"></div><div class="comment-text"><p>Ok. STATUS_OBJECT_PATH_NOT_FOUND is common as a process tries to open things like .ini files that could reside in a number of directories. The other two I'll need to think about.</p><p>You might find it easier to track down the offending program with procmon. It would be pretty fast and simple. If you are up for having a go, check out <a href="http://www.lovemytool.com">http://www.lovemytool.com</a> (yes that really is the name) and look for my blogs on procmon. That should give you enough info to do what's needed. Use procmon with Wireshark - again I cover that in a blog.</p><p>Procmon will tell you which process is issuing the file system call that is causing the error.</p><p>Best regards...Paul</p></div><div id="comment-35641-info" class="comment-info"><span class="comment-age">(20 Aug '14, 14:48)</span> PaulOfford</div></div></div><div id="comment-tools-35471" class="comment-tools"></div><div class="clear"></div><div id="comment-35471-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

