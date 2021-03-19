+++
type = "question"
title = "Interpreting logs"
description = '''We have a trojan on our network as out IP keeps getting blacklisted by CBL. Something is sending spam about once every week and then we get blacklisted and it stops. I installed wireshark and set it to collect traffic data for TCP port 25 and have been waiting for another CBL blacklist. It happened ...'''
date = "2014-09-10T15:55:00Z"
lastmod = "2014-09-10T16:26:00Z"
weight = 36182
keywords = [ "trojan", "logs", "wireshark" ]
aliases = [ "/questions/36182" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Interpreting logs](/questions/36182/interpreting-logs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36182-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a trojan on our network as out IP keeps getting blacklisted by CBL. Something is sending spam about once every week and then we get blacklisted and it stops. I installed wireshark and set it to collect traffic data for TCP port 25 and have been waiting for another CBL blacklist. It happened again yesterday and I have the logs and I am not sure what I am looking for. I can see that the only traffic is through our mail server. We couldn't find any infection on that machine, but I know that doesn't mean anything. I just want to be able to confirm that this machine is the problem before going doing the work to get it offline. Would someone be able to check my logs for me? :)</p></div><div id="question-tags" class="tags-container tags">trojan logs wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '14, 15:55</strong></p><img src="https://secure.gravatar.com/avatar/5517a5df1334938a5792a6fc84526f89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alisononthego&#39;s gravatar image" /><p>Alisononthego<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alisononthego has no accepted answers">0%</span></p></div></div><div id="comments-container-36182" class="comments-container"></div><div id="comment-tools-36182" class="comment-tools"></div><div class="clear"></div><div id="comment-36182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36183"></span>

<div id="answer-container-36183" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36183-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Handing out captures with email conversations in the packets is something you should be careful about. What you should be able to to is to look at the conversations on TCP port 25 and check who is sending mail to which recipients. Maybe there's something that doesn't look right, e.g. strange senders, subjects, etc.</p><p>You can use the "Follow TCP Stream" popup menu option on the conversations to get a ASCII dump of the payload, which makes it easier to read.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '14, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36183" class="comments-container"><span id="36184"></span><div id="comment-36184" class="comment"><div id="post-36184-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the tip.</p><p>The blacklist is for the external IP of our network x.x.x.68. We only have the one and we have been given 8 other IPs in the same range that I have setup as aliases on our firewall x.x.x.96 -x.x.x.103. The mail server uses one of them x.x.x.100, but that isn't the IP that is blacklisted. I'm not that familiar will how all this works, but I naturally assume that all the traffic from us to the outside world looks like its coming from that external address anyway?</p><p>In the logs all I can see is traffic to and from the internal and external IP address of the mail server. The blacklist noted that the last detection was at 12.30pm yesterday give or take 30mins. So I have 3 x 10mb logs that cover that period. Wireshark has used color coding in some lines. I have the default color rules in place, is there a particular color I should look for and then follow that stream?</p></div><div id="comment-36184-info" class="comment-info"><span class="comment-age">(10 Sep '14, 16:58)</span> Alisononthego</div></div><span id="36185"></span><div id="comment-36185" class="comment"><div id="post-36185-score" class="comment-score"></div><div class="comment-text"><p>I converted your answer to a comment.</p><p>Wireshark does not color code for SMTP, but you can easily find those communications by putting the filter "tcp.port==25" into the filter box above the packet list. It may also help to only look at the communication from the IP address that has been blacklisted. You can filter that by entering "ip.addr=x.x.x.68" to see what it does.</p><p>If you know that SMTP from that address is the reason for the blacklisting you can combine the two filters into "ip.addr==x.x.x.68 and tcp.port==25" to filter out anything not related. If you do that and have 0 packets left you probably didn't capture at the correct spot. If you have packets, the next step is to examine them for stuff that looks odd (which, I admit, is easier said than done because it requires experience in spotting odd stuff).</p><p>P.S: it's 2 am in Germany right now, so I need some sleep - if your problem still exists tomorrow we can see if I can take a look at what you got.</p></div><div id="comment-36185-info" class="comment-info"><span class="comment-age">(10 Sep '14, 17:07)</span> Jasper ♦♦</div></div><span id="36186"></span><div id="comment-36186" class="comment"><div id="post-36186-score" class="comment-score"></div><div class="comment-text"><p>Thankyou for fixing my post, I am new here :) The external IP never appears, maybe because the logging is done inside the network, not sure. My capture filter was for TCP port 25, but as you suggested I filtered the saved log for tcp.port==25 and there is color coding. It has coded some lines black with pink writing. I think the error is [TCP Fast Retransmission]. Could this be the spam traffic? Thanks for your help. Hopefully I will solve in the next 24 hours. I am using a smart host to get our mail out, so it isn't that urgent, but its one of those things that has been hard to work out!</p></div><div id="comment-36186-info" class="comment-info"><span class="comment-age">(10 Sep '14, 17:26)</span> Alisononthego</div></div><span id="36194"></span><div id="comment-36194" class="comment"><div id="post-36194-score" class="comment-score"></div><div class="comment-text"><p>No problem ;-)</p><p>Retransmissions (or any TCP message) are not relevant to SPAM, as those messages only indicate symptoms on the TCP (transport) layer, not the actual content.</p><p>Where was the capture taken? It would be best if you could do a capture on the "outside" of the router where the public IP addresses are used, because otherwise you can't really tell what internal (usually private) address is going to be which public IP.</p></div><div id="comment-36194-info" class="comment-info"><span class="comment-age">(11 Sep '14, 02:00)</span> Jasper ♦♦</div></div></div><div id="comment-tools-36183" class="comment-tools"></div><div class="clear"></div><div id="comment-36183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

