+++
type = "question"
title = "Wireshark upgrade to 12.2 X2AP"
description = '''Dear Wireshark Team, What are the plans to upgrade the X2AP protocol (TS 3GPP 36.423) to Release 12.2 versions. There have been inclusion on new X2AP messages for a new logical 3GPP entity (X2GW) in Release 12.2. http://www.3gpp.org/DynaReport/36423.htm On similar lines, 3GPP 36.413 (S1AP) has also ...'''
date = "2014-09-10T04:30:00Z"
lastmod = "2014-09-10T14:10:00Z"
weight = 36150
keywords = [ "x2ap", "36.423", "36.413" ]
aliases = [ "/questions/36150" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark upgrade to 12.2 X2AP](/questions/36150/wireshark-upgrade-to-122-x2ap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36150-score" class="post-score" title="current number of votes">0</div><span id="post-36150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Wireshark Team, What are the plans to upgrade the X2AP protocol (TS 3GPP 36.423) to Release 12.2 versions. There have been inclusion on new X2AP messages for a new logical 3GPP entity (X2GW) in Release 12.2. <a href="http://www.3gpp.org/DynaReport/36423.htm">http://www.3gpp.org/DynaReport/36423.htm</a></p><p>On similar lines, 3GPP 36.413 (S1AP) has also been upgraded to v12.2 to support X2GW</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-x2ap" rel="tag" title="see questions tagged &#39;x2ap&#39;">x2ap</span> <span class="post-tag tag-link-36.423" rel="tag" title="see questions tagged &#39;36.423&#39;">36.423</span> <span class="post-tag tag-link-36.413" rel="tag" title="see questions tagged &#39;36.413&#39;">36.413</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '14, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/ee80d70377743a78e548c5c28f50d072?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Inder&#39;s gravatar image" /><p><span>Inder</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Inder has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Sep '14, 04:32</strong> </span></p></div></div><div id="comments-container-36150" class="comments-container"></div><div id="comment-tools-36150" class="comment-tools"></div><div class="clear"></div><div id="comment-36150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36171"></span>

<div id="answer-container-36171" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36171-score" class="post-score" title="current number of votes">1</div><span id="post-36171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is OpenSource there isn't much of a "plan", stuff gets added when some one has the need for it and decides to send a patch. That said I have updated the S1AP dissector and might do the X2AP one if it isn't to much work and I find the time. The S1AP update is in gerrit but not commited yet pending no problems with building it. The new stuff is untested as I don't have any trace to verify it with. If you could supply a trace in a bug report or on the samples wiki page that would help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '14, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-36171" class="comments-container"><span id="36174"></span><div id="comment-36174" class="comment"><div id="post-36174-score" class="comment-score"></div><div class="comment-text"><p>Thanks a ton :) Will report bugs if any found during usage</p></div><div id="comment-36174-info" class="comment-info"><span class="comment-age">(10 Sep '14, 08:08)</span> <span class="comment-user userinfo">Inder</span></div></div><span id="36181"></span><div id="comment-36181" class="comment"><div id="post-36181-score" class="comment-score"></div><div class="comment-text"><p>No no, you are requested to supply capture files with these new messages in them, for development purposes. You can create an enhancement bug for that, attaching the sample capture to that. These will then be used in automated testing as well.</p></div><div id="comment-36181-info" class="comment-info"><span class="comment-age">(10 Sep '14, 14:10)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-36171" class="comment-tools"></div><div class="clear"></div><div id="comment-36171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

