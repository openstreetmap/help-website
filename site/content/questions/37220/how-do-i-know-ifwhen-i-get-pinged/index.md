+++
type = "question"
title = "How do i know if/when i get pinged?"
description = '''Hello! New to using Wireshark and was looking for guide of sorts. Can i use Wireshark to know when i get pinged? (Pinged so i get disconnected)'''
date = "2014-10-21T03:09:00Z"
lastmod = "2014-10-22T05:12:00Z"
weight = 37220
keywords = [ "pinged", "wireshark" ]
aliases = [ "/questions/37220" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do i know if/when i get pinged?](/questions/37220/how-do-i-know-ifwhen-i-get-pinged)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37220-score" class="post-score" title="current number of votes">0</div><span id="post-37220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>New to using Wireshark and was looking for guide of sorts.</p><p>Can i use Wireshark to know when i get pinged? (Pinged so i get disconnected)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pinged" rel="tag" title="see questions tagged &#39;pinged&#39;">pinged</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '14, 03:09</strong></p><img src="https://secure.gravatar.com/avatar/38608cc99abe1bb6199578b5229586ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Surarn&#39;s gravatar image" /><p><span>Surarn</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Surarn has no accepted answers">0%</span></p></div></div><div id="comments-container-37220" class="comments-container"></div><div id="comment-tools-37220" class="comment-tools"></div><div class="clear"></div><div id="comment-37220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37231"></span>

<div id="answer-container-37231" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37231-score" class="post-score" title="current number of votes">0</div><span id="post-37231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're suspecting that you're getting ping flooded (as in Denial of service), you'll see lots of ICMP traffic (just type icmp in your filter box)</p><p>The flavor of the week, as far as denial of service attacks isn't ping floods though, its usually SYN flooding or NNTP attacks</p><p>A way to test this is to open a command prompt (if you're on windows) and type: ping -t 4.4.2.2</p><p>Then open wireshark and start a capture, type icmp in your filter box, and you'll immediately see pings.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '14, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/eab06dcd69504dc40c68cf8fa84a390e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robotfish1911&#39;s gravatar image" /><p><span>robotfish1911</span><br />
<span class="score" title="17 reputation points">17</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robotfish1911 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Oct '14, 05:19</strong> </span></p></div></div><div id="comments-container-37231" class="comments-container"><span id="37274"></span><div id="comment-37274" class="comment"><div id="post-37274-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer!</p></div><div id="comment-37274-info" class="comment-info"><span class="comment-age">(22 Oct '14, 05:12)</span> <span class="comment-user userinfo">Surarn</span></div></div></div><div id="comment-tools-37231" class="comment-tools"></div><div class="clear"></div><div id="comment-37231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

