+++
type = "question"
title = "Statistics-&gt;Packet Lengths gives incomplete/incorrect data? (looks like a bug)"
description = '''Issue encountered with both Wireshark 2.2.7/Windows 7 and Wireshark 2.2.6/Ubuntu. Capture file contains 2205662 packets; packets truncated at 96 bytes during capture. Statistics-&amp;gt;Packet Lengths displays as follows:   So, Wireshark sees all 2205662 packets, and identifies a max size of 62702 bytes...'''
date = "2017-06-22T10:38:00Z"
lastmod = "2017-06-23T14:38:00Z"
weight = 62241
keywords = [ "#packetlengths", "#statistics" ]
aliases = [ "/questions/62241" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Statistics-&gt;Packet Lengths gives incomplete/incorrect data? (looks like a bug)](/questions/62241/statistics-packet-lengths-gives-incompleteincorrect-data-looks-like-a-bug)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62241-score" class="post-score" title="current number of votes">0</div><span id="post-62241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Issue encountered with both Wireshark 2.2.7/Windows 7 and Wireshark 2.2.6/Ubuntu.</p><p>Capture file contains 2205662 packets; packets truncated at 96 bytes during capture.</p><p>Statistics-&gt;Packet Lengths displays as follows:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2017-06-22_13_09_33-Wireshark_·_Packet_Lengths_·_tcpdump_pbws2888_20170620_0848.jpg" alt="Incorrect Packet Lengths dialog" /></p><p>So, Wireshark sees all 2205662 packets, and identifies a max size of 62702 bytes...but displays a count of 0 for lengths "5120 and greater". If I apply a display filter of "frame.len &gt; 5119", Wireshark finds/displays 46973 packets, as expected; that number accounts for the discrepancy between the total count in Statistics-&gt;Packet Lengths and the displayed counts in the histogram.</p><p>Did I miss a configuration in Preferences, or is this a bug? On a whim, I unchecked "assume short frames" in Ethernet preferences, but that change did not affect this behavior.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-#packetlengths" rel="tag" title="see questions tagged &#39;#packetlengths&#39;">#packetlengths</span> <span class="post-tag tag-link-#statistics" rel="tag" title="see questions tagged &#39;#statistics&#39;">#statistics</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '17, 10:38</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></img></div></div><div id="comments-container-62241" class="comments-container"><span id="62251"></span><div id="comment-62251" class="comment"><div id="post-62251-score" class="comment-score"></div><div class="comment-text"><p>If you think this is a bug please file a bugreport at <a href="https://bugs.wireshark.org">BugZilla</a> including the capture file and these numbers. That gives someone to work with investigating the situation and test possible corrections.</p></div><div id="comment-62251-info" class="comment-info"><span class="comment-age">(22 Jun '17, 23:17)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="62266"></span><div id="comment-62266" class="comment"><div id="post-62266-score" class="comment-score"></div><div class="comment-text"><p>I'll do just that, as soon as I anonymize the trace - I was only doing 'due diligence' to make sure I hadn't missed anything (configuration, preferences, capture options, whatever) on my end before opening a bug report. Thanks!</p></div><div id="comment-62266-info" class="comment-info"><span class="comment-age">(23 Jun '17, 10:53)</span> <span class="comment-user userinfo">wesmorgan1</span></div></div></div><div id="comment-tools-62241" class="comment-tools"></div><div class="clear"></div><div id="comment-62241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62270"></span>

<div id="answer-container-62270" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62270-score" class="post-score" title="current number of votes">0</div><span id="post-62270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, I'm calling this a bug.</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13844">Bug 13844</a> opened against Wireshark 2.2.7</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '17, 14:38</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-62270" class="comments-container"></div><div id="comment-tools-62270" class="comment-tools"></div><div class="clear"></div><div id="comment-62270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

