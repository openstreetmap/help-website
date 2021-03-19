+++
type = "question"
title = "Commerical use of wireshark"
description = '''Hi folks, I wanted to know if I make some changes in wireshark, suppose implementing support for extra protocol not already present in wireshark. Can I make the DLL of my changes and then sell it commercially ? Would it be legal?'''
date = "2012-02-02T22:56:00Z"
lastmod = "2012-02-03T10:14:00Z"
weight = 8798
keywords = [ "usage", "protocol" ]
aliases = [ "/questions/8798" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Commerical use of wireshark](/questions/8798/commerical-use-of-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8798-score" class="post-score" title="current number of votes">0</div><span id="post-8798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi folks,</p><p>I wanted to know if I make some changes in wireshark, suppose implementing support for extra protocol not already present in wireshark. Can I make the DLL of my changes and then sell it commercially ? Would it be legal?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '12, 22:56</strong></p><img src="https://secure.gravatar.com/avatar/d221d26845724614e25ab8e51887c4bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashish_goel&#39;s gravatar image" /><p><span>ashish_goel</span><br />
<span class="score" title="15 reputation points">15</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashish_goel has no accepted answers">0%</span></p></div></div><div id="comments-container-8798" class="comments-container"></div><div id="comment-tools-8798" class="comment-tools"></div><div class="clear"></div><div id="comment-8798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8802"></span>

<div id="answer-container-8802" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8802-score" class="post-score" title="current number of votes">5</div><span id="post-8802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The rules of GPLv2 apply, which state that if you program against the API of the application (like you do using the functionality though dynamic linking) your code is covered by the GPL as well. That means that you are required to distribute your source code, free of charge, of the binary you distribute. This source code can be requested by anyone, and has to be provided by you, for just the cost of the medium on which it is transferred.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '12, 02:37</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-8802" class="comments-container"><span id="8808"></span><div id="comment-8808" class="comment"><div id="post-8808-score" class="comment-score"></div><div class="comment-text"><p>By free of charge what do you mean?? Do I have to sell my complete work for free of cost OR do i have to give the source code free of cost to those buying my product??</p></div><div id="comment-8808-info" class="comment-info"><span class="comment-age">(03 Feb '12, 10:03)</span> <span class="comment-user userinfo">ashish_goel</span></div></div><span id="8810"></span><div id="comment-8810" class="comment"><div id="post-8810-score" class="comment-score"></div><div class="comment-text"><p>You have to give the source code free of cost (other than "a fee charged for the physical act of transferring a copy") to those buying your product <em>AND</em> all copies you distribute of the binary code or the source code are covered under the GPL, which means you cannot prevent anybody who buys your software from giving it, or its source code, away. Read <a href="http://www.gnu.org/licenses/gpl-2.0.html">the GPL Version 2</a>, under which Wireshark is licensed, for details.</p></div><div id="comment-8810-info" class="comment-info"><span class="comment-age">(03 Feb '12, 10:14)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-8802" class="comment-tools"></div><div class="clear"></div><div id="comment-8802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

