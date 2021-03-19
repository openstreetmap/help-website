+++
type = "question"
title = "How do we start analyzing TCP Traffic."
description = '''Hi , I am often confused how do we start to analyze the TCP traffic, I have trace file attached.Can any one guide how do we start.I usually do .Analyze &amp;gt; Export Info Composite. Here i See   TCP Out of Order Previous Segment Lost Fast Re transmission suspected  So i do start.....Now IP : 10.45.56....'''
date = "2012-08-19T08:53:00Z"
lastmod = "2012-08-20T00:55:00Z"
weight = 13741
keywords = [ "smpp", "prev_seg_lost", "newbie", "out-of-order", "tcp" ]
aliases = [ "/questions/13741" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do we start analyzing TCP Traffic.](/questions/13741/how-do-we-start-analyzing-tcp-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13741-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,</p><p>I am often confused how do we start to analyze the TCP traffic, I have trace file attached.Can any one guide how do we start.I usually do .Analyze &gt; Export Info Composite.</p><p>Here i See</p><ol><li>TCP Out of Order</li><li>Previous Segment Lost</li><li>Fast Re transmission suspected</li></ol><p>So i do start.....Now IP : 10.45.56.8 is at our end....</p><p>I am very thankfull in advance for the Guidance given.</p><p><a href="http://www.cloudshark.org/captures/58ef6d4b5ad3">http://www.cloudshark.org/captures/58ef6d4b5ad3</a></p></div><div id="question-tags" class="tags-container tags">smpp prev_seg_lost newbie out-of-order tcp</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '12, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/ea81afbd71dc63ea6a6506203bc83c3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="creative&#39;s gravatar image" /><p>creative<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="creative has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Aug '12, 09:26</p></div></div><div id="comments-container-13741" class="comments-container"></div><div id="comment-tools-13741" class="comment-tools"></div><div class="clear"></div><div id="comment-13741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13745"></span>

<div id="answer-container-13745" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13745-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could start by filtering on "tcp.analysis.flags" which will show you packets that have some kind of expert message from Wireshark. With that you can get an overview over the type of TCP trouble you may have, because to be sure you'll have to verify them.</p><p>First step, if you have a lot of retransmissions and duplicate acks would be to verify that they're not actually duplicates (meaning, they're either totally identical to a former packet, or the same packet but after routing). If you can rule out duplicates you then need to find out if the problems you see are really hurting your transmisson. I usually do not care about a couple of retransmissions that create a delay of just a few milliseconds, but it is a total different story if I see the communication being slowed down in the half second range (or more).</p><p>Another thing you should look at is the TCP window size. Make sure it stays large enough to not slow down the sender. The window size can tell you if a system is too slow when processing incoming data, so this is your best tool to prove that a system is slow, not the network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '12, 00:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13745" class="comments-container"></div><div id="comment-tools-13745" class="comment-tools"></div><div class="clear"></div><div id="comment-13745-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

