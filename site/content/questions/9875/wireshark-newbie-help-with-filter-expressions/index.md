+++
type = "question"
title = "WireShark newbie. Help with filter expressions."
description = '''I am very new to WS. Have a general grasp of things but building expressions to use in a filter is giving me a lot of heartburn. Could someone please help me. Please remember I am not tech savvy.  I need an expression for a capture filter that will do the following: 1) Capture TCP protocol and 2) Fi...'''
date = "2012-03-31T08:51:00Z"
lastmod = "2012-03-31T09:47:00Z"
weight = 9875
keywords = [ "capture-filter" ]
aliases = [ "/questions/9875" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [WireShark newbie. Help with filter expressions.](/questions/9875/wireshark-newbie-help-with-filter-expressions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9875-score" class="post-score" title="current number of votes">0</div><span id="post-9875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am very new to WS. Have a general grasp of things but building expressions to use in a filter is giving me a lot of heartburn. Could someone please help me. Please remember I am not tech savvy.<br />
</p><p>I need an expression for a capture filter that will do the following: 1) Capture TCP protocol and 2) Filter for ports 9501 to 9505 and 3) Filter unique source IP addresses</p><p>I am able to go as far as TCP port 9501 ok but including remaining ports and filtering unique address is proving to be frustrating.</p><p>Thanks in advance...Carlos</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '12, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/9ee79fe3154bbe4ca7f8ec5df28da05f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cafeics&#39;s gravatar image" /><p><span>cafeics</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cafeics has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-9875" class="comments-container"></div><div id="comment-tools-9875" class="comment-tools"></div><div class="clear"></div><div id="comment-9875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9877"></span>

<div id="answer-container-9877" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9877-score" class="post-score" title="current number of votes">4</div><span id="post-9877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To provide a concrete example, I'll assume the source IP address of the host you want to filter on is 192.168.1.1. In this case, you can use the following filter:</p><pre><code>tcp portrange 9501-9505 and ip src host 192.168.1.1</code></pre><p>If you want your capture filter to match more than one IP address, then you can <em><code>or</code></em> them together as follows:</p><pre><code>tcp portrange 9501-9505 and (ip src host 192.168.1.1 or ip src host 192.168.1.2 or ...)</code></pre><p>For more help on capture filters, refer to the <a href="http://www.manpagez.com/man/7/pcap-filter/">pcap-filter</a> man page. The Wireshark <a href="http://wiki.wireshark.org/CaptureFilters">CaptureFilters</a> wiki page also has some examples.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '12, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-9877" class="comments-container"></div><div id="comment-tools-9877" class="comment-tools"></div><div class="clear"></div><div id="comment-9877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

