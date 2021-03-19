+++
type = "question"
title = "how to filter out a specific SMB operation?"
description = '''Hi, As titled, do we have filed for that? I found there is a specific code number for each operation, but was not able to find that code in Microsoft smb protocol doc. For example,   - Session Setup Request (0x01)  - SMB2 WRITE Request (0X09)  - SMB2 WRITE Request (0X08)  - etc.. Is there a field li...'''
date = "2017-03-05T21:39:00Z"
lastmod = "2017-03-08T18:03:00Z"
weight = 59864
keywords = [ "smb2" ]
aliases = [ "/questions/59864" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [how to filter out a specific SMB operation?](/questions/59864/how-to-filter-out-a-specific-smb-operation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59864-score" class="post-score" title="current number of votes">0</div><span id="post-59864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>As titled, do we have filed for that? I found there is a specific code number for each operation, but was not able to find that code in Microsoft smb protocol doc. For example, - Session Setup Request (0x01) - SMB2 WRITE Request (0X09) - SMB2 WRITE Request (0X08) - etc..</p><p>Is there a field like smb.&lt;field&gt; == &lt;codenumber&gt; we can use for filtering? thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-smb2" rel="tag" title="see questions tagged &#39;smb2&#39;">smb2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '17, 21:39</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p><span>SteveZhou</span><br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div></div><div id="comments-container-59864" class="comments-container"></div><div id="comment-tools-59864" class="comment-tools"></div><div class="clear"></div><div id="comment-59864-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59865"></span>

<div id="answer-container-59865" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59865-score" class="post-score" title="current number of votes">2</div><span id="post-59865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SteveZhou has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try "smb.cmd == codenumber" or "smb2.cmd == codenumber"</p><p>and also you can refer to "Display filter expression" dialog and search for "smb" in there to find available expressions:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/smb_filter.JPG" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '17, 22:13</strong></p><img src="https://secure.gravatar.com/avatar/1e22670f8d643ca08d658b80a6782932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Packet_vlad&#39;s gravatar image" /><p><span>Packet_vlad</span><br />
<span class="score" title="436 reputation points">436</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Packet_vlad has 5 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Mar '17, 22:15</strong> </span></p></div></div><div id="comments-container-59865" class="comments-container"><span id="59940"></span><div id="comment-59940" class="comment"><div id="post-59940-score" class="comment-score"></div><div class="comment-text"><p>ah, yes, how could I not checking the SMB Header part. thanks!</p></div><div id="comment-59940-info" class="comment-info"><span class="comment-age">(08 Mar '17, 18:03)</span> <span class="comment-user userinfo">SteveZhou</span></div></div></div><div id="comment-tools-59865" class="comment-tools"></div><div class="clear"></div><div id="comment-59865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59868"></span>

<div id="answer-container-59868" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59868-score" class="post-score" title="current number of votes">2</div><span id="post-59868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To determine the name of any filter field, locate the field of interest in the packet details pane, click the field and the status bar will indicate the filter field name in parentheses:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/smb2cmd.png" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '17, 09:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div></div><div id="comments-container-59868" class="comments-container"><span id="59941"></span><div id="comment-59941" class="comment"><div id="post-59941-score" class="comment-score"></div><div class="comment-text"><p>thank you!</p></div><div id="comment-59941-info" class="comment-info"><span class="comment-age">(08 Mar '17, 18:03)</span> <span class="comment-user userinfo">SteveZhou</span></div></div></div><div id="comment-tools-59868" class="comment-tools"></div><div class="clear"></div><div id="comment-59868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

