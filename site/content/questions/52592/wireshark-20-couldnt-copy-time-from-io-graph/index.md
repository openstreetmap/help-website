+++
type = "question"
title = "Wireshark 2.0 - Couldn&#x27;t copy time from I/O Graph"
description = '''Hi All, I have Wireshark 2.0.3 and when i click [copy] button in Graph I/O then [Paste] the data on Execel sheet .. i was not able to see time interval eventhough i had clicked the check box (time of day) and it is already showed in the graph.  this is what i get when copying the graph io &quot;Interval ...'''
date = "2016-05-15T06:54:00Z"
lastmod = "2017-08-01T11:35:00Z"
weight = 52592
keywords = [ "graph", "graphs", "export", "iograph" ]
aliases = [ "/questions/52592" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 2.0 - Couldn't copy time from I/O Graph](/questions/52592/wireshark-20-couldnt-copy-time-from-io-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52592-score" class="post-score" title="current number of votes">0</div><span id="post-52592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I have Wireshark 2.0.3 and when i click [copy] button in Graph I/O then [Paste] the data on Execel sheet .. i was not able to see time interval eventhough i had clicked the check box (time of day) and it is already showed in the graph.</p><p><strong>this is what i get when copying the graph io</strong> "Interval start","All Traffic" 0,29438 1,21568 2,21588 3,18276 4,17360 5,24058</p><p><strong>instead i want the following:</strong></p><p>"Interval start","All Traffic" 12:00:00,number of packets 12:00:01,number of packets</p><p>Any suggestions? Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-graphs" rel="tag" title="see questions tagged &#39;graphs&#39;">graphs</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-iograph" rel="tag" title="see questions tagged &#39;iograph&#39;">iograph</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '16, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/c2e7fd28b17fefc365eac02702384f3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mudhafar&#39;s gravatar image" /><p><span>Mudhafar</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mudhafar has one accepted answer">100%</span></p></div></div><div id="comments-container-52592" class="comments-container"><span id="54166"></span><div id="comment-54166" class="comment"><div id="post-54166-score" class="comment-score">1</div><div class="comment-text"><p>This works for me with the Gtk version of Wireshark, but not with the Qt version. Which version are you using? If you're using Qt, you could try Gtk.</p></div><div id="comment-54166-info" class="comment-info"><span class="comment-age">(19 Jul '16, 09:57)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="63271"></span><div id="comment-63271" class="comment"><div id="post-63271-score" class="comment-score"></div><div class="comment-text"><p>Thanks cmaynard, Yes it works with Gtk version only.</p></div><div id="comment-63271-info" class="comment-info"><span class="comment-age">(31 Jul '17, 22:45)</span> <span class="comment-user userinfo">Mudhafar</span></div></div></div><div id="comment-tools-52592" class="comment-tools"></div><div class="clear"></div><div id="comment-52592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63272"></span>

<div id="answer-container-63272" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63272-score" class="post-score" title="current number of votes">0</div><span id="post-63272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mudhafar has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As cmaynard said,</p><p>It works on Gtk version only, solved!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '17, 22:47</strong></p><img src="https://secure.gravatar.com/avatar/c2e7fd28b17fefc365eac02702384f3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mudhafar&#39;s gravatar image" /><p><span>Mudhafar</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mudhafar has one accepted answer">100%</span></p></div></div><div id="comments-container-63272" class="comments-container"><span id="63311"></span><div id="comment-63311" class="comment"><div id="post-63311-score" class="comment-score"></div><div class="comment-text"><p>Well, eventually Gtk won't be supported anymore so I wouldn't say this problem is solved; you're merely able to work around it ... for now. That said, I believe this problem has already been reported as <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13717">Bug 13717</a> if anyone wants to track its progress.</p></div><div id="comment-63311-info" class="comment-info"><span class="comment-age">(01 Aug '17, 11:35)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-63272" class="comment-tools"></div><div class="clear"></div><div id="comment-63272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

