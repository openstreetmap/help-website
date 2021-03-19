+++
type = "question"
title = "erspan packets malformed"
description = '''When viewing erspan packets in wireshark, I get malformed packets. The packet are good, but wireshark is not interpreting the packet correct. Packet is formed : EtherII - ip - gre - erspan - etherII - IP - ipdata The first etherII has a trailer of 32 bytes, which is odd the ip headers have the corre...'''
date = "2014-06-25T07:02:00Z"
lastmod = "2014-12-08T14:23:00Z"
weight = 34165
keywords = [ "malformed", "erspan" ]
aliases = [ "/questions/34165" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [erspan packets malformed](/questions/34165/erspan-packets-malformed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34165-score" class="post-score" title="current number of votes">0</div><span id="post-34165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When viewing erspan packets in wireshark, I get malformed packets. The packet are good, but wireshark is not interpreting the packet correct.</p><p>Packet is formed : EtherII - ip - gre - erspan - etherII - IP - ipdata The first etherII has a trailer of 32 bytes, which is odd the ip headers have the correct 'total length', taking into account the extra 32 bytes of the (etherII-ip-gre-erspan) headers the last ip header shows the correct length, the same as the original packet before encapsulation.</p><p>ex an ICMP packet: the ipdata portion of the original ip packet 80 bytes total length with 20bytes header, leaving 60 bytes for the icmp packet. Icmp has an 8 byte header, leaving 52 bytes of data, but wireshark reports 20 bytes, which is 32 bytes too short</p><p>I guess this is a bug in wireshark parsing, put I'm not sure how to report it</p><p>Pieter</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-malformed" rel="tag" title="see questions tagged &#39;malformed&#39;">malformed</span> <span class="post-tag tag-link-erspan" rel="tag" title="see questions tagged &#39;erspan&#39;">erspan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '14, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/ed1a7f9057f9c36693c4d0cad68a8d3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PieterL&#39;s gravatar image" /><p><span>PieterL</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PieterL has no accepted answers">0%</span></p></div></div><div id="comments-container-34165" class="comments-container"></div><div id="comment-tools-34165" class="comment-tools"></div><div class="clear"></div><div id="comment-34165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34170"></span>

<div id="answer-container-34170" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34170-score" class="post-score" title="current number of votes">2</div><span id="post-34170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Second entry from Google search of "wireshark bugs", on the wiki: <a href="http://wiki.wireshark.org/ReportingBugs">Reporting Bugs</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '14, 08:35</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-34170" class="comments-container"><span id="38450"></span><div id="comment-38450" class="comment"><div id="post-38450-score" class="comment-score"></div><div class="comment-text"><p>Link to the bugreport <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10230">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10230</a> It is not a Wireshark bug, but a Cisco bug.</p></div><div id="comment-38450-info" class="comment-info"><span class="comment-age">(08 Dec '14, 14:23)</span> <span class="comment-user userinfo">PieterL</span></div></div></div><div id="comment-tools-34170" class="comment-tools"></div><div class="clear"></div><div id="comment-34170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

