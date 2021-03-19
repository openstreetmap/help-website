+++
type = "question"
title = "Wireshark - Switched vs Routed networks - getting it together in my head"
description = '''Hello forum users, Recently i discovered that you cannot monitor a switched network without doing some special stuff. I solved that by using a named pipe on the server i wanted to monitor. Is it possible in a switched network to monitor the complete switched network without disrupting it or having t...'''
date = "2014-11-27T05:12:00Z"
lastmod = "2014-11-27T08:04:00Z"
weight = 38208
keywords = [ "switchednetwork", "monitor", "general" ]
aliases = [ "/questions/38208" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark - Switched vs Routed networks - getting it together in my head](/questions/38208/wireshark-switched-vs-routed-networks-getting-it-together-in-my-head)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38208-score" class="post-score" title="current number of votes">0</div><span id="post-38208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello forum users,</p><p>Recently i discovered that you cannot monitor a switched network without doing some special stuff. I solved that by using a named pipe on the server i wanted to monitor. Is it possible in a switched network to monitor the complete switched network without disrupting it or having to enable "monitor ports" on the switches? I just want to be able to monitor the complete network of the company i work for. Just for troubleshooting voip, dhcp etc. I know this has bin answered before and there is some documentation on this topic but i don't realy understand.</p><p>kind regards,</p><p>neaJules.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-switchednetwork" rel="tag" title="see questions tagged &#39;switchednetwork&#39;">switchednetwork</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span> <span class="post-tag tag-link-general" rel="tag" title="see questions tagged &#39;general&#39;">general</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '14, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/ad8018b5b1268743bb3ca93ee36788e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neaJules&#39;s gravatar image" /><p><span>neaJules</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neaJules has no accepted answers">0%</span></p></div></div><div id="comments-container-38208" class="comments-container"></div><div id="comment-tools-38208" class="comment-tools"></div><div class="clear"></div><div id="comment-38208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38211"></span>

<div id="answer-container-38211" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38211-score" class="post-score" title="current number of votes">0</div><span id="post-38211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A switch/router forwards packets from the incomming port to the outgoing port towards the destination so the apcket are only accessableto the capturing tool on the sending or reciving server or by switch switch it self which could copy it to a monitoring/span port. Not to other eqipment connected to other ports on the switch/router. You can insert taps(HW equipment) on the cabels connected to the switch port to copy the packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '14, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-38211" class="comments-container"></div><div id="comment-tools-38211" class="comment-tools"></div><div class="clear"></div><div id="comment-38211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38213"></span>

<div id="answer-container-38213" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38213-score" class="post-score" title="current number of votes">0</div><span id="post-38213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I just want to be able to monitor the complete network of the company i work for.<br />
without disrupting it or having to enable "monitor ports" on the switches?</p></blockquote><p>well, if you don't want to enable monitor/mirroring ports, it's going to become diffucult, because the way a switch works will prevent monitoring the "whole" network.</p><p>See the Ethernet Capturing Setup Wiki:</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a><br />
</p></blockquote><p>So, you either</p><ul><li>enable port mirroring, however that's not going to work for the <strong>whole switch</strong></li><li>replace the switch with a hub. Good luck with that approach ;-)</li><li>capture directly on the involved systems (install Wireshark on it)</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '14, 08:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-38213" class="comments-container"></div><div id="comment-tools-38213" class="comment-tools"></div><div class="clear"></div><div id="comment-38213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

