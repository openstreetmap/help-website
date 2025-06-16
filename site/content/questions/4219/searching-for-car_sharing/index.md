+++
type = "question"
title = "Searching for car_sharing"
description = '''I&#x27;m trying to find a way to search for car sharing cars in a given region. I.e. I want to be able to zoom into a specific part of my town and then have OSM show me the locations of amenity=car_sharing. I&#x27;ve tried several variations, like car_sharing near ithaca (no results), just zooming in and sear...'''
date = "2011-03-31T15:35:00Z"
lastmod = "2011-05-12T20:08:00Z"
weight = 4219
keywords = [ "amenity", "nominatim", "car_sharing", "search" ]
aliases = [ "/questions/4219" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Searching for car_sharing](/questions/4219/searching-for-car_sharing)

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
<span id="post-4219-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4219-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-4219-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to find a way to search for car sharing cars in a given region. I.e. I want to be able to zoom into a specific part of my town and then have OSM show me the locations of <code>amenity=car_sharing</code>. I've tried several variations, like <code>car_sharing near ithaca</code> (no results), just zooming in and searching for <code>car_sharing</code> (gives me random carsharing results from all over the place), <code>ithaca carshare</code> (this is the name of the operator; again, no results). Am I totally misunderstanding how the search on OSM works? Is there another way to achieve the desired result? Thanks for your help!</p>
<p>Addition: I know that the tags do exist in the area (I entered them myself) and they are displayed on Mapnik (e.g. <a href="https://www.openstreetmap.org/?lat=42.438694&amp;lon=-76.497517&amp;zoom=18&amp;layers=M">here</a>).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-car_sharing" rel="tag" title="see questions tagged &#39;car_sharing&#39;">car_sharing</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Mar '11, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/eb6970a0658ff5e0c2b7eaa4a02cbbbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hobbesvsboyle&#39;s gravatar image" />
<p><span>hobbesvsboyle</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hobbesvsboyle has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Mar '11, 16:49</strong> </span></p>
</div>
</div>
<div id="comments-container-4219" class="comments-container">
<span id="4222"></span>
<div id="comment-4222" class="comment">
<div id="post-4222-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Are you sure that in the area of ithaca there is any car_sharing object already in the OSM data? When nobody has enteres such an object in the OSM data, it cannot be found by the nominatim search. When there is such an object in your desired area, please giva us a permalink to that so that we can investigate further. (Please edit your original question if you have more info for us)</p>
</div>
<div id="comment-4222-info" class="comment-info">
<span class="comment-age">(31 Mar '11, 16:43)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="4223"></span>
<div id="comment-4223" class="comment">
<div id="post-4223-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Okay, maybe I have found the answer to my own question: 1. searching for "car_sharing" produces different results than searching for "car sharing". Searching for "car sharing near stuttgart" for example produces correct results. 2. This does not, however, work for the are linked in the addition to my question. I suspect that this is due to the fact that the nodes have been created very recently (Tuesday, I think) and therefore might not be in Nominatim yet.</p>
</div>
<div id="comment-4223-info" class="comment-info">
<span class="comment-age">(31 Mar '11, 16:56)</span> <span class="comment-user userinfo">hobbesvsboyle</span>
</div>
</div>
</div>
<div id="comment-tools-4219" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4219-form-container" class="comment-form-container">
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

<span id="4257"></span>

<div id="answer-container-4257" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4257-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>As to how this <em>should</em> work:</strong></p>
<p>Searching for "car sharing near Ithaca" should work. "car sharing" is one of the <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases">special phrases</a> which Nominatim understands. The term "car sharing" is an alias for places with the tag <code>amenity=car_sharing</code> - which is just what you want.</p>
<p>If I search for "car sharing near münchen", I get appropriate results from München, which shows that this search methods works in principle.</p>
<p><strong>As to why searching for "car_sharing near ithaca" does not return results:</strong></p>
<p>I'm not sure why this does not work. The search query is correct (see above), and the car sharing node you link to appears to be correct. The might be a problem with Nominatim's updates (normally, there should be an indication on the Nominatim page when it was last updated, but that is currently missing). Try again in a few days, and if the problem persists, you might consider filing a bug on nominatim in trac ( <a href="http://trac.openstreetmap.org/">http://trac.openstreetmap.org/</a> )</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Apr '11, 15:41</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Apr '11, 15:42</strong> </span></p>
</div>
</div>
<div id="comments-container-4257" class="comments-container">
<span id="4258"></span>
<div id="comment-4258" class="comment">
<div id="post-4258-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the explanation. I've also come to the conclusion that it must be a Nominatim problem. The Nominatim discussion page mentions that something's wrong with the updating; unfortunately there are no specifics about what is wrong and when updating will resume.</p>
</div>
<div id="comment-4258-info" class="comment-info">
<span class="comment-age">(03 Apr '11, 16:31)</span> <span class="comment-user userinfo">hobbesvsboyle</span>
</div>
</div>
</div>
<div id="comment-tools-4257" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4257-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5161"></span>

<div id="answer-container-5161" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5161-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Since this issue still persists and Nominatim updates are working again, I am now assuming that it must be a bug in Nominatim and have created a ticket in track: <a href="http://trac.openstreetmap.org/ticket/3762">http://trac.openstreetmap.org/ticket/3762</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 May '11, 20:08</strong></p>
<img src="https://secure.gravatar.com/avatar/eb6970a0658ff5e0c2b7eaa4a02cbbbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hobbesvsboyle&#39;s gravatar image" />
<p><span>hobbesvsboyle</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hobbesvsboyle has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5161" class="comments-container">
&#10;</div>
<div id="comment-tools-5161" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5161-form-container" class="comment-form-container">
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

