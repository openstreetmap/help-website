+++
type = "question"
title = "1.12.0 does not show me https"
description = '''Hello Dear Wireshark Technicians and skilled users of Wireshark I want to ask you on here , what is up with not seeing https in the new version 1.12.0 ? I am by any means no expert. I was instructed how I can check on my DNS if it is constantly encrypted. Wireshark version 1.10.8 did show me alwys h...'''
date = "2014-09-01T09:34:00Z"
lastmod = "2014-09-01T15:25:00Z"
weight = 35913
keywords = [ "display", "https", "no" ]
aliases = [ "/questions/35913" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [1.12.0 does not show me https](/questions/35913/1120-does-not-show-me-https)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35913-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>Dear Wireshark Technicians and skilled users of Wireshark</p><p>I want to ask you on here , what is up with not seeing https in the new version 1.12.0 ? I am by any means no expert. I was instructed how I can check on my DNS if it is constantly encrypted. Wireshark version 1.10.8 did show me alwys https , everytime I enabled the DNS to be encrypted. I really want to reinstall this 1.12.0 , but before I do I want to ask you on here what the hell ..ah I start get frustrated sorry, everytime something not working or some changes that one must spend more life time. All I see is this:</p><p>60 who has .....(light pink background)</p><p>HTTP 496 [TCP Retransmission] HTTP/1.1 200 ok (black backgroung,red writing)</p><p>TCP 60 443 49363 [RST] (darkred background, yellow writing)</p><p>TLSV1 91 Encrypted Alert (Light gray background, black writing) this appears like only 2 times out of this crazy long list.</p><p>This was not like before. What happened here. according to this my DNS is not encrypted or what? Encryption is turned on. I am running this on Win7. Can someone reply with some decent Information pleace why the new Version of Wireshark 1.12.0 do this? I really do not want update nothing anymore.I know what i am going to do , but please I think I want to ask here before I do what I have in mind.</p><p>Thank you ! I appreciate your help!</p></div><div id="question-tags" class="tags-container tags">display https no</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '14, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/475cfe7efcc4240e887592a67757b2c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="httpsnotshown1120&#39;s gravatar image" /><p>httpsnotshow...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="httpsnotshown1120 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Sep '14, 09:37</p></div></div><div id="comments-container-35913" class="comments-container"></div><div id="comment-tools-35913" class="comment-tools"></div><div class="clear"></div><div id="comment-35913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35917"></span>

<div id="answer-container-35917" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35917-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>We'd have to see a sample capture to see what's happening, but if Wireshark says "HTTP 496 [TCP Retransmission] HTTP/1.1 200 ok", then either that traffic was <em>NOT</em> https (i.e., it was HTTP-directly-over-TCP, not HTTP-over-SSL/TLS-over-TCP), or it was un-encrypted SSL/TLS, or Wireshark had been configured to decrypt the traffic and was doing so.</p><p>I.e., either it wasn't encrypted, or Wireshark was decrypting it. In that packet, either there's an SSL/TLS layer, in which case it was over SSL/TLS but was either not encrypted or was being decrypted by Wireshark, or there's no SSL/TLS layer, in which case it wasn't even going over SSL/TLS. If it was encrypted and was being decrypted by Wireshark, the hex dump pane should, I think, have both a tab showing the encrypted data and another tab showing the decrypted data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Sep '14, 15:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Sep '14, 15:27</p></div></div><div id="comments-container-35917" class="comments-container"></div><div id="comment-tools-35917" class="comment-tools"></div><div class="clear"></div><div id="comment-35917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

