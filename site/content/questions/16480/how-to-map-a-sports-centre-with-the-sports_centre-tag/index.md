+++
type = "question"
title = "How to map a Sports Centre with the Sports_Centre tag"
description = '''I&#x27;ve recently created a Sports_Centra area but am struggeling to add al the sporting venues inside of the building. The wiki page for Sports_Centre does not say how to map multiple sports to an area:   https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dsports_centre  I would like to add the sports Swi...'''
date = "2012-09-26T11:55:00Z"
lastmod = "2012-09-26T12:20:00Z"
weight = 16480
keywords = [ "sports_centre", "amenity", "sport", "leisure", "area" ]
aliases = [ "/questions/16480" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to map a Sports Centre with the Sports_Centre tag](/questions/16480/how-to-map-a-sports-centre-with-the-sports_centre-tag)

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
<span id="post-16480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16480-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've recently created a Sports_Centra area but am struggeling to add al the sporting venues inside of the building.</p>
<p>The wiki page for Sports_Centre does not say how to map multiple sports to an area:</p>
<ul>
<li><a href="https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dsports_centre">https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dsports_centre</a></li>
</ul>
<p>I would like to add the sports Swimming and Fitness to the sports centre. The Sports Centre also contains a statium for big events. How should i map this? Is there a correct example available?</p>
<p>Thank you in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sports_centre" rel="tag" title="see questions tagged &#39;sports_centre&#39;">sports_centre</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-sport" rel="tag" title="see questions tagged &#39;sport&#39;">sport</span> <span class="post-tag tag-link-leisure" rel="tag" title="see questions tagged &#39;leisure&#39;">leisure</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Sep '12, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/c5cf4556a05f84a8c1877908095b3b07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kattenbakvulling&#39;s gravatar image" />
<p><span>Kattenbakvul...</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kattenbakvulling has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16480" class="comments-container">
&#10;</div>
<div id="comment-tools-16480" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16480-form-container" class="comment-form-container">
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

<span id="16481"></span>

<div id="answer-container-16481" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16481-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-16481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kattenbakvulling has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For mapping individual sports inside the <a href="https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dsports_centre">sports centre</a> you just have to create individual objects (nodes, areas or ways) and add the corresponding <a href="https://wiki.openstreetmap.org/wiki/Key:leisure">leisure</a> and <a href="https://wiki.openstreetmap.org/wiki/Key:sport">sport</a> tag. For example the stadium should be tagged with <a href="https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dstadium">leisure=stadium</a> and maybe <a href="https://wiki.openstreetmap.org/wiki/Tag:sport%3Dmulti">sport=multi</a>.</p>
<p>You can see an example <a href="https://www.openstreetmap.org/?lat=50.6766&amp;lon=11.27468&amp;zoom=17&amp;layers=M">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Sep '12, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Sep '12, 12:34</strong> </span></p>
</div>
</div>
<div id="comments-container-16481" class="comments-container">
&#10;</div>
<div id="comment-tools-16481" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16481-form-container" class="comment-form-container">
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

