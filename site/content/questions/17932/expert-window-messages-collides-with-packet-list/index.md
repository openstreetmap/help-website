+++
type = "question"
title = "Expert window messages collides with packet list"
description = '''Hi everybody, Another little incomprehension. Right in this moment I analyze a capture file from a customer. I use the following display filter &quot;!eth.type == 0x8922 &amp;amp;&amp;amp; !arp &amp;amp;&amp;amp; !stp &amp;amp;&amp;amp; !nbns &amp;amp;&amp;amp; !bootp&quot;. When I open the expert info window I see a lot of bad checksum err...'''
date = "2013-01-24T07:09:00Z"
lastmod = "2013-01-25T01:47:00Z"
weight = 17932
keywords = [ "expert-info" ]
aliases = [ "/questions/17932" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Expert window messages collides with packet list](/questions/17932/expert-window-messages-collides-with-packet-list)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17932-score" class="post-score" title="current number of votes">0</div><span id="post-17932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody,</p><p>Another little incomprehension. Right in this moment I analyze a capture file from a customer. I use the following display filter "!eth.type == 0x8922 &amp;&amp; !arp &amp;&amp; !stp &amp;&amp; !nbns &amp;&amp; !bootp". When I open the expert info window I see a lot of bad checksum errors. If I choose a packet number from this window, the packet is not shown, because the filter works. If I clear the filter, the error was cleared in the expert window but I remember the packet number so the bad checksum is shown on the packet list. What`s that, if I use a filter Wireshark tells me more errors as without a filter. Normal??????? ps, the bad checksum error is an stp error!!!!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-expert-info" rel="tag" title="see questions tagged &#39;expert-info&#39;">expert-info</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '13, 07:09</strong></p><img src="https://secure.gravatar.com/avatar/d6cab55f3f8d50d3a16c726d050325ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikethebandit31&#39;s gravatar image" /><p><span>mikethebandit31</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikethebandit31 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jan '13, 11:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-17932" class="comments-container"><span id="17943"></span><div id="comment-17943" class="comment"><div id="post-17943-score" class="comment-score"></div><div class="comment-text"><p>Can you post a sample capture file to <a href="http://www.cloudshark.org/">cloudshark</a> or <a href="http://news.gmane.org/gmane.network.wireshark.devel">wireshark-dev</a> or ...?</p><p>Without a capture file, my best guess is that somewhere we have one or more <code>expert_add_info_format()</code>'s within an <code>if (tree) { ... }</code> block, which is not allowed.</p></div><div id="comment-17943-info" class="comment-info"><span class="comment-age">(24 Jan '13, 14:17)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-17932" class="comment-tools"></div><div class="clear"></div><div id="comment-17932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17933"></span>

<div id="answer-container-17933" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17933-score" class="post-score" title="current number of votes">0</div><span id="post-17933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Where was that capture taken? There are many cases where the checksum errors where false positives, usually caused by checksum offloading when doing a capture on the sending server or client. Basic rule is: if the checksum would really have been bad it most likely not make it into the capture file in the first place, because it is dropped before it gets there.</p><p>The expert behaviour sounds a bit strange; it should either show messages regarding only filtered packets or all packets, but it should not have less messages when the filter is cleared. I doubt that you could post the capture file for us to take a look at since it contains customer data, but maybe you could open a bug report at <a href="http://bugs.wireshark.org">bugs.wireshark.org</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '13, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-17933" class="comments-container"><span id="17953"></span><div id="comment-17953" class="comment"><div id="post-17953-score" class="comment-score"></div><div class="comment-text"><p>sorry you right, there were a lot of customer data in it so i can<code>t post it. A bug report is my idea too. I take a look to make it today because i</code>m very busy at the moment. Thanks for help at this time.</p><p>[Edit: moved the comment here since it was obviously attached at the wrong place before]</p></div><div id="comment-17953-info" class="comment-info"><span class="comment-age">(25 Jan '13, 01:47)</span> <span class="comment-user userinfo">mikethebandit31</span></div></div></div><div id="comment-tools-17933" class="comment-tools"></div><div class="clear"></div><div id="comment-17933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

