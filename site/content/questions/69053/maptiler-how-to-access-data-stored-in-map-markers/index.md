+++
type = "question"
title = "[Maptiler] How to access data stored in map markers"
description = '''I&#x27;m trying to reproduce my Google Fusion tables maps before Fusion Tables is removed from Google Maps in August. I am not an experienced GIS person and getting into the world of OSM has been very difficult for me as a Google Maps user. My maps are simply markers on a map, positioned by lat and long,...'''
date = "2019-05-02T20:52:00Z"
lastmod = "2019-05-02T20:52:00Z"
weight = 69053
keywords = [ "markers" ]
aliases = [ "/questions/69053" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[Maptiler\] How to access data stored in map markers](/questions/69053/maptiler-how-to-access-data-stored-in-map-markers)

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
<span id="post-69053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69053-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to reproduce my Google Fusion tables maps before Fusion Tables is removed from Google Maps in August. I am not an experienced GIS person and getting into the world of OSM has been very difficult for me as a Google Maps user.</p>
<p>My maps are simply markers on a map, positioned by lat and long, and with several points of data associated with each marker. I have tens of thousands of points</p>
<p>So far I have been able to render my data into tile sets using Maptiler desktop, then style and host the maps on Maptiler Cloud. The last step is I need to figure out how to access the data stored with each marker to display in a popup info window for each marker. In the Maptiler Cloud interface I can see the values of "name" and "description" for each point, which seem to be the default values used by the platform. Based on that, I am not sure if my other data for each point has been stored. As an example the data I need to include in each point and display in the map popup is:</p>
<p>Name ID State County</p>
<p>My questions are:</p>
<ol>
<li><p>I'm assuming the data is accessed by JS like Leaflet and then displayed in the marker popup. How does the script access these data points? Is there some kind of map inspector I can use to see what data resides in each marker?</p></li>
<li><p>How is the data in each marker stored?</p></li>
<li><p>My data that was rendered as tiles was KML. Is there a certain KML format I need to use to ensure that all data points are being included in the tile sets, and can be accessed by JS in the map?</p></li>
</ol>
<p>I'm just looking for some high-level info here that I can use to guide the development efforts related to this project. Any hel is greatly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-markers" rel="tag" title="see questions tagged &#39;markers&#39;">markers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 May '19, 20:52</strong></p>
<img src="https://secure.gravatar.com/avatar/c334155bdc611fc832405ba366ba0a2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Earthventures&#39;s gravatar image" />
<p><span>Earthventures</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Earthventures has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 May '19, 22:28</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-69053" class="comments-container">
&#10;</div>
<div id="comment-tools-69053" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69053-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

