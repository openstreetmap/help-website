+++
type = "question"
title = "Problem seeing ssl handshake as a server"
description = '''Hi, I&#x27;m quite new to wireshark, so there probably is a simple answer to my question. However I can&#x27;t seem to find it on my own... I have two machines - 192.168.0.105 (my laptop running windows7) and 192.168.0.24 (an Ubuntu server). Wireshark runs on my laptop, as well as an Abyss webserver configure...'''
date = "2014-12-09T00:27:00Z"
lastmod = "2014-12-09T06:34:00Z"
weight = 38463
keywords = [ "ssl", "handshake", "https" ]
aliases = [ "/questions/38463" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Problem seeing ssl handshake as a server](/questions/38463/problem-seeing-ssl-handshake-as-a-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38463-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38463-score" class="post-score" title="current number of votes">0</div><span id="post-38463-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm quite new to wireshark, so there probably is a simple answer to my question. However I can't seem to find it on my own...</p><p>I have two machines - 192.168.0.105 (my laptop running windows7) and 192.168.0.24 (an Ubuntu server). Wireshark runs on my laptop, as well as an Abyss webserver configured to listen to https on port 8080. On the Ubuntu server, I have Apache configured to listen on https on port 443.</p><p>When I connect with chrome from my laptop to the Apache server, I see a nice SSL Handshake procedure. However, when I try to do the opposit, i.e. connect with firefox from the Ubuntu machine to my Abyss webserver, I only get TCP traffic. If I type ssl in the filter dialog, it's empty. I still se the page though, and my certificate is in there as shown in the picture.</p><p>The reason I ask is that I have an "SSL Handshake problem" error on an embedded thingie I'm programming, and I would really need to troubleshoot this.</p><p>I wasn't allowed to upload pictures, but put two screenshots here: <a href="http://www.creativia.se/ws">Screenshots</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-handshake" rel="tag" title="see questions tagged &#39;handshake&#39;">handshake</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '14, 00:27</strong></p><img src="https://secure.gravatar.com/avatar/0d38f78315c13a6ff05f47c416e35778?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nanne&#39;s gravatar image" /><p><span>nanne</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nanne has no accepted answers">0%</span></p></div></div><div id="comments-container-38463" class="comments-container"></div><div id="comment-tools-38463" class="comment-tools"></div><div class="clear"></div><div id="comment-38463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38467"></span>

<div id="answer-container-38467" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38467-score" class="post-score" title="current number of votes">2</div><span id="post-38467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nanne has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>webserver configured to listen to https on port 8080</p></blockquote><p>Wireshark detects the protocols mainly (but not only) based on the ports. Port 8080 is not associated with SSL traffic, that's the reason why it's shown a TCP.</p><p>You have four options:</p><ul><li><p><strong>Edit -&gt; Preferences -&gt; Protocols -&gt; HTTP -&gt; SSL/TLS Ports</strong> and add 8080 to the list of ports: 443, 8080.</p></li><li><p>right click on any frame with port 8080 and choose "Decode as". Then select "TCP destination (8080)" and "SSL"</p></li><li><p>run your server on port 443 ;-)</p></li><li><p>use DNAT on the target server to translate only <code>C:* -&gt; S:443</code> to <code>C:* -&gt; S:8080</code> and then connect to the server via port 443 from the client ;-))))))))</p></li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '14, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Dec '14, 02:12</strong> </span></p></div></div><div id="comments-container-38467" class="comments-container"><span id="38476"></span><div id="comment-38476" class="comment"><div id="post-38476-score" class="comment-score"></div><div class="comment-text"><p>Thank you! Number 1 did indeed solve the problem. As I am sure that the other more or less serious suggestions would do, now that I understand what's going on :-)</p></div><div id="comment-38476-info" class="comment-info"><span class="comment-age">(09 Dec '14, 04:32)</span> <span class="comment-user userinfo">nanne</span></div></div><span id="38482"></span><div id="comment-38482" class="comment"><div id="post-38482-score" class="comment-score"></div><div class="comment-text"><p><span>@nanne</span></p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-38482-info" class="comment-info"><span class="comment-age">(09 Dec '14, 06:20)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="38484"></span><div id="comment-38484" class="comment"><div id="post-38484-score" class="comment-score"></div><div class="comment-text"><blockquote><p>As I am sure that the other <strong>more or less serious suggestions</strong> would do,</p></blockquote><p>They are <strong>all serious suggestions</strong>! ;-) Just more work than the easy one :-)</p><p>Regards<br />
Kurt</p></div><div id="comment-38484-info" class="comment-info"><span class="comment-age">(09 Dec '14, 06:34)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-38467" class="comment-tools"></div><div class="clear"></div><div id="comment-38467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

