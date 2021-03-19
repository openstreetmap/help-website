+++
type = "question"
title = "A ghost prints during the night on a printer."
description = '''Hi, Each night, without any people send anything, a printer prints 10 blank pages. When the printer is not connected to the network, it prints nothing. Impossible to know who send this (what server, what device, what machine on the network, during the night, without any people in the plant). So I&#x27;m ...'''
date = "2017-10-20T05:57:00Z"
lastmod = "2017-10-20T08:33:00Z"
weight = 64047
keywords = [ "device", "printing" ]
aliases = [ "/questions/64047" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [A ghost prints during the night on a printer.](/questions/64047/a-ghost-prints-during-the-night-on-a-printer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64047-score" class="post-score" title="current number of votes">1</div><span id="post-64047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Each night, without any people send anything, a printer prints 10 blank pages. When the printer is not connected to the network, it prints nothing. Impossible to know who send this (what server, what device, what machine on the network, during the night, without any people in the plant). So I'm searching a tool, that I lunch on my desktop on the afternoon, to discover which IP address sent some traffic to this printer. Our network countains 390 PC, 20 servers, 40 IP printers, and others IP tools, in 5 buildings. Question 1 : is wireshark the good tool to have this information. Q2 : if yes, how can I do this ? Q3 : if no, is there another tool to do this ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-device" rel="tag" title="see questions tagged &#39;device&#39;">device</span> <span class="post-tag tag-link-printing" rel="tag" title="see questions tagged &#39;printing&#39;">printing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '17, 05:57</strong></p><img src="https://secure.gravatar.com/avatar/d136a544c7c69bfadc754e2b0845aa9e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JMiG&#39;s gravatar image" /><p><span>JMiG</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JMiG has no accepted answers">0%</span></p></div></div><div id="comments-container-64047" class="comments-container"><span id="64051"></span><div id="comment-64051" class="comment"><div id="post-64051-score" class="comment-score"></div><div class="comment-text"><p>Is this a enterprise type printer, or a simple model? What kind of logging / accounting can it do? Does this allow you to at least narrow down when this job is being printed?</p></div><div id="comment-64051-info" class="comment-info"><span class="comment-age">(20 Oct '17, 08:27)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="64052"></span><div id="comment-64052" class="comment"><div id="post-64052-score" class="comment-score"></div><div class="comment-text"><p>It's a label printer =&gt; "Intermec PD42". Normally only the MRP software (when we receeive a shipment, the software automatically prints labels for the received parts). This software runs only on a server. The server send labels. But I searched in the logs of this software, a not any label has been sent during the night.</p></div><div id="comment-64052-info" class="comment-info"><span class="comment-age">(20 Oct '17, 08:33)</span> <span class="comment-user userinfo">JMiG</span></div></div></div><div id="comment-tools-64047" class="comment-tools"></div><div class="clear"></div><div id="comment-64047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64048"></span>

<div id="answer-container-64048" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64048-score" class="post-score" title="current number of votes">1</div><span id="post-64048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, Wireshark would be my tool of choice (or any other packet capture tool). Problem is that it won't do any good to run it on your desktop: the packets going to the printer are not going to be visible there in a switched network.</p><p>What you need to do is this:</p><ol><li>Find the switch the printer is connected to</li><li>determine if that switch is manageable and can be configured for a SPAN port (also called monitor port), which means that you can send copies of packets from one port (the printer port) to the port where you attach your Wireshark laptop/PC</li><li>if the switch is not configurable for SPAN you are in trouble and need to find other ways, e.g. using a TAP (which you probably don't have) or getting a small configurable switch you can insert into the link to the printer</li><li>capture the packets</li></ol><p>For capture setup information, check out</p><p><a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><p><a href="https://blog.packet-foo.com/2016/10/the-network-capture-playbook-part-1-ethernet-basics/">https://blog.packet-foo.com/2016/10/the-network-capture-playbook-part-1-ethernet-basics/</a></p><p>In the end you should have packets around the time the printer prints (make sure the capture laptop/PC clock is correct) and can easily see the IP/MAC the traffic is coming from.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '17, 06:03</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-64048" class="comments-container"></div><div id="comment-tools-64048" class="comment-tools"></div><div class="clear"></div><div id="comment-64048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

