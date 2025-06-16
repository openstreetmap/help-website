+++
type = "question"
title = "Getting to the base map"
description = '''Is it possible to remove the tags, for example shop names and taxi signs, from a section of the map so you can get back to the base map - so that it&#x27;s just plain roads and building outlines and so on. '''
date = "2011-02-28T16:56:00Z"
lastmod = "2011-02-28T18:01:00Z"
weight = 3452
keywords = [ "map", "base", "rendering" ]
aliases = [ "/questions/3452" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting to the base map](/questions/3452/getting-to-the-base-map)

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
<span id="post-3452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3452-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to remove the tags, for example shop names and taxi signs, from a section of the map so you can get back to the base map - so that it's just plain roads and building outlines and so on.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-base" rel="tag" title="see questions tagged &#39;base&#39;">base</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '11, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/8ea26407c7de8dd35cceee1b446d825a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="STEVE&#39;s gravatar image" />
<p><span>STEVE</span><br />
<span class="score" title="30 reputation points">30</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="STEVE has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Mar '11, 09:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span></p>
</div>
</div>
<div id="comments-container-3452" class="comments-container">
&#10;</div>
<div id="comment-tools-3452" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3452-form-container" class="comment-form-container">
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

<span id="3453"></span>

<div id="answer-container-3453" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3453-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-3453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, the default map on the OpenStreetMap homepage shows a lot of features such as shop names, and can look rather cluttered for some purposes.</p>
<p>There are alternatives. Take a look at <a href="http://open.mapquest.com/"></a><a href="http://open.mapquest.com"></a><a href="http://open.mapquest.com">open.mapquest.com</a>. That's OpenStreetMap data rendered differently. Take a look at <a href="http://maps.cloudmade.com/"></a><a href="http://maps.cloudmade.com"></a><a href="http://maps.cloudmade.com">maps.cloudmade.com</a> and try clicking 'Edit map styles'. You can create your own map rendering styles there. That's all OpenStreetMap data, and with both these services, you're allowed to embed the map on your own website.</p>
<p>How is this possible? Because OpenStreetMap offers access to the raw data people can use 'Rendering' software to render the map in their own styles. See the <a href="https://wiki.openstreetmap.org/wiki/Rendering">Rendering</a> page for details of the options. If you want something very similar to the OpenStreetMap default style, but with less features showing, then you'd want to look into Mapnik and the OpenStreetMap stylesheet. This software can be quite technical to get up and running, and also resource-hungry for the server you run it on, but it does give you complete cartographic control, and that's something which is pretty much uniquely possible using OpenStreetMap's free and open data set.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '11, 18:01</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-3453" class="comments-container">
&#10;</div>
<div id="comment-tools-3453" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3453-form-container" class="comment-form-container">
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

