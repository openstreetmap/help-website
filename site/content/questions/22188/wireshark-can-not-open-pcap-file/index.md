+++
type = "question"
title = "wireshark can not open pcap file"
description = '''I downloaded wireshark source code and built it successfully. Then I try to open an exist pcap file with wireshark.exe. It shows error&quot;The file C:&#92;source&#92;snep_p2p_trace.pcap is a capture for a network type that Wireshark doesn&#x27;t support.(pcap:network type 245 unknown or unsupported)&quot;.'''
date = "2013-06-19T19:25:00Z"
lastmod = "2013-06-19T23:55:00Z"
weight = 22188
keywords = [ "nfc", "wireshark" ]
aliases = [ "/questions/22188" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark can not open pcap file](/questions/22188/wireshark-can-not-open-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22188-score" class="post-score" title="current number of votes">0</div><span id="post-22188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I downloaded wireshark source code and built it successfully. Then I try to open an exist pcap file with wireshark.exe. It shows error"The file C:\source\snep_p2p_trace.pcap is a capture for a network type that Wireshark doesn't support.(pcap:network type 245 unknown or unsupported)".</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nfc" rel="tag" title="see questions tagged &#39;nfc&#39;">nfc</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '13, 19:25</strong></p><img src="https://secure.gravatar.com/avatar/f378a0d8809978a31afab288a17abb14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TommyXu&#39;s gravatar image" /><p><span>TommyXu</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TommyXu has no accepted answers">0%</span></p></div></div><div id="comments-container-22188" class="comments-container"></div><div id="comment-tools-22188" class="comment-tools"></div><div class="clear"></div><div id="comment-22188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22189"></span>

<div id="answer-container-22189" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22189-score" class="post-score" title="current number of votes">1</div><span id="post-22189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>According to <a href="http://www.tcpdump.org/linktypes.html">the official list of link-layer header type values</a>, 245 is LINKTYPE_NFC_LLCP, which is supported by Wireshark 1.8 and 1.10, but not by Wireshark 1.6. You will need to install Wireshark 1.8 or later in order to read that file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '13, 19:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-22189" class="comments-container"><span id="22190"></span><div id="comment-22190" class="comment"><div id="post-22190-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your kindly help, You're right. I got it.</p></div><div id="comment-22190-info" class="comment-info"><span class="comment-age">(19 Jun '13, 23:55)</span> <span class="comment-user userinfo">TommyXu</span></div></div></div><div id="comment-tools-22189" class="comment-tools"></div><div class="clear"></div><div id="comment-22189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

