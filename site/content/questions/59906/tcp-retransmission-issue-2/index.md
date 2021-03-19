+++
type = "question"
title = "TCP Retransmission Issue (2)"
description = '''We have an issue that sometimes the client (10.10.10.70) requests a main menu from the server (192.168.1.56), it stucks and the connection times out eventually and the main menu does not get displayed at the client. We did a capture and saw the re-transmission issue as shown in the screenshot below....'''
date = "2017-03-07T22:16:00Z"
lastmod = "2017-03-08T01:52:00Z"
weight = 59906
keywords = [ "retransmissions", "tcp", "wireshark" ]
aliases = [ "/questions/59906" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Retransmission Issue (2)](/questions/59906/tcp-retransmission-issue-2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59906-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have an issue that sometimes the client (10.10.10.70) requests a main menu from the server (192.168.1.56), it stucks and the connection times out eventually and the main menu does not get displayed at the client. We did a capture and saw the re-transmission issue as shown in the screenshot below. The server seems to be sending the data back but the client never acknowledges it. Other than the main menu request, the client and the server seem to be communicating properly according to the capture. Any help identifying this issue is greatly appreciated. Thank you</p><p><img src="https://osqa-ask.wireshark.org/upfiles/MainMenuIssue.PNG" alt="alt text" /><br />
</p></div><div id="question-tags" class="tags-container tags">retransmissions tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '17, 22:16</strong></p><img src="https://secure.gravatar.com/avatar/331b3ed2fb21864d41705b7b188041bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Khojal&#39;s gravatar image" /><p>Khojal<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Khojal has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-59906" class="comments-container"></div><div id="comment-tools-59906" class="comment-tools"></div><div class="clear"></div><div id="comment-59906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59909"></span>

<div id="answer-container-59909" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59909-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The capture was probably taken on the server, which is why you have phantom packet sizes larger than 1514 bytes in your file (those never really exist on the network). Please check out this blog post why this can be problematic for troubleshooting:</p><p><a href="https://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/">https://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/</a></p><p>Other than that, my guess is that you have an MTU problem. Small packets make it through, full packets don't. It's a bit hard to tell because your capture method gives inaccurate results, but it still looks like MTU trouble to me. You might want to check the connection path for the lowest MTU; some device is probably silently blocking big packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '17, 01:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-59909" class="comments-container"><span id="59942"></span><div id="comment-59942" class="comment"><div id="post-59942-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jasper for the feedback. I too suspect the issue could be related to the MTU size. However, when I checked, all MTU sizes that I could see so far are set to 1500. I'm not sure where else could be blocking big packets. Here is how the environment is setup:</p><ol><li>Windows host machine (192.168.1.0/24) where the server exists.</li><li>Virtual Ubuntu server with IPTABLES firewall enabled (under Oracle Virtualbox) enp0s8 interface (192.168.1.0/24) and enp0s3 interface (10.10.10.0) where the client network resides.</li><li>Virtual Android client (under GenyMotion) that is integrated with Virtualbox) -&gt; NIC 1 connected to "Virtual Host Only Network #6" and NIC 2 connected to enp0s3 interface (10.10.10.0/24).</li></ol><p>Do we still need to adjust the MTU size anywhere in this setup?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/MTU_HOST_rfLjgIj.PNG" width="640" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/MTU_Virtual.PNG" width="640" /></p></div><div id="comment-59942-info" class="comment-info"><span class="comment-age">(08 Mar '17, 19:00)</span> Khojal</div></div><span id="59951"></span><div id="comment-59951" class="comment"><div id="post-59951-score" class="comment-score"></div><div class="comment-text"><p>How many hops are between client and server? Any router can be blocking the big packets, so you need to check all subnet MTUs between sender and receiver.</p></div><div id="comment-59951-info" class="comment-info"><span class="comment-age">(09 Mar '17, 01:35)</span> Jasper ♦♦</div></div><span id="59952"></span><div id="comment-59952" class="comment"><div id="post-59952-score" class="comment-score"></div><div class="comment-text"><p>If all system resides on one physical machine you can try to update the NIC drivers, as sometimes old drivers have a problem with offloading.</p></div><div id="comment-59952-info" class="comment-info"><span class="comment-age">(09 Mar '17, 01:58)</span> Christian_R</div></div></div><div id="comment-tools-59909" class="comment-tools"></div><div class="clear"></div><div id="comment-59909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

