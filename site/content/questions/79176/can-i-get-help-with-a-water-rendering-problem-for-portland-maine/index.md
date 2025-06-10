+++
type = "question"
title = "Can I get help with a water rendering problem for Portland, Maine?"
description = '''Hello I share maps out of OSM in PDF form so I can use them as bases to create my own maps in Illustrator. I am having a problem that seems specific to Portland, Maine. The map appears correct in the PDF, but when I open it in Illustrator, the bodies of water are gone or greatly diminished (harbor t...'''
date = "2021-03-08T02:47:00Z"
lastmod = "2021-03-13T16:14:00Z"
weight = 79176
keywords = [ "water", "pdf", "illustrator" ]
aliases = [ "/questions/79176" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I get help with a water rendering problem for Portland, Maine?](/questions/79176/can-i-get-help-with-a-water-rendering-problem-for-portland-maine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79176-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello</p>
<p>I share maps out of OSM in PDF form so I can use them as bases to create my own maps in Illustrator. I am having a problem that seems specific to Portland, Maine.</p>
<p>The map appears correct in the PDF, but when I open it in Illustrator, the bodies of water are gone or greatly diminished (harbor turned into a skinny river). (Area here: <a href="https://www.openstreetmap.org/#map=13/43.6561/-70.2476)">https://www.openstreetmap.org/#map=13/43.6561/-70.2476)</a> Most importantly, this leaves me without a defined coastline and makes the map unusable for me.</p>
<p>I have read in this forum of others having similar difficulties, but I have tried several locations down the US East Coast and Portland is the only area where I have come up with a problem. Can someone suggest a fix or workaround for a technically-unskilled user such as myself?</p>
<p>Thanks much</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-pdf" rel="tag" title="see questions tagged &#39;pdf&#39;">pdf</span> <span class="post-tag tag-link-illustrator" rel="tag" title="see questions tagged &#39;illustrator&#39;">illustrator</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '21, 02:47</strong></p>
<img src="https://secure.gravatar.com/avatar/75e472c610bdf8aad010db1a92d7e581?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John%20Friedmann&#39;s gravatar image" />
<p><span>John Friedmann</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John Friedmann has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79176" class="comments-container">
&#10;</div>
<div id="comment-tools-79176" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79176-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="79212"></span>

<div id="answer-container-79212" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79212-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Illustrator can have particular issues with loading PDFs produced by Mapnik (the rendering software that OpenStreetMap uses). If the coastline geometry is too big for Illustrator to handle - including the 'invisible' sections beyond the clipping box - then it will just refuse to load it.</p>
<p>You might be able to use another PDF-handling program to clip the PDF before loading it into Illustrator. Alternatively, a quick and dirty hack would be to screenshot the PDF, load the screenshot into Illustrator, then use the "Trace Image" function to vectorise the blue coastline area. Paste and scale it into your PDF.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '21, 20:15</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-79212" class="comments-container">
<span id="79247"></span>
<div id="comment-79247" class="comment">
<div id="post-79247-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I'll try clipping the PDF through another program and see if that works.</p>
</div>
<div id="comment-79247-info" class="comment-info">
<span class="comment-age">(13 Mar '21, 16:14)</span> <span class="comment-user userinfo">John Friedmann</span>
</div>
</div>
</div>
<div id="comment-tools-79212" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79212-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79180"></span>

<div id="answer-container-79180" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79180-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>I think the reason for the water area around the Fore River not being rendered is because it's not mapped as a water area, only the coastline and river line are mapped. Whereas other places have the water area mapped as well, like around the Ipswich River to the south. I don't know if this is specifically the cause of your problem but it certainly is a difference.</p>
<p>Regards</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '21, 08:09</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-79180" class="comments-container">
<span id="79207"></span>
<div id="comment-79207" class="comment">
<div id="post-79207-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting, not sure how to fix but it is a difference. Thanks</p>
</div>
<div id="comment-79207-info" class="comment-info">
<span class="comment-age">(09 Mar '21, 19:52)</span> <span class="comment-user userinfo">John Friedmann</span>
</div>
</div>
<span id="79208"></span>
<div id="comment-79208" class="comment">
<div id="post-79208-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also, North America appears to have been broken at the last <a href="https://osmdata.openstreetmap.de/internal/coastline/">attempt</a>.</p>
</div>
<div id="comment-79208-info" class="comment-info">
<span class="comment-age">(10 Mar '21, 02:21)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-79180" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79180-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

