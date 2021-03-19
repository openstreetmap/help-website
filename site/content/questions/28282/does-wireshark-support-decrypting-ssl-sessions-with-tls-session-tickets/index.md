+++
type = "question"
title = "does wireshark support decrypting ssl sessions with &#x27;tls session tickets&#x27;?"
description = '''I&#x27;m pretty sure i&#x27;ve finally configured ssl to correctly decrypt my ssl packets, from a capture of and ssl session on and IIS 7.5 server. I say this, because when i use the filter &#x27;ssl&#x27; in wireshark, i occasionally see a green http packet, and when inspecting the packet, i can see the ssl section in...'''
date = "2013-12-18T23:51:00Z"
lastmod = "2013-12-19T15:14:00Z"
weight = 28282
keywords = [ "tls", "resumption", "session", "iis", "7.5" ]
aliases = [ "/questions/28282" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [does wireshark support decrypting ssl sessions with 'tls session tickets'?](/questions/28282/does-wireshark-support-decrypting-ssl-sessions-with-tls-session-tickets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28282-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28282-score" class="post-score" title="current number of votes">0</div><span id="post-28282-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm pretty sure i've finally configured ssl to correctly decrypt my ssl packets, from a capture of and ssl session on and IIS 7.5 server.</p><p>I say this, because when i use the filter 'ssl' in wireshark, i occasionally see a green http packet, and when inspecting the packet, i can see the ssl section in the detail window, followed by the decrypted http packet information.</p><p>However, there are only a very few of these readable packets.</p><p>I read another post where the problem cause was the use of 'tls session tickets', and the poster was told to file an enhancement request. In the meantime, the work around was to 'disable the use of tls session tickets'.</p><p>a) how can i tell if I am having the same problem? What would i look for in the ssl debug log? b) if it is the same problem, does wireshark now support decryption of sessions using tls session tickets? c) if wireshark does not, does anyone know how to disable the use of tls session tickets on iis 7.5?</p><p>thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-resumption" rel="tag" title="see questions tagged &#39;resumption&#39;">resumption</span> <span class="post-tag tag-link-session" rel="tag" title="see questions tagged &#39;session&#39;">session</span> <span class="post-tag tag-link-iis" rel="tag" title="see questions tagged &#39;iis&#39;">iis</span> <span class="post-tag tag-link-7.5" rel="tag" title="see questions tagged &#39;7.5&#39;">7.5</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Dec '13, 23:51</strong></p><img src="https://secure.gravatar.com/avatar/8a1c296b364850c080cc8fea3bb3f534?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dmc_lat47&#39;s gravatar image" /><p><span>dmc_lat47</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dmc_lat47 has no accepted answers">0%</span></p></div></div><div id="comments-container-28282" class="comments-container"></div><div id="comment-tools-28282" class="comment-tools"></div><div class="clear"></div><div id="comment-28282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28290"></span>

<div id="answer-container-28290" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28290-score" class="post-score" title="current number of votes">0</div><span id="post-28290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>a) how can i tell if I am having the same problem?</p></blockquote><p>Please use the following display filter: <code>ssl.handshake.session_ticket</code></p><p>If you see some frames, it's a good sign for session tickets.</p><blockquote><p>does wireshark now support decryption of sessions using tls session tickets?</p></blockquote><p>AFIAK: No, but there is an open Enhancement Bug for this:</p><blockquote><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5963">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5963</a></p></blockquote><p>Even if it would be able to work with session tickets, there is a structural problem. If you just captured traffic with session tickets, there is no way for Wireshark to figure out the key that has been used. So, even if Wireshark will support session tickets eventually, you will have to capture the first handshake to be able to decrypt the session.</p><blockquote><p>if wireshark does not, does anyone know how to disable the use of tls session tickets on iis 7.5?</p></blockquote><p>I guess the people at a Microsoft forum are the better crowd to ask ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Dec '13, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28290" class="comments-container"><span id="28293"></span><div id="comment-28293" class="comment"><div id="post-28293-score" class="comment-score"></div><div class="comment-text"><p>thanks for your help!</p><p>so, i used the filter... ssl.handshake.session_ticket</p><p>not a packet came up! Now i am at a loss as to why only some packets can be decrypted.</p><p>Anyone have any ideas?</p><p>thanks again</p></div><div id="comment-28293-info" class="comment-info"><span class="comment-age">(19 Dec '13, 09:24)</span> <span class="comment-user userinfo">dmc_lat47</span></div></div><span id="28301"></span><div id="comment-28301" class="comment"><div id="post-28301-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Anyone have any ideas?</p></blockquote><p>without the debug log? No.</p></div><div id="comment-28301-info" class="comment-info"><span class="comment-age">(19 Dec '13, 15:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-28290" class="comment-tools"></div><div class="clear"></div><div id="comment-28290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

