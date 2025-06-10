+++
type = "question"
title = "Render railways at zoom level below 12"
description = '''Hi There, I&#x27;ve been messing around with building my own tile server on Ubuntu 14.04 just to see what it&#x27;s like. I followed this guide: https://switch2osm.org/ I&#x27;m only a few days into this so I&#x27;m extremely new. I have a particular interest in railways. I have a few questions right off the bat that s...'''
date = "2015-04-21T16:11:00Z"
lastmod = "2015-04-21T16:48:00Z"
weight = 42522
keywords = [ "rendering", "railway" ]
aliases = [ "/questions/42522" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Render railways at zoom level below 12](/questions/42522/render-railways-at-zoom-level-below-12)

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
<span id="post-42522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42522-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi There,</p>
<p>I've been messing around with building my own tile server on Ubuntu 14.04 just to see what it's like. I followed this guide: <a href="https://switch2osm.org/">https://switch2osm.org/</a></p>
<p>I'm only a few days into this so I'm extremely new.</p>
<p>I have a particular interest in railways. I have a few questions right off the bat that someone may be able to answer:</p>
<p>I noticed that the railways only get rendered at zoom level 12 and above. Is there a way to change this? Where would I start? At which point in the process does this get defined?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Apr '15, 16:11</strong></p>
<img src="https://secure.gravatar.com/avatar/c1e1f546a7fc955f3b937a7e80c83ae5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="templar&#39;s gravatar image" />
<p><span>templar</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="templar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42522" class="comments-container">
&#10;</div>
<div id="comment-tools-42522" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42522-form-container" class="comment-form-container">
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

<span id="42524"></span>

<div id="answer-container-42524" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42524-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Near the very end. Usally a program that reads the raw data file such as a .osm XMLdata file: and then uses rules either fixed in the rendering program code, or a special format file such as .mapcss or other config file; to work out how to draw the features. If you are lucky you can find a format file in the tile making system you've just made that you can tweek to control specific problem. I'm personaly not to sure what system options you have but either others will fill in the details or I'll look into it in a bit. I'm downloading tilemill now. this page might help you in understanding the process:- <a href="http://wiki.openstreetmap.org/wiki/MapCSS">http://wiki.openstreetmap.org/wiki/MapCSS</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '15, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/30d90feb3a40fa6255767f95a8cd7943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Govanus&#39;s gravatar image" />
<p><span>Govanus</span><br />
<span class="score" title="154 reputation points">154</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Govanus has one accepted answer">3%</span></p>
</div>
</div>
<div id="comments-container-42524" class="comments-container">
<span id="42525"></span>
<div id="comment-42525" class="comment">
<div id="post-42525-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://www.mapbox.com/editor/#style">https://www.mapbox.com/editor/#style</a></p>
<p>tile maker seems to use .mss files which are working in a similar way to the mapcss page above.</p>
<p>this page might help you as it seems to work with similar stylesheets to tilemaker:-</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Phyghtmap/CartoCSS">http://wiki.openstreetmap.org/wiki/Phyghtmap/CartoCSS</a></p>
</div>
<div id="comment-42525-info" class="comment-info">
<span class="comment-age">(21 Apr '15, 16:48)</span> <span class="comment-user userinfo">Govanus</span>
</div>
</div>
</div>
<div id="comment-tools-42524" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42524-form-container" class="comment-form-container">
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

