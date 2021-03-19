+++
type = "question"
title = "SKINNY protocol analysis"
description = '''Hello! I am engaged in development of the program for the analysis of packets of SKINNY protocol. How program WireShark obtains the data of this protocol? How information Message ID and Call Identifier is extracted from packet SKINNY?  Thanks for the help! '''
date = "2011-01-02T10:52:00Z"
lastmod = "2011-01-02T15:33:00Z"
weight = 1587
keywords = [ "development", "skinny", "protocol" ]
aliases = [ "/questions/1587" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SKINNY protocol analysis](/questions/1587/skinny-protocol-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1587-score" class="post-score" title="current number of votes">0</div><span id="post-1587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! I am engaged in development of the program for the analysis of packets of SKINNY protocol. How program WireShark obtains the data of this protocol? How information <strong>Message ID</strong> and <strong>Call Identifier</strong> is extracted from packet SKINNY? Thanks for the help! <img src="http://photomaster.ucoz.com/skinny.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-skinny" rel="tag" title="see questions tagged &#39;skinny&#39;">skinny</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '11, 10:52</strong></p><img src="https://secure.gravatar.com/avatar/dd20d3abb5d78de1f6ac206f33946fc3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="masterbloger&#39;s gravatar image" /><p><span>masterbloger</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="masterbloger has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jan '11, 11:01</strong> </span></p></div></div><div id="comments-container-1587" class="comments-container"></div><div id="comment-tools-1587" class="comment-tools"></div><div class="clear"></div><div id="comment-1587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1590"></span>

<div id="answer-container-1590" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1590-score" class="post-score" title="current number of votes">1</div><span id="post-1590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you are going to develop a program that works like Wireshark, then you might want to look at the source-code. Looking at the <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-skinny.c?view=markup">skinny protocol dissector code</a> it is just pulled out at the correct offsets. (Don't forget to consider the obligation of the GPL if you are going to use the Wireshark code)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '11, 15:33</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-1590" class="comments-container"></div><div id="comment-tools-1590" class="comment-tools"></div><div class="clear"></div><div id="comment-1590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

