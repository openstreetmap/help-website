+++
type = "question"
title = "Why am I getting random packets"
description = '''Hi I&#x27;m new to using wireshark. I&#x27;m trying to do a lab for school in which I inspect the packets from accessing a simple web file. When I do that I get a bunch of random packets from a bunch of different ip addresses including my school(which doesn&#x27;t make sense because I&#x27;m at home) random servers, an...'''
date = "2016-09-18T14:30:00Z"
lastmod = "2016-09-19T08:16:00Z"
weight = 55636
keywords = [ "problem", "packet", "beginner" ]
aliases = [ "/questions/55636" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why am I getting random packets](/questions/55636/why-am-i-getting-random-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55636-score" class="post-score" title="current number of votes">0</div><span id="post-55636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I'm new to using wireshark. I'm trying to do a lab for school in which I inspect the packets from accessing a simple web file. When I do that I get a bunch of random packets from a bunch of different ip addresses including my school(which doesn't make sense because I'm at home) random servers, and other devices on my local network. My friend who is also working with me on the lab is not getting these random packets. Why is this happening?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-beginner" rel="tag" title="see questions tagged &#39;beginner&#39;">beginner</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '16, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/3f9343c28300fbcb53e066e0d7355f5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GP2&#39;s gravatar image" /><p><span>GP2</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GP2 has no accepted answers">0%</span></p></div></div><div id="comments-container-55636" class="comments-container"></div><div id="comment-tools-55636" class="comment-tools"></div><div class="clear"></div><div id="comment-55636-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55641"></span>

<div id="answer-container-55641" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55641-score" class="post-score" title="current number of votes">1</div><span id="post-55641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>These packets are not "random". On top of your browser downloading the web page, there are other applications and processes in your PC, some of which are network applications and thus talk to their relevant servers. Besides, some browsers tend to update links in cache. So if you were visiting your school's web page in the past (or you even have it open in another browser tab although you are not currently watching it), this could be an explanation why your school's IP appears in your packet list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '16, 01:32</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-55641" class="comments-container"><span id="55659"></span><div id="comment-55659" class="comment"><div id="post-55659-score" class="comment-score"></div><div class="comment-text"><p>thanks for the response. I can see why that would cause those packets to appear. Do you know what processes would cause these packets to appear? As I said, my friend, who was working on the lab with me and connected to the same network as me did not have these packets show up. Also these packets did not show up for me when I was at school.</p></div><div id="comment-55659-info" class="comment-info"><span class="comment-age">(19 Sep '16, 07:54)</span> <span class="comment-user userinfo">GP2</span></div></div><span id="55663"></span><div id="comment-55663" class="comment"><div id="post-55663-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Do you know what processes would cause these packets to appear?</p></blockquote><p>No, I don't - these may be application auto-update processes, Windows 10 calling home (which they do almost continuously), ...</p><p>But the good news is that you don't need to care about them to fulfil your assignment. Use a display filter to make Wireshark show you only packets to/from the IP address of the web server from which you are downloading that "simple web file". This is what Wireshark users routinely do, and if you ask your teacher, he is likely to tell you that this was part of the exercise goal.</p></div><div id="comment-55663-info" class="comment-info"><span class="comment-age">(19 Sep '16, 08:16)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-55641" class="comment-tools"></div><div class="clear"></div><div id="comment-55641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

