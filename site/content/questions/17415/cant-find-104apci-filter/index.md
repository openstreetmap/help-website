+++
type = "question"
title = "Can&#x27;t find 104apci filter"
description = '''Hi! I have done two installations of wireshark Version 1.8.3, 32bit . One in a virtual machine (w-xp) and one in my host machine (w-7).  I want to capture telegrams for the iec 60870-5-104 protocol. I can find this filter (104apci) on the virtual machin by pressing &quot;Expression&quot; in Wireshark. But not...'''
date = "2013-01-03T08:16:00Z"
lastmod = "2013-01-04T08:43:00Z"
weight = 17415
keywords = [ "104apci" ]
aliases = [ "/questions/17415" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't find 104apci filter](/questions/17415/cant-find-104apci-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17415-score" class="post-score" title="current number of votes">0</div><span id="post-17415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I have done two installations of wireshark Version 1.8.3, 32bit . One in a virtual machine (w-xp) and one in my host machine (w-7).</p><p>I want to capture telegrams for the iec 60870-5-104 protocol. I can find this filter (104apci) on the virtual machin by pressing "Expression" in Wireshark. But not on the host machine.</p><p>I have used the same installation files. How can I get that filter on my host machine?</p><p>Regards, Wolfgang</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-104apci" rel="tag" title="see questions tagged &#39;104apci&#39;">104apci</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jan '13, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/7760a40995cb7f1771d6638f23b1ee81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wolfgangQQQ&#39;s gravatar image" /><p><span>wolfgangQQQ</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wolfgangQQQ has no accepted answers">0%</span></p></div></div><div id="comments-container-17415" class="comments-container"></div><div id="comment-tools-17415" class="comment-tools"></div><div class="clear"></div><div id="comment-17415-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17416"></span>

<div id="answer-container-17416" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17416-score" class="post-score" title="current number of votes">0</div><span id="post-17416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I can find this filter (104apci) on the virtual machin by pressing "Expression" in Wireshark. But not on the host machine.</p></blockquote><p>That happens when the protocol is disabled. Please enable it on the host machine.</p><blockquote><p><code>Analyze -&gt; Enabled Protocols -&gt; 104acpi</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '13, 09:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-17416" class="comments-container"><span id="17441"></span><div id="comment-17441" class="comment"><div id="post-17441-score" class="comment-score"></div><div class="comment-text"><p>Thanks! It works fine now /Wolfgang</p></div><div id="comment-17441-info" class="comment-info"><span class="comment-age">(04 Jan '13, 07:07)</span> <span class="comment-user userinfo">wolfgangQQQ</span></div></div><span id="17443"></span><div id="comment-17443" class="comment"><div id="post-17443-score" class="comment-score"></div><div class="comment-text"><p>Good!</p><p><strong>Hint</strong>: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-17443-info" class="comment-info"><span class="comment-age">(04 Jan '13, 08:43)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-17416" class="comment-tools"></div><div class="clear"></div><div id="comment-17416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

