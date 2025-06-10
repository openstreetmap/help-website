+++
type = "question"
title = "Convert OpenMapTiles Style to Mapnik XML style?"
description = '''There seems to be a proliferation of style sources for vector tiles such as OpenMapTiles. Is it possible to convert and leverage (and if so how) such styles for use with classic OSM image tile server using Mapnik and renderd?'''
date = "2017-05-11T14:34:00Z"
lastmod = "2017-05-12T14:03:00Z"
weight = 56125
keywords = [ "style", "renderd", "osm", "stylesheet", "mapnik" ]
aliases = [ "/questions/56125" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Convert OpenMapTiles Style to Mapnik XML style?](/questions/56125/convert-openmaptiles-style-to-mapnik-xml-style)

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
<span id="post-56125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56125-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There seems to be a proliferation of style sources for vector tiles such as <a href="https://openmaptiles.org">OpenMapTiles</a>. Is it possible to convert and leverage (and if so how) such styles for use with classic OSM image tile server using Mapnik and renderd?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-stylesheet" rel="tag" title="see questions tagged &#39;stylesheet&#39;">stylesheet</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 May '17, 14:34</strong></p>
<img src="https://secure.gravatar.com/avatar/88d088c7b8b53519aa8026bd00ce121c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rgwozdz&#39;s gravatar image" />
<p><span>rgwozdz</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rgwozdz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56125" class="comments-container">
&#10;</div>
<div id="comment-tools-56125" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56125-form-container" class="comment-form-container">
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

<span id="56154"></span>

<div id="answer-container-56154" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56154-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rgwozdz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I believe the answer is: no. Naturally given enough time, money and whatever it is probably possible to convert such styles, maybe even programmatically. However even if you could I doubt that it would make a lot of sense from a cartographic point of view as good Mapnik based styles tend to be far more refined than anything at least I've seen generated with mapbox-gl.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 May '17, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 May '17, 14:03</strong> </span></p>
</div>
</div>
<div id="comments-container-56154" class="comments-container">
&#10;</div>
<div id="comment-tools-56154" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56154-form-container" class="comment-form-container">
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

