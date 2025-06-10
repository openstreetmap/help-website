+++
type = "question"
title = "Naming Garmin (RoadTrip) maps something other than &quot;OSM Map&quot;"
description = '''I have been experimenting with generating Garmin maps with mkgmap, and then converting them to Garmin&#x27;s Mac-platform &quot;.gmapi&quot; format for using them in RoadTrip, by using &quot;Gmapi Builder.app&quot;. This works great, except for one thing. The maps are always named &quot;OSM Map&quot;, and that means that I can only i...'''
date = "2012-06-21T09:08:00Z"
lastmod = "2012-06-21T14:30:00Z"
weight = 13677
keywords = [ "mkgmap", "garmin", "gmapi", "roadtrip" ]
aliases = [ "/questions/13677" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Naming Garmin (RoadTrip) maps something other than "OSM Map"](/questions/13677/naming-garmin-roadtrip-maps-something-other-than-osm-map)

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
<span id="post-13677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13677-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been experimenting with generating Garmin maps with mkgmap, and then converting them to Garmin's Mac-platform ".gmapi" format for using them in RoadTrip, by using "Gmapi Builder.app". This works great, except for one thing. The maps are always named "OSM Map", and that means that I can only install one at a time — they seem to overwrite each other. Now, mkgmap has gazillion switches for setting various names and identifiers on maps. Which one of all these is it that I need to change?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mkgmap" rel="tag" title="see questions tagged &#39;mkgmap&#39;">mkgmap</span> <span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span> <span class="post-tag tag-link-gmapi" rel="tag" title="see questions tagged &#39;gmapi&#39;">gmapi</span> <span class="post-tag tag-link-roadtrip" rel="tag" title="see questions tagged &#39;roadtrip&#39;">roadtrip</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '12, 09:08</strong></p>
<img src="https://secure.gravatar.com/avatar/80abc4597de5aeb507c5a7ccd4ccee7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="turepalsson&#39;s gravatar image" />
<p><span>turepalsson</span><br />
<span class="score" title="836 reputation points">836</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="turepalsson has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-13677" class="comments-container">
&#10;</div>
<div id="comment-tools-13677" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13677-form-container" class="comment-form-container">
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

<span id="13690"></span>

<div id="answer-container-13690" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13690-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>--family-name and --area-name did not make much apparent difference. Eventually, I concluded that --series-name seems to be the critical one.</p>
<p>Here is what my workflow looks like:</p>
<p>I start with a bunch of .osm.pbf files, let's say rhone-alpes.osm.pbf and ile-de-france.osm.pbf. I run 'splitter' on each one of these, each in a "clean" directory, giving each a unique --mapid. So, r-a might get 19710001 and i-d-f gets 19720001. This results in a set of tile .osm.pbf files named 19710001.osm.pbf, 19710002.osm.pbf and so on for r-a, and 19720001, 19720002, etc for i-d-f.</p>
<p>I then run mkgmap once for each directory. I set the family ID to 1971 for r-a, 1972 for i-d-f. The family name, series name and area name are all set to the basename of the .osm.pbf file it started with. This gives me (in each directory) files named osmmap.tdb and osmmap.img.</p>
<p>Finally, i open each osmmap.tdb file in Gmapi builder and hit "convert". This gives me rhone-alpes.gmapi and ile-de-france.gmapi. These can be installed by double-clicking them, and display fine in Road Trip and Base Camp. The only remaining problem is that I can only see one of them at a time. Is it possible to have maps that are installed separately, but display at the same time in e.g. RoadTrip?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '12, 14:30</strong></p>
<img src="https://secure.gravatar.com/avatar/80abc4597de5aeb507c5a7ccd4ccee7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="turepalsson&#39;s gravatar image" />
<p><span>turepalsson</span><br />
<span class="score" title="836 reputation points">836</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="turepalsson has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-13690" class="comments-container">
&#10;</div>
<div id="comment-tools-13690" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13690-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13679"></span>

<div id="answer-container-13679" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13679-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><em>--family-name</em> and perhaps <em>--area-name</em> will let you set display names of maps differently.</p>
<p>More importantly, you need to set <em>--product-id</em> to a different value for every map, otherwise your garmin device will only see one of the *.img files.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '12, 09:54</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-13679" class="comments-container">
&#10;</div>
<div id="comment-tools-13679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13679-form-container" class="comment-form-container">
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

