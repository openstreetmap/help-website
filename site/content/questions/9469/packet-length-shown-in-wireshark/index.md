+++
type = "question"
title = "Packet length shown in Wireshark"
description = '''Does the packet length shown in Wireshark in the main column under Length include the header length? I am working out bottleneck bandwidth and need to know. Thank you. Steve.'''
date = "2012-03-11T06:15:00Z"
lastmod = "2012-03-11T11:09:00Z"
weight = 9469
keywords = [ "header", "length", "wireshark" ]
aliases = [ "/questions/9469" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Packet length shown in Wireshark](/questions/9469/packet-length-shown-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9469-score" class="post-score" title="current number of votes">0</div><span id="post-9469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does the packet length shown in Wireshark in the main column under Length include the header length?</p><p>I am working out bottleneck bandwidth and need to know.</p><p>Thank you.</p><p>Steve.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-header" rel="tag" title="see questions tagged &#39;header&#39;">header</span> <span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '12, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/a4b621a76eff366846027168bfd758e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sjb89&#39;s gravatar image" /><p><span>sjb89</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sjb89 has no accepted answers">0%</span></p></div></div><div id="comments-container-9469" class="comments-container"></div><div id="comment-tools-9469" class="comment-tools"></div><div class="clear"></div><div id="comment-9469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9471"></span>

<div id="answer-container-9471" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9471-score" class="post-score" title="current number of votes">1</div><span id="post-9471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sjb89 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The packet length (aka the field named <code>frame.len</code>) is the size of the frame as seen "on the wire".</p><p>Note that it's possible that the actual bytes captured may be smaller if a "snaplen" limit has been set for the capture to only keep some initial part of each frame; the packet length shown will still be the original length of the frame.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '12, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-9471" class="comments-container"><span id="9473"></span><div id="comment-9473" class="comment"><div id="post-9473-score" class="comment-score"></div><div class="comment-text"><p>Thank you for this.</p></div><div id="comment-9473-info" class="comment-info"><span class="comment-age">(11 Mar '12, 11:09)</span> <span class="comment-user userinfo">sjb89</span></div></div></div><div id="comment-tools-9471" class="comment-tools"></div><div class="clear"></div><div id="comment-9471-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

