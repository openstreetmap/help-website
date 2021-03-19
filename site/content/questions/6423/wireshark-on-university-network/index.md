+++
type = "question"
title = "Wireshark on University Network"
description = '''Hello, I am teaching a Computer Networks class, and I have access to my University wired and wireless computer network. I am an ordinary user, and I do not have any network administrative privilege. If I use Wireshark installed on my laptop computer while the computer is connected to the University ...'''
date = "2011-09-16T09:01:00Z"
lastmod = "2011-09-16T09:57:00Z"
weight = 6423
keywords = [ "security", "compromise" ]
aliases = [ "/questions/6423" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark on University Network](/questions/6423/wireshark-on-university-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6423-score" class="post-score" title="current number of votes">0</div><span id="post-6423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am teaching a Computer Networks class, and I have access to my University wired and wireless computer network. I am an ordinary user, and I do not have any network administrative privilege.</p><p>If I use Wireshark installed on my laptop computer while the computer is connected to the University network, can it compromise other network users' privacy/security?<br />
</p><p>What impact my occasional use of Wireshark can have on the University network and where can I find such documentation that I can share with concerned people?</p><p>Thank you very much for any information someone can provide to this regard!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-security" rel="tag" title="see questions tagged &#39;security&#39;">security</span> <span class="post-tag tag-link-compromise" rel="tag" title="see questions tagged &#39;compromise&#39;">compromise</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '11, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/3c6872ec0fcc72d88d459879a5292165?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="learnerou&#39;s gravatar image" /><p><span>learnerou</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="learnerou has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-6423" class="comments-container"></div><div id="comment-tools-6423" class="comment-tools"></div><div class="clear"></div><div id="comment-6423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6424"></span>

<div id="answer-container-6424" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6424-score" class="post-score" title="current number of votes">2</div><span id="post-6424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Can it compromise other network users's privacy/security? The short answer is, yes, potentially. It's a matter of to what degree.</p><p>University networks are usually pretty modern, so the wired network is probably fully switched, in which case you should only see traffic to and from your own PC, plus broadcast traffic. Also, any really sensitive traffic (for example, a user logging into his online banking account) should be encrypted. However, to the extend that you CAN see other people's traffic and it's unencrypted, there is at least the potential to see things that are private.</p><p>If the wireless network is encrypted, then you will be able to see other people's traffic, but it will not be readable. If the wireless network allows open, unencrypted access, then you will be able to read other people's traffic; at least other people using the same access point.</p><p>Use of Wireshark on the University network will have no impact, because Wireshark is a passive tool that does not generate any traffic, with one exception: If you have network name resolution turned on, Wireshark will generate a DNS PTR query for each new IP address seen. If you turn network name resolution off, Wireshark should have no impact on the network.</p><p>Using Wireshark in a computer network class is an eminently reasonable and sensible thing to do, and is very common. Many instructors have student exercises that require the use of Wireshark. If you think it might run afoul of your University's Acceptable Use Policies, then you should discuss it with the network administration staff. You might want to modify the course syllabus for next semester to include Wireshark, which would certainly bolster your case for using it in class.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '11, 09:57</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Sep '11, 11:08</strong> </span></p></div></div><div id="comments-container-6424" class="comments-container"></div><div id="comment-tools-6424" class="comment-tools"></div><div class="clear"></div><div id="comment-6424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

