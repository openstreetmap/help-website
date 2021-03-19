+++
type = "question"
title = "Addresses and ports"
description = '''This is probably been asked, but I cannot find it. I am looking to move an application servers from on-prem to AWS. I am trying to determine all the IP addresses and on what ports that are hitting this server so I can setup our firewalls and the security groups accordingly. I need to run a survey fo...'''
date = "2017-06-08T05:49:00Z"
lastmod = "2017-06-08T06:09:00Z"
weight = 61865
keywords = [ "capture", "endpoints", "survey" ]
aliases = [ "/questions/61865" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Addresses and ports](/questions/61865/addresses-and-ports)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61865-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is probably been asked, but I cannot find it. I am looking to move an application servers from on-prem to AWS. I am trying to determine all the IP addresses and on what ports that are hitting this server so I can setup our firewalls and the security groups accordingly. I need to run a survey for about 24 hours to get a good idea of all the endpoints and ports.</p><p>I have tried setting the capture settings to only capture 64b of data and recreate a new file every 10 minutes. When Wireshark does not crash after about 2 hours, it is generating a lot of files and using a chunk of disk space. It is also going to be something of a pain to analyze. Does anyone have a better way of doing this?</p></div><div id="question-tags" class="tags-container tags">capture endpoints survey</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '17, 05:49</strong></p><img src="https://secure.gravatar.com/avatar/42bc00954fde59d9064398e6da0d6a75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NDanger69&#39;s gravatar image" /><p>NDanger69<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NDanger69 has no accepted answers">0%</span></p></div></div><div id="comments-container-61865" class="comments-container"></div><div id="comment-tools-61865" class="comment-tools"></div><div class="clear"></div><div id="comment-61865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61866"></span>

<div id="answer-container-61866" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61866-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes. See this blog post I wrote: <a href="https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/</a></p><p>Also, if you're looking at what ports that server is hosting services on, why not run a "netstat" command on the server itself to check which ports are open? Or, if you can't do that, run an <a href="https://nmap.org/">nmap</a> scan against the server IP to see which ports are in service?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '17, 06:09</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jun '17, 06:11</p></div></div><div id="comments-container-61866" class="comments-container"></div><div id="comment-tools-61866" class="comment-tools"></div><div class="clear"></div><div id="comment-61866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

