+++
type = "question"
title = "OSM maps look truncated near the last tile near New Zealand and Fiji"
description = '''Excuse me if this has been asked before or there&#x27;s a simple explanation. I have been working on a project that overlays data over OSM which brought this truncation to my attention. It only happens on one zoom level, the default level shown on your homepage, which is a good example: http://www.openst...'''
date = "2012-07-18T19:45:00Z"
lastmod = "2012-07-24T22:21:00Z"
weight = 14374
keywords = [ "rendering", "osm" ]
aliases = [ "/questions/14374" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM maps look truncated near the last tile near New Zealand and Fiji](/questions/14374/osm-maps-look-truncated-near-the-last-tile-near-new-zealand-and-fiji)

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
<span id="post-14374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14374-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Excuse me if this has been asked before or there's a simple explanation. I have been working on a project that overlays data over OSM which brought this truncation to my attention. It only happens on one zoom level, the default level shown on your homepage, which is a good example:</p>
<p><a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a></p>
<p>If you look, the label for New Zealand and Fiji has been truncated, which suggests the loss of some data of some description.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jul '12, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/f03a430638986c3a47dbdcd215ddd597?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hambwez&#39;s gravatar image" />
<p><span>hambwez</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hambwez has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14374" class="comments-container">
<span id="14379"></span>
<div id="comment-14379" class="comment">
<div id="post-14379-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to clarify, it's zoom level 2.</p>
</div>
<div id="comment-14379-info" class="comment-info">
<span class="comment-age">(18 Jul '12, 21:02)</span> <span class="comment-user userinfo">hambwez</span>
</div>
</div>
</div>
<div id="comment-tools-14374" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14374-form-container" class="comment-form-container">
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

<span id="14382"></span>

<div id="answer-container-14382" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14382-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14382-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-14382-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like the label's overlaying the 180 degree meridian:</p>
<p><a href="https://www.openstreetmap.org/?lat=-30.3&amp;lon=-179.7&amp;zoom=2&amp;layers=M">https://www.openstreetmap.org/?lat=-30.3&amp;lon=-179.7&amp;zoom=2&amp;layers=M</a></p>
<p>Maybe it's related to that?<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jul '12, 22:13</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-14382" class="comments-container">
<span id="14555"></span>
<div id="comment-14555" class="comment">
<div id="post-14555-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So no ideas on whether this is a bug with the maps or not?</p>
</div>
<div id="comment-14555-info" class="comment-info">
<span class="comment-age">(24 Jul '12, 22:21)</span> <span class="comment-user userinfo">hambwez</span>
</div>
</div>
</div>
<div id="comment-tools-14382" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14382-form-container" class="comment-form-container">
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

