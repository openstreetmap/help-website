+++
type = "question"
title = "OSM Feature Count and Feature Extraction"
description = '''1)what is the total amount of places per country (by places I mean village, city, hamlet, etc). The count does not have to be split out, just one number per nation. And how do I figure this number out on my own for future reference? 2)I was told to run a overpass turbo query to extract specific feat...'''
date = "2017-10-09T23:01:00Z"
lastmod = "2017-10-11T16:03:00Z"
weight = 60032
keywords = [ "thailand", "digitalglobe", "places" ]
aliases = [ "/questions/60032" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM Feature Count and Feature Extraction](/questions/60032/osm-feature-count-and-feature-extraction)

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
<span id="post-60032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60032-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>1)what is the total amount of places per country (by places I mean village, city, hamlet, etc). The count does not have to be split out, just one number per nation. And how do I figure this number out on my own for future reference?</p>
<p>2)I was told to run a overpass turbo query to extract specific features I wanted to review. How would I run it, or create it based on this information:</p>
<h1 id="nsroadimport-thailand-source-digitalglobe-and-import-yes">nsroadimport #thailand, source = digitalglobe and import = yes</h1>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-thailand" rel="tag" title="see questions tagged &#39;thailand&#39;">thailand</span> <span class="post-tag tag-link-digitalglobe" rel="tag" title="see questions tagged &#39;digitalglobe&#39;">digitalglobe</span> <span class="post-tag tag-link-places" rel="tag" title="see questions tagged &#39;places&#39;">places</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '17, 23:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2cb187a5504c9f0897f3cf4504b8e82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MapMakinMeyers&#39;s gravatar image" />
<p><span>MapMakinMeyers</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MapMakinMeyers has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60032" class="comments-container">
&#10;</div>
<div id="comment-tools-60032" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60032-form-container" class="comment-form-container">
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

<span id="60033"></span>

<div id="answer-container-60033" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60033-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's a sample script for counting the place features in a country:</p>
<p><a href="http://overpass-turbo.eu/s/seM">http://overpass-turbo.eu/s/seM</a></p>
<p>(click on <code>show data</code> when the warning pops up)</p>
<p>The <code>geocodeArea:Thailand</code> is a feature of the Overpass Turbo website, to do the query directly against Overpass API it needs to be replaced with a reference to the OSM object the Overpass API area object is created from:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29">http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29</a></p>
<p><a href="http://overpass-turbo.eu/s/seN">A query like area["name:en"="Thailand"][admin_level="2"]-&gt;.searchArea;</a> should also usually work.</p>
<p>Overpass API doesn't support queries against changeset tags, but if the tags are on the objects you want to review, just putting something like <code>import=yes and source=digitalglobe</code> into the Overpass Turbo wizard will return objects with those tags. There are some resource limits on the public instances, so queries returning a large number of objects may time out. Limiting the query to some smaller bounding box is one way to deal with that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '17, 23:24</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Oct '17, 23:28</strong> </span></p>
</div>
</div>
<div id="comments-container-60033" class="comments-container">
<span id="60066"></span>
<div id="comment-60066" class="comment">
<div id="post-60066-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Seeing how place is sometimes used, the more interesting query probably also checks for name.</p>
</div>
<div id="comment-60066-info" class="comment-info">
<span class="comment-age">(11 Oct '17, 16:03)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-60033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60033-form-container" class="comment-form-container">
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

