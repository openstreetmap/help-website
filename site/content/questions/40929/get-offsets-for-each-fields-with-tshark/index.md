+++
type = "question"
title = "Get offsets for each fields with tshark"
description = '''Tshark command like  tshark -r &amp;lt;pcapFile&amp;gt; -V -P  can produce detailed info about fields of a packet and the output can be piped to other application for some processing. Wonder if it&#x27;s possible to get information on offsets of each fields in addition. This is an analogy to wireshark where you ...'''
date = "2015-03-26T20:34:00Z"
lastmod = "2015-05-07T11:57:00Z"
weight = 40929
keywords = [ "tshark" ]
aliases = [ "/questions/40929" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Get offsets for each fields with tshark](/questions/40929/get-offsets-for-each-fields-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40929-score" class="post-score" title="current number of votes">0</div><span id="post-40929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Tshark command like</p><pre><code>tshark -r &lt;pcapFile&gt; -V -P</code></pre><p>can produce detailed info about fields of a packet and the output can be piped to other application for some processing. Wonder if it's possible to get information on offsets of each fields in addition. This is an analogy to wireshark where you click a decoded field, the relevant bytes in the pcap got highlighted.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '15, 20:34</strong></p><img src="https://secure.gravatar.com/avatar/0228802baecfa9b8d8764a043fea883b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sharkfun&#39;s gravatar image" /><p><span>sharkfun</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sharkfun has no accepted answers">0%</span></p></div></div><div id="comments-container-40929" class="comments-container"></div><div id="comment-tools-40929" class="comment-tools"></div><div class="clear"></div><div id="comment-40929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41001"></span>

<div id="answer-container-41001" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41001-score" class="post-score" title="current number of votes">0</div><span id="post-41001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sharkfun has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's not possible with the current release. It would require a code change. If you want/need that feature, please file an enhancement bug at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '15, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-41001" class="comments-container"><span id="41007"></span><div id="comment-41007" class="comment"><div id="post-41007-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt, I created a ticket on this.</p></div><div id="comment-41007-info" class="comment-info"><span class="comment-age">(30 Mar '15, 06:43)</span> <span class="comment-user userinfo">sharkfun</span></div></div><span id="41008"></span><div id="comment-41008" class="comment"><div id="post-41008-score" class="comment-score"></div><div class="comment-text"><p>Please post the bug ID or the link here for other users.</p></div><div id="comment-41008-info" class="comment-info"><span class="comment-age">(30 Mar '15, 06:52)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="42192"></span><div id="comment-42192" class="comment"><div id="post-42192-score" class="comment-score"></div><div class="comment-text"><p>Sorry didn't see this comment earlier. The bug ID is 11097. Thanks.</p></div><div id="comment-42192-info" class="comment-info"><span class="comment-age">(07 May '15, 11:57)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-41001" class="comment-tools"></div><div class="clear"></div><div id="comment-41001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

