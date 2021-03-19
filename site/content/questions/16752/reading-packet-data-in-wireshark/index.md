+++
type = "question"
title = "Reading packet data in wireshark"
description = '''Hello team, i captured some openflow packets ,and i want to read the data inside Data (47 bytes) its in hexadecimal .Can i read and analyse the content of that data ? thanks in advance '''
date = "2012-12-10T11:16:00Z"
lastmod = "2012-12-12T08:44:00Z"
weight = 16752
keywords = [ "openflow" ]
aliases = [ "/questions/16752" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reading packet data in wireshark](/questions/16752/reading-packet-data-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16752-score" class="post-score" title="current number of votes">0</div><span id="post-16752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello team,</p><p>i captured some openflow packets ,and i want to read the data inside Data (47 bytes) its in hexadecimal .Can i read and analyse the content of that data ?</p><p>thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-openflow" rel="tag" title="see questions tagged &#39;openflow&#39;">openflow</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '12, 11:16</strong></p><img src="https://secure.gravatar.com/avatar/ec4ab66e10a8390b959b8110364f5b34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tyler&#39;s gravatar image" /><p><span>Tyler</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tyler has no accepted answers">0%</span></p></div></div><div id="comments-container-16752" class="comments-container"></div><div id="comment-tools-16752" class="comment-tools"></div><div class="clear"></div><div id="comment-16752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16815"></span>

<div id="answer-container-16815" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16815-score" class="post-score" title="current number of votes">0</div><span id="post-16815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think we need some additional information:</p><blockquote><p>i captured some openflow packets</p></blockquote><p>You did this with Wireshark or a different tool? If the later, which tool and how looks the output of that tool (can you post a sample)?</p><blockquote><p>Can i read and analyse the content of that data</p></blockquote><p>Do you want to read and analyze it with Wireshark? If so, what is the format you've got? Is it just the openflow payload data in HEX?</p><p>If the later, you could format that data into something that <a href="http://www.wireshark.org/docs/man-pages/text2pcap.html">text2pcap</a> understands and then add dummy headers (see man page of text2pcap).</p><blockquote><p><code>text2pcap -T 5000,595 hex.dat openflow.cap</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '12, 08:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-16815" class="comments-container"></div><div id="comment-tools-16815" class="comment-tools"></div><div class="clear"></div><div id="comment-16815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

