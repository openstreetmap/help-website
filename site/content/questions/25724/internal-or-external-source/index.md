+++
type = "question"
title = "Internal or external source?"
description = '''Hello all, I am still very new to wireshark, and I am curious if someone can guide me in the right direction. I have a packet captured, and we know there is an intruder, but I do not know if there is a way to tell if they are coming from within the network or an outside source. Does Wireshark tell u...'''
date = "2013-10-07T11:34:00Z"
lastmod = "2013-10-07T11:53:00Z"
weight = 25724
keywords = [ "detection", "intruder" ]
aliases = [ "/questions/25724" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Internal or external source?](/questions/25724/internal-or-external-source)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25724-score" class="post-score" title="current number of votes">0</div><span id="post-25724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I am still very new to wireshark, and I am curious if someone can guide me in the right direction. I have a packet captured, and we know there is an intruder, but I do not know if there is a way to tell if they are coming from within the network or an outside source. Does Wireshark tell us that information?<br />
</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-detection" rel="tag" title="see questions tagged &#39;detection&#39;">detection</span> <span class="post-tag tag-link-intruder" rel="tag" title="see questions tagged &#39;intruder&#39;">intruder</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '13, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/ff42a025a287795dd2f6ea45a43e9e5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ruinzifra&#39;s gravatar image" /><p><span>Ruinzifra</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ruinzifra has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-25724" class="comments-container"></div><div id="comment-tools-25724" class="comment-tools"></div><div class="clear"></div><div id="comment-25724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25725"></span>

<div id="answer-container-25725" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25725-score" class="post-score" title="current number of votes">2</div><span id="post-25725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ruinzifra has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I have <strong>a packet</strong> captured,<br />
we know there is an intruder<br />
if they are coming from within the network or an outside source.</p></blockquote><p>well, if you think you identified the intruder action within <strong>that single</strong> packet, just look at the source IP. If it is from your network, the intruder might be internal or external (see below). Otherwise: external (internet, other network).</p><p><strong>HOWEVER</strong>: I doubt you will find an intruder with just a few packets (except in some easy to spot cases). So, if you think there is an intruder, you need to develop an idea which system he/she is attacking and how (protocols). Then you can capture traffic to the target and see who is doing what on that system. By that you will identify the suspicious IP addresses. If they are internal, it can still be an intruder from external. In that case he might just have successfully attacked another system on your network and is now using that 'hacked' system to attack and/or probe the rest of the network.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '13, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Oct '13, 12:22</strong> </span></p></div></div><div id="comments-container-25725" class="comments-container"></div><div id="comment-tools-25725" class="comment-tools"></div><div class="clear"></div><div id="comment-25725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

