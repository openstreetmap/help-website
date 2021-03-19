+++
type = "question"
title = "ISDN LAPD X.25 packet data"
description = '''I try to analyze ISDN data which contain SAPI 16 packet data, which is X.31. X.31 data is X.25 packet data (layer 3). So far I know, wireshark can decode X.25, but if I select the data field, I cannot decode it since Decode as is not available (grayed out). The layer 2 LAPD data is displayed correct...'''
date = "2012-07-19T02:33:00Z"
lastmod = "2012-07-22T12:31:00Z"
weight = 12848
keywords = [ "x.25", "x.31", "isdn", "lapd" ]
aliases = [ "/questions/12848" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ISDN LAPD X.25 packet data](/questions/12848/isdn-lapd-x25-packet-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12848-score" class="post-score" title="current number of votes">0</div><span id="post-12848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I try to analyze ISDN data which contain SAPI 16 packet data, which is X.31. X.31 data is X.25 packet data (layer 3). So far I know, wireshark can decode X.25, but if I select the data field, I cannot decode it since Decode as is not available (grayed out). The layer 2 LAPD data is displayed correctly, the address field SAPI is also correctly displayed as "X.25 Level 3 procedures (16)", but the content of the I field is not decoded. Does it be possible to tell wireshark somehow, that a I field on a LAPD frame with SAPI 16 has X.25 content ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-x.25" rel="tag" title="see questions tagged &#39;x.25&#39;">x.25</span> <span class="post-tag tag-link-x.31" rel="tag" title="see questions tagged &#39;x.31&#39;">x.31</span> <span class="post-tag tag-link-isdn" rel="tag" title="see questions tagged &#39;isdn&#39;">isdn</span> <span class="post-tag tag-link-lapd" rel="tag" title="see questions tagged &#39;lapd&#39;">lapd</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '12, 02:33</strong></p><img src="https://secure.gravatar.com/avatar/dad979d18dd5521cfea866e759630daa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pingus&#39;s gravatar image" /><p><span>pingus</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pingus has no accepted answers">0%</span></p></div></div><div id="comments-container-12848" class="comments-container"></div><div id="comment-tools-12848" class="comment-tools"></div><div class="clear"></div><div id="comment-12848-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12851"></span>

<div id="answer-container-12851" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12851-score" class="post-score" title="current number of votes">1</div><span id="post-12851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It seems that the X.25 dissector doesn't register itself with the LAPD dissector for this SAPI. I'm not sure why. You could/should register a bug for this at <a href="http://bugs.wireshark.org"></a><a href="http://bugs.wireshark.org">bugs.wireshark.org</a>, attaching a sample capture file showing this, so it can be addressed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '12, 04:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-12851" class="comments-container"><span id="12900"></span><div id="comment-12900" class="comment"><div id="post-12900-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the hint, I did this and I also added a quick patch I did to decode the LAPD X31 traffic as X.25. It would better if somebody with more knowledge about wiresharks internals to add X.31 as variant of X.25, but with the patch it works for me well enough.</p></div><div id="comment-12900-info" class="comment-info"><span class="comment-age">(22 Jul '12, 10:35)</span> <span class="comment-user userinfo">pingus</span></div></div><span id="12901"></span><div id="comment-12901" class="comment"><div id="post-12901-score" class="comment-score"></div><div class="comment-text"><p>For reference the bug is <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7514">7514</a>.</p></div><div id="comment-12901-info" class="comment-info"><span class="comment-age">(22 Jul '12, 12:31)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-12851" class="comment-tools"></div><div class="clear"></div><div id="comment-12851-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

