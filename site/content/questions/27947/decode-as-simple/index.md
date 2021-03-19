+++
type = "question"
title = "Decode as SIMPLE"
description = '''Hi, I would like to decode packets as SIMPLE (Standard Interface for Multiple Platform Link Evaluation) but I cannot find any support for this. The SIMPLE format is included in a formal NATO Standardization Agreement called STANAG 5602. It allows for SIMPLE packets to be transmitted as either TCP or...'''
date = "2013-12-09T05:12:00Z"
lastmod = "2015-09-03T04:09:00Z"
weight = 27947
keywords = [ "simple" ]
aliases = [ "/questions/27947" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Decode as SIMPLE](/questions/27947/decode-as-simple)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27947-score" class="post-score" title="current number of votes">0</div><span id="post-27947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I would like to decode packets as SIMPLE (Standard Interface for Multiple Platform Link Evaluation) but I cannot find any support for this. The SIMPLE format is included in a formal NATO Standardization Agreement called STANAG 5602. It allows for SIMPLE packets to be transmitted as either TCP or UDP (multicast or broadcast).</p><p>Does anyone know if this "decode as" capability is available anywhere? Many thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-simple" rel="tag" title="see questions tagged &#39;simple&#39;">simple</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '13, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/6c624404e89ce34954c34bd892dd16b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mark_H&#39;s gravatar image" /><p><span>Mark_H</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mark_H has no accepted answers">0%</span></p></div></div><div id="comments-container-27947" class="comments-container"></div><div id="comment-tools-27947" class="comment-tools"></div><div class="clear"></div><div id="comment-27947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27950"></span>

<div id="answer-container-27950" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27950-score" class="post-score" title="current number of votes">0</div><span id="post-27950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There does not appear to be a Wireshark dissector for the "SIMPLE" protocol (STANAG 5602).</p><p>Feel free to submit an enhancement request (or a patch for a dissector) at bugs.wireshark.org.</p><p>There has been some recent work on STANAG dissectors, so maybe someone will take up the request.</p><p>Also: please provide a link to the protocol specification (if available publicly) and attach a (small) capture file containing packets with the protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '13, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Dec '13, 07:03</strong> </span></p></div></div><div id="comments-container-27950" class="comments-container"></div><div id="comment-tools-27950" class="comment-tools"></div><div class="clear"></div><div id="comment-27950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45613"></span>

<div id="answer-container-45613" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45613-score" class="post-score" title="current number of votes">0</div><span id="post-45613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I finished to develop a simple SIMPLE dissector with complete DIS SIMPLE, and partial L11 SIMPLE , L16 SIMPLE embedded dissectors.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '15, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/fb95e7da5d43be8e3f3cac454230c780?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ph6564&#39;s gravatar image" /><p><span>ph6564</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ph6564 has no accepted answers">0%</span></p></div></div><div id="comments-container-45613" class="comments-container"><span id="45614"></span><div id="comment-45614" class="comment"><div id="post-45614-score" class="comment-score"></div><div class="comment-text"><p>See "Send us your code" on this page <a href="https://www.wireshark.org/develop.html">https://www.wireshark.org/develop.html</a></p></div><div id="comment-45614-info" class="comment-info"><span class="comment-age">(03 Sep '15, 04:09)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-45613" class="comment-tools"></div><div class="clear"></div><div id="comment-45613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

