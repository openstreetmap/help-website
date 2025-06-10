+++
type = "question"
title = "extracting street data from osm files"
description = '''Hi Iam quite new to open street map so have a pretty basic question How would I go about extracting all the street data from an osm file. Eg Street number , street name, suburb, post code , long, lat Regards Adrian'''
date = "2013-05-24T17:24:00Z"
lastmod = "2013-05-25T20:06:00Z"
weight = 22736
keywords = [ "extraction" ]
aliases = [ "/questions/22736" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [extracting street data from osm files](/questions/22736/extracting-street-data-from-osm-files)

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
<span id="post-22736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22736-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Iam quite new to open street map so have a pretty basic question</p>
<p>How would I go about extracting all the street data from an osm file.</p>
<p>Eg</p>
<p>Street number , street name, suburb, post code , long, lat</p>
<p>Regards Adrian</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extraction" rel="tag" title="see questions tagged &#39;extraction&#39;">extraction</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '13, 17:24</strong></p>
<img src="https://secure.gravatar.com/avatar/729e211fba7cdec048f42501868dd950?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adrian&#39;s gravatar image" />
<p><span>adrian</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adrian has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22736" class="comments-container">
&#10;</div>
<div id="comment-tools-22736" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22736-form-container" class="comment-form-container">
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

<span id="22738"></span>

<div id="answer-container-22738" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22738-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tag you'll find most streets under is <code>highway</code>. There are lots of different used values for <code>highway</code>, e.g. <code>highway=motorway</code>, <code>highway=residential</code>.</p>
<p>Also, what is the lat/lon of a street in your context - the middle node?</p>
<p>Suburbs and postcodes are not connected to streets other than through their respective geographic location, which means you need at least some kind of GIS-like functionality to get the suburb for a street (or hope there are addresses that reference the street).</p>
<p>Probably you need to load a suitable OSM extract into a PostGIS database and work from there. You can start with <a href="http://wiki.openstreetmap.org/wiki/Osm2pgsql">http://wiki.openstreetmap.org/wiki/Osm2pgsql</a> and read on from there.</p>
<p>Also, note that OSM street data is not complete and that suburb data quality and quantity and suburb tagging may vary from country to country.</p>
<p>So no, thats not a basic question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '13, 19:08</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-22738" class="comments-container">
&#10;</div>
<div id="comment-tools-22738" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22738-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22762"></span>

<div id="answer-container-22762" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22762-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-22762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are not the first one asking this question.</p>
<p>Please type keywords like "extract street" or similar in the searchbox of this FAQ site, and you will get a number of hints about your aim.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '13, 20:06</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-22762" class="comments-container">
&#10;</div>
<div id="comment-tools-22762" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22762-form-container" class="comment-form-container">
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

