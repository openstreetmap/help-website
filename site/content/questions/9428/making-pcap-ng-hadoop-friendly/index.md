+++
type = "question"
title = "making pcap-ng hadoop friendly"
description = '''Are there any plans to make the pcap-ng format more friendly to hadoop and mapreduce. Meaning being able to &quot;split&quot; a single file and stay on cut. I believe this can be accomplished with pcap-ng and just wondering if was in the plans.'''
date = "2012-03-08T04:47:00Z"
lastmod = "2012-03-08T14:34:00Z"
weight = 9428
keywords = [ "pcapng", "hadoop" ]
aliases = [ "/questions/9428" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [making pcap-ng hadoop friendly](/questions/9428/making-pcap-ng-hadoop-friendly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9428-score" class="post-score" title="current number of votes">0</div><span id="post-9428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Are there any plans to make the pcap-ng format more friendly to hadoop and mapreduce. Meaning being able to "split" a single file and stay on cut. I believe this can be accomplished with pcap-ng and just wondering if was in the plans.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcapng" rel="tag" title="see questions tagged &#39;pcapng&#39;">pcapng</span> <span class="post-tag tag-link-hadoop" rel="tag" title="see questions tagged &#39;hadoop&#39;">hadoop</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '12, 04:47</strong></p><img src="https://secure.gravatar.com/avatar/56254faac61acbf97dd784a2de28f6c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jdbethge&#39;s gravatar image" /><p><span>jdbethge</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jdbethge has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Mar '12, 14:32</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-9428" class="comments-container"></div><div id="comment-tools-9428" class="comment-tools"></div><div class="clear"></div><div id="comment-9428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9430"></span>

<div id="answer-container-9430" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9430-score" class="post-score" title="current number of votes">1</div><span id="post-9430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The inherent sequential nature of network capture analysis makes it unfit for such processing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '12, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-9430" class="comments-container"><span id="9440"></span><div id="comment-9440" class="comment"><div id="post-9440-score" class="comment-score"></div><div class="comment-text"><p>I would disagree. As there seems to alot of work currently in analyzing pcap using hadoop map reduce. See <a href="https://labs.ripe.net/Members/wnagele/large-scale-pcap-data-analysis-using-apache-hadoop">https://labs.ripe.net/Members/wnagele/large-scale-pcap-data-analysis-using-apache-hadoop</a></p></div><div id="comment-9440-info" class="comment-info"><span class="comment-age">(08 Mar '12, 12:11)</span> <span class="comment-user userinfo">jdbethge</span></div></div></div><div id="comment-tools-9430" class="comment-tools"></div><div class="clear"></div><div id="comment-9430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9438"></span>

<div id="answer-container-9438" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9438-score" class="post-score" title="current number of votes">0</div><span id="post-9438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are no plans to change the pcap format, as there's not much you can do to change it - you can't add new fields to the file header or the packet header, as that would break all code that reads pcap files. A new file format would need a new magic number, but that amounts to a different file format.</p><p>pcap-NG is extensible, so there's more that could be done, but, as Jaap notes, there are limits to the amount of parallelism possible when processing a capture file - the proper interpretation of a packet may depend on the contents of previous packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '12, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9438" class="comments-container"><span id="9442"></span><div id="comment-9442" class="comment"><div id="post-9442-score" class="comment-score"></div><div class="comment-text"><p>I am not talking about changing pcap (that would be crazy), but adding capability to pcapng.</p></div><div id="comment-9442-info" class="comment-info"><span class="comment-age">(08 Mar '12, 12:13)</span> <span class="comment-user userinfo">jdbethge</span></div></div><span id="9444"></span><div id="comment-9444" class="comment"><div id="post-9444-score" class="comment-score"></div><div class="comment-text"><p>OK, so I edited the qestion to clarify that.</p><p>If the capability in question can be provided by adding a new block type to pcap-NG, it can probably be done; if so, indicate what sort of block that would be.</p><p>(The existing pcap-ng format is less likely to be changed in an incompatible fashion, as there's already code out there that reads and writes it; that would involve a new major version number.)</p></div><div id="comment-9444-info" class="comment-info"><span class="comment-age">(08 Mar '12, 14:34)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-9438" class="comment-tools"></div><div class="clear"></div><div id="comment-9438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

