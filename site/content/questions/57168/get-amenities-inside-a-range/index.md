+++
type = "question"
title = "Get amenities inside a range"
description = '''I am trying to extract all the amenities inside a bounding box for different segments, I don&#x27;t want to download them from the server every single time. Instead, I just want to download a general area and then if you select a specific street or segment show all the amenities in it.  I&#x27;m trying to bui...'''
date = "2017-07-19T00:47:00Z"
lastmod = "2017-07-19T11:19:00Z"
weight = 57168
keywords = [ "bounding", "python", "amenity", "routing" ]
aliases = [ "/questions/57168" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get amenities inside a range](/questions/57168/get-amenities-inside-a-range)

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
<span id="post-57168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57168-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to extract all the amenities inside a bounding box for different segments, I don't want to download them from the server every single time. Instead, I just want to download a general area and then if you select a specific street or segment show all the amenities in it.</p>
<p>I'm trying to build a python program where you specify two nodes (coordinates) and print out the amenities in that route.</p>
<p>Could you help please?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bounding" rel="tag" title="see questions tagged &#39;bounding&#39;">bounding</span> <span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jul '17, 00:47</strong></p>
<img src="https://secure.gravatar.com/avatar/5a1445bc38c0400517ab4a869f813832?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sandra%20Garcia%20L&#39;s gravatar image" />
<p><span>Sandra Garcia L</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sandra Garcia L has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57168" class="comments-container">
&#10;</div>
<div id="comment-tools-57168" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57168-form-container" class="comment-form-container">
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

<span id="57175"></span>

<div id="answer-container-57175" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57175-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are naturally many ways to achieve what you want, but a typical approach would be to import the POIs (extracted from a OSM planet dump) in a suitable format in to a database. You could either add a street reference to the POI before import, or use a geo-spatially enabled database (for example postgres with postgis) to on the fly determine which POIs to show based on their location.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '17, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-57175" class="comments-container">
&#10;</div>
<div id="comment-tools-57175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57175-form-container" class="comment-form-container">
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

