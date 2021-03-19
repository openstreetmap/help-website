+++
type = "question"
title = "HTTP request was not displayed in my wireshark."
description = '''I have a pcap extracted from a malware pcap. It looks like a simple HTTP transaction, but I don&#x27;t know why it looks different on my wireshark (1.10.6): packet 4 is not shown as the HTTP transaction (it&#x27;s shown as TCP segment of a reassemblied PDU. The HTTP request is shown for packet 9.  I know my w...'''
date = "2015-06-23T22:07:00Z"
lastmod = "2015-06-24T06:26:00Z"
weight = 43491
keywords = [ "wireshark" ]
aliases = [ "/questions/43491" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [HTTP request was not displayed in my wireshark.](/questions/43491/http-request-was-not-displayed-in-my-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43491-score" class="post-score" title="current number of votes">0</div><span id="post-43491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcap extracted from a malware pcap. It looks like a simple HTTP transaction, but I don't know why it looks different on my wireshark (1.10.6): packet 4 is not shown as the HTTP transaction (it's shown as TCP segment of a reassemblied PDU. The HTTP request is shown for packet 9.<br />
</p><p>I know my wireshark (which is a little old), but a little surprised that this basic pcap has the problem. Just want to confirm.</p><p><a href="https://www.cloudshark.org/captures/a923c12be2aa">pcap</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '15, 22:07</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span> </br></p></div></div><div id="comments-container-43491" class="comments-container"></div><div id="comment-tools-43491" class="comment-tools"></div><div class="clear"></div><div id="comment-43491-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43492"></span>

<div id="answer-container-43492" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43492-score" class="post-score" title="current number of votes">0</div><span id="post-43492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go to Edit &gt; Preferences &gt; Protocols &gt; TCP and uncheck "Allow subdissector to reassemble TCP streams."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '15, 22:22</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-43492" class="comments-container"><span id="43501"></span><div id="comment-43501" class="comment"><div id="post-43501-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@jim</span>-aragon. It helps. Wonder exactly what "Allow subdissector to reassemble TCP streams." means here. After all, Packet 7,8,9 don't have any TCP data, packet 4 has all the tcp data for a complete HTTP request. Wonder why is the need for changing the option "Allow subdissector to reassemble TCP streams.". Thanks.</p></div><div id="comment-43501-info" class="comment-info"><span class="comment-age">(24 Jun '15, 06:26)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-43492" class="comment-tools"></div><div class="clear"></div><div id="comment-43492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

