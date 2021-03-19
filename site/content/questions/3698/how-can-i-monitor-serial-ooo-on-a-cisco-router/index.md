+++
type = "question"
title = "How can I monitor serial o/o/o on a cisco router?"
description = '''With wireshark how can I monitor packets that are coming and going on the serial port of a Cisco router 3945? '''
date = "2011-04-22T14:48:00Z"
lastmod = "2011-04-24T18:40:00Z"
weight = 3698
keywords = [ "serial", "cisco" ]
aliases = [ "/questions/3698" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I monitor serial o/o/o on a cisco router?](/questions/3698/how-can-i-monitor-serial-ooo-on-a-cisco-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3698-score" class="post-score" title="current number of votes">0</div><span id="post-3698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>With wireshark how can I monitor packets that are coming and going on the serial port of a Cisco router 3945?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-serial" rel="tag" title="see questions tagged &#39;serial&#39;">serial</span> <span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '11, 14:48</strong></p><img src="https://secure.gravatar.com/avatar/9a6cfbe9c0b161025491b5c39fb31091?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lateris&#39;s gravatar image" /><p><span>lateris</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lateris has no accepted answers">0%</span></p></div></div><div id="comments-container-3698" class="comments-container"><span id="3699"></span><div id="comment-3699" class="comment"><div id="post-3699-score" class="comment-score"></div><div class="comment-text"><p>Hmm, I'm not sure it can be done with stock Wireshark. Won't you need to introduce a serial tap that understands HDLC or PPP? (not sure what you're using).<br />
</p><p>I'm pretty sure Wireshark has both dissectors included, but never having used it, I couldn't bet my life on it.<br />
</p><p>However, can't you just monitor the traffic from the Ethernet side? For the serial interface, you can track the errors etc. via show commands. Or is there something specific on the serial interface that you are trying to get at?</p></div><div id="comment-3699-info" class="comment-info"><span class="comment-age">(23 Apr '11, 08:22)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-3698" class="comment-tools"></div><div class="clear"></div><div id="comment-3698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3705"></span>

<div id="answer-container-3705" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3705-score" class="post-score" title="current number of votes">0</div><span id="post-3705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can monitor the traffic from the ethernet side, but in that case it is framed in ethernet. To get hdlc or ppp you will have to somehow tap on the serial side. Wireshark integrates nicely into GNS3 (even on serial links) if you are wanting to play around without a serial tap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '11, 18:40</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p><span>Paul Stewart</span><br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span> </br></br></p></div></div><div id="comments-container-3705" class="comments-container"></div><div id="comment-tools-3705" class="comment-tools"></div><div class="clear"></div><div id="comment-3705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

