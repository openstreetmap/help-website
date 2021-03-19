+++
type = "question"
title = "Wireshark IO Graph"
description = '''Can we present tcp streams in wireshark IO Graph? '''
date = "2013-06-13T01:33:00Z"
lastmod = "2013-06-14T06:19:00Z"
weight = 21992
keywords = [ "graph", "io", "wireshark" ]
aliases = [ "/questions/21992" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark IO Graph](/questions/21992/wireshark-io-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21992-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21992-score" class="post-score" title="current number of votes">0</div><span id="post-21992-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can we present tcp streams in wireshark IO Graph?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-io" rel="tag" title="see questions tagged &#39;io&#39;">io</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '13, 01:33</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p><span>kishan pandey</span><br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-21992" class="comments-container"></div><div id="comment-tools-21992" class="comment-tools"></div><div class="clear"></div><div id="comment-21992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21995"></span>

<div id="answer-container-21995" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21995-score" class="post-score" title="current number of votes">0</div><span id="post-21995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not exactly sure what you are asking for, so here we go:</p><p>If you are asking for an IO graph for one stream:</p><ul><li>open the IO graph: Statistics -&gt; IO graph</li><li>enter the filter for your stream: tcp.stream == 1</li><li>select the unit (packets/tick or Bits/tick)</li><li>draw the graph</li></ul><p>If you are asking for an IO graph for all tcp streams:</p><ul><li>do the same as above, with a different filter: tcp</li></ul><p>If neither of the above is what you want/need, please add more details.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '13, 03:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-21995" class="comments-container"><span id="22005"></span><div id="comment-22005" class="comment"><div id="post-22005-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,when adding filter with tcp.stream eq 1 i can just see the flat line or rather say it doesnt show the graph.</p></div><div id="comment-22005-info" class="comment-info"><span class="comment-age">(13 Jun '13, 05:08)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="22006"></span><div id="comment-22006" class="comment"><div id="post-22006-score" class="comment-score"></div><div class="comment-text"><p>are you sure that</p><ul><li>there is a stream nr. 1</li><li>there are enough packets in the stream to draw anything</li><li>you pressed the "Graph 1" button</li></ul></div><div id="comment-22006-info" class="comment-info"><span class="comment-age">(13 Jun '13, 06:06)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22011"></span><div id="comment-22011" class="comment"><div id="post-22011-score" class="comment-score"></div><div class="comment-text"><p>yes infact there are too many packets but only flat horizontal line is showing.</p></div><div id="comment-22011-info" class="comment-info"><span class="comment-age">(13 Jun '13, 06:40)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="22015"></span><div id="comment-22015" class="comment"><div id="post-22015-score" class="comment-score"></div><div class="comment-text"><p>can you please add a screenshot of the IO graph window to your question? Did you try to change the Scale: settings?</p><p>BTW: What is your Wireshark version and OS?</p></div><div id="comment-22015-info" class="comment-info"><span class="comment-age">(13 Jun '13, 07:15)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22057"></span><div id="comment-22057" class="comment"><div id="post-22057-score" class="comment-score"></div><div class="comment-text"><p>Thanks kurt now i got it.</p></div><div id="comment-22057-info" class="comment-info"><span class="comment-age">(14 Jun '13, 06:03)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="22058"></span><div id="comment-22058" class="comment not_top_scorer"><div id="post-22058-score" class="comment-score"></div><div class="comment-text"><p>good!</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-22058-info" class="comment-info"><span class="comment-age">(14 Jun '13, 06:19)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-21995" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-21995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22030"></span>

<div id="answer-container-22030" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22030-score" class="post-score" title="current number of votes">0</div><span id="post-22030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Select a packet of the desired tcp session in the desired direction and go to</p><p>Statistics -&gt; TCP StreamGraph -&gt; Time Sequence Graph (Stevens) and you'll get the increments of the sequencenumbers over the time. <img src="https://osqa-ask.wireshark.org/upfiles/tcpstream.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '13, 14:33</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-22030" class="comments-container"></div><div id="comment-tools-22030" class="comment-tools"></div><div class="clear"></div><div id="comment-22030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

