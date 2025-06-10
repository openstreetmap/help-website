+++
type = "question"
title = "Add addresses via GPS coordinates."
description = '''I work for a private gated community; I have fixed all the roads and I would like to add addresses for the residences. I drove through every driveway and captured the coordinates of each home. So now I know the address and coordinates etc. I can overlay these on a map, mapbox etc, but I would like t...'''
date = "2023-08-02T20:26:00Z"
lastmod = "2023-08-03T06:40:00Z"
weight = 87593
keywords = [ "bulk", "gps", "address" ]
aliases = [ "/questions/87593" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Add addresses via GPS coordinates.](/questions/87593/add-addresses-via-gps-coordinates)

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
<span id="post-87593-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87593-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87593-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I work for a private gated community; I have fixed all the roads and I would like to add addresses for the residences. I drove through every driveway and captured the coordinates of each home. So now I know the address and coordinates etc. I can overlay these on a map, mapbox etc, but I would like to add the address data to the actual base map so we can do turn by turn navigation. I have about 1600 of these, placing them visually on the map does not work since the imagery just shows woods for the most part as we are in a very forested area. I do not want to create any duplicate data (I know there would be some) but what is the best way to add many addresses using coordinates preferably in a bulk fashion.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bulk" rel="tag" title="see questions tagged &#39;bulk&#39;">bulk</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '23, 20:26</strong></p>
<img src="https://secure.gravatar.com/avatar/7e86c8bb7affb96b3b6325334cfa0b99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tkarez&#39;s gravatar image" />
<p><span>tkarez</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tkarez has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87593" class="comments-container">
&#10;</div>
<div id="comment-tools-87593" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87593-form-container" class="comment-form-container">
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

<span id="87594"></span>

<div id="answer-container-87594" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87594-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is an open data plug-in available for the JOSM editor that can take a spreadsheet file in the form of a comma separated value (CSV). It might also take a XLS format but I haven’t tried that.</p>
<p>You can use that plug-in to either load your address data directly into the OSM map layer or, better, load it into a separate layer and then merge the non-conflicting data into the map layer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '23, 01:03</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-87594" class="comments-container">
&#10;</div>
<div id="comment-tools-87594" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87594-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87595"></span>

<div id="answer-container-87595" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87595-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can upload to OSM your gpx file with the captured coordinates of each home. Then download the GPS data with the OSM data into JOSM. These layers can be shown over any imagery.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '23, 06:40</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-87595" class="comments-container">
&#10;</div>
<div id="comment-tools-87595" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87595-form-container" class="comment-form-container">
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

