+++
type = "question"
title = "SSL Bad certificate"
description = '''Hi, I have the following capture of an SSL V2.0 connection. https://onedrive.live.com/redir?resid=EB9C351AD3F72D5%21103 The packet capture was taken on proxy server the client returns Alert Level:Fatal, Description Bad Certificate. Can anybody explain to me why, looking at the capture file. Can this...'''
date = "2014-07-29T07:29:00Z"
lastmod = "2014-07-30T01:47:00Z"
weight = 34969
keywords = [ "ssl", "bad", "certificate" ]
aliases = [ "/questions/34969" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Bad certificate](/questions/34969/ssl-bad-certificate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34969-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have the following capture of an SSL V2.0 connection. <a href="https://onedrive.live.com/redir?resid=EB9C351AD3F72D5%21103">https://onedrive.live.com/redir?resid=EB9C351AD3F72D5%21103</a></p><p>The packet capture was taken on proxy server the client returns Alert Level:Fatal, Description Bad Certificate. Can anybody explain to me why, looking at the capture file. Can this be because the CA's are not trusted on the client?</p></div><div id="question-tags" class="tags-container tags">ssl bad certificate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '14, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/4e4fe7d1f0efa24d139041750ac07c76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Herbaliser&#39;s gravatar image" /><p>Herbaliser<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Herbaliser has no accepted answers">0%</span></p></div></div><div id="comments-container-34969" class="comments-container"></div><div id="comment-tools-34969" class="comment-tools"></div><div class="clear"></div><div id="comment-34969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34991"></span>

<div id="answer-container-34991" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34991-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Frame #4: The client sends a CONNECT to the proxy, requesting a TCP connection on port 443 to the <strong>IP address</strong> 193.194.158.88, see also the Host header:</p><blockquote><p>host: 193.194.158.88</p></blockquote><p>Frame #15: The proxy sends the cert of the target server. The subject of the cert is: <strong>*.custo.bvdep.com</strong></p><p>Result: The client complains about an invalid cert due to the mismatch between the subject of the cert (*.custo.bvdep.com) and the Host it was contacting: 193.194.158.88</p><p>There could have been a second reason, which I cannot check, as there is no information about that in the capture file (the capture was taken on the proxy - so the timestamp does not help):</p><p>The clients date/time could be outside of the validity range of the cert, which would trigger the client to complain about an invalid cert as well.</p><p>So, looks 'normal' to me.</p><p>Regards Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '14, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span></p></div></div><div id="comments-container-34991" class="comments-container"></div><div id="comment-tools-34991" class="comment-tools"></div><div class="clear"></div><div id="comment-34991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

