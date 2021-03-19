+++
type = "question"
title = "Browser User-Agent"
description = '''Capturing traffic with tcpdump on Linux CentOS 5.7 machine running Apache httpd and analyzing in Wireshark. IE browser user-agent is somethimes captured fine in both the http log and network traffic captured http get request. And sometimes only in the http log. However the BlackBerry 7 (9810 Torch) ...'''
date = "2012-03-02T19:48:00Z"
lastmod = "2012-03-03T08:30:00Z"
weight = 9321
keywords = [ "browser", "blackberry", "user-agent" ]
aliases = [ "/questions/9321" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Browser User-Agent](/questions/9321/browser-user-agent)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9321-score" class="post-score" title="current number of votes">0</div><span id="post-9321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Capturing traffic with tcpdump on Linux CentOS 5.7 machine running Apache httpd and analyzing in Wireshark.</p><p>IE browser user-agent is somethimes captured fine in both the http log and network traffic captured http get request. And sometimes only in the http log.</p><p>However the BlackBerry 7 (9810 Torch) browser 'user-agent' string is captured in http log, <strong>but is never in the network traffic captured http get request.</strong></p><p><strong>Why is the 'user-agent' not in the http get request network traffic capture?</strong></p><p>Thanks</p><p>HTTP Log Entry:</p><p>n.n.n.n - - [02/Mar/2012:19:00:20 -0800] "GET /bbua.html HTTP/1.1" 200 467 "" "Mozilla/5.0 (BlackBerry; U; BlackBerry 9810; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.261 Mobile Safari/534.11+"</p><p>n.n.n.n - - [02/Mar/2012:19:37:07 -0800] "GET /bbua.html HTTP/1.1" 200 467 "-" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.1.4322; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)"</p><p>Network Traffic HTTP Get Capture:</p><p>GET /bbua.html HTTP/1.1 Accept-Language:</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-browser" rel="tag" title="see questions tagged &#39;browser&#39;">browser</span> <span class="post-tag tag-link-blackberry" rel="tag" title="see questions tagged &#39;blackberry&#39;">blackberry</span> <span class="post-tag tag-link-user-agent" rel="tag" title="see questions tagged &#39;user-agent&#39;">user-agent</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '12, 19:48</strong></p><img src="https://secure.gravatar.com/avatar/fb0be57cb38cb228c08b34a06872ee0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NOYB&#39;s gravatar image" /><p><span>NOYB</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NOYB has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Mar '12, 08:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-9321" class="comments-container"><span id="9326"></span><div id="comment-9326" class="comment"><div id="post-9326-score" class="comment-score"></div><div class="comment-text"><p>The proper way to answer your own question, is to do exactly that :-)</p><p>I'll edit your question and put your own answer in a answer for you, so people can lrean from your experience too...</p></div><div id="comment-9326-info" class="comment-info"><span class="comment-age">(03 Mar '12, 08:29)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-9321" class="comment-tools"></div><div class="clear"></div><div id="comment-9321-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9327"></span>

<div id="answer-container-9327" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9327-score" class="post-score" title="current number of votes">0</div><span id="post-9327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SYN-bit has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><strong>Never mind</strong>. I figured it out about 30 seconds after hitting the submit button.</p><p>tcpdump -s options (packet truncation).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '12, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9327" class="comments-container"></div><div id="comment-tools-9327" class="comment-tools"></div><div class="clear"></div><div id="comment-9327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

