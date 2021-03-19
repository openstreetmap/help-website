+++
type = "question"
title = "How can I convert pcapng to wav?"
description = '''I have a pcapng file, and I want to convert it to .wav file. How can I do that? Thank you!'''
date = "2012-08-10T14:01:00Z"
lastmod = "2012-08-11T03:58:00Z"
weight = 13549
keywords = [ "pcapng" ]
aliases = [ "/questions/13549" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How can I convert pcapng to wav?](/questions/13549/how-can-i-convert-pcapng-to-wav)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13549-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcapng file, and I want to convert it to .wav file. How can I do that?</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags">pcapng</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '12, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/09007851a53284730ec4728a37f03903?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="roubao&#39;s gravatar image" /><p>roubao<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="roubao has no accepted answers">0%</span></p></div></div><div id="comments-container-13549" class="comments-container"></div><div id="comment-tools-13549" class="comment-tools"></div><div class="clear"></div><div id="comment-13549-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13553"></span>

<div id="answer-container-13553" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13553-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't. A pcapng file is a container file for network packets, with packet headers and their payload. If you captured a wave file being transported inside the packets you could try to extract the payload to get the reassembled file. If you used HTTP or SMB you could export the file by using "File" -&gt; "Export Objects" and then "HTTP" or "SMB". Otherwise you could try to use the "Follow TCP Stream" Popup Menu option, and save the conversation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '12, 03:58</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13553" class="comments-container"><span id="13559"></span><div id="comment-13559" class="comment"><div id="post-13559-score" class="comment-score">2</div><div class="comment-text"><p>If it's RTP see <a href="http://wiki.wireshark.org/RTP_statistics">http://wiki.wireshark.org/RTP_statistics</a></p></div><div id="comment-13559-info" class="comment-info"><span class="comment-age">(11 Aug '12, 11:33)</span> Anders ♦</div></div><span id="13588"></span><div id="comment-13588" class="comment"><div id="post-13588-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for answering my question! I used the "Follow TCP Stream" method (in fact I used "Follow UDP stream"). And it worked! I'll try the RTP method next time when I have a RTP pcapng. Thank you very much for this great help!</p></div><div id="comment-13588-info" class="comment-info"><span class="comment-age">(13 Aug '12, 08:21)</span> roubao</div></div></div><div id="comment-tools-13553" class="comment-tools"></div><div class="clear"></div><div id="comment-13553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

