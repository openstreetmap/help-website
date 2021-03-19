+++
type = "question"
title = "why do I see a additional Data layer above tcp?"
description = '''HI, I have a trace shows me a &quot;Data protocol&quot; as below. What is this? The application was just sending data through tcp, why there would an additional &quot;Data Layer&quot; be presented? Is it a wireshark behaivor? '''
date = "2014-08-16T07:58:00Z"
lastmod = "2014-08-17T20:40:00Z"
weight = 35510
keywords = [ "tcp" ]
aliases = [ "/questions/35510" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [why do I see a additional Data layer above tcp?](/questions/35510/why-do-i-see-a-additional-data-layer-above-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35510-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35510-score" class="post-score" title="current number of votes">0</div><span id="post-35510-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI,</p><p>I have a trace shows me a "Data protocol" as below. What is this? The application was just sending data through tcp, why there would an additional "Data Layer" be presented? Is it a wireshark behaivor? <img src="https://osqa-ask.wireshark.org/upfiles/8-16-2014_10-54-39_PM.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '14, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p><span>SteveZhou</span><br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></img></div></div><div id="comments-container-35510" class="comments-container"></div><div id="comment-tools-35510" class="comment-tools"></div><div class="clear"></div><div id="comment-35510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35512"></span>

<div id="answer-container-35512" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35512-score" class="post-score" title="current number of votes">2</div><span id="post-35512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SteveZhou has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, there should be <em>something</em> above TCP since TCP is a transport protocol and is it presumably transporting some sort of data. Of course the TCP packets with no data--such as connection establishment, connection teardown, and pure acknowledgment packets--won't have anything above TCP.</p><p>However, when Wireshark identifies something as "Data," it really means "unidentified." Normally you should see the higher layer protocol listed: HTTP, SMTP, POP, Telnet, FTP, etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '14, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-35512" class="comments-container"><span id="35513"></span><div id="comment-35513" class="comment"><div id="post-35513-score" class="comment-score">1</div><div class="comment-text"><p>I.e., the data layer is showing the data being sent through TCP. That data isn't considered part of the TCP protocol, it's part of some <em>other</em> protocol and, in this case, Wireshark can't determine what that protocol is and hasn't been told by the user what protocol it is, so it just shows it as raw data.</p></div><div id="comment-35513-info" class="comment-info"><span class="comment-age">(16 Aug '14, 15:24)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="35520"></span><div id="comment-35520" class="comment"><div id="post-35520-score" class="comment-score"></div><div class="comment-text"><p>thank you!</p></div><div id="comment-35520-info" class="comment-info"><span class="comment-age">(17 Aug '14, 20:40)</span> <span class="comment-user userinfo">SteveZhou</span></div></div></div><div id="comment-tools-35512" class="comment-tools"></div><div class="clear"></div><div id="comment-35512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

