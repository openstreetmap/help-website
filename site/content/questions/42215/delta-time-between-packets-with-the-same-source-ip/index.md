+++
type = "question"
title = "Delta Time Between Packets with the Same Source IP"
description = '''Hello,  Is there a way to create a display or color filter that would show delta time between frames from the same source IP. Without first filtering on 1 source IP, I&#x27;m looking at UDP/RTP packets.  I&#x27;m trying to display gaps in transmitted data from a given source, having both directions src/dst in...'''
date = "2015-05-08T07:57:00Z"
lastmod = "2015-05-08T08:15:00Z"
weight = 42215
keywords = [ "diplay-filter", "frame.time.delta", "ip.src" ]
aliases = [ "/questions/42215" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Delta Time Between Packets with the Same Source IP](/questions/42215/delta-time-between-packets-with-the-same-source-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42215-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42215-score" class="post-score" title="current number of votes">0</div><span id="post-42215-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Is there a way to create a display or color filter that would show delta time between frames from the same source IP. Without first filtering on 1 source IP, I'm looking at UDP/RTP packets.<br />
</p><p>I'm trying to display gaps in transmitted data from a given source, having both directions src/dst in the pcap.</p><p>Thank you....</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diplay-filter" rel="tag" title="see questions tagged &#39;diplay-filter&#39;">diplay-filter</span> <span class="post-tag tag-link-frame.time.delta" rel="tag" title="see questions tagged &#39;frame.time.delta&#39;">frame.time.delta</span> <span class="post-tag tag-link-ip.src" rel="tag" title="see questions tagged &#39;ip.src&#39;">ip.src</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '15, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/48bf9231a93f6d3b12a065bd9054f614?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raf&#39;s gravatar image" /><p><span>Raf</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raf has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-42215" class="comments-container"></div><div id="comment-tools-42215" class="comment-tools"></div><div class="clear"></div><div id="comment-42215-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42217"></span>

<div id="answer-container-42217" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42217-score" class="post-score" title="current number of votes">0</div><span id="post-42217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Within TCP you can enable "Conversation Timestamps" which will show you the time since the first packet in the TCP session and also the time difference between this packet and the previous packet in the TCP session.</p><p>This has not been implemented in other protocols. So for UDP/RTP packets, there is no out-of-the-box way to do it.</p><p>However, you should be able to do this with either <a href="https://wiki.wireshark.org/Mate">MATE</a> or <a href="https://wiki.wireshark.org/Lua">LUA</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '15, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-42217" class="comments-container"></div><div id="comment-tools-42217" class="comment-tools"></div><div class="clear"></div><div id="comment-42217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

