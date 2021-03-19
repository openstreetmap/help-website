+++
type = "question"
title = "SSl/TLS Handshake Protocol: Cipher Suites (20 suites)?"
description = '''I am using version 1.10.7 of Wireshark. I have seen a few tutorials that describe the various contents of a &quot;handshake&quot; packet. I have only found tutorials for older versions, so when it describes the details of the packet under Handshake Protocol: and I get to the part where it says Cipher Suite: e...'''
date = "2014-04-28T18:20:00Z"
lastmod = "2014-04-28T20:51:00Z"
weight = 32278
keywords = [ "suites", "cipher" ]
aliases = [ "/questions/32278" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [SSl/TLS Handshake Protocol: Cipher Suites (20 suites)?](/questions/32278/ssltls-handshake-protocol-cipher-suites-20-suites)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32278-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32278-score" class="post-score" title="current number of votes">0</div><span id="post-32278-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using version 1.10.7 of Wireshark.</p><p>I have seen a few tutorials that describe the various contents of a "handshake" packet. I have only found tutorials for older versions, so when it describes the details of the packet under Handshake Protocol: and I get to the part where it says Cipher Suite: etc... I don't see the cipher suite used. Instead I see a list of 20 cipher suites. I can't see which one of the suites was actually used.</p><p>Little help?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-suites" rel="tag" title="see questions tagged &#39;suites&#39;">suites</span> <span class="post-tag tag-link-cipher" rel="tag" title="see questions tagged &#39;cipher&#39;">cipher</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '14, 18:20</strong></p><img src="https://secure.gravatar.com/avatar/2d9a090b965aaa347b9c9c4704d1b552?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="plasmasnakeneo&#39;s gravatar image" /><p><span>plasmasnakeneo</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="plasmasnakeneo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Apr '14, 20:53</strong> </span></p></div></div><div id="comments-container-32278" class="comments-container"></div><div id="comment-tools-32278" class="comment-tools"></div><div class="clear"></div><div id="comment-32278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32279"></span>

<div id="answer-container-32279" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32279-score" class="post-score" title="current number of votes">1</div><span id="post-32279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="plasmasnakeneo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I guess you're talking about a SSL/TLS handshake. The list of cyphers is sent from one node to the other, which then picks the cypher it likes best, sending back the index of the chosen cypher in its next packet. You should be able to find it by looking for that packet following the cypher list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '14, 18:51</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32279" class="comments-container"><span id="32281"></span><div id="comment-32281" class="comment"><div id="post-32281-score" class="comment-score"></div><div class="comment-text"><p>Yes, thank you. I thought I should have seen what cipher suite it used within the handshake packet but that was not the case. I updated the title of the thread so that it reflects my initial problem better, since you seemed unclear about what I was looking for, that way others can find it easier as well.</p></div><div id="comment-32281-info" class="comment-info"><span class="comment-age">(28 Apr '14, 20:51)</span> <span class="comment-user userinfo">plasmasnakeneo</span></div></div></div><div id="comment-tools-32279" class="comment-tools"></div><div class="clear"></div><div id="comment-32279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

