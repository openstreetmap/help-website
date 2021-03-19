+++
type = "question"
title = "Making a dissector that filters packets"
description = '''Hi! What I wonder is, how can you make so that your dissector compares the next packet to the previous one? I want to make so that if the next packet has the same data as the previous one, it wont be displayed. I dont want to show a large amount of packtes in a row that are identical, I only want to...'''
date = "2012-04-09T01:09:00Z"
lastmod = "2012-04-09T02:02:00Z"
weight = 10022
keywords = [ "filter", "compare", "dissector", "packet", "wireshark" ]
aliases = [ "/questions/10022" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Making a dissector that filters packets](/questions/10022/making-a-dissector-that-filters-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10022-score" class="post-score" title="current number of votes">0</div><span id="post-10022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! What I wonder is, how can you make so that your dissector compares the next packet to the previous one? I want to make so that if the next packet has the same data as the previous one, it wont be displayed. I dont want to show a large amount of packtes in a row that are identical, I only want to show packets where some change has been made to the data.</p><p>Anyone knows?</p><p>Cheers / Martino</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-compare" rel="tag" title="see questions tagged &#39;compare&#39;">compare</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '12, 01:09</strong></p><img src="https://secure.gravatar.com/avatar/90140f74d53512910ba33db4ef7d30de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Martino&#39;s gravatar image" /><p><span>Martino</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Martino has no accepted answers">0%</span></p></div></div><div id="comments-container-10022" class="comments-container"></div><div id="comment-tools-10022" class="comment-tools"></div><div class="clear"></div><div id="comment-10022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10025"></span>

<div id="answer-container-10025" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10025-score" class="post-score" title="current number of votes">1</div><span id="post-10025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't make a dissector decide whether a frame will be displayed or not, that is only possible through display filters. But you can make them work together.</p><p>For example, if you create a field in your dissector that is only present if the packet is different from the previous packet in the same conversation, then you can filter in that field with a display filter.</p><p>For this to work, you need to work with "conversations" and "per-packet" data. See paragraph 2.2.1 and 2.5 in <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/README.developer?revision=41400&amp;view=markup">"doc/README.developer"</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '12, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-10025" class="comments-container"></div><div id="comment-tools-10025" class="comment-tools"></div><div class="clear"></div><div id="comment-10025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

