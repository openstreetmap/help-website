+++
type = "question"
title = "Forced to join a network"
description = '''Hi everybody, I&#x27;m new here and I&#x27;m a Wireshark layman. Wireshark was running on my computer, because I wanted to check, whether my computer perhaps is getting hacked. I&#x27;ve done the following steps one after another several times: 1) Starting a capture with Wireshark (promiscouos) 2) After starting t...'''
date = "2016-12-27T10:28:00Z"
lastmod = "2016-12-27T16:36:00Z"
weight = 58369
keywords = [ "middle", "the", "in", "network", "man" ]
aliases = [ "/questions/58369" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Forced to join a network](/questions/58369/forced-to-join-a-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58369-score" class="post-score" title="current number of votes">0</div><span id="post-58369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody, I'm new here and I'm a Wireshark layman. Wireshark was running on my computer, because I wanted to check, whether my computer perhaps is getting hacked. I've done the following steps one after another several times:</p><p>1) Starting a capture with Wireshark (promiscouos) 2) After starting the capture I've switched on my router</p><p>And the result was always the same: Immediately after switching on the router there was started a routine, which has to do with the IP 169.254.242.58. I myself are not able to find out, how to stop that, or which program is the trigger of that and of course I'd like to know, if that is maybe the preperation for a man-in-the-middle-attack. In my Wireshark capture was also a query as follows: "A request for all records the server/cache has available (255)" I also have installed the Comodo-Browser, because it can give warnings, if there are attacks like man-in-the-middle, and anyway Comodo gave to me the hint "joined to network 169.254.242.58/16" (!) and it gave to me a warning, that there could be an attack. There also have been more troubles: If I wanted to visit Google, there was the Comodo hint, that there is something wrong with the Google certificate and furthermore "https" was crossed out.</p><p>This is my first post in this forum here. I want to know the way to stop to be forced to a network, although today that hint didn‘t appear again. Neither Comodo has blocked that, because of a sandbox, or that 169.254.242.58 network isn‘t running today. Thank you very much in advance for help and tips.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-middle" rel="tag" title="see questions tagged &#39;middle&#39;">middle</span> <span class="post-tag tag-link-the" rel="tag" title="see questions tagged &#39;the&#39;">the</span> <span class="post-tag tag-link-in" rel="tag" title="see questions tagged &#39;in&#39;">in</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-man" rel="tag" title="see questions tagged &#39;man&#39;">man</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Dec '16, 10:28</strong></p><img src="https://secure.gravatar.com/avatar/13b6056a763038e0914816d3f36011f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="R53&#39;s gravatar image" /><p><span>R53</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="R53 has no accepted answers">0%</span></p></div></div><div id="comments-container-58369" class="comments-container"></div><div id="comment-tools-58369" class="comment-tools"></div><div class="clear"></div><div id="comment-58369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58385"></span>

<div id="answer-container-58385" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58385-score" class="post-score" title="current number of votes">0</div><span id="post-58385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think you're getting confused.</p><p>An address in the 169.254.0.0/16 block (which 169.254.242.58 is), is known as an IPv4 <a href="https://en.wikipedia.org/wiki/Link-local_address">APIPA</a> or link-local address, and is automatically assigned by Windows to an interface if that interface is configured for DHCP and is unable to contact a DHCP server.</p><p>This happens in your tests as the router is off, normally in a home network the router acts as a DHCP server.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '16, 16:36</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-58385" class="comments-container"></div><div id="comment-tools-58385" class="comment-tools"></div><div class="clear"></div><div id="comment-58385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

