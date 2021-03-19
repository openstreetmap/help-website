+++
type = "question"
title = "delete/edit display filter history"
description = '''how can I clear the display filter history in the dropdown box? It&#x27;s easy to delete saved filters but not apparent how to edit/delete the history.'''
date = "2010-10-11T19:37:00Z"
lastmod = "2010-10-12T07:28:00Z"
weight = 479
keywords = [ "filters", "history" ]
aliases = [ "/questions/479" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [delete/edit display filter history](/questions/479/deleteedit-display-filter-history)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-479-score" class="post-score" title="current number of votes">0</div><span id="post-479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how can I clear the display filter history in the dropdown box? It's easy to delete saved filters but not apparent how to edit/delete the history.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filters" rel="tag" title="see questions tagged &#39;filters&#39;">filters</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '10, 19:37</strong></p><img src="https://secure.gravatar.com/avatar/bcf711a40000b9ef4623f12fad6c56c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ziplock&#39;s gravatar image" /><p><span>ziplock</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ziplock has no accepted answers">0%</span></p></div></div><div id="comments-container-479" class="comments-container"></div><div id="comment-tools-479" class="comment-tools"></div><div class="clear"></div><div id="comment-479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="482"></span>

<div id="answer-container-482" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-482-score" class="post-score" title="current number of votes">2</div><span id="post-482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ziplock has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is no functionality within Wireshark to edit/delete the filters in the display filter history. However, the entries are saved in the file "recent_common" in your personal preferences folder (see "Help -&gt; About wireshark -&gt; Folders" for the location of this folder on your system).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '10, 23:05</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-482" class="comments-container"></div><div id="comment-tools-482" class="comment-tools"></div><div class="clear"></div><div id="comment-482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="481"></span>

<div id="answer-container-481" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-481-score" class="post-score" title="current number of votes">1</div><span id="post-481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go to<br />
Edit -&gt; Preferences...<br />
Change the number at Filter display max. list entries: 10<br />
Click Apply and OK<br />
<br />
</p><p>Or change the Preferences file.<br />
C:\Users\user\AppData\Roaming\Wireshark\Preferences or look for the file location at<br />
Help -&gt; About wireshark -&gt; Folders<br />
</p><p>Change the number at:<br />
# The max. number of entries in the display filter list.<br />
# A decimal number.<br />
gui.recent_display_filter_entries.max: 10</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '10, 21:16</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Oct '10, 21:46</strong> </span></p></div></div><div id="comments-container-481" class="comments-container"></div><div id="comment-tools-481" class="comment-tools"></div><div class="clear"></div><div id="comment-481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="489"></span>

<div id="answer-container-489" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-489-score" class="post-score" title="current number of votes">0</div><span id="post-489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Got it, thanks!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '10, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/bcf711a40000b9ef4623f12fad6c56c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ziplock&#39;s gravatar image" /><p><span>ziplock</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ziplock has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-489" class="comments-container"></div><div id="comment-tools-489" class="comment-tools"></div><div class="clear"></div><div id="comment-489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

