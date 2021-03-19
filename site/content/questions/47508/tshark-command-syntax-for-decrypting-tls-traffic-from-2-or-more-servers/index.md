+++
type = "question"
title = "tshark: command syntax for decrypting TLS traffic from 2 or more servers"
description = '''Hi everyone, I&#x27;m able to correctly decrypt the TLS traffic from one server by specifying the command option: -o ssl.keys_list:192.168.10.1,1200,tpkt,&quot;server-key1.pem&quot;  Now I need to simultaneously decrypt also the communication with another server. I made a few tries, but I can&#x27;t guess the correct s...'''
date = "2015-11-11T03:45:00Z"
lastmod = "2015-11-11T04:09:00Z"
weight = 47508
keywords = [ "tls", "decryption", "tshark", "options" ]
aliases = [ "/questions/47508" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark: command syntax for decrypting TLS traffic from 2 or more servers](/questions/47508/tshark-command-syntax-for-decrypting-tls-traffic-from-2-or-more-servers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47508-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I'm able to correctly decrypt the TLS traffic from one server by specifying the command option:</p><pre><code>-o ssl.keys_list:192.168.10.1,1200,tpkt,&quot;server-key1.pem&quot;</code></pre><p>Now I need to simultaneously decrypt also the communication with another server. I made a few tries, but I can't guess the correct syntax for doing this. Using:</p><pre><code>-o ssl.keys_list:192.168.10.1,1200,tpkt,&quot;server-key1.pem&quot; -o ssl.keys_list:192.168.10.2,1200,tpkt,&quot;server-key2.pem&quot;</code></pre><p>the second command option overwrite the first one, so I'm able to decrypt only the traffic from the second server.</p><p>Does anyone knows the right syntax?</p></div><div id="question-tags" class="tags-container tags">tls decryption tshark options</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '15, 03:45</strong></p><img src="https://secure.gravatar.com/avatar/eca830854093757dbe9847c9d44241b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="theo66&#39;s gravatar image" /><p>theo66<br />
<span class="score" title="91 reputation points">91</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="theo66 has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Nov '15, 03:46</p></div></div><div id="comments-container-47508" class="comments-container"></div><div id="comment-tools-47508" class="comment-tools"></div><div class="clear"></div><div id="comment-47508-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47509"></span>

<div id="answer-container-47509" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47509-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Solution found!</p><pre><code>-o &quot;ssl.keys_list:192.168.10.1,1200,tpkt,server-key1.pem;192.168.10.2,1200,tpkt,server-key2.pem&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '15, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/eca830854093757dbe9847c9d44241b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="theo66&#39;s gravatar image" /><p>theo66<br />
<span class="score" title="91 reputation points">91</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="theo66 has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Nov '15, 04:22</p></div></div><div id="comments-container-47509" class="comments-container"></div><div id="comment-tools-47509" class="comment-tools"></div><div class="clear"></div><div id="comment-47509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

