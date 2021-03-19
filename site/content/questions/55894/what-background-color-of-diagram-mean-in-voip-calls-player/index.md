+++
type = "question"
title = "What background color of diagram mean in VoIP calls player?"
description = '''At VoIP calls dialog I am opened some calls in player. I see that different calls have different background color on diagram. Each call have same background after reopen, so it don&#x27;t looks like random color. Did this color indicate some information, and where i can read about it?  '''
date = "2016-09-27T01:56:00Z"
lastmod = "2016-09-27T07:33:00Z"
weight = 55894
keywords = [ "interface", "voipcalls", "color-rules", "voip" ]
aliases = [ "/questions/55894" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What background color of diagram mean in VoIP calls player?](/questions/55894/what-background-color-of-diagram-mean-in-voip-calls-player)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55894-score" class="post-score" title="current number of votes">0</div><span id="post-55894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>At VoIP calls dialog I am opened some calls in player. I see that different calls have different background color on diagram. Each call have same background after reopen, so it don't looks like random color. Did this color indicate some information, and where i can read about it? <img src="https://osqa-ask.wireshark.org/upfiles/1_g6J6GhD.PNG" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/2_p429GmW.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-voipcalls" rel="tag" title="see questions tagged &#39;voipcalls&#39;">voipcalls</span> <span class="post-tag tag-link-color-rules" rel="tag" title="see questions tagged &#39;color-rules&#39;">color-rules</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '16, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/032be4c624f9cbd83a4288ecca8fda1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dembin&#39;s gravatar image" /><p><span>dembin</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dembin has no accepted answers">0%</span></p></img></div></div><div id="comments-container-55894" class="comments-container"></div><div id="comment-tools-55894" class="comment-tools"></div><div class="clear"></div><div id="comment-55894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55913"></span>

<div id="answer-container-55913" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55913-score" class="post-score" title="current number of votes">1</div><span id="post-55913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dembin has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>These colors are useful to highlight which messages belong to the same call if you display more than one call in the ladder diagram (<code>Telephony -&gt; VoIP Calls -&gt;</code> choose several calls <code>-&gt; Flow Sequence</code>) and the calls overlap in time. Likewise, if you choose multiple calls and press the <code>Play Streams</code> button, all RTP streams belonging to all chosen calls are shown in the RTP Player window, and the color identifies streams belonging to the same call and allows you to easily correlate the RTP streams in this window to the call control messages in the Flow Sequence window.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '16, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></img></div></div><div id="comments-container-55913" class="comments-container"></div><div id="comment-tools-55913" class="comment-tools"></div><div class="clear"></div><div id="comment-55913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

