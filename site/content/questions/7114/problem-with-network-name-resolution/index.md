+++
type = "question"
title = "problem with network name resolution"
description = '''I&#x27;m running wireshark 1.6.2. I have a main site with a network of 10.0.0.x and a sattelite office with a network of 192.168.17.x the machines on the 192.168.17.x network use a dns server on the 10.0.0.x network. from a machine on the 10.0.0.x network if I ping sat1 it correctly resolves and pings th...'''
date = "2011-10-27T16:40:00Z"
lastmod = "2011-10-28T00:09:00Z"
weight = 7114
keywords = [ "dns" ]
aliases = [ "/questions/7114" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [problem with network name resolution](/questions/7114/problem-with-network-name-resolution)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7114-score" class="post-score" title="current number of votes">0</div><span id="post-7114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running wireshark 1.6.2. I have a main site with a network of 10.0.0.x and a sattelite office with a network of 192.168.17.x the machines on the 192.168.17.x network use a dns server on the 10.0.0.x network. from a machine on the 10.0.0.x network if I ping sat1 it correctly resolves and pings the machine at the remote office. If I look at the DNS server I see host records for the machines in the 192.168.17.x network. But if I enable network name resolution is a trace I only see ames being resolved for names in the local 10.0.0.x network. Is there a way to enable this for all of my machines? Thanks in advance for any info.</p><p>-Phil</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '11, 16:40</strong></p><img src="https://secure.gravatar.com/avatar/2b6a51c18570aeed19f0f83be56164da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Philip810&#39;s gravatar image" /><p><span>Philip810</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Philip810 has no accepted answers">0%</span></p></div></div><div id="comments-container-7114" class="comments-container"></div><div id="comment-tools-7114" class="comment-tools"></div><div class="clear"></div><div id="comment-7114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7128"></span>

<div id="answer-container-7128" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7128-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7128-score" class="post-score" title="current number of votes">0</div><span id="post-7128-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do you have reverse DNS setup properly?</p><p>What you test with ping is normal, forward DNS: resolve name to IP address.</p><p>What Wireshark does is reverse DNS: resolve IP address to name.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '11, 00:09</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7128" class="comments-container"></div><div id="comment-tools-7128" class="comment-tools"></div><div class="clear"></div><div id="comment-7128-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

