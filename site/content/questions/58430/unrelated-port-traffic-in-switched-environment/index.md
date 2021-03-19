+++
type = "question"
title = "Unrelated port traffic in switched environment"
description = '''Hi all, maybe it is a very simple question, but i am new to network monitoring and i am courious. We use Dell PowerConnect 28xx series of managed switches. I did monitor the communication of printer that makes some trouble when it comes to sending mails. I use an old hub instead of port mirroring, b...'''
date = "2016-12-30T01:19:00Z"
lastmod = "2016-12-30T04:16:00Z"
weight = 58430
keywords = [ "switch", "unrelated", "traffic" ]
aliases = [ "/questions/58430" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unrelated port traffic in switched environment](/questions/58430/unrelated-port-traffic-in-switched-environment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58430-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>maybe it is a very simple question, but i am new to network monitoring and i am courious.</p><p>We use Dell PowerConnect 28xx series of managed switches. I did monitor the communication of printer that makes some trouble when it comes to sending mails. I use an old hub instead of port mirroring, because I'm more flexible with it. Cables are plugged in the hub as follows.</p><p>Hub &lt;- (printer, local network (switched), monitoring laptop)</p><p>Question:</p><p>Is it normal for a switched environment, that I can see traffic completly unrelated to the printer on my monitored Port? I don't mean broadcast or multicast traffic, but traffic like packets from our gateway to our webserver and stuff like that. There are many TCP packets from a bunch of hosts, wich all are communicating with other hosts, but not the monitored printer. Can this somehow be explained?</p><p>Maybe VLAN related? There is one VLAN configured on the switch, but only for the uplink ports. And I don't see the traffic for that VLAN on my monitored Port...</p><p>Any comments or hints are appreciated.</p></div><div id="question-tags" class="tags-container tags">switch unrelated traffic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '16, 01:19</strong></p><img src="https://secure.gravatar.com/avatar/8f9f95a49e645bb7fd00f431ac0a9645?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="delis&#39;s gravatar image" /><p>delis<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="delis has no accepted answers">0%</span></p></div></div><div id="comments-container-58430" class="comments-container"></div><div id="comment-tools-58430" class="comment-tools"></div><div class="clear"></div><div id="comment-58430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58434"></span>

<div id="answer-container-58434" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58434-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Those are most likely just flooded packets where the switch had to learn the MAC address first. Check this blog post for some more details:</p><p><a href="https://blog.packet-foo.com/2016/10/the-network-capture-playbook-part-1-ethernet-basics/">https://blog.packet-foo.com/2016/10/the-network-capture-playbook-part-1-ethernet-basics/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '16, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-58434" class="comments-container"></div><div id="comment-tools-58434" class="comment-tools"></div><div class="clear"></div><div id="comment-58434-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

