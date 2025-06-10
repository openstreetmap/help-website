+++
type = "question"
title = "Annotating OSM"
description = '''I&#x27;m looking for a good way to add additional data (annotations) to OSM. I&#x27;ve a custom routing application (programmed in java) which requires additional, application specific data. For example, each road segment needs to be annotated with a &quot;priority&quot; field. Since this is an application specific fie...'''
date = "2016-04-18T18:45:00Z"
lastmod = "2016-04-19T10:55:00Z"
weight = 49286
keywords = [ "annotate" ]
aliases = [ "/questions/49286" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Annotating OSM](/questions/49286/annotating-osm)

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
<span id="post-49286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49286-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for a good way to add additional data (annotations) to OSM. I've a custom routing application (programmed in java) which requires additional, application specific data. For example, each road segment needs to be annotated with a "priority" field. Since this is an application specific field, this is not something you want to add directly to the existing OSM data. Consequently, I was wondering whether there's a good way to add a new layer ('ApplicationLayer') on top of the OSM data. The purpose of this layer is to add additional application-specific data. Ideally, I'm looking for a way to create the layer such that it remains compatible with the underlying OSM data. So if somebody updates/changes OSM, than this should be reflected in the ApplicationLayer. It would be very annoying if there's no way to keep the ApplicationLayer synchronized with the OSM data, or to detect conflicts.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-annotate" rel="tag" title="see questions tagged &#39;annotate&#39;">annotate</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '16, 18:45</strong></p>
<img src="https://secure.gravatar.com/avatar/6feb1ed05cdbdc6c0d788f514fd07e1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JorisK&#39;s gravatar image" />
<p><span>JorisK</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JorisK has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49286" class="comments-container">
<span id="49288"></span>
<div id="comment-49288" class="comment">
<div id="post-49288-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>are you talking of software development? What do you mean by "reflected"? Do you mean if a shop is moved 20 meters in OSM, then your annotations should also move?</p>
</div>
<div id="comment-49288-info" class="comment-info">
<span class="comment-age">(18 Apr '16, 19:10)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-49286" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49286-form-container" class="comment-form-container">
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

<span id="49294"></span>

<div id="answer-container-49294" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49294-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49294-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49294-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not easy to do, particularly because you cannot assume that OSM ids are stable. I would suggest looking at <a href="http://opentraffic.io/">http://opentraffic.io/</a> for way matching code. While their application is slightly different they essentially had to solve the same issue as you.</p>
<p>Naturally you could build something that tracks changes by consuming diffs, however this is likely to be very tricky to do and you would still need to use something as indicated above as a fallback.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '16, 10:55</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Apr '16, 15:33</strong> </span></p>
</div>
</div>
<div id="comments-container-49294" class="comments-container">
&#10;</div>
<div id="comment-tools-49294" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49294-form-container" class="comment-form-container">
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

