+++
type = "question"
title = "When I do a filter for my QoS packets using ip.dsfield.dscp==46 I also get DSCP 22 packets"
description = '''All of the DSCP 22 packets are not expected since my filter is only for DSCP 46 packets. All of these DSCP 22 packets are ICMP, stating the destination unreachable (Port unreachable). Is there a reason these packets are being displayed? '''
date = "2015-09-16T08:38:00Z"
lastmod = "2015-09-16T10:37:00Z"
weight = 45882
keywords = [ "icmp", "ip.dsfield.dscp", "dscp", "display-filter" ]
aliases = [ "/questions/45882" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [When I do a filter for my QoS packets using ip.dsfield.dscp==46 I also get DSCP 22 packets](/questions/45882/when-i-do-a-filter-for-my-qos-packets-using-ipdsfielddscp46-i-also-get-dscp-22-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45882-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>All of the DSCP 22 packets are not expected since my filter is only for DSCP 46 packets. All of these DSCP 22 packets are ICMP, stating the destination unreachable (Port unreachable). Is there a reason these packets are being displayed?</p></div><div id="question-tags" class="tags-container tags">icmp ip.dsfield.dscp dscp display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '15, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/b114edba31957b6d4cc145712b52f3ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MotoRider&#39;s gravatar image" /><p>MotoRider<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MotoRider has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Sep '15, 10:38</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-45882" class="comments-container"></div><div id="comment-tools-45882" class="comment-tools"></div><div class="clear"></div><div id="comment-45882-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45886"></span>

<div id="answer-container-45886" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45886-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm guessing that the embedded IP part of those ICMP packets have DSCP==46, right?</p><p>This is a commonly asked question. The trick is to know/remember that the display filter <code>ip.dsfield.dscp == 46</code> means "there exists a field named <code>ip.dsfield.dscp</code> whose value is 46".</p><p>In your case the frame has 2 fields named <code>ip.dsfield.dscp</code>: one with a value of 22 (the outer IP packet) and another with a value of 46 (the IP part of the embedded ICMP packet).</p><p>There has been a lot of discussion about this type of problem, in particular to find a method to specify that you're only interested in, for example, the first occurrence of the field within the frame but so far nothing has been done.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '15, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-45886" class="comments-container"><span id="45888"></span><div id="comment-45888" class="comment"><div id="post-45888-score" class="comment-score"></div><div class="comment-text"><p>Correct, there is an embedded IP part, which does have the DSCP==46. I was expecting that it would only find the outer one and then stop, but as you say field exist elsewhere in the frame.</p></div><div id="comment-45888-info" class="comment-info"><span class="comment-age">(16 Sep '15, 14:16)</span> MotoRider</div></div><span id="45890"></span><div id="comment-45890" class="comment"><div id="post-45890-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately when I do a ip.dsfield.dscp!=48, I still get packets with 48 in the DSCP column.</p></div><div id="comment-45890-info" class="comment-info"><span class="comment-age">(16 Sep '15, 15:18)</span> MotoRider</div></div><span id="45914"></span><div id="comment-45914" class="comment"><div id="post-45914-score" class="comment-score"></div><div class="comment-text"><p>Yep, that's the same thing. The outer part has ip.dsfield.dscp!=48 so it gets included, even when the inner part has ip.dsfield.dscp==48. That's why the filter entry box is colored yellow ('this might behave differently than you expect').</p><p>The correct filter syntax is !(ip.dsfield.dscp==48)</p></div><div id="comment-45914-info" class="comment-info"><span class="comment-age">(17 Sep '15, 04:25)</span> Jaap ♦</div></div></div><div id="comment-tools-45886" class="comment-tools"></div><div class="clear"></div><div id="comment-45886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

