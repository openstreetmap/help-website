+++
type = "question"
title = "No [SYN, ACK] from some web sites"
description = '''I’ve set up a lone server connected via LAN to a router. It used to work fine, but something happened and messed up my Network settings. Now after re-setting up the lan connection to the gateway I can only open some sites from the server. The sites I can’t open - I get using the Wireshark software t...'''
date = "2012-05-17T05:11:00Z"
lastmod = "2012-05-17T14:26:00Z"
weight = 11099
keywords = [ "ack", "respons", "syn", "no" ]
aliases = [ "/questions/11099" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [No \[SYN, ACK\] from some web sites](/questions/11099/no-syn-ack-from-some-web-sites)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11099-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I’ve set up a lone server connected via LAN to a router. It used to work fine, but something happened and messed up my Network settings.</p><p>Now after re-setting up the lan connection to the gateway <strong>I can only open some sites</strong> from the server. The sites I can’t open - I get using the Wireshark software this message: 4679 6697.004581 10.0.0.5 50.96.125.67 TCP 66 descent &gt; http [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=4 SACK_PERM=1 Which goes out 3 times and then nothing; my explorer just fails to open the page. So 3 times it sends the [SYN] and do not get a reply [SYN, ACK]. Can anyone give me some help? Please?</p></div><div id="question-tags" class="tags-container tags">ack respons syn no</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '12, 05:11</strong></p><img src="https://secure.gravatar.com/avatar/8e9b0eefeef2f2dc1b2bb5c73b425456?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JosephW&#39;s gravatar image" /><p>JosephW<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JosephW has no accepted answers">0%</span></p></div></div><div id="comments-container-11099" class="comments-container"></div><div id="comment-tools-11099" class="comment-tools"></div><div class="clear"></div><div id="comment-11099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11106"></span>

<div id="answer-container-11106" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11106-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Can you ping the remote 50.96.125.67 host? What happens if you telnet to port 80 on 50.96.125.67? Can you get to any other internet hosts from this system?</p><p>First thing to do: check your firewall settings &amp; confirm source/destination rules permit this traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '12, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/d1f7fabf169915dc5ba93025794b84db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Labnuke&#39;s gravatar image" /><p>Labnuke<br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Labnuke has no accepted answers">0%</span></p></div></div><div id="comments-container-11106" class="comments-container"><span id="11109"></span><div id="comment-11109" class="comment"><div id="post-11109-score" class="comment-score"></div><div class="comment-text"><p>Thank you Labnuke for helping. Both pinging and telnet fails to all external sites, but I can ping and connect normally to the router 10.0.0.2. The strange thing is that I can connect to some sites out there through the web browser.</p></div><div id="comment-11109-info" class="comment-info"><span class="comment-age">(17 May '12, 11:10)</span> JosephW</div></div><span id="11111"></span><div id="comment-11111" class="comment"><div id="post-11111-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", that makes it easier for people to follow the discussion, please see the FAQ)</p><p>Then maybe your browser is using a proxy server and your router/FW is configured to not allow direct access to the Internet? Sounds like you are on a network controlled by someone else and the security policy has been tightened...</p></div><div id="comment-11111-info" class="comment-info"><span class="comment-age">(17 May '12, 11:17)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-11106" class="comment-tools"></div><div class="clear"></div><div id="comment-11106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11117"></span>

<div id="answer-container-11117" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11117-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, I can neither connect to 50.96.125.67 on port 80 nor can I ping it. So, the host might just be down, filtered by a packetfilter, or the whole net is not reachable right now. So, it's probably not your environment (local firewall) but the remote host, which possibly explains why you can connect to other hosts.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '12, 14:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-11117" class="comments-container"><span id="11125"></span><div id="comment-11125" class="comment"><div id="post-11125-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt, That was just a random IP; the problem is consistent (no reply) to all external ips (both with pining and telnet), BUT I can get through to some sites through my browser and I did clear my local web copies. So - some (few) sites work and most not and none with pining or telnet. I thought this would be a brainteaser even for you fundies. Joe</p></div><div id="comment-11125-info" class="comment-info"><span class="comment-age">(17 May '12, 23:36)</span> JosephW</div></div><span id="11126"></span><div id="comment-11126" class="comment"><div id="post-11126-score" class="comment-score"></div><div class="comment-text"><p>(Joseph, please use "add comment" instead of "your answer" to respond to to a given answer. I converted your answer to a comment again)</p></div><div id="comment-11126-info" class="comment-info"><span class="comment-age">(17 May '12, 23:50)</span> SYN-bit ♦♦</div></div><span id="11127"></span><div id="comment-11127" class="comment"><div id="post-11127-score" class="comment-score"></div><div class="comment-text"><p>Did you check the comment of SYN-bit (Proxies, Firewalls, etc.)?</p></div><div id="comment-11127-info" class="comment-info"><span class="comment-age">(18 May '12, 01:42)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11117" class="comment-tools"></div><div class="clear"></div><div id="comment-11117-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

