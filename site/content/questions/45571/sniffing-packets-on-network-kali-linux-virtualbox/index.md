+++
type = "question"
title = "Sniffing packets on network kali linux VirtualBox"
description = '''So I have A WINDOWS 8 host machine and installed using Virtual Box Kali Linux.  I have an Ethernet cable directly plugged into my computer. Cant capture packets  I have tried Bridging the network and &quot;Allows VMls and Allow All&quot; but nothing has worked.  If you guys can please help me out that would b...'''
date = "2015-09-01T10:19:00Z"
lastmod = "2015-09-01T13:27:00Z"
weight = 45571
keywords = [ "kali", "network", "linux" ]
aliases = [ "/questions/45571" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Sniffing packets on network kali linux VirtualBox](/questions/45571/sniffing-packets-on-network-kali-linux-virtualbox)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45571-score" class="post-score" title="current number of votes">0</div><span id="post-45571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I have A WINDOWS 8 host machine and installed using Virtual Box Kali Linux. I have an Ethernet cable directly plugged into my computer. Cant capture packets</p><p>I have tried Bridging the network and "Allows VMls and Allow All" but nothing has worked.</p><p>If you guys can please help me out that would be fantastic. IP address conflict at work.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-kali" rel="tag" title="see questions tagged &#39;kali&#39;">kali</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '15, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/5bed56a64cd281f8272b3a155f578cbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="toucansam313&#39;s gravatar image" /><p><span>toucansam313</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="toucansam313 has no accepted answers">0%</span></p></div></div><div id="comments-container-45571" class="comments-container"></div><div id="comment-tools-45571" class="comment-tools"></div><div class="clear"></div><div id="comment-45571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45579"></span>

<div id="answer-container-45579" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45579-score" class="post-score" title="current number of votes">0</div><span id="post-45579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My guess is that the VM doesn't get the packets that are not directed at it's MAC address. I don't think this setup will work if you intend to pickup packets from the cable.</p><p>But what you could do is ping the IP in question from your Kali while Wireshark is running. You should see one ARP request and at least two ARP responses - with those you know which MAC addresses the duplicate IP is on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Sep '15, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-45579" class="comments-container"></div><div id="comment-tools-45579" class="comment-tools"></div><div class="clear"></div><div id="comment-45579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

