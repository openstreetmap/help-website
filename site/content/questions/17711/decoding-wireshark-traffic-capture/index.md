+++
type = "question"
title = "Decoding WireShark Traffic Capture"
description = '''Hi All, We are using an ASP application and sometimes the application does not let the user type data in a given field. This issue occurs on different fields and screens of the program. We have opened support tickets with the vendor on this issue and they are claiming the reason the user can&#x27;t type ...'''
date = "2013-01-15T16:36:00Z"
lastmod = "2013-01-16T16:19:00Z"
weight = 17711
keywords = [ "application", "asp", "packets", "lost" ]
aliases = [ "/questions/17711" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding WireShark Traffic Capture](/questions/17711/decoding-wireshark-traffic-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17711-score" class="post-score" title="current number of votes">0</div><span id="post-17711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>We are using an ASP application and sometimes the application does not let the user type data in a given field. This issue occurs on different fields and screens of the program. We have opened support tickets with the vendor on this issue and they are claiming the reason the user can't type is because packets are being lost between the client computer and the ASP server.</p><p>Using Wireshark, I have captured the network traffic between the client computer and the ASP server when this issue has occurred. Unfortunately, I do no have the knowledge to interrupter the captured data to determine if lost packets are causing an issue.</p><p>I have uploaded the capture file to: <a href="http://www.cloudshark.org/captures/ef215c13669a">http://www.cloudshark.org/captures/ef215c13669a</a></p><p>Would anyone be will to review the file and render an opinion?</p><p>Thanks,</p><p>Doug</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-application" rel="tag" title="see questions tagged &#39;application&#39;">application</span> <span class="post-tag tag-link-asp" rel="tag" title="see questions tagged &#39;asp&#39;">asp</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-lost" rel="tag" title="see questions tagged &#39;lost&#39;">lost</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '13, 16:36</strong></p><img src="https://secure.gravatar.com/avatar/de472b397cadf24924025dd7cada4b22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dwerner&#39;s gravatar image" /><p><span>dwerner</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dwerner has no accepted answers">0%</span></p></div></div><div id="comments-container-17711" class="comments-container"></div><div id="comment-tools-17711" class="comment-tools"></div><div class="clear"></div><div id="comment-17711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17712"></span>

<div id="answer-container-17712" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17712-score" class="post-score" title="current number of votes">0</div><span id="post-17712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I haven't bothered to look at your capture file because your vendor's explanation is bogus. B-O-G-U-S bogus.</p><p>You mention ASP, which means HTTP, which means TCP, which means lost packets get transmitted automatically by the network stack. The stack will try and try and try until it succeeds, and the higher level code never sees any of this. At worst, the ASP level code will see a conversation be truncated if a lost packet is never able to be retransmitted successfully. It won't see lost information.</p><p>If someone <em>did</em> examine your capture file, they're not terribly likely to be able to do much with it without being one of the developers of the application in question, or at least having login details so they can play with it from the client side. A raw capture file doesn't have enough information to provide a diagnosis, except by sheerest blind luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '13, 18:36</strong></p><img src="https://secure.gravatar.com/avatar/8b0e3f6ae64ff27a7a01a0f49f8ee469?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Warren%20Young&#39;s gravatar image" /><p><span>Warren Young</span><br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Warren Young has no accepted answers">0%</span></p></div></div><div id="comments-container-17712" class="comments-container"><span id="17723"></span><div id="comment-17723" class="comment"><div id="post-17723-score" class="comment-score"></div><div class="comment-text"><p>Hi Warren,</p><p>Thanks for your response.<br />
</p><p>I highly suspected you are correct in your analysis of my situation. I have given the vendor several of our captures files when this issues occurs and they are "reviewing" them. Although I am using to having to jump through hoops to get vendors to address their issues, this particular vendor is particular vexing in blaming all our issues on network performance. I had no decision authority in picking or remaining with this vendor, but if they are offering an ASP program, I would think their program should account for various network performance issues.</p><p>Thanks again,</p><p>Doug</p></div><div id="comment-17723-info" class="comment-info"><span class="comment-age">(16 Jan '13, 09:04)</span> <span class="comment-user userinfo">dwerner</span></div></div><span id="17729"></span><div id="comment-17729" class="comment"><div id="post-17729-score" class="comment-score"></div><div class="comment-text"><p>Re "thanks": On a site like this, upvotes are better than "thanks," particularly to one such as me, with 16 whole points so far. :)</p><p>Re "network performance": Your vendor may well be right, that your network is crap. It may even be losing packets. My only point is that lost packets aren't going to result in corrupted conversations, due to data missing from the middle of a transmission. TCP takes care of that. But, bad network performance can still cause application problems. If this is what's going on, your vendor would just need a more intelligent explanation than "lost packets".</p></div><div id="comment-17729-info" class="comment-info"><span class="comment-age">(16 Jan '13, 16:19)</span> <span class="comment-user userinfo">Warren Young</span></div></div></div><div id="comment-tools-17712" class="comment-tools"></div><div class="clear"></div><div id="comment-17712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

