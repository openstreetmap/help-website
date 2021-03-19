+++
type = "question"
title = "Odd NETBIOS traffic"
description = '''It is to my understanding that NetBIOS operates on port 137. I&#x27;m seeing NetBIOS traffic going from my machine to a remote address associated with an AT&amp;amp;T based IP address. I have that port blocked so I don&#x27;t know why NBNS traffic is still showing up. Please see below. I think this is a cause for...'''
date = "2015-06-14T12:26:00Z"
lastmod = "2015-06-14T13:37:00Z"
weight = 43148
keywords = [ "nbns", "netbios" ]
aliases = [ "/questions/43148" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Odd NETBIOS traffic](/questions/43148/odd-netbios-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43148-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>It is to my understanding that NetBIOS operates on port 137. I'm seeing NetBIOS traffic going from my machine to a remote address associated with an AT&amp;T based IP address. I have that port blocked so I don't know why NBNS traffic is still showing up.</p><p>Please see below. I think this is a cause for concern.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/veryodd_VO41AgK.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">nbns netbios</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '15, 12:26</strong></p><img src="https://secure.gravatar.com/avatar/4784c5fb1a0142030d51a339706a456c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beldum&#39;s gravatar image" /><p>Beldum<br />
<span class="score" title="49 reputation points">49</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beldum has no accepted answers">0%</span></p></img></div></div><div id="comments-container-43148" class="comments-container"></div><div id="comment-tools-43148" class="comment-tools"></div><div class="clear"></div><div id="comment-43148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43153"></span>

<div id="answer-container-43153" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43153-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The NB name queries are broadcast packets being sent by 192.168.1.13, looking for a host named WPAD.</p><p>The NBSTAT name queries are attempts by some Windows machine on your network to try to determine the NetBIOS host name for 12.83.88.89; that's just what Windows <em>does</em>, at least if it's configured to use NetBIOS-over-TCP, if some program is trying to find a host name for 12.83.88.89 - it might try DNS first, and fall back on NetBIOS-over-TCP if that fails, or it might even try NetBIOS-over-TCP first.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '15, 13:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-43153" class="comments-container"></div><div id="comment-tools-43153" class="comment-tools"></div><div class="clear"></div><div id="comment-43153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

