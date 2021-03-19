+++
type = "question"
title = "Why I am seeing multiple syn packets when I open a web page?"
description = '''Hi Trying to find an explanation for a slow network response, I installed the wireshark sniffer. When I opened a web page I see that multiple syn packets are being sent to the web server, in less tan 0.005 seconds. Any idea why this happens ? '''
date = "2014-10-29T17:20:00Z"
lastmod = "2014-10-30T08:04:00Z"
weight = 37447
keywords = [ "packets", "multiple", "syn" ]
aliases = [ "/questions/37447" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why I am seeing multiple syn packets when I open a web page?](/questions/37447/why-i-am-seeing-multiple-syn-packets-when-i-open-a-web-page)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37447-score" class="post-score" title="current number of votes">0</div><span id="post-37447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Trying to find an explanation for a slow network response, I installed the wireshark sniffer. When I opened a web page I see that multiple syn packets are being sent to the web server, in less tan 0.005 seconds. Any idea why this happens ? <img src="https://osqa-ask.wireshark.org/upfiles/Capture_TwewsHN.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '14, 17:20</strong></p><img src="https://secure.gravatar.com/avatar/70c6260241f2d88e4d96c44be255baeb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alzav&#39;s gravatar image" /><p><span>Alzav</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alzav has no accepted answers">0%</span></p></img></div></div><div id="comments-container-37447" class="comments-container"></div><div id="comment-tools-37447" class="comment-tools"></div><div class="clear"></div><div id="comment-37447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37452"></span>

<div id="answer-container-37452" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37452-score" class="post-score" title="current number of votes">2</div><span id="post-37452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is because your browser wants to have multiple parallel sessions to the server to speed up communication. In your case 6 sessions are started right away - I think this is the default for Chrome In Mozilla you can control this in <a href="http://kb.mozillazine.org/About:config_entries">about:config</a><br />
</p><p>Regards Matthias</p><hr /><p>From <a href="http://tools.ietf.org/html/draft-ietf-tcpm-initcwnd-00">http://tools.ietf.org/html/draft-ietf-tcpm-initcwnd-00</a></p><pre><code>   In the mean time, applications have responded to TCP&#39;s &quot;slow&quot; start.
   Web sites use multiple sub-domains [Bel10] to circumvent HTTP 1.1
   regulation on two connections per physical host [RFC2616]. As of
   today, major web browsers open multiple connections to the same site
   (up to six connections per domain [Ste08] and the number is growing).
   This trend is to remedy HTTP serialized download to achieve
   parallelism and higher performance.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '14, 23:10</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Oct '14, 00:03</strong> </span></p></div></div><div id="comments-container-37452" class="comments-container"><span id="37467"></span><div id="comment-37467" class="comment"><div id="post-37467-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot</p></div><div id="comment-37467-info" class="comment-info"><span class="comment-age">(30 Oct '14, 08:04)</span> <span class="comment-user userinfo">Alzav</span></div></div></div><div id="comment-tools-37452" class="comment-tools"></div><div class="clear"></div><div id="comment-37452-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

