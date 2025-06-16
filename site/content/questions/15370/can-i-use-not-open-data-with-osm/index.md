+++
type = "question"
title = "Can I use not-open data with OSM?"
description = '''Hi, I&#x27;d like to use OSM database with some additional not open-licensed data - is this possible without licensing the data as open? Will it be the same situation after transition of OSM to Odbl? My client wants custom markers to appear on the map in his application, while keeping database of the mar...'''
date = "2012-08-22T13:13:00Z"
lastmod = "2012-08-22T16:36:00Z"
weight = 15370
keywords = [ "osm", "open", "license" ]
aliases = [ "/questions/15370" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can I use not-open data with OSM?](/questions/15370/can-i-use-not-open-data-with-osm)

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
<span id="post-15370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15370-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'd like to use OSM database with some additional not open-licensed data - is this possible without licensing the data as open? Will it be the same situation after transition of OSM to Odbl?<br />
My client wants custom markers to appear on the map in his application, while keeping database of the markers not public and not open-licensed - I've spent some time studying the legal wiki, but not sure if that thing is actually possible.<br />
Also it looks like some <a href="https://wiki.openstreetmap.org/wiki/List_of_OSM_based_Services">OSM-based services</a> are keeping their data separated from the OSM database while keeping parts of the data not released as open and I'm curious how it looks like from the legal view.<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-open" rel="tag" title="see questions tagged &#39;open&#39;">open</span> <span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '12, 13:13</strong></p>
<img src="https://secure.gravatar.com/avatar/89b0eb6b5ed4f11aa012d215b737caf8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mr%C3%B3wa&#39;s gravatar image" />
<p><span>Mrówa</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mrówa has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-15370" class="comments-container">
&#10;</div>
<div id="comment-tools-15370" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15370-form-container" class="comment-form-container">
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

<span id="15386"></span>

<div id="answer-container-15386" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15386-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general, as long as you don't create a derivate product, you don't have to merge the datasets, and you can use proprietary information.</p>
<p>e.g. if you would use OSM data to geocode your POI, that would make the location data of the POI is derived from OSM data, so your POI dataset has to be open.</p>
<p>But if you make a georeferenced rendering of OSM data and a georeferenced rendering of your POI (both separated), you can diplay the layers on top of each other without problem.</p>
<p>For services keeping their database proprietary, this is also possible since only the contens of the database is protected, and not the format in which it is stored. So if they just use a tool to change the format (and anyone could use that tool to get the same format), there is no problem. Those tools can be used to have a more optimal format (XML isn't optimal), or filter out only certain tags to render etc.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '12, 15:21</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span> </br></p>
</div>
</div>
<div id="comments-container-15386" class="comments-container">
<span id="15396"></span>
<div id="comment-15396" class="comment">
<div id="post-15396-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Some more hints can be found in the OSM wiki about <a href="https://wiki.openstreetmap.org/wiki/Legal_FAQ">https://wiki.openstreetmap.org/wiki/Legal_FAQ</a></p>
<p>or at</p>
<p><a href="/questions/6905/is-it-possible-to-create-my-individual-layer">https://help.openstreetmap.org/questions/6905/is-it-possible-to-create-my-individual-layer</a></p>
<p><a href="/questions/6102/can-i-add-a-custom-layer">https://help.openstreetmap.org/questions/6102/can-i-add-a-custom-layer</a></p>
</div>
<div id="comment-15396-info" class="comment-info">
<span class="comment-age">(22 Aug '12, 16:36)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-15386" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15386-form-container" class="comment-form-container">
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

