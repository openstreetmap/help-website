+++
type = "question"
title = "Where are the Winpcap / Network Packet filter drivers located?"
description = '''I&#x27;m wondering this primarily for educational purposes. I installed Winpcap, but can&#x27;t actually find reference to it on the system. In services.msc I see no reference to Winpcap or NTP. I&#x27;m able to start the service by typing &quot;net start ntp&quot;, and it confirms that the NetGroup Packet Filter has starte...'''
date = "2015-01-08T14:01:00Z"
lastmod = "2015-01-09T12:56:00Z"
weight = 38974
keywords = [ "winpcap" ]
aliases = [ "/questions/38974" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Where are the Winpcap / Network Packet filter drivers located?](/questions/38974/where-are-the-winpcap-network-packet-filter-drivers-located)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38974-score" class="post-score" title="current number of votes">0</div><span id="post-38974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm wondering this primarily for educational purposes. I installed Winpcap, but can't actually find reference to it on the system.</p><p>In services.msc I see no reference to Winpcap or NTP.</p><p>I'm able to start the service by typing "net start ntp", and it confirms that the NetGroup Packet Filter has started. However if I type "net start" again, it generates a list of the windows services that are running, and I see no reference to the NetGroup Packet Filter which I just started and is running, nor a reference to winpcap.</p><p>So basically, I can start and stop it, and it works, but I can't actually find record of it running, as if its invisible. So how can I find it?</p><p>note: wireshark works just fine, I'm just wondering purely for my own knowledge of understanding how this service or driver can be seemingly invisibly running.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '15, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/26ff756283e1feedba661d27d697de57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mxmaniac&#39;s gravatar image" /><p><span>mxmaniac</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mxmaniac has no accepted answers">0%</span></p></div></div><div id="comments-container-38974" class="comments-container"></div><div id="comment-tools-38974" class="comment-tools"></div><div class="clear"></div><div id="comment-38974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38985"></span>

<div id="answer-container-38985" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38985-score" class="post-score" title="current number of votes">2</div><span id="post-38985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mxmaniac has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can query the status of the service with the sc.exe command (service control):</p><pre><code>sc query npf</code></pre><p>npf is the "NetGroup Packet Filter Driver" service comming with Winpcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '15, 23:07</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-38985" class="comments-container"><span id="39011"></span><div id="comment-39011" class="comment"><div id="post-39011-score" class="comment-score"></div><div class="comment-text"><p>thank you!</p></div><div id="comment-39011-info" class="comment-info"><span class="comment-age">(09 Jan '15, 12:56)</span> <span class="comment-user userinfo">mxmaniac</span></div></div></div><div id="comment-tools-38985" class="comment-tools"></div><div class="clear"></div><div id="comment-38985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

