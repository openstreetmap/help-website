+++
type = "question"
title = "Many hosts for capture"
description = '''Hello!  I need capture traffic from 1500 hosts. I write this rule &quot;host X.X.X.X or host X.X.X.X....... e.g.&quot;. When I try run capture with this rule I see &quot;Error&quot;. I know that this rule is correct, because with lower count of hosts this rule accepted Wireshark and programm properly done. Sometimes bi...'''
date = "2015-04-11T12:01:00Z"
lastmod = "2015-04-11T23:26:00Z"
weight = 41384
keywords = [ "many", "hosts", "for", "capture" ]
aliases = [ "/questions/41384" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Many hosts for capture](/questions/41384/many-hosts-for-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41384-score" class="post-score" title="current number of votes">0</div><span id="post-41384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! I need capture traffic from 1500 hosts. I write this rule "host X.X.X.X or host X.X.X.X....... e.g.". When I try run capture with this rule I see "Error". I know that this rule is correct, because with lower count of hosts this rule accepted Wireshark and programm properly done. Sometimes big rules correct run/done. With tshark result the same like Wireshark.</p><p>What can I do for correct working this rule? I want capture traffic with Wireshark and Tshark</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-many" rel="tag" title="see questions tagged &#39;many&#39;">many</span> <span class="post-tag tag-link-hosts" rel="tag" title="see questions tagged &#39;hosts&#39;">hosts</span> <span class="post-tag tag-link-for" rel="tag" title="see questions tagged &#39;for&#39;">for</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '15, 12:01</strong></p><img src="https://secure.gravatar.com/avatar/92e86a9f772817162dde7499f9ad6412?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aleksandr&#39;s gravatar image" /><p><span>Aleksandr</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aleksandr has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Apr '15, 12:02</strong> </span></p></div></div><div id="comments-container-41384" class="comments-container"><span id="41385"></span><div id="comment-41385" class="comment"><div id="post-41385-score" class="comment-score"></div><div class="comment-text"><p>"Error", but nothing else? Does Wireshark or TShark say what type of error it was?</p></div><div id="comment-41385-info" class="comment-info"><span class="comment-age">(11 Apr '15, 15:33)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-41384" class="comment-tools"></div><div class="clear"></div><div id="comment-41384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41389"></span>

<div id="answer-container-41389" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41389-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41389-score" class="post-score" title="current number of votes">0</div><span id="post-41389-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There was something else. Like "Coudn't find interface..." and some text in bad codepage. But early I wrote <strong>tshark -i 6 -b duration:14400 -B 50 -w D:\test.pcap "host 1.2.3.4 or host 2.3.4.5. or... e.g"</strong> and this version of rule I have this a problem. Now I writing with -f key <strong>tshark -i 6 -b duration:14400 -B 50 -w D:\test.pcap -f "host 1.2.3.4 or host 2.3.4.5. or... e.g"</strong> and this problem gone out. If this problem repeat with this key I will write here again. Thank you for your answers!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '15, 23:26</strong></p><img src="https://secure.gravatar.com/avatar/92e86a9f772817162dde7499f9ad6412?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aleksandr&#39;s gravatar image" /><p><span>Aleksandr</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aleksandr has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Apr '15, 23:28</strong> </span></p></div></div><div id="comments-container-41389" class="comments-container"></div><div id="comment-tools-41389" class="comment-tools"></div><div class="clear"></div><div id="comment-41389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

