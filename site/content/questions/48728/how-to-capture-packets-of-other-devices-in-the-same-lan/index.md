+++
type = "question"
title = "how to capture packets of other devices in the same lan ?"
description = '''I am begginer in wireshark. I have two computers in the same lan(Ubuntu and windows 7). When I run whireshark from one computer, whireshark returns all the packets from the same computer and not from both. How can I run wireshark from computer_1 and take packets results from computer_2 ?  Thank you ...'''
date = "2015-12-28T01:27:00Z"
lastmod = "2015-12-28T05:50:00Z"
weight = 48728
keywords = [ "computers", "caputer", "other", "packets", "from" ]
aliases = [ "/questions/48728" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to capture packets of other devices in the same lan ?](/questions/48728/how-to-capture-packets-of-other-devices-in-the-same-lan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48728-score" class="post-score" title="current number of votes">0</div><span id="post-48728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am begginer in wireshark. I have two computers in the same lan(Ubuntu and windows 7). When I run whireshark from one computer, whireshark returns all the packets from the same computer and not from both. How can I run wireshark from computer_1 and take packets results from computer_2 ?</p><p>Thank you in advance !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-computers" rel="tag" title="see questions tagged &#39;computers&#39;">computers</span> <span class="post-tag tag-link-caputer" rel="tag" title="see questions tagged &#39;caputer&#39;">caputer</span> <span class="post-tag tag-link-other" rel="tag" title="see questions tagged &#39;other&#39;">other</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-from" rel="tag" title="see questions tagged &#39;from&#39;">from</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Dec '15, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/8a004fbcdf63fc571a12c3bf472faf46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="%CE%91%CE%BD%CF%84%CF%8E%CE%BD%CE%B7%CF%82%20%CE%A3%CE%BA%CE%B1%CF%81%CE%BB%CE%AC%CF%84%CE%BF%CF%82&#39;s gravatar image" /><p><span>Αντώνης Σκαρ...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Αντώνης Σκαρλάτος has no accepted answers">0%</span></p></div></div><div id="comments-container-48728" class="comments-container"></div><div id="comment-tools-48728" class="comment-tools"></div><div class="clear"></div><div id="comment-48728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48731"></span>

<div id="answer-container-48731" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48731-score" class="post-score" title="current number of votes">1</div><span id="post-48731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm assuming you are using a switch. If so, you would need to use a hub or mirror the traffic from the other port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Dec '15, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/dbc4d8cb6be85bd586ca4bf211e1337c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thetechfirm&#39;s gravatar image" /><p><span>thetechfirm</span><br />
<span class="score" title="64 reputation points">64</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thetechfirm has no accepted answers">0%</span></p></div></div><div id="comments-container-48731" class="comments-container"><span id="48733"></span><div id="comment-48733" class="comment"><div id="post-48733-score" class="comment-score"></div><div class="comment-text"><p>You can look <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">here</a> for a more comprehensive description of your options.</p></div><div id="comment-48733-info" class="comment-info"><span class="comment-age">(28 Dec '15, 05:50)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-48731" class="comment-tools"></div><div class="clear"></div><div id="comment-48731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

