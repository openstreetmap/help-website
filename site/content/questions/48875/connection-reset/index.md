+++
type = "question"
title = "Connection Reset"
description = '''Can I get some help figuring out where and why this is occuring? Here is a link to the capture file: https://www.cloudshark.org/captures/7c1b696a2e4d I am attempting to send an HL7 message to an application on a remote server.'''
date = "2016-01-05T11:24:00Z"
lastmod = "2016-01-05T13:12:00Z"
weight = 48875
keywords = [ "connection_reset", "hl7", "tcp" ]
aliases = [ "/questions/48875" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Connection Reset](/questions/48875/connection-reset)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48875-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I get some help figuring out where and why this is occuring?</p><p>Here is a link to the capture file: <a href="https://www.cloudshark.org/captures/7c1b696a2e4d">https://www.cloudshark.org/captures/7c1b696a2e4d</a></p><p>I am attempting to send an HL7 message to an application on a remote server.</p></div><div id="question-tags" class="tags-container tags">connection_reset hl7 tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '16, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/01c936a8b6d50509b8f84334c5cc2529?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thebrain&#39;s gravatar image" /><p>thebrain<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thebrain has no accepted answers">0%</span></p></div></div><div id="comments-container-48875" class="comments-container"></div><div id="comment-tools-48875" class="comment-tools"></div><div class="clear"></div><div id="comment-48875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48880"></span>

<div id="answer-container-48880" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48880-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can spot the following two things in the trace:</p><ol><li>There is a retransmission of the Initial SYN packet.</li><li>The server terminates the session with an RST packet. The RST packet contains the Acknowledgement for the whole of packet #7</li></ol><p>So if I where you, I would check the server side (logfile analysis or additional trace) or/and the Layer4 / Layer7 devices (FW or loadbalancer) on the network path.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '16, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Jan '16, 13:16</p></div></div><div id="comments-container-48880" class="comments-container"><span id="48881"></span><div id="comment-48881" class="comment"><div id="post-48881-score" class="comment-score"></div><div class="comment-text"><p>To clarify, when you say the server terminates the session, are you saying the destination server terminates it, or the source server?</p></div><div id="comment-48881-info" class="comment-info"><span class="comment-age">(05 Jan '16, 13:22)</span> thebrain</div></div><span id="48883"></span><div id="comment-48883" class="comment"><div id="post-48883-score" class="comment-score"></div><div class="comment-text"><p>Yes I mean the 172.18.110.52</p></div><div id="comment-48883-info" class="comment-info"><span class="comment-age">(05 Jan '16, 13:30)</span> Christian_R</div></div><span id="48890"></span><div id="comment-48890" class="comment"><div id="post-48890-score" class="comment-score"></div><div class="comment-text"><p>@thebrain, the word "server" has an exact meaning in protocols like tcp, where the "client" is the party which sends the initial request (in this case, to establish a tcp session) and the "server" is the party which expects and fulfils/responds such requests (and it usually does so on a fixed, "well-known" port identifying the particular application/service accessible using tcp transport, like http, telnet, ..., while a client is using a temporarily assigned arbitrary port to send the request).</p><p>The fact that powerful "non-personal" computers are called "servers" too is a regrettable source of confusion :-)</p></div><div id="comment-48890-info" class="comment-info"><span class="comment-age">(05 Jan '16, 15:00)</span> sindy</div></div></div><div id="comment-tools-48880" class="comment-tools"></div><div class="clear"></div><div id="comment-48880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

