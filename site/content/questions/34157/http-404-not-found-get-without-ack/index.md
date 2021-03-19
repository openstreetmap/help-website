+++
type = "question"
title = "HTTP 404 not found, GET without ACK"
description = '''Hi, I have a packet capture taken on a proxy server. The first packet is GET http://serveurl send from the client towards proxy. Then immediatly after that packet i get HTTP/1.1 404 not found. Then the client ACK&#x27;s this HTTP not found packet. Should the normal sequence not be: CLIENT: HTTP GET SERVE...'''
date = "2014-06-25T02:50:00Z"
lastmod = "2014-06-25T05:05:00Z"
weight = 34157
keywords = [ "http", "analysis" ]
aliases = [ "/questions/34157" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP 404 not found, GET without ACK](/questions/34157/http-404-not-found-get-without-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34157-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a packet capture taken on a proxy server.<br />
The first packet is GET <a href="http://serveurl">http://serveurl</a> send from the client towards proxy. Then immediatly after that packet i get HTTP/1.1 404 not found. Then the client ACK's this HTTP not found packet.</p><p>Should the normal sequence not be:</p><pre><code>CLIENT: HTTP GET
SERVER: TCP-ACK
SERVER: HTTP NOT FOUND
CLIENT TCP-ACK</code></pre><p>It seems like i am missing an ACK packet. And maybe this is why i get an HTTP not found?</p><p>Or am i mistaken?</p></div><div id="question-tags" class="tags-container tags">http analysis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '14, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/4e4fe7d1f0efa24d139041750ac07c76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Herbaliser&#39;s gravatar image" /><p>Herbaliser<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Herbaliser has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jun '14, 03:00</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-34157" class="comments-container"><span id="34159"></span><div id="comment-34159" class="comment"><div id="post-34159-score" class="comment-score"></div><div class="comment-text"><p>Does received HTTP/1.1 404 packet is part of same session.The 404 or Not Found error message is a HTTP standard response code indicating that the client was able to communicate with a given server, but the server could not find what was requested.Would be easier to answer if you share the capture.</p></div><div id="comment-34159-info" class="comment-info"><span class="comment-age">(25 Jun '14, 02:58)</span> kishan pandey</div></div><span id="34160"></span><div id="comment-34160" class="comment"><div id="post-34160-score" class="comment-score"></div><div class="comment-text"><p>Capture can be found at: <a href="https://onedrive.live.com/?cid=0eb9c351ad3f72d5&amp;id=EB9C351AD3F72D5%21103&amp;ithint=folder,.cap&amp;authkey=!AFwAd1Uj4eQsg48">https://onedrive.live.com/?cid=0eb9c351ad3f72d5&amp;id=EB9C351AD3F72D5%21103&amp;ithint=folder,.cap&amp;authkey=!AFwAd1Uj4eQsg48</a></p></div><div id="comment-34160-info" class="comment-info"><span class="comment-age">(25 Jun '14, 03:30)</span> Herbaliser</div></div><span id="34161"></span><div id="comment-34161" class="comment"><div id="post-34161-score" class="comment-score"></div><div class="comment-text"><p>Hi,everything looks fine here,Generally, a Not Found status error (usually a 404 HTTP status code) is returned when we attempts to visit a page that doesn’t exist—either because you deleted or renamed it without redirecting the old URL to a new page, or because of a typo mistake in a link.</p></div><div id="comment-34161-info" class="comment-info"><span class="comment-age">(25 Jun '14, 05:00)</span> kishan pandey</div></div></div><div id="comment-tools-34157" class="comment-tools"></div><div class="clear"></div><div id="comment-34157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34162"></span>

<div id="answer-container-34162" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34162-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, you're not missing an ACK. In TCP, it is not necessary to have an ACK for every data packet. In this case, there is an ACK in the Not Found packet.</p><p>You're getting Not Found simply because the page was not found, not because of a missing ACK.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '14, 05:05</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-34162" class="comments-container"></div><div id="comment-tools-34162" class="comment-tools"></div><div class="clear"></div><div id="comment-34162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

