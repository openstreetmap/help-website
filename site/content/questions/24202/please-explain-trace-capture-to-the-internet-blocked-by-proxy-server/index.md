+++
type = "question"
title = "Please explain: Trace capture to the internet blocked by Proxy Server"
description = '''Hi Everyone, I captured a trace of my network connection to the internet. I noticed there were a lot of reset packets being sent by the internet server - which was not surprising as my internet browser was not configured with my proxy address settings. Now, my question is this: If I required access ...'''
date = "2013-08-30T09:21:00Z"
lastmod = "2013-08-30T10:57:00Z"
weight = 24202
keywords = [ "proxy-server", "reset", "packets" ]
aliases = [ "/questions/24202" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Please explain: Trace capture to the internet blocked by Proxy Server](/questions/24202/please-explain-trace-capture-to-the-internet-blocked-by-proxy-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24202-score" class="post-score" title="current number of votes">0</div><span id="post-24202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Everyone,</p><p>I captured a trace of my network connection to the internet. I noticed there were a lot of reset packets being sent by the internet server - which was not surprising as my internet browser was not configured with my proxy address settings.</p><p>Now, my question is this: If I required access to the proxy server to browse, how come what was being displayed in Wireshark were the Ip addresses of the various internet servers I was trying to connect to? I thought that since the proxy server was blocking access, I should have seen it sending the TCP rest packers.</p><p>Could some one please put me explain this to me?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-proxy-server" rel="tag" title="see questions tagged &#39;proxy-server&#39;">proxy-server</span> <span class="post-tag tag-link-reset" rel="tag" title="see questions tagged &#39;reset&#39;">reset</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '13, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/94f27085e7e89c7c4bb3ea7a7deacb6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pontish&#39;s gravatar image" /><p><span>pontish</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pontish has no accepted answers">0%</span></p></div></div><div id="comments-container-24202" class="comments-container"></div><div id="comment-tools-24202" class="comment-tools"></div><div class="clear"></div><div id="comment-24202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24205"></span>

<div id="answer-container-24205" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24205-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24205-score" class="post-score" title="current number of votes">0</div><span id="post-24205-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It probably is your firewall sending the resets, but spoofing the address of the web server you're trying to reach. TCP is connection-oriented. The reset must come from the IP address that the client was trying to reach, otherwise the client has no way of knowing what the reset is in response to.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '13, 09:49</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-24205" class="comments-container"><span id="24208"></span><div id="comment-24208" class="comment"><div id="post-24208-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Sorry but one last question: is there any way to know for sure that it is the firewall spoofing the address of the website.</p><p>many thanks.</p></div><div id="comment-24208-info" class="comment-info"><span class="comment-age">(30 Aug '13, 10:48)</span> <span class="comment-user userinfo">pontish</span></div></div><span id="24209"></span><div id="comment-24209" class="comment"><div id="post-24209-score" class="comment-score"></div><div class="comment-text"><p>Capture on both sides of the firewall. If the traffic appears only on the inside, then the firewall replied on behalf of the web server. If the traffic appears on both sides of the firewall, then the traffic was passed on by the firewall and the reply came from some other device.</p></div><div id="comment-24209-info" class="comment-info"><span class="comment-age">(30 Aug '13, 10:57)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-24205" class="comment-tools"></div><div class="clear"></div><div id="comment-24205-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

