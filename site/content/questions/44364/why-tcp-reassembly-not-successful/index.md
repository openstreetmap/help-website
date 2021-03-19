+++
type = "question"
title = "Why TCP reassembly not successful?"
description = '''The trace with problem can be downloaded from the link below.  https://www.dropbox.com/s/rk8il8u6z73t57d/TLS.pcap?dl=0 First, decode it as SSL.  And Frame#7 is supposed to be reassembled with Frame#6. However, Frame#7 only shows &quot;TCP segment of a reassembled PDU&quot;.  Is it the issue with those two fra...'''
date = "2015-07-22T02:26:00Z"
lastmod = "2015-07-22T06:08:00Z"
weight = 44364
keywords = [ "reassembly" ]
aliases = [ "/questions/44364" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why TCP reassembly not successful?](/questions/44364/why-tcp-reassembly-not-successful)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44364-score" class="post-score" title="current number of votes">0</div><span id="post-44364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The trace with problem can be downloaded from the link below.</p><p><a href="https://www.dropbox.com/s/rk8il8u6z73t57d/TLS.pcap?dl=0">https://www.dropbox.com/s/rk8il8u6z73t57d/TLS.pcap?dl=0</a></p><p>First, decode it as SSL.</p><p>And Frame#7 is supposed to be reassembled with Frame#6. However, Frame#7 only shows "TCP segment of a reassembled PDU".</p><p>Is it the issue with those two frames? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '15, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/656b507d77afaec001faa43272047565?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="radhk&#39;s gravatar image" /><p><span>radhk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="radhk has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jul '15, 02:29</strong> </span></p></div></div><div id="comments-container-44364" class="comments-container"></div><div id="comment-tools-44364" class="comment-tools"></div><div class="clear"></div><div id="comment-44364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44367"></span>

<div id="answer-container-44367" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44367-score" class="post-score" title="current number of votes">2</div><span id="post-44367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="radhk has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What are the TCP Protocol Preference <code>Allow subdissector to reassemble TCP streams</code> or the SSL Preference <code>Reassemble SSL records spanning multiple TCP segments</code> settings? With those enabled, it reassembles for me (1.99.8).</p><p><strong>Edit:</strong></p><p>Also need to disable the TCP Preference <code>Do not call subdissectors for error packets</code>. The frames after #7 all have TCP errors and passing them into the SSL dissector breaks it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '15, 03:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jul '15, 03:42</strong> </span></p></div></div><div id="comments-container-44367" class="comments-container"><span id="44368"></span><div id="comment-44368" class="comment"><div id="post-44368-score" class="comment-score"></div><div class="comment-text"><p>Grahamb, thanks for your reply. All those options have been enabled. The reassembly works with other traces but not this one. Thanks.</p></div><div id="comment-44368-info" class="comment-info"><span class="comment-age">(22 Jul '15, 03:15)</span> <span class="comment-user userinfo">radhk</span></div></div><span id="44369"></span><div id="comment-44369" class="comment"><div id="post-44369-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark, and what OS?</p></div><div id="comment-44369-info" class="comment-info"><span class="comment-age">(22 Jul '15, 03:30)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="44370"></span><div id="comment-44370" class="comment"><div id="post-44370-score" class="comment-score"></div><div class="comment-text"><p>See the edit to my answer.</p></div><div id="comment-44370-info" class="comment-info"><span class="comment-age">(22 Jul '15, 03:37)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="44372"></span><div id="comment-44372" class="comment"><div id="post-44372-score" class="comment-score"></div><div class="comment-text"><p>Grahamb, great. Now, it works after enabling, "Do not call subdissectors for error packets".</p></div><div id="comment-44372-info" class="comment-info"><span class="comment-age">(22 Jul '15, 05:51)</span> <span class="comment-user userinfo">radhk</span></div></div><span id="44373"></span><div id="comment-44373" class="comment"><div id="post-44373-score" class="comment-score"></div><div class="comment-text"><p><span>@radhk</span></p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-44373-info" class="comment-info"><span class="comment-age">(22 Jul '15, 06:08)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-44367" class="comment-tools"></div><div class="clear"></div><div id="comment-44367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

