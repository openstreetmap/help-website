+++
type = "question"
title = "Lower Source port traffic lost on internet"
description = '''We have a process for credit card payments to a third party vendor. Two servers, one for customer facing transactions on a Windows 2012 OS, the other on a Windows 2003 OS (I know, not supported anymore). The Windows 2012 OS only uses private port range somewhere in the range of 49000 - 65000. Window...'''
date = "2016-05-20T06:08:00Z"
lastmod = "2016-07-19T08:18:00Z"
weight = 52803
keywords = [ "source", "lower", "ports", "lost" ]
aliases = [ "/questions/52803" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lower Source port traffic lost on internet](/questions/52803/lower-source-port-traffic-lost-on-internet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52803-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a process for credit card payments to a third party vendor. Two servers, one for customer facing transactions on a Windows 2012 OS, the other on a Windows 2003 OS (I know, not supported anymore). The Windows 2012 OS only uses private port range somewhere in the range of 49000 - 65000. Windows 2003 uses 1023-5000. We have noticed in a wireshark capture that sometimes when the server(Windows 2003), or the firewall (NAT) changes the source port to a number lower than 1550, the traffic is lost outside our network and never gets to our vendor. Has anyone witnessed this type of activity? We have spoken to our ISP and they say they do not block anything. I suspect that these lower source ports are in conflict with another application beyond our control.</p></div><div id="question-tags" class="tags-container tags">source lower ports lost</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '16, 06:08</strong></p><img src="https://secure.gravatar.com/avatar/1418eb034f06e6496e14295819c45ed8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jbanu2&#39;s gravatar image" /><p>Jbanu2<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jbanu2 has no accepted answers">0%</span></p></div></div><div id="comments-container-52803" class="comments-container"></div><div id="comment-tools-52803" class="comment-tools"></div><div class="clear"></div><div id="comment-52803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54157"></span>

<div id="answer-container-54157" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54157-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you suspect a port conflict, you could try modifying your application to use a fixed source port in a range above 1550, rather than using an ephemeral port. If you can't (or don't want to) modify the application, or if doing so doesn't help, you could try to reserve ports below 1550 so they're not included in the dynamic pool. See <a href="https://support.microsoft.com/en-us/kb/812873">https://support.microsoft.com/en-us/kb/812873</a> for more information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '16, 08:18</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-54157" class="comments-container"><span id="54161"></span><div id="comment-54161" class="comment"><div id="post-54161-score" class="comment-score"></div><div class="comment-text"><blockquote><p>sometimes when the server(Windows 2003), or the firewall (NAT) changes the source port to a number lower than 1550...</p></blockquote><p>Does this mean that you don't know whether it is the firewall or the server that chooses these "low" port numbers, or that both of them sometimes do that? Because if both can do that, you have to configure both the Windows and the firewall to avoid using these ports.</p><blockquote><p>I suspect that these lower source ports are in conflict with another application beyond our control.</p></blockquote><p>If you have in mind an application on the PC, then no, for two reasons:</p><ul><li><p>an application cannot freely choose an ephemeral port for a TCP session, it asks the TCP stack for one; if a local TCP port is already occupied by either a running client session or by a server application listening on it, the TCP stack wouldn't give the same port (well, socket) to another application</p></li><li><p>I don't know how W2003's TCP stack works exactly, but it should require that the conflicting application would open sessions towards the same remote server that the conflict could happen. Using port X as ephemeral one for connection to server Y port A and using it at the same time for connection to server Y port B or to server Z port A is perfectly OK from the point of view of TCP</p></li></ul><p>Besides, if it would be an application on your own PC or in your own network, I doubt it would listen on all ports below 1550 and not send anything back.</p><p>So if <em>your</em> ISP says they don't block anything, ask them to check it using Wireshark or tcpdump at their output route towards the server, and if your requests are still visible there, move the investigation to the receiving end - the third party vendor also have their ISP and security guys.</p></div><div id="comment-54161-info" class="comment-info"><span class="comment-age">(19 Jul '16, 09:05)</span> sindy</div></div></div><div id="comment-tools-54157" class="comment-tools"></div><div class="clear"></div><div id="comment-54157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

