+++
type = "question"
title = "SSL&#x27;s Handshake Dissecting"
description = ''' In the attached Wireshark window, I&#x27;m wondering why the Change Cipher Spec and Encrypted Handshake Message are displayed in two separate packets (19 and 20). While they are displayed in one packet number (22). Thank you. '''
date = "2014-08-27T15:26:00Z"
lastmod = "2014-10-21T03:24:00Z"
weight = 35822
keywords = [ "ssl", "handshake", "dissector", "wireshark" ]
aliases = [ "/questions/35822" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [SSL's Handshake Dissecting](/questions/35822/ssls-handshake-dissecting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35822-score" class="post-score" title="current number of votes">0</div><span id="post-35822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_-_14-08-27_-_05:13:55_PM.png" alt="alt text" /></p><p>In the attached Wireshark window, I'm wondering why the <strong>Change Cipher Spec</strong> and <strong>Encrypted Handshake Message</strong> are displayed in two separate packets (19 and 20). While they are displayed in one packet number (22).</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-handshake" rel="tag" title="see questions tagged &#39;handshake&#39;">handshake</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '14, 15:26</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p><span>flora</span><br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Aug '14, 15:27</strong> </span></p></div></div><div id="comments-container-35822" class="comments-container"></div><div id="comment-tools-35822" class="comment-tools"></div><div class="clear"></div><div id="comment-35822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35836"></span>

<div id="answer-container-35836" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35836-score" class="post-score" title="current number of votes">1</div><span id="post-35836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flora has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your looking at messages from the client to the server (frames 19 &amp; 20) that each contain an individual record and a message from the server to the client (frame 22) that contains both records.</p><p>The capture was likely made at the client so you see the two records as separate frames, before the NIC likely coalesces them onto the wire, and the incoming records from the server have been coalesced into one frame.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '14, 03:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35836" class="comments-container"><span id="37219"></span><div id="comment-37219" class="comment"><div id="post-37219-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your explanation.It makes sense but I can't confirm as I didn't capture the traffic by myself and I don't have information about the capture's location. In deed, I'm interested in knowing more about how the NIC can effect the frames as it does in the given example but I'm I'm not sure what the term used to describe this in order to be able to goole it. I'd appreciate if you know it and can mention it here. Thanks.</p></div><div id="comment-37219-info" class="comment-info"><span class="comment-age">(21 Oct '14, 02:44)</span> <span class="comment-user userinfo">flora</span></div></div><span id="37222"></span><div id="comment-37222" class="comment"><div id="post-37222-score" class="comment-score"></div><div class="comment-text"><p><a href="http://en.wikipedia.org/wiki/Nagle&#39;s_algorithm">Nagle</a> can be used to coalesce small writes into one TCP segment, but it has other issues so is usually disabled by the application.</p><p>Applications can also buffer small writes and then send them to the socket in a larger chunk.</p><p>Also, various NIC drivers have offload functionality, where the driver handles all sorts of things, e.g. checksums, and depending on where in the stack the capture is made then different things will be visible in the capture. See <span>@jasper</span> blog <a href="http://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/">article</a> on capturing locally on the target machines.</p></div><div id="comment-37222-info" class="comment-info"><span class="comment-age">(21 Oct '14, 03:24)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-35836" class="comment-tools"></div><div class="clear"></div><div id="comment-35836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

