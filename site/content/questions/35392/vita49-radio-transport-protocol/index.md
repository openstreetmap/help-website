+++
type = "question"
title = "VITA49 radio transport protocol"
description = '''How to analyse VITA49 radio transport protocol on wireshark?'''
date = "2014-08-11T02:10:00Z"
lastmod = "2014-08-11T08:16:00Z"
weight = 35392
keywords = [ "vita49", "wireshark" ]
aliases = [ "/questions/35392" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [VITA49 radio transport protocol](/questions/35392/vita49-radio-transport-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35392-score" class="post-score" title="current number of votes">0</div><span id="post-35392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to analyse VITA49 radio transport protocol on wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vita49" rel="tag" title="see questions tagged &#39;vita49&#39;">vita49</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '14, 02:10</strong></p><img src="https://secure.gravatar.com/avatar/0897aab5f1379239c665d37d5c663383?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bhavika&#39;s gravatar image" /><p><span>Bhavika</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bhavika has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Aug '14, 11:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-35392" class="comments-container"></div><div id="comment-tools-35392" class="comment-tools"></div><div class="clear"></div><div id="comment-35392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35407"></span>

<div id="answer-container-35407" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35407-score" class="post-score" title="current number of votes">2</div><span id="post-35407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Actually it looks like Wireshark does support it since version 1.10.0. The changes came in via bugs <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8506">8506</a> and <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8507">8507</a>.</p><p><strong>Edit:</strong> Oh, as for the actual question of <em>how</em> to decode the traffic, Wireshark expects to see the traffic on UDP port 4991. If your traffic is not on that port you should adjust the dissector's preference (Edit-&gt;Preferences-&gt;Protocols-&gt;Vita 49 and change the port number appropriately).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '14, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Aug '14, 11:27</strong> </span></p></div></div><div id="comments-container-35407" class="comments-container"></div><div id="comment-tools-35407" class="comment-tools"></div><div class="clear"></div><div id="comment-35407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35396"></span>

<div id="answer-container-35396" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35396-score" class="post-score" title="current number of votes">0</div><span id="post-35396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By adding a dissector for it or looking at the data if the transport protocol used e.g there is no dissector for that protocol as far as I know.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '14, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-35396" class="comments-container"></div><div id="comment-tools-35396" class="comment-tools"></div><div class="clear"></div><div id="comment-35396-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

