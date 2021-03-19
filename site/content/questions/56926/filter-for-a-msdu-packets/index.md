+++
type = "question"
title = "Filter for A-MSDU packets"
description = '''To find the percentage of A-MSDU packets in a wireless packet trace using wireshark, which filter should I use from those mentioned below? A-MDSU packets : wlan_aggregate.a_mdsu.subframe ..... filter 1 A-MSDU packets : wlan.qos.amsdupresent == 1 ..........filter 2 filter 1 shows there are 0% A-MDSU ...'''
date = "2016-11-02T06:51:00Z"
lastmod = "2016-11-04T16:07:00Z"
weight = 56926
keywords = [ "a-msdu", "packets", "wireshark" ]
aliases = [ "/questions/56926" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Filter for A-MSDU packets](/questions/56926/filter-for-a-msdu-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56926-score" class="post-score" title="current number of votes">0</div><span id="post-56926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>To find the percentage of A-MSDU packets in a wireless packet trace using wireshark, which filter should I use from those mentioned below?</p><p>A-MDSU packets : wlan_aggregate.a_mdsu.subframe ..... filter 1<br />
A-MSDU packets : wlan.qos.amsdupresent == 1 ..........filter 2</p><p>filter 1 shows there are 0% A-MDSU packets in the trace, whereas filter 2 shows there are 3.5% A-MSDU packets in the same trace.What is the difference between A-MDSU and A-MSDU and which filter is the correct filter to obtain the A-MSDU packets?</p><p>Also, how to obtain A-MPDU packets in the trace? Is the filter mentioned below correct?<br />
A-MPDU packets : radiotap.present.ampdu</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-a-msdu" rel="tag" title="see questions tagged &#39;a-msdu&#39;">a-msdu</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '16, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/af9be6f06a1796e714e11c49026054e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harshada%20Kelkar&#39;s gravatar image" /><p><span>Harshada Kelkar</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harshada Kelkar has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Nov '16, 11:47</strong> </span></p></div></div><div id="comments-container-56926" class="comments-container"></div><div id="comment-tools-56926" class="comment-tools"></div><div class="clear"></div><div id="comment-56926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56932"></span>

<div id="answer-container-56932" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56932-score" class="post-score" title="current number of votes">1</div><span id="post-56932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Harshada Kelkar has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you seen this question:</p><p><a href="https://ask.wireshark.org/questions/53848/how-to-capture-aggregated-packets-a-mpdu-a-msdu-using-wireshark?page=1&amp;focusedAnswerId=54079#54079">https://ask.wireshark.org/questions/53848/how-to-capture-aggregated-packets-a-mpdu-a-msdu-using-wireshark?page=1&amp;focusedAnswerId=54079#54079</a></p><p>I am embarrassed I don't know what an A-MDSU is. Can you provide some context? Maybe I never read that part of the 802.11 specification.<br />
</p><p>I think you want your option 2: wlan.qos.amsdupresent</p><p>To obtain A-MPDU packets, try sniffing on an an 802.11ac network - that should do. I am no expert as far as A-MPDU, but my experience is that not all drivers will populate that field, but that doesn't mean you won't obtain them. The filter might be described as how to present them in Wireshark if that field is populated.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '16, 14:35</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></br></p></div></div><div id="comments-container-56932" class="comments-container"><span id="56994"></span><div id="comment-56994" class="comment"><div id="post-56994-score" class="comment-score"></div><div class="comment-text"><p>The filter 1 mentions aggregate.a_mdsu so was confused about what a-mdsu is or what that filter does.</p><p>However thanks for the help on a-msdu and a-mpdu filters. This does answer my question. Thanks.</p></div><div id="comment-56994-info" class="comment-info"><span class="comment-age">(04 Nov '16, 12:29)</span> <span class="comment-user userinfo">Harshada Kelkar</span></div></div><span id="57001"></span><div id="comment-57001" class="comment"><div id="post-57001-score" class="comment-score"></div><div class="comment-text"><p>Can you accept the answer? Thats how the site works by voting.</p></div><div id="comment-57001-info" class="comment-info"><span class="comment-age">(04 Nov '16, 16:07)</span> <span class="comment-user userinfo">Bob Jones</span></div></div></div><div id="comment-tools-56932" class="comment-tools"></div><div class="clear"></div><div id="comment-56932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

