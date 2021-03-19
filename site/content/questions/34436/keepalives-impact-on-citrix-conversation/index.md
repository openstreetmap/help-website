+++
type = "question"
title = "Keepalives impact on Citrix conversation"
description = '''Hi Folks, I am having intermittent issues with Citrix XenApp Latency over WAN. I have been running wireshark on client machines during the week recording periods both good and poor performnace periods. Firstly I have not found any errors, retransmissions, Dup acks in the captures nor have I found an...'''
date = "2014-07-05T04:35:00Z"
lastmod = "2014-07-05T04:35:00Z"
weight = 34436
keywords = [ "rtt", "citrix", "keepalive" ]
aliases = [ "/questions/34436" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Keepalives impact on Citrix conversation](/questions/34436/keepalives-impact-on-citrix-conversation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34436-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Folks,</p><p>I am having intermittent issues with Citrix XenApp Latency over WAN. I have been running wireshark on client machines during the week recording periods both good and poor performnace periods.</p><p>Firstly I have not found any errors, retransmissions, Dup acks in the captures nor have I found any 0 window size packets.</p><p>When I used the IO graph to plot the citrix TCP stream I noticed there were drop offs in packet throughput periodically during goodish periods and more frequently during bad periods. There were no errors to corealate these drops in throughput to.</p><p>I then overlayed the 'TCP.time_delta &gt;.6' into the IO graph and noticed these values spiked before and after the citrix traffic packet throughput drops.</p><p>The only thing that appear to corealate to the packet throughout drops and the TCP time delta &gt;.6 was that the client machies were receiving keepalive messages from 2x MS Exchange servers right before and sometimes during the Citrix packet throughput drops.</p><p>Infact in the captures taken during particularly bad periods the number of MS Exchange keepalives being received by the client is much higer than during the good periods.</p><p>I'm not sure what to make of this as normally I filter out keepalive messages I have never seen anything like this before. has anyone else?</p></div><div id="question-tags" class="tags-container tags">rtt citrix keepalive</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '14, 04:35</strong></p><img src="https://secure.gravatar.com/avatar/55af0207b10dbbd15ebb9f852822a294?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ciag&#39;s gravatar image" /><p>Ciag<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ciag has no accepted answers">0%</span></p></div></div><div id="comments-container-34436" class="comments-container"></div><div id="comment-tools-34436" class="comment-tools"></div><div class="clear"></div><div id="comment-34436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

