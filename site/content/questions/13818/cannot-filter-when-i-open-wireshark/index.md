+++
type = "question"
title = "cannot filter when i open wireshark"
description = '''when i open a cap with the wireshark(ver after 1.413) i cannot key-in any words in filter i must wait 1-3 min to key-in any words in filter  my pc win7 32bit Language ch   '''
date = "2012-08-22T09:16:00Z"
lastmod = "2012-12-12T19:38:00Z"
weight = 13818
keywords = [ "filter" ]
aliases = [ "/questions/13818" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [cannot filter when i open wireshark](/questions/13818/cannot-filter-when-i-open-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13818-score" class="post-score" title="current number of votes">0</div><span id="post-13818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>when i open a cap with the wireshark(ver after 1.413) i cannot key-in any words in filter i must wait 1-3 min to key-in any words in filter my pc win7 32bit Language ch</p><p><img src="https://osqa-ask.wireshark.org/upfiles/1.413.jpg" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/1.6.10.jpg" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/1.82.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '12, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/9f271dbc1840d5307035613db8920be0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jin_lost&#39;s gravatar image" /><p><span>jin_lost</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jin_lost has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Aug '12, 20:13</strong> </span></p></div></div><div id="comments-container-13818" class="comments-container"><span id="13821"></span><div id="comment-13821" class="comment"><div id="post-13821-score" class="comment-score"></div><div class="comment-text"><p>to clarify it:</p><ul><li>you open a capture file</li><li>wireshark loads the whole file and displays packets in the packet list</li><li>you cannot enter a display filter for up to 1-3 minutes, as the display filter field does not react on key strokes?</li></ul><p>Is that correct?</p></div><div id="comment-13821-info" class="comment-info"><span class="comment-age">(22 Aug '12, 10:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="13824"></span><div id="comment-13824" class="comment"><div id="post-13824-score" class="comment-score"></div><div class="comment-text"><p>How large is the file that you're loading?</p><p>Is there a dialog box visible while you're waiting?</p><p>Have you tried the latest version of Wireshark (1.8.2)?</p></div><div id="comment-13824-info" class="comment-info"><span class="comment-age">(22 Aug '12, 11:54)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="14309"></span><div id="comment-14309" class="comment"><div id="post-14309-score" class="comment-score"></div><div class="comment-text"><p>I meet the same problem too....</p></div><div id="comment-14309-info" class="comment-info"><span class="comment-age">(16 Sep '12, 19:52)</span> <span class="comment-user userinfo">iSunky</span></div></div></div><div id="comment-tools-13818" class="comment-tools"></div><div class="clear"></div><div id="comment-13818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16826"></span>

<div id="answer-container-16826" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16826-score" class="post-score" title="current number of votes">0</div><span id="post-16826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I found a solution. Try to right click on the filter bar and change Input Methods to None. It seems to work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '12, 19:38</strong></p><img src="https://secure.gravatar.com/avatar/704154f4b0a8d88bd339ec3502d86b05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tydd&#39;s gravatar image" /><p><span>tydd</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tydd has no accepted answers">0%</span></p></img></div></div><div id="comments-container-16826" class="comments-container"></div><div id="comment-tools-16826" class="comment-tools"></div><div class="clear"></div><div id="comment-16826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

