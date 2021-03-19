+++
type = "question"
title = "ICMP not showing up after filtering tcp.port"
description = '''I was troubleshooting a network issue on a host remotely, I had the following filter set: ip.addr eq my.ip.addr and tcp.port !=#### I set the tcp.port to not equal the one LogMeIn was using so that I can see other traffic coming from me to the remote host that is not the remote desktop session. But ...'''
date = "2013-07-08T16:51:00Z"
lastmod = "2013-07-08T16:59:00Z"
weight = 22739
keywords = [ "icmp", "display-filter" ]
aliases = [ "/questions/22739" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ICMP not showing up after filtering tcp.port](/questions/22739/icmp-not-showing-up-after-filtering-tcpport)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22739-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was troubleshooting a network issue on a host remotely, I had the following filter set: <code>ip.addr eq my.ip.addr and tcp.port !=####</code> I set the tcp.port to not equal the one LogMeIn was using so that I can see other traffic coming from me to the remote host that is not the remote desktop session. But it was filtering out my ICMP traffic to the host as well, not sure what I'm doing wrong here.</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">icmp display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '13, 16:51</strong></p><img src="https://secure.gravatar.com/avatar/f08740de6f428d94664d52640ad2f113?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="reikokuko&#39;s gravatar image" /><p>reikokuko<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="reikokuko has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jul '13, 17:41</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-22739" class="comments-container"></div><div id="comment-tools-22739" class="comment-tools"></div><div class="clear"></div><div id="comment-22739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22740"></span>

<div id="answer-container-22740" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22740-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since you specified a filter part that filters on a TCP port it will filter away ICMP because that is just not TCP (unless you get an ICMP error that quotes a TCP layer). You could change your filter to</p><pre><code>ip.addr eq my.ip.addy and icmp or tcp.port !=####</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '13, 16:59</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-22740" class="comments-container"></div><div id="comment-tools-22740" class="comment-tools"></div><div class="clear"></div><div id="comment-22740-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

