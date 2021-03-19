+++
type = "question"
title = "Why ACK not sent back"
description = '''have an app timing out intermittently hitting a database. client is win2k8 server is Oracle Enterprise Linux. No firewall inbetween. To try and troubleshoot, I got a version of the app to run every second. Leaving it for a day I might get 2-3 timeouts. not much, but affects us real bad when it happe...'''
date = "2014-09-10T04:46:00Z"
lastmod = "2014-09-10T05:09:00Z"
weight = 36153
keywords = [ "accept", "retransmissions", "tcp", "failing" ]
aliases = [ "/questions/36153" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why ACK not sent back](/questions/36153/why-ack-not-sent-back)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36153-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>have an app timing out intermittently hitting a database. client is win2k8 server is Oracle Enterprise Linux. No firewall inbetween.</p><p>To try and troubleshoot, I got a version of the app to run every second. Leaving it for a day I might get 2-3 timeouts. not much, but affects us real bad when it happens in a prod environment. PCAP running the client, tcpdump on the sever. this is what they look like, client sends the START, server gets it, tries to send ACK back but client doesnt get it. You can see the retransmission attempts. the app times out at this point, and starts running fine again.</p><p>10gb NICs either side. No server load. No client load. No error messages on either side.<br />
Ran it to different server. Same problem.<br />
Ran from different client, same problem Wireshark 1.12.0</p><p>What could cause this?<br />
</p><p>CLIENT <img src="http://i58.tinypic.com/2zi77r9.jpg" alt="alt text" /></p><p>SERVER <img src="http://i58.tinypic.com/2is8l8z.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">accept retransmissions tcp failing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '14, 04:46</strong></p><img src="https://secure.gravatar.com/avatar/80b449cfa1db066f054940a233bff779?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carsmusings&#39;s gravatar image" /><p>carsmusings<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carsmusings has no accepted answers">0%</span> </br></br></p></img></div></div><div id="comments-container-36153" class="comments-container"></div><div id="comment-tools-36153" class="comment-tools"></div><div class="clear"></div><div id="comment-36153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36154"></span>

<div id="answer-container-36154" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36154-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If there is no firewall in the network between client and server something else must prevent the SYN/ACK to reach the client. Is there any host based firewall running on the client, and if so, can you try to turn it off for a test? Also, some anti virus solutions sometimes mess with the network stack, so maybe disabled that for a test could be an option, too.</p><p>Both actions (turning off any security software like the firewall or anti virus) is of course a risk. If you can't live with that you might want to try to capture the client traffic right before it gets to the client. E.g configure a monitor port on the switch the client is connected to and capture the client traffic with an additional PC. That way you can determine if the SYN/ACK can be seen on the way to the client, because if you see it there and not on the client itself you know it gets lost in the client itself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '14, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></p></img></div></div><div id="comments-container-36154" class="comments-container"><span id="36159"></span><div id="comment-36159" class="comment"><div id="post-36159-score" class="comment-score"></div><div class="comment-text"><p>Thinking along the same lines, I do have a firewall for some other apps, I generated a timeout event from a client the other side of it. The client PCAP shows same thing, server shows same thing, but the firewall does not see the return event so this says its either getting lost at the server NIC or switch.</p><p>iptables off on the server.<br />
</p><p>1 very peculiar thing, as Im sure we all know all that TCP SYN/ACK stuff happens in milliseconds. During the troubleshooting when testing with the firewall, if I search the firewall for that port in the time out event, example 42966 in the above dumps, I could see the ACCEPT of the port coming back something like 2 minutes later. The client PCAP doesnt show this but Im guessing at that point the TCP stream is dead from its side.</p><p>Delayed ACKs maybe but from reading, that can only happen up to under a second, but 2 minutes?</p></div><div id="comment-36159-info" class="comment-info"><span class="comment-age">(10 Sep '14, 05:51)</span> carsmusings</div></div><span id="36161"></span><div id="comment-36161" class="comment"><div id="post-36161-score" class="comment-score"></div><div class="comment-text"><p>If the client PCAPs are captured <strong>on</strong> the client you may not see what's really happening. Local captures are often misleading and do not show what really happened on the network. This is why I recommend to capture on the network, not the nodes involved.</p><p>"Delayed ACKs" are not relevant to session setups, they happen when the data flow is already established and an odd number of segments are transmitted.</p></div><div id="comment-36161-info" class="comment-info"><span class="comment-age">(10 Sep '14, 05:58)</span> Jasper ♦♦</div></div></div><div id="comment-tools-36154" class="comment-tools"></div><div class="clear"></div><div id="comment-36154-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

