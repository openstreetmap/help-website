+++
type = "question"
title = "Getting The connection has timed out when using asus router"
description = '''Hi everyone I can connect to https://hvid1.azehosting.net:2083 using other network connection; but using my RT-AC87U I get &quot;The connection has timed out&quot;. So I tried to capture the traffic between my pc and the website. Look at picture attached. Do you have an idea to what&#x27;s wrong or what to try to ...'''
date = "2017-03-21T07:10:00Z"
lastmod = "2017-03-21T07:20:00Z"
weight = 60222
keywords = [ "spurious", "timeout", "tcp" ]
aliases = [ "/questions/60222" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting The connection has timed out when using asus router](/questions/60222/getting-the-connection-has-timed-out-when-using-asus-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60222-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone</p><p>I can connect to <a href="https://hvid1.azehosting.net:2083">https://hvid1.azehosting.net:2083</a> using other network connection; but using my RT-AC87U I get "The connection has timed out".</p><p>So I tried to capture the traffic between my pc and the website. Look at picture attached.</p><p>Do you have an idea to what's wrong or what to try to fix the problem?</p><p>I can connect to lots of other site including this site :-) using the same router. <img src="https://osqa-ask.wireshark.org/upfiles/Capture_Ozfjxwy.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">spurious timeout tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '17, 07:10</strong></p><img src="https://secure.gravatar.com/avatar/723d9a1dd30b38b1a459d1d01e14ee03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rgry&#39;s gravatar image" /><p>rgry<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rgry has no accepted answers">0%</span></p></img></div></div><div id="comments-container-60222" class="comments-container"></div><div id="comment-tools-60222" class="comment-tools"></div><div class="clear"></div><div id="comment-60222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60223"></span>

<div id="answer-container-60223" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60223-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The image shows repeated attempts by machine with the IP address 192.1682.135 to open a TCP connection to the IP address 185.121.172.165 (which is the site you mention). The remote end either fails to respond or closes the connection attempt with a RST response.</p><p>Not much more to be said as the capture is likely to be from the machine attempting the connection and thus we have no idea what's happening in the router, is it even attempting to open a connection to the remote site or are the RST's actually coming from the remote site. Capturing on the remote site would show if the connection requests are received there, may be the logs in your router might show some info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '17, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60223" class="comments-container"><span id="60225"></span><div id="comment-60225" class="comment"><div id="post-60225-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer, but I cannot capture at the remote site; not my server. I have ssh access to my router - is there a way to capture on the router? It's running some kind of Linux. Do you know where these logs typically is places or called?</p></div><div id="comment-60225-info" class="comment-info"><span class="comment-age">(21 Mar '17, 07:52)</span> rgry</div></div></div><div id="comment-tools-60223" class="comment-tools"></div><div class="clear"></div><div id="comment-60223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

