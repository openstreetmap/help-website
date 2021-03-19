+++
type = "question"
title = "Can somebody help me with analyzing my capture ipsec/l2tp"
description = '''Hello community, I have setup a zywall firewall which gives me the possibility to connect via L2TP. Our customers connect to this, but we have only one where it is not working. I have already connected via teamviewer to the customer and looked in his VPN settings. All ok. Now I the only possibility ...'''
date = "2015-08-20T01:26:00Z"
lastmod = "2015-08-20T06:24:00Z"
weight = 45260
keywords = [ "analyze", "l2tp", "captured", "ipsec" ]
aliases = [ "/questions/45260" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can somebody help me with analyzing my capture ipsec/l2tp](/questions/45260/can-somebody-help-me-with-analyzing-my-capture-ipsecl2tp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45260-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello community, I have setup a zywall firewall which gives me the possibility to connect via L2TP. Our customers connect to this, but we have only one where it is not working.</p><p>I have already connected via teamviewer to the customer and looked in his VPN settings. All ok.</p><p>Now I the only possibility is now that his router makes some troubles. Therefore I installed Wireshark on his computer and captured the "try" to establish a connection to our router. Following you will find the captured analyze.</p><p>Only what makes me really crazy is, that sometimes he can connect. But only sometimes. When I look on my firewall I see him trying to connect (see Port 500 coming in) - most of the time after Port 500 nothing more. But there should be still Port 1701 and 4500.</p><p>Information about the captured file: My firewall has the ip 61.50.148.122 His client ip address is 192.168.0.132 Okay hopefully somebody can find something in my log, I sadly don`t understand the logfile. For me there is nowhere a failure. But please see below: <a href="http://tempsend.com/B5B4A241DE">Click me for the catpure</a></p><p>Thank you Paul</p></div><div id="question-tags" class="tags-container tags">analyze l2tp captured ipsec</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '15, 01:26</strong></p><img src="https://secure.gravatar.com/avatar/77d2f12c8ee81c2f17229ac4ff2845e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul6552&#39;s gravatar image" /><p>Paul6552<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul6552 has no accepted answers">0%</span></p></div></div><div id="comments-container-45260" class="comments-container"></div><div id="comment-tools-45260" class="comment-tools"></div><div class="clear"></div><div id="comment-45260-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45267"></span>

<div id="answer-container-45267" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45267-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is only the client who runs Windows on Apple having problems?</p><p>ISAKMP phase 2 is not being established. Check the logs on the firewall. It will be easier than decrypting the packet capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '15, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-45267" class="comments-container"><span id="45282"></span><div id="comment-45282" class="comment"><div id="post-45282-score" class="comment-score"></div><div class="comment-text"><p>Hello Roland,</p><p>Here is the log from my firewall: <img src="https://osqa-ask.wireshark.org/upfiles/errorLogin.PNG" alt="alt text" /></p><p>I see only that the Client has send some information and then it is over. I think the Firewall is waiting for something, but when I look in the captured wireshark file on the client side I see that the client is sending all the time things to the firewall but they don`t arrive by the firewall.</p></div><div id="comment-45282-info" class="comment-info"><span class="comment-age">(20 Aug '15, 17:26)</span> Paul6552</div></div><span id="45301"></span><div id="comment-45301" class="comment"><div id="post-45301-score" class="comment-score"></div><div class="comment-text"><p>The screenshot is not helping. Maybe you can turn on a vpn debug on the device.</p></div><div id="comment-45301-info" class="comment-info"><span class="comment-age">(21 Aug '15, 11:30)</span> Roland</div></div></div><div id="comment-tools-45267" class="comment-tools"></div><div class="clear"></div><div id="comment-45267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

