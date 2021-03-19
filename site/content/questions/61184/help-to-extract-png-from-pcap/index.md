+++
type = "question"
title = "Help to extract PNG from pcap"
description = '''Hey, I need help to try and extract a file from this pcap, https://www.cloudshark.org/captures/096933d95411 At first I thought there was a PNG in there, and it&#x27;s got metadata from Photoshop, but I can&#x27;t see the first hex bytes of a PNG file in the items that Wireshark extracted for me. In plaintext,...'''
date = "2017-05-03T02:35:00Z"
lastmod = "2017-05-03T06:25:00Z"
weight = 61184
keywords = [ "extract", "png" ]
aliases = [ "/questions/61184" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Help to extract PNG from pcap](/questions/61184/help-to-extract-png-from-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61184-score" class="post-score" title="current number of votes">0</div><span id="post-61184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>I need help to try and extract a file from this pcap, <a href="https://www.cloudshark.org/captures/096933d95411">https://www.cloudshark.org/captures/096933d95411</a> At first I thought there was a PNG in there, and it's got metadata from Photoshop, but I can't see the first hex bytes of a PNG file in the items that Wireshark extracted for me.</p><p>In plaintext, I would like help with:</p><ol><li>If there is an image in there, can it get extracted? Also I would appreciate some comments/instructions how it can be done as I'm not able to. Got to keep learning!</li><li>If no image, what file is it?</li></ol><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-png" rel="tag" title="see questions tagged &#39;png&#39;">png</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '17, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/b03dd31dcffe98206cdb8feb41522d01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Suedish&#39;s gravatar image" /><p><span>Suedish</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Suedish has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 May '17, 03:42</strong> </span></p></div></div><div id="comments-container-61184" class="comments-container"><span id="61191"></span><div id="comment-61191" class="comment"><div id="post-61191-score" class="comment-score">1</div><div class="comment-text"><p>Unless you make the file publicly accessible, we can't assist you.</p></div><div id="comment-61191-info" class="comment-info"><span class="comment-age">(03 May '17, 04:30)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="61193"></span><div id="comment-61193" class="comment"><div id="post-61193-score" class="comment-score"></div><div class="comment-text"><p>Sorry, new to cloudshark. It should be public now</p></div><div id="comment-61193-info" class="comment-info"><span class="comment-age">(03 May '17, 04:32)</span> <span class="comment-user userinfo">Suedish</span></div></div></div><div id="comment-tools-61184" class="comment-tools"></div><div class="clear"></div><div id="comment-61184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61206"></span>

<div id="answer-container-61206" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61206-score" class="post-score" title="current number of votes">0</div><span id="post-61206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The file magic 'ab cd 98 76' lead to a single hit on <a href="https://github.com/Macuyiko/weiyun-api/blob/master/chunkformat.txt">GitHub</a> (<a href="https://github.com/Macuyiko/weiyun-api/blob/master/chunkformat.txt),">https://github.com/Macuyiko/weiyun-api/blob/master/chunkformat.txt),</a> so it seems a Weiyun API related format. The involved IP address seems to support this observation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '17, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61206" class="comments-container"></div><div id="comment-tools-61206" class="comment-tools"></div><div class="clear"></div><div id="comment-61206-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

