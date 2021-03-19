+++
type = "question"
title = "Howto find port blocking"
description = '''There is an application which is trying to talk to a host on a particular port and I want to see if that port is getting blocked .. I have the wireshark captures but unable to find out which error to look for. Can you please advice ?'''
date = "2016-08-05T04:52:00Z"
lastmod = "2016-08-13T22:04:00Z"
weight = 54610
keywords = [ "block", "port", "trace" ]
aliases = [ "/questions/54610" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Howto find port blocking](/questions/54610/howto-find-port-blocking)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54610-score" class="post-score" title="current number of votes">0</div><span id="post-54610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>There is an application which is trying to talk to a host on a particular port and I want to see if that port is getting blocked .. I have the wireshark captures but unable to find out which error to look for.</p><p>Can you please advice ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-block" rel="tag" title="see questions tagged &#39;block&#39;">block</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-trace" rel="tag" title="see questions tagged &#39;trace&#39;">trace</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '16, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/5b265b748da73e4d2cb64baaeb86b61a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gurushant&#39;s gravatar image" /><p><span>Gurushant</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gurushant has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Aug '16, 07:09</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-54610" class="comments-container"><span id="54614"></span><div id="comment-54614" class="comment"><div id="post-54614-score" class="comment-score"></div><div class="comment-text"><p>That totally depends on where these captures were made, on which interfaces it was done.</p></div><div id="comment-54614-info" class="comment-info"><span class="comment-age">(05 Aug '16, 07:09)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="54616"></span><div id="comment-54616" class="comment"><div id="post-54616-score" class="comment-score"></div><div class="comment-text"><p>These traces were ran on a windows server where we have the config server application hosted which acts as a server and other application which is a client is trying to access the main application through the port. So we ran traces to identify the traffic that is coming into the server and want to identify if the port is getting blocked at any point of time ? Can you let us know how we identify this within the trace results ?</p><p>Thank you !</p></div><div id="comment-54616-info" class="comment-info"><span class="comment-age">(05 Aug '16, 08:34)</span> <span class="comment-user userinfo">Gurushant</span></div></div><span id="54701"></span><div id="comment-54701" class="comment"><div id="post-54701-score" class="comment-score"></div><div class="comment-text"><p>Trace from the client and you will be able to see [SYN], [RST] patterns as long as the server itself is rejecting (No App listening etc): If there is a Firewall, you may not see anything except retransmissions going to nowhere. Trace on the server and you probably wont see anything unless there is software blocking the port up the stack somewhere. But you can see that with netstat or tcpview. Not entirely 100% sure if you mean the client software is also running on the server or if it is a separate computer.</p></div><div id="comment-54701-info" class="comment-info"><span class="comment-age">(09 Aug '16, 06:15)</span> <span class="comment-user userinfo">DarrenWright</span></div></div></div><div id="comment-tools-54610" class="comment-tools"></div><div class="clear"></div><div id="comment-54610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54787"></span>

<div id="answer-container-54787" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54787-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54787-score" class="post-score" title="current number of votes">0</div><span id="post-54787-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Depending on the security appliances on the remote site (firewall, proxy server, switch/router ACL's, etc) you will see one of the following symptoms in the 3-way handshake:</p><p>1) TCP SYN packets going out, but no TCP SYN ACK replies</p><p>2) TCP SYN packets going out, but with a TCP SYN RST reply</p><p>Item 1) above could also be due to an inability to find a return route as well, thus not just symptomatic of a blocked port.</p><p>FWIW</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '16, 22:04</strong></p><img src="https://secure.gravatar.com/avatar/6c8f0de8cb4ef9ad7093eefe24030e4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbenton&#39;s gravatar image" /><p><span>wbenton</span><br />
<span class="score" title="29 reputation points">29</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbenton has no accepted answers">0%</span></p></div></div><div id="comments-container-54787" class="comments-container"></div><div id="comment-tools-54787" class="comment-tools"></div><div class="clear"></div><div id="comment-54787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

