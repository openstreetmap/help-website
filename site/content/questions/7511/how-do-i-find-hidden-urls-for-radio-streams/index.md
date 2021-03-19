+++
type = "question"
title = "How do i find hidden URL&#x27;s for radio streams?"
description = '''I downloaded Wireshark for MAC and do not understand how it works. i watched the video but do not see how to get a URL? i am looking for streams my customers request to play in the Beautiful Clock Radio app.  I have come across a site that i can not figure out the stream even though they have a ipho...'''
date = "2011-11-18T18:15:00Z"
lastmod = "2011-11-23T19:34:00Z"
weight = 7511
keywords = [ "url", "streaming", "radio" ]
aliases = [ "/questions/7511" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do i find hidden URL's for radio streams?](/questions/7511/how-do-i-find-hidden-urls-for-radio-streams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7511-score" class="post-score" title="current number of votes">0</div><span id="post-7511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I downloaded Wireshark for MAC and do not understand how it works. i watched the video but do not see how to get a URL?</p><p>i am looking for streams my customers request to play in the Beautiful Clock Radio app.</p><p>I have come across a site that i can not figure out the stream even though they have a iphone stream available. http://www.zmonline.co.nz/player/listenlive/</p><p>i click on stream and nothing comes up in wireshark.</p><p>Can someone give me a clue how to get this app to work for finding streams?</p><p>Thanks Mark www.BeautifulClockRadio.com</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-streaming" rel="tag" title="see questions tagged &#39;streaming&#39;">streaming</span> <span class="post-tag tag-link-radio" rel="tag" title="see questions tagged &#39;radio&#39;">radio</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '11, 18:15</strong></p><img src="https://secure.gravatar.com/avatar/3feda5371834d88ff75d4ef308f45523?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mj662&#39;s gravatar image" /><p><span>mj662</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mj662 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Nov '11, 18:16</strong> </span></p></div></div><div id="comments-container-7511" class="comments-container"></div><div id="comment-tools-7511" class="comment-tools"></div><div class="clear"></div><div id="comment-7511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7515"></span>

<div id="answer-container-7515" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7515-score" class="post-score" title="current number of votes">1</div><span id="post-7515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>'How to get a URL?' If you mean an URL from HTTP then use Statistics|HTTP|Requests.</p><p>From the site you referred to the stream is send using RTMP.</p><p>'nothing comes up in Wireshark'. Does that mean that zero packets are captured, or that you can't find the media? In the fist case check your capture setup/interfaces. The second case is likely looking in the wrong place.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '11, 01:08</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7515" class="comments-container"><span id="7592"></span><div id="comment-7592" class="comment"><div id="post-7592-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap,</p><p>I guess i need to learn how to use WireShark. if you could teach me how to use this i could pay you for your time.</p><p>Mark</p></div><div id="comment-7592-info" class="comment-info"><span class="comment-age">(23 Nov '11, 19:34)</span> <span class="comment-user userinfo">mj662</span></div></div></div><div id="comment-tools-7515" class="comment-tools"></div><div class="clear"></div><div id="comment-7515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

