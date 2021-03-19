+++
type = "question"
title = "Follow tcp stream showing incorrect HTTP payload"
description = '''I have a single TCP flow in a pcap. &quot;Follow --&amp;gt; TCP Stream&quot; seems to be showing the wrong HTTP payload in Wireshark 2.2.1 (Win7-64 SP1). (But all 23 packets seem to be shown correctly; it&#x27;s just the payload decode that seems to be incorrect.)   Is this a known bug? I searched but didn&#x27;t find an e...'''
date = "2016-10-17T09:17:00Z"
lastmod = "2016-10-17T12:30:00Z"
weight = 56471
keywords = [ "follow.tcp.stream", "http" ]
aliases = [ "/questions/56471" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Follow tcp stream showing incorrect HTTP payload](/questions/56471/follow-tcp-stream-showing-incorrect-http-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56471-score" class="post-score" title="current number of votes">0</div><span id="post-56471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a single TCP flow in a pcap. "Follow --&gt; TCP Stream" seems to be showing the wrong HTTP payload in Wireshark 2.2.1 (Win7-64 SP1). (But all 23 packets seem to be shown correctly; it's just the payload decode that seems to be incorrect.)<br />
<img src="https://osqa-ask.wireshark.org/upfiles/Wireshark2.2.1-Win7-shot1_qmLum5c.png" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/Wireshark2.2.1-Win7-shot2_GMnFepm.png" alt="alt text" /></p><p>Is this a known bug? I searched but didn't find an existing defect. Anyone else observed something similar?</p><p>Note, "Follow --&gt; TCP Stream" does seem to work correctly in Wireshark 2.0.1 (Mac OSX 10.11.6). <img src="https://osqa-ask.wireshark.org/upfiles/Wireshark2.0.1-Mac.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-follow.tcp.stream" rel="tag" title="see questions tagged &#39;follow.tcp.stream&#39;">follow.tcp.stream</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '16, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/fe8d839d303ac5484d9d834f812726ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wwwalker&#39;s gravatar image" /><p><span>wwwalker</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wwwalker has no accepted answers">0%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Oct '16, 09:23</strong> </span></p></div></div><div id="comments-container-56471" class="comments-container"></div><div id="comment-tools-56471" class="comment-tools"></div><div class="clear"></div><div id="comment-56471-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56476"></span>

<div id="answer-container-56476" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56476-score" class="post-score" title="current number of votes">2</div><span id="post-56476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wwwalker has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like you're running into <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12855">bug 12855</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '16, 12:30</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></img></div></div><div id="comments-container-56476" class="comments-container"></div><div id="comment-tools-56476" class="comment-tools"></div><div class="clear"></div><div id="comment-56476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

