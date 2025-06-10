+++
type = "question"
title = "topo custom map problems"
description = '''Hello I have problem for create custom map! when i download map from Openstreetmap with Grandtruth and srtm2osm, there are area on my map that have not topo information (pic 1 and 2 on blac boxes) why there are this problem on my custom maps? thank you Mostafa  '''
date = "2015-05-02T08:18:00Z"
lastmod = "2015-05-02T10:02:00Z"
weight = 42805
keywords = [ "topographic", "srtm" ]
aliases = [ "/questions/42805" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [topo custom map problems](/questions/42805/topo-custom-map-problems)

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
<span id="post-42805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42805-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello I have problem for create custom map! when i download map from Openstreetmap with Grandtruth and srtm2osm, there are area on my map that have not topo information (pic 1 and 2 on blac boxes) why there are this problem on my custom maps?</p>
<p>thank you Mostafa <img src="http://s6.uplod.ir/i/00589/upolteyn72sx.jpg" alt="alt text" /></p>
<p><img src="http://s6.uplod.ir/i/00589/rdgrcc0k7qne.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-topographic" rel="tag" title="see questions tagged &#39;topographic&#39;">topographic</span> <span class="post-tag tag-link-srtm" rel="tag" title="see questions tagged &#39;srtm&#39;">srtm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 May '15, 08:18</strong></p>
<img src="https://secure.gravatar.com/avatar/b0f63a4b4ed14f08b22e34d5bc6245bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mo2200&#39;s gravatar image" />
<p><span>mo2200</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mo2200 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 May '15, 15:11</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</img>
</div>
</div>
<div id="comments-container-42805" class="comments-container">
&#10;</div>
<div id="comment-tools-42805" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42805-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="42806"></span>

<div id="answer-container-42806" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42806-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-42806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The artifacts you are seeing are likely voids in the SRTM data, which are due to the way the data was collected.</p>
<p>Googling for "void filling SRTM" will give you a lot of hits.</p>
<p>To get around the issue you either need to fill the voids yourself, or use a dataset were that has already been done. For example: <a href="http://opendem.info/download_contours.html">http://opendem.info/download_contours.html</a> There are however a number of different providers that you can choose from.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 May '15, 10:02</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 May '15, 13:06</strong> </span></p>
</div>
</div>
<div id="comments-container-42806" class="comments-container">
&#10;</div>
<div id="comment-tools-42806" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42806-form-container" class="comment-form-container">
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

