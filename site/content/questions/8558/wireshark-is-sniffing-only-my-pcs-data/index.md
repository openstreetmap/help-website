+++
type = "question"
title = "Wireshark is sniffing only my pc&#x27;s data"
description = '''Hi, managed to make wireshark work with my new macbook air 11&quot; with OS X 10.7.1 Lion. I can correctly see the network interface named en0 in the list of capture devices, however, when I start the packet sniffing on my own network to testing it, I only receive informations from my own computer&#x27;s IP a...'''
date = "2012-01-23T04:15:00Z"
lastmod = "2012-01-23T15:09:00Z"
weight = 8558
keywords = [ "mac", "macbook", "lion", "air" ]
aliases = [ "/questions/8558" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark is sniffing only my pc's data](/questions/8558/wireshark-is-sniffing-only-my-pcs-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8558-score" class="post-score" title="current number of votes">0</div><span id="post-8558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>managed to make wireshark work with my new macbook air 11" with OS X 10.7.1 Lion. I can correctly see the network interface named en0 in the list of capture devices, however, when I start the packet sniffing on my own network to testing it, I only receive informations from my own computer's IP address.</p><p>How can i fix this? Is there any way? Sorry for my ignorance, but I'm new to Wireshark and was doing just so experiments.</p><p>Regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-macbook" rel="tag" title="see questions tagged &#39;macbook&#39;">macbook</span> <span class="post-tag tag-link-lion" rel="tag" title="see questions tagged &#39;lion&#39;">lion</span> <span class="post-tag tag-link-air" rel="tag" title="see questions tagged &#39;air&#39;">air</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '12, 04:15</strong></p><img src="https://secure.gravatar.com/avatar/c5a1d8ca5116d95bde9a65e267ef3040?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="codemark&#39;s gravatar image" /><p><span>codemark</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="codemark has no accepted answers">0%</span></p></div></div><div id="comments-container-8558" class="comments-container"></div><div id="comment-tools-8558" class="comment-tools"></div><div class="clear"></div><div id="comment-8558-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8573"></span>

<div id="answer-container-8573" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8573-score" class="post-score" title="current number of votes">2</div><span id="post-8573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As it's a MacBook Air, <code>en0</code> is the AirPort device (MacBook Airs don't come with an Ethernet interface, you need a USB Ethernet for that). By default, it should see traffic from <em>AND</em> to your machine's IP address.</p><p>If you want to capture other traffic on your wireless network, you need to put it in monitor mode. Wireshark should have a checkbox for monitor mode in the dialog box that pops up if you select "Options" from the "Capture" menu and then try to capture on <code>en0</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '12, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8573" class="comments-container"></div><div id="comment-tools-8573" class="comment-tools"></div><div class="clear"></div><div id="comment-8573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

