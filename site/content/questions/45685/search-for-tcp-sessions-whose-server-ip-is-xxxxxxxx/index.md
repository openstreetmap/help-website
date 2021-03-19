+++
type = "question"
title = "Search for TCP sessions whose server IP is xx.xx.xx.xx"
description = '''Wonder if there is a way to search for TCP sessions whose tcp server IP is xx.xx.xx.xx. Can&#x27;t find a capture filter (BPF) nor display filter to do this. Any ideas? Thanks.'''
date = "2015-09-07T20:42:00Z"
lastmod = "2015-09-08T07:20:00Z"
weight = 45685
keywords = [ "wireshark" ]
aliases = [ "/questions/45685" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Search for TCP sessions whose server IP is xx.xx.xx.xx](/questions/45685/search-for-tcp-sessions-whose-server-ip-is-xxxxxxxx)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45685-score" class="post-score" title="current number of votes">0</div><span id="post-45685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wonder if there is a way to search for TCP sessions whose tcp <strong>server</strong> IP is xx.xx.xx.xx. Can't find a capture filter (BPF) nor display filter to do this. Any ideas? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '15, 20:42</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-45685" class="comments-container"></div><div id="comment-tools-45685" class="comment-tools"></div><div class="clear"></div><div id="comment-45685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45689"></span>

<div id="answer-container-45689" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45689-score" class="post-score" title="current number of votes">1</div><span id="post-45689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Wonder if there is a way to search for TCP sessions whose tcp <strong>server</strong> IP is xx.xx.xx.xx.</p></blockquote><p>There is nothing in the TCP layer that indicates what's a "server" and what's a "client", except <em>maybe</em> the initial handshake <em>if</em> the client initiates the connection (which is the usual case, although there can be protocols where the connection is initiated by the server, for example in response to traffic in another protocol as with some FTP data connections).</p><p>However, that would require that the initial handshake be captured <em>and</em> that its information is made available to the filter, which is not the case for capture filters or display filters.</p><p>So it'd have to be based either on identifying the server by TCP port number, for protocols with a registered or well-known port number, such as 80 for HTTP or 443 for HTTP-over-SSL, or on somehow identifying the server and client for some <em>particular</em> protocol based on the packet data for that protocol. In either case, there's no general protocol-independent solution; you can't say "show me all sessions whose server is xx.xx.xx.xx", you could only say, for some particular protocol, "show me all protocol XXX sessions whose server is xx.xx.xx.xx".</p><p>So:</p><blockquote><p>Can't find a capture filter (BPF)</p></blockquote><p>...you'd have to either:</p><ul><li>Search for specific services by port, where traffic to the server goes to that port and traffic from that server comes from that port, so you could do something such as <code>(src host xx.xx.xx.xx and src port 80) or (dst host xx.xx.xx.xx and dst port 80)</code></li></ul><p>or</p><ul><li>Somehow identify the protocol and the server vs. client direction based on something in the packet *data)</li></ul><blockquote><p>nor display filter to do this.</p></blockquote><p>...you'd either have to do something based on the port number, similar to what was suggested in the first example for capture filters, or based on fields in the protocol(s) running on top of TCP, as dissected by Wireshark, which is similar in concept to the second example for capture filters, but possibly easier <em>if</em> Wireshark dissects that particular protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '15, 22:28</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-45689" class="comments-container"><span id="45700"></span><div id="comment-45700" class="comment"><div id="post-45700-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the explanation and work-arounds. They work in some cases.</p></div><div id="comment-45700-info" class="comment-info"><span class="comment-age">(08 Sep '15, 07:20)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-45689" class="comment-tools"></div><div class="clear"></div><div id="comment-45689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

