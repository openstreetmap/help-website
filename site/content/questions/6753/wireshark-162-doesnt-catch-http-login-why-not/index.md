+++
type = "question"
title = "Wireshark 1.6.2 doesn&#x27;t catch http: login. Why not?"
description = '''Hi, I&#x27;m trying to catch the packet that contains the data for my home page login. I get the 401 not authorised page and Chrome/IE offer the login box. I put in my username and password but Wireshark doesn&#x27;t seem to catch it. Can anyone explain please?'''
date = "2011-10-06T09:52:00Z"
lastmod = "2011-10-06T15:52:00Z"
weight = 6753
keywords = [ "login" ]
aliases = [ "/questions/6753" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.6.2 doesn't catch http: login. Why not?](/questions/6753/wireshark-162-doesnt-catch-http-login-why-not)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6753-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm trying to catch the packet that contains the data for my home page login. I get the 401 not authorised page and Chrome/IE offer the login box. I put in my username and password but Wireshark doesn't seem to catch it. Can anyone explain please?</p></div><div id="question-tags" class="tags-container tags">login</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '11, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/34ba702965394ab5d7e0b405d437e1e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="turnbui&#39;s gravatar image" /><p>turnbui<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="turnbui has no accepted answers">0%</span></p></div></div><div id="comments-container-6753" class="comments-container"><span id="6754"></span><div id="comment-6754" class="comment"><div id="post-6754-score" class="comment-score"></div><div class="comment-text"><p>How do you know that "Wireshark doesn't seem to catch it"?</p></div><div id="comment-6754-info" class="comment-info"><span class="comment-age">(06 Oct '11, 10:26)</span> Jaap ♦</div></div><span id="6755"></span><div id="comment-6755" class="comment"><div id="post-6755-score" class="comment-score"></div><div class="comment-text"><p>because i can't find a packet with my username/password in it. it isn't https so i expect clear text. also i check the frame number then press login then heck frame umber again only to find there re no new frames.</p></div><div id="comment-6755-info" class="comment-info"><span class="comment-age">(06 Oct '11, 12:54)</span> turnbui</div></div></div><div id="comment-tools-6753" class="comment-tools"></div><div class="clear"></div><div id="comment-6753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6765"></span>

<div id="answer-container-6765" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6765-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The browser has several methods to proof the user's identity. In most cases the credentials are somewhat obfuscated with one of these methods:</p><ul><li>Username and password can be encoded in BASE64. Wireshark can decode the credentials. Use the search function and search for a string in the packet details.</li><li>In a Windows domain you might have Windows integrated authentication. In this configuration the credentials can be send as NTLM hash or even as Kerberos ticket.</li></ul><p>These items are found in the clients HTTP request header.</p><p>Another option is to trigger a Javascript, that obfuscates the username and password before sending it with a POST to the server. From a security perspective this is quite silly.</p><p>Good hunting!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '11, 15:52</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-6765" class="comments-container"><span id="6766"></span><div id="comment-6766" class="comment"><div id="post-6766-score" class="comment-score"></div><div class="comment-text"><p>thanks for the info.</p></div><div id="comment-6766-info" class="comment-info"><span class="comment-age">(06 Oct '11, 23:45)</span> turnbui</div></div></div><div id="comment-tools-6765" class="comment-tools"></div><div class="clear"></div><div id="comment-6765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

