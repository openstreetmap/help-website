+++
type = "question"
title = "Separate two different sources?"
description = '''Hi all, I am remotely capturing packets from two different machines simultaneously, and was wondering if it is possible to either separate the two machines completely by their IP address, or if I need to, somehow run two instances of Wireshark at the same time? Sorry for the newbie questions, I have...'''
date = "2015-10-27T09:51:00Z"
lastmod = "2015-10-28T02:04:00Z"
weight = 46993
keywords = [ "rpcap", "wireshark" ]
aliases = [ "/questions/46993" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Separate two different sources?](/questions/46993/separate-two-different-sources)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46993-score" class="post-score" title="current number of votes">0</div><span id="post-46993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am remotely capturing packets from two different machines simultaneously, and was wondering if it is possible to either separate the two machines completely by their IP address, or if I need to, somehow run two instances of Wireshark at the same time? Sorry for the newbie questions, I have been looking through the user guide but can't seem to find anything about this. Or maybe I'm not phrasing my question very well. Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rpcap" rel="tag" title="see questions tagged &#39;rpcap&#39;">rpcap</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '15, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/1b0111f78e1f65adab7dde8313aea857?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MWMWMW&#39;s gravatar image" /><p><span>MWMWMW</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MWMWMW has no accepted answers">0%</span></p></div></div><div id="comments-container-46993" class="comments-container"></div><div id="comment-tools-46993" class="comment-tools"></div><div class="clear"></div><div id="comment-46993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46996"></span>

<div id="answer-container-46996" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46996-score" class="post-score" title="current number of votes">1</div><span id="post-46996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MWMWMW has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can do either/both.</p><p>If you run a single Wireshark instance and capture traffic to/from both machines, you can use Wireshark <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html">display filters</a> to display traffic to/from only 1 of the machines, and you can even save those packets matching the filter to a separate file.</p><p>If you prefer, you can instead launch 2 Wireshark instances with each one capturing traffic only to/from a particular machine using an appropriate <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">capture filter</a>.</p><p>Use whichever method best meets your needs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '15, 11:03</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-46996" class="comments-container"><span id="47008"></span><div id="comment-47008" class="comment"><div id="post-47008-score" class="comment-score"></div><div class="comment-text"><p>Great, thank you very much for the help</p></div><div id="comment-47008-info" class="comment-info"><span class="comment-age">(28 Oct '15, 02:04)</span> <span class="comment-user userinfo">MWMWMW</span></div></div></div><div id="comment-tools-46996" class="comment-tools"></div><div class="clear"></div><div id="comment-46996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

