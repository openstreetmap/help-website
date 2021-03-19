+++
type = "question"
title = "Call_dissector?"
description = '''Hello, I&#x27;m developing a plugin for Wireshark. I&#x27;m trying to understand the 802.15.4 dissector and I would like to know, where is &quot;call_dissector&quot; function defined? And if it&#x27;s possible to have a reference of the functions that Wireshark implements and where are defined? Thanks,'''
date = "2013-11-25T02:40:00Z"
lastmod = "2013-11-27T01:35:00Z"
weight = 27337
keywords = [ "802.15.4", "dissector", "call", "wireshark" ]
aliases = [ "/questions/27337" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Call\_dissector?](/questions/27337/call_dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27337-score" class="post-score" title="current number of votes">0</div><span id="post-27337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm developing a plugin for Wireshark. I'm trying to understand the 802.15.4 dissector and I would like to know, where is "<code>call_dissector</code>" function defined? And if it's possible to have a reference of the functions that Wireshark implements and where are defined?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-802.15.4" rel="tag" title="see questions tagged &#39;802.15.4&#39;">802.15.4</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-call" rel="tag" title="see questions tagged &#39;call&#39;">call</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '13, 02:40</strong></p><img src="https://secure.gravatar.com/avatar/347a473627a1c8b558663368d033097c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lina&#39;s gravatar image" /><p><span>lina</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lina has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Nov '13, 06:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-27337" class="comments-container"></div><div id="comment-tools-27337" class="comment-tools"></div><div class="clear"></div><div id="comment-27337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27348"></span>

<div id="answer-container-27348" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27348-score" class="post-score" title="current number of votes">1</div><span id="post-27348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <code>call_dissector</code> function is defined in <code>epan/packet.c</code>. In <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/packet.c?revision=53559&amp;view=markup">revision 53559</a>, the current revision as of this writing, you can find it defined from lines 2137-2142.</p><p>The best reference for Wireshark is the source files themselves. Most of the core dissection-related code is in the <code>epan/</code> directory. Run something like, "<code>tree -d</code>" to get a general idea of the directory layout. Use your favorite search tool, (e.g., <code>grep</code>) to help you find what you're looking for. The more you work with the sources, the easier it is to find everything.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '13, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-27348" class="comments-container"><span id="27389"></span><div id="comment-27389" class="comment"><div id="post-27389-score" class="comment-score"></div><div class="comment-text"><p>Thanks cmaynard!</p></div><div id="comment-27389-info" class="comment-info"><span class="comment-age">(26 Nov '13, 02:09)</span> <span class="comment-user userinfo">lina</span></div></div><span id="27399"></span><div id="comment-27399" class="comment"><div id="post-27399-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-27399-info" class="comment-info"><span class="comment-age">(26 Nov '13, 03:25)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-27348" class="comment-tools"></div><div class="clear"></div><div id="comment-27348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27473"></span>

<div id="answer-container-27473" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27473-score" class="post-score" title="current number of votes">0</div><span id="post-27473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I've found this:</p><p><a href="http://www.wireshark.org/docs/wsar_html/epan/group__packet.html">http://www.wireshark.org/docs/wsar_html/epan/group__packet.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '13, 01:35</strong></p><img src="https://secure.gravatar.com/avatar/347a473627a1c8b558663368d033097c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lina&#39;s gravatar image" /><p><span>lina</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lina has no accepted answers">0%</span></p></div></div><div id="comments-container-27473" class="comments-container"></div><div id="comment-tools-27473" class="comment-tools"></div><div class="clear"></div><div id="comment-27473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

