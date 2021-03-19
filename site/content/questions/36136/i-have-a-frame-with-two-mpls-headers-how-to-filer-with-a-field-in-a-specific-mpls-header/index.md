+++
type = "question"
title = "I have a frame with two mpls headers. How to filer with a field in a specific mpls header?"
description = '''My frames MPLS headers are as follows:    MultiProtocol Label Switching Header, Label: 13746, Exp: 0, S: 0, TTL: 255  0000 0011 0101 1011 0010 .... .... .... = MPLS Label: 13746  .... .... .... .... .... 000. .... .... = MPLS Experimental Bits: 0  .... .... .... .... .... ...0 .... .... = MPLS Botto...'''
date = "2014-09-09T22:42:00Z"
lastmod = "2014-09-10T03:57:00Z"
weight = 36136
keywords = [ "multiple-headers", "display-filter" ]
aliases = [ "/questions/36136" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I have a frame with two mpls headers. How to filer with a field in a specific mpls header?](/questions/36136/i-have-a-frame-with-two-mpls-headers-how-to-filer-with-a-field-in-a-specific-mpls-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36136-score" class="post-score" title="current number of votes">0</div><span id="post-36136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My frames MPLS headers are as follows:<br />
</p><pre><code>        MultiProtocol Label Switching Header, Label: 13746, Exp: 0, S: 0, TTL: 255
              0000 0011 0101 1011 0010 .... .... .... = MPLS Label: 13746
              .... .... .... .... .... 000. .... .... = MPLS Experimental Bits: 0
              .... .... .... .... .... ...0 .... .... = MPLS Bottom Of Label Stack: 0
              .... .... .... .... .... .... 1111 1111 = MPLS TTL: 255
        MultiProtocol Label Switching Header, Label: 19772, Exp: 0, S: 1, TTL: 2
              0000 0100 1101 0011 1100 .... .... .... = MPLS Label: 19772
              .... .... .... .... .... 000. .... .... = MPLS Experimental Bits: 0
              .... .... .... .... .... ...1 .... .... = MPLS Bottom Of Label Stack: 1
              .... .... .... .... .... .... 0000 0010 = MPLS TTL: 2</code></pre><p>I want to filter with respect to mpls header of only first mpls frame. If I use filter like 'mpls.label == 13746' wireshark filters even those frames where second mpls headers label is 13746 even though second mpls header is different. I How to achieve filtering with respect to only first mpls headers label field?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-multiple-headers" rel="tag" title="see questions tagged &#39;multiple-headers&#39;">multiple-headers</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '14, 22:42</strong></p><img src="https://secure.gravatar.com/avatar/13c01090e672eed966eb0deac4a1abf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chetan%20Ragi&#39;s gravatar image" /><p><span>Chetan Ragi</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chetan Ragi has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Sep '14, 03:57</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-36136" class="comments-container"></div><div id="comment-tools-36136" class="comment-tools"></div><div class="clear"></div><div id="comment-36136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36146"></span>

<div id="answer-container-36146" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36146-score" class="post-score" title="current number of votes">0</div><span id="post-36146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use a distinguishing mark of the outer label, eg. MPLS Bottom Of Label Stack == 0. But this only helps if you always have two labels. A <em>real</em> solution would require an addition to the Wireshark display filter engine to be able to address the level at which the field occurs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '14, 03:57</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-36146" class="comments-container"></div><div id="comment-tools-36146" class="comment-tools"></div><div class="clear"></div><div id="comment-36146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

