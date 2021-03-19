+++
type = "question"
title = "get packet from wireshark from CET time 16::00 to 17::00"
description = '''i want to write the filter to get packets in a time slice; and it seems wireshark use GMT time. and so how to write the filer?'''
date = "2012-10-13T20:41:00Z"
lastmod = "2013-02-15T06:32:00Z"
weight = 14995
keywords = [ "time" ]
aliases = [ "/questions/14995" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [get packet from wireshark from CET time 16::00 to 17::00](/questions/14995/get-packet-from-wireshark-from-cet-time-1600-to-1700)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14995-score" class="post-score" title="current number of votes">0</div><span id="post-14995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i want to write the filter to get packets in a time slice; and it seems wireshark use GMT time. and so how to write the filer?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '12, 20:41</strong></p><img src="https://secure.gravatar.com/avatar/c44c38834d429d06c537c451e6a4a119?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="boyxiaolong&#39;s gravatar image" /><p><span>boyxiaolong</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="boyxiaolong has no accepted answers">0%</span></p></div></div><div id="comments-container-14995" class="comments-container"><span id="15017"></span><div id="comment-15017" class="comment"><div id="post-15017-score" class="comment-score"></div><div class="comment-text"><p>The UI is localized to your timezone by default. Unless you change it to display absolute time. But I don't quite understand your question. Are you talking about a display filter?<br />
</p><p>And of course there's just the "manually adjust your time" option.</p></div><div id="comment-15017-info" class="comment-info"><span class="comment-age">(15 Oct '12, 07:31)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-14995" class="comment-tools"></div><div class="clear"></div><div id="comment-14995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15024"></span>

<div id="answer-container-15024" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15024-score" class="post-score" title="current number of votes">1</div><span id="post-15024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Select any packet in the Packet List. Expand the Frame section in the Packet Details pane. Right-click on Arrival Time and select Prepare a Filter &gt; Selected. You will get something like this in the display filter field:</p><p>frame.time == "Oct 15, 2012 16:36:01.009638000"</p><p>Edit this display filter. Change the "==" to "&gt;=" and change the time to the earliest time you want your display filter to show. For example:</p><p>frame.time &gt;= "Oct 15, 2012 16:00:00"</p><p>Now right-click on Arrival Time again and select Prepare a Filter &gt; And Selected. You will now have something like this:</p><p>(frame.time &gt;= "Oct 15, 2012 16:00:00") &amp;&amp; (frame.time == "Oct 15, 2012 16:36:01.009638000")</p><p>Now edit the second part of the filter. Change "==" to "&lt;=" and change the time to the latest time you want your display filter to show. For example:</p><p>(frame.time &gt;= "Oct 15, 2012 16:00:00") &amp;&amp; (frame.time &lt;= "Oct 15, 2012 17:00:00")</p><p>Click Apply. This example display filter will show all frames arriving between 16:00 and 17:00 local time on October 15th.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '12, 19:58</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span> </br></p></div></div><div id="comments-container-15024" class="comments-container"><span id="18653"></span><div id="comment-18653" class="comment"><div id="post-18653-score" class="comment-score"></div><div class="comment-text"><p>Excellent, straight forward answer. Thanks!</p></div><div id="comment-18653-info" class="comment-info"><span class="comment-age">(15 Feb '13, 06:32)</span> <span class="comment-user userinfo">MEMark</span></div></div></div><div id="comment-tools-15024" class="comment-tools"></div><div class="clear"></div><div id="comment-15024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

