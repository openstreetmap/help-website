+++
type = "question"
title = "SMB2 Successful Create of a Blank File?"
description = '''Below is the SMB2 header for a successful Create from a client to a server. The next packet in the trace says the Create was successful. How do I figure out what file was created and where? There is nothing in the Filename and nothing under the Tree Id.  '''
date = "2014-08-18T10:13:00Z"
lastmod = "2014-08-19T13:05:00Z"
weight = 35541
keywords = [ "create", "smb2" ]
aliases = [ "/questions/35541" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SMB2 Successful Create of a Blank File?](/questions/35541/smb2-successful-create-of-a-blank-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35541-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Below is the SMB2 header for a successful Create from a client to a server. The next packet in the trace says the Create was successful. How do I figure out what file was created and where? There is nothing in the Filename and nothing under the Tree Id.<br />
</p><p><img src="https://osqa-ask.wireshark.org/upfiles/BlankFile_1.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">create smb2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '14, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/89f1bff2baf084744ed4e4650224ba40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tom%20Fury&#39;s gravatar image" /><p>Tom Fury<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tom Fury has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-35541" class="comments-container"></div><div id="comment-tools-35541" class="comment-tools"></div><div class="clear"></div><div id="comment-35541-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35595"></span>

<div id="answer-container-35595" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35595-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Tom,</p><p>I've often seen this in SMB2 traces. I think the answer is that the client is opening the root directory relative to the current share. The share is identified by the Tree ID value, and if you've captured the connection to the share you'll see the Tree Connect request which will contain the share name.</p><p>I've noticed a typical scenario is the client opens the directory with a Create Request (Disposition - Open), issues a Find Request looking for a particular file (sometimes with wildcard values) and then you see a Close Request for the directory.</p><p>Some information that may help:</p><ul><li>Overview of SMB: <a href="http://www.advance7.com/smb-2-file-server-protocol-overview">http://www.advance7.com/smb-2-file-server-protocol-overview</a></li><li>SMB2 Protocol Definition - <a href="http://download.microsoft.com/download/9/5/E/95EF66AF-9026-4BB0-A41D-A4F81802D92C/%5BMS-SMB2%5D.pdf">http://download.microsoft.com/download/9/5/E/95EF66AF-9026-4BB0-A41D-A4F81802D92C/%5BMS-SMB2%5D.pdf</a></li><li>File System Control Codes - <a href="http://download.microsoft.com/download/9/5/E/95EF66AF-9026-4BB0-A41D-A4F81802D92C/%5BMS-FSCC%5D.pdf">http://download.microsoft.com/download/9/5/E/95EF66AF-9026-4BB0-A41D-A4F81802D92C/%5BMS-FSCC%5D.pdf</a></li></ul><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '14, 13:05</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-35595" class="comments-container"></div><div id="comment-tools-35595" class="comment-tools"></div><div class="clear"></div><div id="comment-35595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

