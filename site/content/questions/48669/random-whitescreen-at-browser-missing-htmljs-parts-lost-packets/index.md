+++
type = "question"
title = "Random whitescreen at browser, missing HTML/JS parts, lost packets?"
description = '''Srs, could you please help me with this issue?  I am a software developer and we are having a hard time trying to explain to our Infra that there is something weird in our server network (and not in our application or user machine, as this is happening to everyone and every app, even from users outs...'''
date = "2015-12-22T03:15:00Z"
lastmod = "2015-12-22T05:19:00Z"
weight = 48669
keywords = [ "whitescreen", "packets", "lost" ]
aliases = [ "/questions/48669" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Random whitescreen at browser, missing HTML/JS parts, lost packets?](/questions/48669/random-whitescreen-at-browser-missing-htmljs-parts-lost-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48669-score" class="post-score" title="current number of votes">0</div><span id="post-48669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Srs, could you please help me with this issue?</p><p>I am a software developer and we are having a hard time trying to explain to our Infra that there is something weird in our server network (and not in our application or user machine, as this is happening to everyone and every app, even from users outside our company)</p><p>When users are navigating through one of our applications, after a few requests they randomly receive a "white screen" at their browsers, we have checked using Firebug and we noticed that one of HTML, JS or CSS (random each time) are not completed. File ends at random parts, InternetExplorer keeps "Pending" until a 10-min timeout</p><p>I installed WireShark at my machine (user), but we don't have access to do that in the servers and neither our Infra know what WireShark is.</p><p>Print: <a href="http://i.imgur.com/6Sa2sPN.png">logs here</a></p><p>Everytime this error happens we receive exactly this order: [RST,ACK], many TCP Dup Ack and another [RST,ACK]. Also, I received random [RST,ACK] while navigating through our applications, but TCP Dup ACK only when the error came out.</p><p>Does that means anything? How can i find more info and a possible solution for this error?</p><p>If you need anything else from our user side, I can provide.</p><p>Thanks in advance! Regards, Diogo</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-whitescreen" rel="tag" title="see questions tagged &#39;whitescreen&#39;">whitescreen</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-lost" rel="tag" title="see questions tagged &#39;lost&#39;">lost</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '15, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/00408cd85c2650585efe322f10128b19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="diogoreis&#39;s gravatar image" /><p><span>diogoreis</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="diogoreis has no accepted answers">0%</span></p></div></div><div id="comments-container-48669" class="comments-container"><span id="48670"></span><div id="comment-48670" class="comment"><div id="post-48670-score" class="comment-score"></div><div class="comment-text"><p>Pictures are pretty useless, a (non-filtered) capture file (eg through cloudshark.org), even without TCP payload, and an infra layout would be needed to get going here.</p></div><div id="comment-48670-info" class="comment-info"><span class="comment-age">(22 Dec '15, 04:00)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="48671"></span><div id="comment-48671" class="comment"><div id="post-48671-score" class="comment-score"></div><div class="comment-text"><p>Jaap, thanks for your reply, so you mean we would need to get both sides running wireshark anyway, right?</p></div><div id="comment-48671-info" class="comment-info"><span class="comment-age">(22 Dec '15, 04:51)</span> <span class="comment-user userinfo">diogoreis</span></div></div><span id="48672"></span><div id="comment-48672" class="comment"><div id="post-48672-score" class="comment-score"></div><div class="comment-text"><p><span>@diogoreis</span>: Preferably yes, but you could start with the basics: The actual capture (not a screen dump), and an overview (of the relevant parts) of the infra involved.</p></div><div id="comment-48672-info" class="comment-info"><span class="comment-age">(22 Dec '15, 05:19)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-48669" class="comment-tools"></div><div class="clear"></div><div id="comment-48669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

