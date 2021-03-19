+++
type = "question"
title = "Multiple TCP connections"
description = '''Hello everyone, I got some strange situation in Wireshark. When I sniffing traffic between my PC and some website, it appears that my PC request multiple connection to that website all at once, before any of this connections to be accepted by the server. What can be the issue? There is a picture of ...'''
date = "2017-05-22T11:50:00Z"
lastmod = "2017-05-22T11:55:00Z"
weight = 61546
keywords = [ "connections", "multiple", "stream", "tcp" ]
aliases = [ "/questions/61546" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Multiple TCP connections](/questions/61546/multiple-tcp-connections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61546-score" class="post-score" title="current number of votes">0</div><span id="post-61546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,</p><p>I got some strange situation in Wireshark. When I sniffing traffic between my PC and some website, it appears that my PC request multiple connection to that website all at once, before any of this connections to be accepted by the server. What can be the issue?</p><p>There is a picture of this: (BTW I'm using Windows 10) <img src="https://osqa-ask.wireshark.org/upfiles/wireshark_7EccD1F.jpg" alt="alt text" /></p><p>Also, for not asking in new question, I want to ask how TCP creates Streams and why one connection to the same server use to have more Stream.</p><p>Thank you in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-connections" rel="tag" title="see questions tagged &#39;connections&#39;">connections</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '17, 11:50</strong></p><img src="https://secure.gravatar.com/avatar/6e54c4932635e2972923dfe65553c08b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nicola%20Tesla&#39;s gravatar image" /><p><span>Nicola Tesla</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nicola Tesla has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 May '17, 11:54</strong> </span></p></div></div><div id="comments-container-61546" class="comments-container"></div><div id="comment-tools-61546" class="comment-tools"></div><div class="clear"></div><div id="comment-61546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61547"></span>

<div id="answer-container-61547" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61547-score" class="post-score" title="current number of votes">1</div><span id="post-61547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Nicola Tesla has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's something you see when a browser starts multiple connections to pull various elements from the web server, and the round trip time is higher than just a few milliseconds. In that case the SYNs are sent on their way before the first SYN/ACKs come back. It's absolutely normal.</p><p>TCP creates stream/connections based on what the application wants - so if the application asks TCP to open multiple connections, TCP will do just that. And its usually to parallelize the requests to get content faster.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '17, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61547" class="comments-container"></div><div id="comment-tools-61547" class="comment-tools"></div><div class="clear"></div><div id="comment-61547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

