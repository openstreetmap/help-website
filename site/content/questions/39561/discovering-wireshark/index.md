+++
type = "question"
title = "Discovering wireshark"
description = '''Hello guys Since a few weeks, I started using Wireshark, an amazing program.  I discovered some vids on youtube about sniffing etc, so I decided to do some network sniffing on my own network in order to steal my own cookies.  First, I ran 2 browsers on my laptop while capturing my network. On one br...'''
date = "2015-02-02T08:21:00Z"
lastmod = "2015-02-02T08:28:00Z"
weight = 39561
keywords = [ "sniffing", "network" ]
aliases = [ "/questions/39561" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Discovering wireshark](/questions/39561/discovering-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39561-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello guys</p><p>Since a few weeks, I started using Wireshark, an amazing program. I discovered some vids on youtube about sniffing etc, so I decided to do some network sniffing on my own network in order to steal my own cookies.</p><p>First, I ran 2 browsers on my laptop while capturing my network. On one browser, I logged in onto an website (HTTP) ... I saw results as 'GET...' and so on. Here, I could find my cookies and paste them in Firefox using Greasemonkey.</p><p>Now... I ran into a strange thing. I wanted to try this using 2 laptops instead of 2 browsers on 1 laptop. The problem that I encountered is that I didn't receive results such as 'GET...' and so on, but more notifications like 'NOTIFY...'. I looked at different places to find the cookies, but I didn't find it.</p><p>The 2 laptops were connected to the same network, on my laptop, the monitor mode was selected (for my router) and the website did have HTTP.</p><p>Now... Could anyone tell me what I did wrong? Or do I have to give some more information?</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags">sniffing network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '15, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/24aeb6a4a91d04c5a176d4f5302a9224?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Olivierm_&#39;s gravatar image" /><p>Olivierm_<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Olivierm_ has no accepted answers">0%</span></p></div></div><div id="comments-container-39561" class="comments-container"><span id="39563"></span><div id="comment-39563" class="comment"><div id="post-39563-score" class="comment-score"></div><div class="comment-text"><p>How are the laptops connected to the router?</p></div><div id="comment-39563-info" class="comment-info"><span class="comment-age">(02 Feb '15, 08:28)</span> grahamb ♦</div></div><span id="39566"></span><div id="comment-39566" class="comment"><div id="post-39566-score" class="comment-score"></div><div class="comment-text"><p>I used a wireless connection (WPA2 secured)</p></div><div id="comment-39566-info" class="comment-info"><span class="comment-age">(02 Feb '15, 09:02)</span> Olivierm_</div></div><span id="39570"></span><div id="comment-39570" class="comment"><div id="post-39570-score" class="comment-score"></div><div class="comment-text"><p>And what is the OS on the 2 laptops?</p></div><div id="comment-39570-info" class="comment-info"><span class="comment-age">(02 Feb '15, 09:48)</span> grahamb ♦</div></div><span id="39581"></span><div id="comment-39581" class="comment"><div id="post-39581-score" class="comment-score"></div><div class="comment-text"><p>One runs os x yosemite and the other windows 7</p></div><div id="comment-39581-info" class="comment-info"><span class="comment-age">(02 Feb '15, 13:55)</span> Olivierm_</div></div></div><div id="comment-tools-39561" class="comment-tools"></div><div class="clear"></div><div id="comment-39561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39564"></span>

<div id="answer-container-39564" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39564-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>How did you capture? Did you use the second laptop, hoping to capture what the first laptop was doing? If so, you won't get the packets you want unless you configure your network for the capture, e.g. by setting up a SPAN port on a configurable switch.</p><p>See <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a> for more information about capture setups.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '15, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39564" class="comments-container"><span id="39567"></span><div id="comment-39567" class="comment"><div id="post-39567-score" class="comment-score"></div><div class="comment-text"><p>Well indeed, I used my laptop (let's say nr. 1) to capture what laptop nr 2 was doing. So: with laptop nr 2, I logged in on a site in order to see, or discover, the cookies via Wireshark on laptop nr 1.</p></div><div id="comment-39567-info" class="comment-info"><span class="comment-age">(02 Feb '15, 09:06)</span> Olivierm_</div></div><span id="39569"></span><div id="comment-39569" class="comment"><div id="post-39569-score" class="comment-score"></div><div class="comment-text"><p>If you're using wireless, you'll probably not be able to decrypt the packets of the laptop no. 2, unless you have the secret key of the access point and captured the full WiFi connection setup.</p></div><div id="comment-39569-info" class="comment-info"><span class="comment-age">(02 Feb '15, 09:48)</span> Jasper ♦♦</div></div><span id="39583"></span><div id="comment-39583" class="comment"><div id="post-39583-score" class="comment-score"></div><div class="comment-text"><p>I also thought of that, but even when I changed my router into an open network, with no security settings, I didn't see anything... That would be like if I was in a shop with an open network sniffing the network, but did not see the right packets. Or not?</p></div><div id="comment-39583-info" class="comment-info"><span class="comment-age">(02 Feb '15, 13:57)</span> Olivierm_</div></div></div><div id="comment-tools-39564" class="comment-tools"></div><div class="clear"></div><div id="comment-39564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

