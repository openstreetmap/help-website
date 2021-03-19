+++
type = "question"
title = "data.data shows only 24byte"
description = '''I want to create a txt-file with the data of my filtered UDP-packets. When i create a custom colu**mn with the field-type &quot;data.data&quot; it shows my filtered packet-data but only the first 24byte and &quot;...&quot;  Is it possible to create a txt-file with the full frame-content (without the header information)...'''
date = "2012-11-05T00:23:00Z"
lastmod = "2014-09-17T08:49:00Z"
weight = 15531
keywords = [ "data.data" ]
aliases = [ "/questions/15531" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [data.data shows only 24byte](/questions/15531/datadata-shows-only-24byte)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15531-score" class="post-score" title="current number of votes">1</div><span id="post-15531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to create a txt-file with the data of my filtered UDP-packets. When i create a custom colu**mn with the field-type "data.data" it shows my filtered packet-data but only the first 24byte and "..."</p><p><em>Is it possible to create a txt-file with the full frame-content (without the header information)?</em></p><p>Thanks a lot!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-data.data" rel="tag" title="see questions tagged &#39;data.data&#39;">data.data</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '12, 00:23</strong></p><img src="https://secure.gravatar.com/avatar/3a0d3f18d3a2c059ba609267e7b8438f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sharkline&#39;s gravatar image" /><p><span>Sharkline</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sharkline has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Nov '12, 00:24</strong> </span></p></div></div><div id="comments-container-15531" class="comments-container"><span id="15549"></span><div id="comment-15549" class="comment"><div id="post-15549-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "without the header information"?</p></div><div id="comment-15549-info" class="comment-info"><span class="comment-age">(05 Nov '12, 12:32)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="15550"></span><div id="comment-15550" class="comment"><div id="post-15550-score" class="comment-score"></div><div class="comment-text"><p>I believe he means the payload data, similar to "Follow UDP Stream".</p></div><div id="comment-15550-info" class="comment-info"><span class="comment-age">(05 Nov '12, 12:35)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-15531" class="comment-tools"></div><div class="clear"></div><div id="comment-15531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36411"></span>

<div id="answer-container-36411" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36411-score" class="post-score" title="current number of votes">0</div><span id="post-36411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can try using tshark with the -x option that will basically dump the whole packet including hex bytes in textform and filter/grep for the parts you're looking for or try using the data.data field sogether with -Tfields</p><p>e.g. <code>tshark -r test.pcap -Y udp -Tfields -e data.data</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '14, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-36411" class="comments-container"></div><div id="comment-tools-36411" class="comment-tools"></div><div class="clear"></div><div id="comment-36411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

