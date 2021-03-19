+++
type = "question"
title = "Using dumpcap without installing Wireshark"
description = '''I learned here about the utility DumpCap to get the right ip on which Wireshark is actually captures(the syntax is DumpCap -D -M, thanks Kurt). I want to deploy it inside my open source application but if there is a better alternative I&#x27;d be very happy, since it demands to deploy all the dll&#x27;s that ...'''
date = "2012-08-06T01:04:00Z"
lastmod = "2012-08-07T12:14:00Z"
weight = 13381
keywords = [ "dumpcap", "wireshark" ]
aliases = [ "/questions/13381" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using dumpcap without installing Wireshark](/questions/13381/using-dumpcap-without-installing-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13381-score" class="post-score" title="current number of votes">0</div><span id="post-13381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I learned here about the utility DumpCap to get the right ip on which Wireshark is actually captures(the syntax is DumpCap -D -M, thanks Kurt). I want to deploy it inside my open source application but if there is a better alternative I'd be very happy, since it demands to deploy all the dll's that come with Wireshark(Wireshark itself is not deployed but WinPcap does) Can someone direct me regarding and alternative? Thanks in advance I. Lesher</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '12, 01:04</strong></p><img src="https://secure.gravatar.com/avatar/c46b9d0cf13adb17325f5d9519406546?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="triplebit&#39;s gravatar image" /><p><span>triplebit</span><br />
<span class="score" title="1 reputation points">1</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="triplebit has no accepted answers">0%</span></p></div></div><div id="comments-container-13381" class="comments-container"><span id="13390"></span><div id="comment-13390" class="comment"><div id="post-13390-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I want to deploy it inside my open source application</p></blockquote><p>do you want to capture packets in your application or just let it print the IP addresses (dumpcap -D -M)?</p></div><div id="comment-13390-info" class="comment-info"><span class="comment-age">(06 Aug '12, 05:49)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="13435"></span><div id="comment-13435" class="comment"><div id="post-13435-score" class="comment-score"></div><div class="comment-text"><p>Thanks Mr. Kurt I want it just to print the IP addresses. Regards I. Lesher</p></div><div id="comment-13435-info" class="comment-info"><span class="comment-age">(07 Aug '12, 11:09)</span> <span class="comment-user userinfo">triplebit</span></div></div><span id="13439"></span><div id="comment-13439" class="comment"><div id="post-13439-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I want it just to print the IP addresses</p></blockquote><p>then running one of these commands would be the easiest way:</p><blockquote><p><code>ipconfig /all | find "address"</code><br />
<code>netsh interface dump | find "address="</code></p></blockquote><p>Available on all windows systems &gt;= WinXP, no need to install any libraries.</p><p>Then parse the output to extract the ip addresses.</p></div><div id="comment-13439-info" class="comment-info"><span class="comment-age">(07 Aug '12, 12:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-13381" class="comment-tools"></div><div class="clear"></div><div id="comment-13381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13437"></span>

<div id="answer-container-13437" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13437-score" class="post-score" title="current number of votes">0</div><span id="post-13437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Then the "better alternative" might be to just use, in your application, the same WinPcap calls that dumpcap uses (I say "WinPcap" because you say "dll's" rather than "shared libraries" or "so's" or ".so's", so you're presumably doing this on Windows).</p><p>The call is <code>pcap_findalldevs()</code>, and it returns a list of network interfaces and, for each interface, the list of IPv4 and IPv6 addresses for the interface; here's <a href="http://www.winpcap.org/docs/docs_412/html/group__wpcapfunc.html#ga7b128eaeef627b408f6a6e2a2f5eb45d">the WinPcap documentation for it</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '12, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></p></div></div><div id="comments-container-13437" class="comments-container"></div><div id="comment-tools-13437" class="comment-tools"></div><div class="clear"></div><div id="comment-13437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

