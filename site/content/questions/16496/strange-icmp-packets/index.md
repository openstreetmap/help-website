+++
type = "question"
title = "Strange ICMP (?) Packets"
description = '''I&#x27;m pinging my local desktop from a server (Solarwinds Log &amp;amp; Event Manager Virtual Appliance) and when I type &quot;ICMP&quot; into the display filter nothing shows up. However, when I do a &quot;ip.host == 10.96.4.130&quot; in the display filter I start seeing syn + rst/ack packets.   Can anyone tell me why these ...'''
date = "2012-12-03T02:39:00Z"
lastmod = "2012-12-03T03:01:00Z"
weight = 16496
keywords = [ "icmp", "ping" ]
aliases = [ "/questions/16496" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Strange ICMP (?) Packets](/questions/16496/strange-icmp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16496-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm pinging my local desktop from a server (Solarwinds Log &amp; Event Manager Virtual Appliance) and when I type "ICMP" into the display filter nothing shows up. However, when I do a "ip.host == 10.96.4.130" in the display filter I start seeing syn + rst/ack packets.<br />
</p><p><img src="http://i.imgur.com/RPMth.png" alt="alt text" /></p><p>Can anyone tell me why these aren't showing up as regular ICMP packets? When I get a colleague to ping my machine they show up ok, as ICMP, so I don't think it's a setting on my local host.</p><p>Server Address = 10.96.4.130 PC Address = 10.96.47.6 Capture taken from PC.</p></div><div id="question-tags" class="tags-container tags">icmp ping</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '12, 02:39</strong></p><img src="https://secure.gravatar.com/avatar/dd97e5720f9820925500a05ad27350f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m0wax&#39;s gravatar image" /><p>m0wax<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m0wax has no accepted answers">0%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 03 Dec '12, 02:41</p></div></div><div id="comments-container-16496" class="comments-container"></div><div id="comment-tools-16496" class="comment-tools"></div><div class="clear"></div><div id="comment-16496-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16497"></span>

<div id="answer-container-16497" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16497-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like the server ping uses TCP SYN "scans" against the echo service instead of regular pings, but I can't say why. How did you ping from the server? Is it from command line, or an integrated server feature? Try using the ping command from the command line; these should show up as ICMP messages.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '12, 03:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-16497" class="comments-container"><span id="16499"></span><div id="comment-16499" class="comment"><div id="post-16499-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I'm pinging my local desktop from a server (Solarwinds</p></blockquote><p>@m0wax: Did you choose a monitoring method called <strong>echoping</strong> in the Solarwinds appliance? If so, the appliance is most certainly using the <a href="http://echoping.sourceforge.net/">echoping</a> tool and you get what you see.</p></div><div id="comment-16499-info" class="comment-info"><span class="comment-age">(03 Dec '12, 04:15)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16497" class="comment-tools"></div><div class="clear"></div><div id="comment-16497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

