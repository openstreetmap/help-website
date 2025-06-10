+++
type = "question"
title = "Park map with tilemill"
description = '''I am an ios developer who is making a tour app that involves a live map of a park. I have used mapBox to pull in the basic map, but would like to generate my own so I can customize the look just so. It&#x27;s a very small area that I am actually concerned about, so I don&#x27;t know the best way to accomplish...'''
date = "2014-07-10T22:27:00Z"
lastmod = "2014-07-11T09:50:00Z"
weight = 34817
keywords = [ "tilemill", "ios" ]
aliases = [ "/questions/34817" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Park map with tilemill](/questions/34817/park-map-with-tilemill)

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
<span id="post-34817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34817-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am an ios developer who is making a tour app that involves a live map of a park. I have used mapBox to pull in the basic map, but would like to generate my own so I can customize the look just so. It's a very small area that I am actually concerned about, so I don't know the best way to accomplish this. I've downloaded tile mill and tried to follow their instructions for osm bright. I am lacking even a clear concept as to what each of these apps are doing.</p>
<p>Why do I use OSM Bright with tile map?</p>
<p>How can I get street data in tile map that I can style? If I download shapefiles directly, do I still need osm bright?</p>
<p>How do I know which zip files to use with osm bright? Where can I find those?</p>
<p>What should I expect to see when I launch the osm bright project in tilemill? I'm only seeing the base map layer at high zoom levels. Does this mean I've done something wrong, or is it working. If so, how to I get streets, trials, etc?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-ios" rel="tag" title="see questions tagged &#39;ios&#39;">ios</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '14, 22:27</strong></p>
<img src="https://secure.gravatar.com/avatar/04f95734f7ac143ab00e226262fce1e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pukeanddie&#39;s gravatar image" />
<p><span>pukeanddie</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pukeanddie has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34817" class="comments-container">
&#10;</div>
<div id="comment-tools-34817" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34817-form-container" class="comment-form-container">
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

<span id="34826"></span>

<div id="answer-container-34826" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34826-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM Bright is the style (a description of what the map should look like). Tilemill is a tool that helps writing and visualising styles. It uses data downloaded in osm format and imported into a postgresql database, does the actual rendering using Mapnik, and presents the whole thing with a slippy map, text editor, and project management.</p>
<p>The OSM-Bright readme has clear instruction on how to get data into the database. Once you have that, create a Tilemill project that points to your style and your database. Edit the style to your taste, and then copy all the tilemill-generated images for you app to use.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '14, 09:50</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-34826" class="comments-container">
&#10;</div>
<div id="comment-tools-34826" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34826-form-container" class="comment-form-container">
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

