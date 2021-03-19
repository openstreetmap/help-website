+++
type = "question"
title = "how to crate udp to capture ?"
description = '''Is there anyone help me to crate udp packets? I have a subject about udp and anylies them, but i don&#x27;t know crate them quickly? may you help me clearly, step by step? help me. thanks much.'''
date = "2010-12-31T05:55:00Z"
lastmod = "2011-01-01T04:35:00Z"
weight = 1556
keywords = [ "capture" ]
aliases = [ "/questions/1556" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [how to crate udp to capture ?](/questions/1556/how-to-crate-udp-to-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1556-score" class="post-score" title="current number of votes">0</div><span id="post-1556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there anyone help me to crate udp packets? I have a subject about udp and anylies them, but i don't know crate them quickly? may you help me clearly, step by step? help me. thanks much.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '10, 05:55</strong></p><img src="https://secure.gravatar.com/avatar/4f406866b1740fdc247ba628d2515395?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="haquyen&#39;s gravatar image" /><p><span>haquyen</span><br />
<span class="score" title="1 reputation points">1</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="haquyen has no accepted answers">0%</span></p></div></div><div id="comments-container-1556" class="comments-container"></div><div id="comment-tools-1556" class="comment-tools"></div><div class="clear"></div><div id="comment-1556-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="1558"></span>

<div id="answer-container-1558" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1558-score" class="post-score" title="current number of votes">0</div><span id="post-1558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Why do you need to create one? DNS queries and answers are in UDP so you could just capture your DNS traffic. DNS does use TCP, but its mostly used for zone transfers - not end user queries.</p><p>Or you can generate syslog, snmp etc which all use UDP.</p><p>If you are on a a Cisco based network, you'll most likely run into HSRP traffic which also uses UDP.</p><p>Finally, most modern day computers use UDP (multicast) for a lot of things in the background. If you capture on your NIC in a promiscuous mode, I'll bet you capture some UDP traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '10, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-1558" class="comments-container"></div><div id="comment-tools-1558" class="comment-tools"></div><div class="clear"></div><div id="comment-1558-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1561"></span>

<div id="answer-container-1561" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1561-score" class="post-score" title="current number of votes">0</div><span id="post-1561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In addition, you could use netcat to create UDP packets. I guess it all depends on what you want your UDP packets to look like.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '10, 15:25</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p><span>Paul Stewart</span><br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1561" class="comments-container"></div><div id="comment-tools-1561" class="comment-tools"></div><div class="clear"></div><div id="comment-1561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1569"></span>

<div id="answer-container-1569" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1569-score" class="post-score" title="current number of votes">0</div><span id="post-1569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>thanks Hansangb and Paul Stewart much! Happy New Year</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '11, 04:35</strong></p><img src="https://secure.gravatar.com/avatar/4f406866b1740fdc247ba628d2515395?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="haquyen&#39;s gravatar image" /><p><span>haquyen</span><br />
<span class="score" title="1 reputation points">1</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="haquyen has no accepted answers">0%</span></p></div></div><div id="comments-container-1569" class="comments-container"></div><div id="comment-tools-1569" class="comment-tools"></div><div class="clear"></div><div id="comment-1569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

