+++
type = "question"
title = "Capturing Traffic between multiple hosts"
description = '''I am able to capture data from my machine to different hosts in test environment.  Currently while doing tcpdum command on individual host provide me communication traffic between my machine and that particular host. But I want to capture communication between the hosts. see attached diagram for cle...'''
date = "2017-07-31T06:16:00Z"
lastmod = "2017-07-31T06:56:00Z"
weight = 63255
keywords = [ "multiple-ip-capture", "remote-capture" ]
aliases = [ "/questions/63255" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Capturing Traffic between multiple hosts](/questions/63255/capturing-traffic-between-multiple-hosts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63255-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am able to capture data from my machine to different hosts in test environment. Currently while doing tcpdum command on individual host provide me communication traffic between my machine and that particular host. But I want to capture communication between the hosts. see attached diagram for clearity.<img src="https://osqa-ask.wireshark.org/upfiles/Wireshark_multiplehost.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">multiple-ip-capture remote-capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '17, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/5297abbb36d8a3bc0c96de06b703e64a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sid147228&#39;s gravatar image" /><p>Sid147228<br />
<span class="score" title="9 reputation points">9</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sid147228 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-63255" class="comments-container"><span id="63256"></span><div id="comment-63256" class="comment"><div id="post-63256-score" class="comment-score"></div><div class="comment-text"><p>Well, that's a statement, not a question. Even if the question would be "how to do that?", there is not enough information about the physical topology of the network - it is hard to believe that each of the applications at your picture runs on a separate physical server and these talk to each other using point-to-point links. So please elaborate on this part.</p></div><div id="comment-63256-info" class="comment-info"><span class="comment-age">(31 Jul '17, 06:25)</span> sindy</div></div><span id="63258"></span><div id="comment-63258" class="comment"><div id="post-63258-score" class="comment-score"></div><div class="comment-text"><p>each Server has its own IP. So my questions was how I can capture traffic between those IP from my Machine using wireshark. Its a Web application, And if I perform any transaction on UI, request should go through all these server and come back. I need to capture e2e journey</p></div><div id="comment-63258-info" class="comment-info"><span class="comment-age">(31 Jul '17, 07:01)</span> Sid147228</div></div><span id="63260"></span><div id="comment-63260" class="comment"><div id="post-63260-score" class="comment-score">1</div><div class="comment-text"><p>Wireshark can only capture traffic running through a network interface it can reach directly or remotely. So you can</p><ul><li><p>either install <code>dumpcap</code> on all servers and control it remotely from Wireshark running on a controlling machine,</p></li><li><p>or manually run <code>tcpdump</code> on each of your servers on all interfaces involved in the communication, example: <code>tcpdump -i eth1 -i eth2 -s 0 -w /some_directory/capture_from_server_X</code> and then copy the files to the machine on which you are going to analyse them.</p></li></ul><p>If the physical topology allows traffic mirroring on a physical or virtual switch, you may run <code>tcpdump</code> or <code>Wireshark</code> at single machine connected to a mirroring port.</p></div><div id="comment-63260-info" class="comment-info"><span class="comment-age">(31 Jul '17, 07:40)</span> sindy</div></div><span id="63261"></span><div id="comment-63261" class="comment"><div id="post-63261-score" class="comment-score"></div><div class="comment-text"><p>You can run <code>dumpcap</code> manually, but there seemed to be some issues with triggering <code>tcpdump</code> remotely, that's why I've suggested it the way above.</p></div><div id="comment-63261-info" class="comment-info"><span class="comment-age">(31 Jul '17, 07:44)</span> sindy</div></div></div><div id="comment-tools-63255" class="comment-tools"></div><div class="clear"></div><div id="comment-63255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63257"></span>

<div id="answer-container-63257" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63257-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I want to capture communication between the hosts.</p></blockquote><p>So that means that you'll have to tell tcpdump to capture on the network interface between the hosts, not the network interface between the host and your machine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '17, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-63257" class="comments-container"><span id="63259"></span><div id="comment-63259" class="comment"><div id="post-63259-score" class="comment-score"></div><div class="comment-text"><p>Thanks Can you give an example to picture me your answer</p></div><div id="comment-63259-info" class="comment-info"><span class="comment-age">(31 Jul '17, 07:02)</span> Sid147228</div></div></div><div id="comment-tools-63257" class="comment-tools"></div><div class="clear"></div><div id="comment-63257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

