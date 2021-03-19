+++
type = "question"
title = "Alert (Level: Fatal, Description: Inappropriate Fallback) just for https://www.google.it"
description = '''Hi all, in our offices some users started some weeks ago to complain  about https://www.google.it home page unreachability just with the following conditions :  Connection: WiFi Guest Device: Smartphone/Tablet Android Note: Specific browser Url: Just Google is KO Protocol : TLS V1.1  We manage proxy...'''
date = "2016-08-23T15:01:00Z"
lastmod = "2016-09-19T06:01:00Z"
weight = 55083
keywords = [ "fallback", "inappropriate" ]
aliases = [ "/questions/55083" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Alert (Level: Fatal, Description: Inappropriate Fallback) just for https://www.google.it](/questions/55083/alert-level-fatal-description-inappropriate-fallback-just-for-httpswwwgoogleit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55083-score" class="post-score" title="current number of votes">-1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, in our offices some users started some weeks ago to complain about <a href="https://www.google.it">https://www.google.it</a> home page unreachability just with the following conditions :</p><ul><li>Connection: WiFi Guest</li><li>Device: Smartphone/Tablet Android</li><li>Note: Specific browser</li><li>Url: Just Google is KO</li><li>Protocol : TLS V1.1</li></ul><p>We manage proxy chain to let users reach internet. Capturing traffic, we notice that HQ proxy replies to branch proxy with the message in the subject.</p><p>In the meanwhile that we do other tests, is there something wellknow about this issue ? What does this message found in the capture is telling ?</p><p>The browsing user experience is a message which informs that the connection has been reset.</p><p>Thanks a lot</p></div><div id="question-tags" class="tags-container tags">fallback inappropriate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Aug '16, 15:01</strong></p><img src="https://secure.gravatar.com/avatar/bba638c3a54975c52c98530defa199af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ValerioItaly&#39;s gravatar image" /><p>ValerioItaly<br />
<span class="score" title="5 reputation points">5</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ValerioItaly has no accepted answers">0%</span></p></div></div><div id="comments-container-55083" class="comments-container"><span id="55096"></span><div id="comment-55096" class="comment"><div id="post-55096-score" class="comment-score"></div><div class="comment-text"><p>Update: We have discovered that the main browser that has got this problem (with <a href="https://www.google.it">https://www.google.it</a>) in our case is Google Chrome, and the problem appeares just when the Client SSL Connection is TLS 1.1, with TLS_FALLBACK_SCSV Cipher suite option in the Client Hello request.</p><p>No problem with Firefox (it uses TLS 1.2) or IE (TLS 1.2)</p><p>If the same Chrome decides (I don't know on which basis) to use TLS 1.2 for <a href="https://www.google.it">https://www.google.it</a> the home page is reached. This is done for example using an older version of Chrome (example -&gt; Ver 48).</p><p>So, as far as now, we have the cause of the problem. Now we need to find the cure. :)</p></div><div id="comment-55096-info" class="comment-info"><span class="comment-age">(24 Aug '16, 07:54)</span> ValerioItaly</div></div><span id="55125"></span><div id="comment-55125" class="comment"><div id="post-55125-score" class="comment-score"></div><div class="comment-text"><p>This definitely sounds like the new X25519 cipher which is the cipher Google servers and services are now choosing for TLS as the most preferred to use. And since current Chrome 52 browser supports X25519, it will try to connect with that to Google's servers.</p><p>Browsing internet it seems that Proxy should either support elliptic curve 0x001d, or remove elliptic curves from the Client Hello of the client that it doesn't understand.</p><p>Taking a capture by notebook side on the SAME WiFi Guest architecture (Transparent mode), different PC but same Version 52, it seems that when Chrome decides to speak with TLS V1.1 it has got an extension called Elliptic Curve set as UNKNOWN.</p><p>Moreover if Notebooks that have got the issue with Chrome 52 from WiFi Guest launch the browser disabling several Cipher suites using “ellipting curve”, It works.</p><p>This is the extension we have used to start chrome<br />
--cipher-suite-blacklist=0xc02f,0xc02b,0xcc14,0xcc13,0xc009,0xc013,0xc00a,0xc014</p><p>So this is a confirmation that the problem is this.</p><p>Now we are looking for the cure.</p></div><div id="comment-55125-info" class="comment-info"><span class="comment-age">(26 Aug '16, 05:42)</span> ValerioItaly</div></div></div><div id="comment-tools-55083" class="comment-tools"></div><div class="clear"></div><div id="comment-55083-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55653"></span>

<div id="answer-container-55653" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55653-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Issue solved using DHCP WPad in the WCCP Architecture. This forces the clients to use TLS V1.2.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '16, 06:01</strong></p><img src="https://secure.gravatar.com/avatar/bba638c3a54975c52c98530defa199af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ValerioItaly&#39;s gravatar image" /><p>ValerioItaly<br />
<span class="score" title="5 reputation points">5</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ValerioItaly has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-55653" class="comments-container"></div><div id="comment-tools-55653" class="comment-tools"></div><div class="clear"></div><div id="comment-55653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

