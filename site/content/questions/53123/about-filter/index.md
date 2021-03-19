+++
type = "question"
title = "about filter"
description = '''hi, if I use this filter tcp.flags.syn ==1 and tcp.flags.ack == 0 that search that those 2 conditions will be right on 1 segments? or search on tcp call (that can be few segment) that those 2 conditions will be right  for example. if I get 2 segment from one ip, on first segment the syn flag=1, ack ...'''
date = "2016-06-01T20:56:00Z"
lastmod = "2016-06-01T21:57:00Z"
weight = 53123
keywords = [ "filter" ]
aliases = [ "/questions/53123" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [about filter](/questions/53123/about-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53123-score" class="post-score" title="current number of votes">0</div><span id="post-53123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, if I use this filter <code>tcp.flags.syn ==1 and tcp.flags.ack == 0</code> that search that those 2 conditions will be right on 1 segments? or search on tcp call (that can be few segment) that those 2 conditions will be right<br />
</p><p>for example.</p><p>if I get 2 segment from one ip, on first segment the syn flag=1, ack flag=0, on second segment syn flag=0 , ack flag=1</p><p>if I use this filter I need to see those 2 segment? or nothing? thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '16, 20:56</strong></p><img src="https://secure.gravatar.com/avatar/d71ea383349163c7df003fe3ec12b622?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dvir1999&#39;s gravatar image" /><p><span>dvir1999</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dvir1999 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jun '16, 21:58</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-53123" class="comments-container"></div><div id="comment-tools-53123" class="comment-tools"></div><div class="clear"></div><div id="comment-53123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53124"></span>

<div id="answer-container-53124" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53124-score" class="post-score" title="current number of votes">0</div><span id="post-53124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I may have got your question wrong, but:</p><p>the display filter is evaluated for each packet (frame) separately, not for a set of packets related together (such as a UDP stream or a TCP session).</p><p>So in your example, you'd see the first "segment" (which matches your filter example), but not the second one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '16, 21:57</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jun '16, 22:05</strong> </span></p></div></div><div id="comments-container-53124" class="comments-container"></div><div id="comment-tools-53124" class="comment-tools"></div><div class="clear"></div><div id="comment-53124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

