+++
type = "question"
title = "Problem with wrong calculated boundary box"
description = '''I think that I might have a problem with osmosis tool, while importing osm.pbf file into graphhopper a boundary box on the map is placed with coordinates: &quot;bbox&quot;: [0.090027, 0.246737, 0.10008, 0.255576] But from beggining. What I want to achieve is to merge my local edited map with official OSM map,...'''
date = "2020-12-15T14:09:00Z"
lastmod = "2020-12-15T14:09:00Z"
weight = 77936
keywords = [ "boundaries", "merge", "graphhopper", "osmosis" ]
aliases = [ "/questions/77936" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with wrong calculated boundary box](/questions/77936/problem-with-wrong-calculated-boundary-box)

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
<span id="post-77936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77936-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I think that I might have a problem with osmosis tool, while importing osm.pbf file into graphhopper a boundary box on the map is placed with coordinates: <code>"bbox": [0.090027, 0.246737, 0.10008, 0.255576]</code><br />
<br />
But from beggining. What I want to achieve is to merge my local edited map with official OSM map, and upload result to my local OSM editor. In shortcut main pipeline goes like:<br />
1) Download osm.pbf file from geofabrik.de<br />
2) <code>osmosis --read-pbf file=$ORIGIN_PBF_NAME --sort --read-pbf file=$EDITED_PBF_NAME --sort --merge conflictResolutionMethod=lastSource --write-pbf file=$FINAL_PBF_NAME</code><br />
3) <code>osmosis --read-pbf file=$FINAL_PBF_NAME --write-apidb host=$DBHOST database=$DBNAME user=$DBUSER password=$DBPASSWORD validateSchemaVersion="no"</code></p>
<p>The <code>$FINAL_PBF_NAME</code> file which is merge result I can load into graphhopper, but I cannot use it because boundary box is between coordinates which I posted in earlier.<br />
<br />
What is curious? When I simply download plain new osm map from geofabrik, than upload it to DB and back save to PBF file with scripts:<br />
1) <code>osmosis -v --read-pbf file=$FINAL_PBF_NAME --write-apidb host=$DBHOST database=$DBNAME user=$DBUSER password=$DBPASSWORD lockTables=no validateSchemaVersion="no"</code><br />
2) <code>osmosis --read-apidb host=$DBHOST database=$DBNAME user=$DBUSER password=$DBPASSWORD validateSchemaVersion=no --log-progress --sort --write-pbf file=$LATEST_PBF_NAME granularity=10000</code><br />
<br />
than boundary box is calculated correctly around my map area.<br />
I've read osmosis documentation in this topic, but I didn't find anything related to.<br />
Can anyone tell me what exactly is bbox and how it's generated? Can I somehow override or set those values while saving to <code>osm.pbf</code> file?<br />
In additional what is unclear for me- is those values stored somewhere in postgres DB or it's calculating "on the fly" by external tools (i.e. graphhopper) based on some osm properties?<br />
<br />
What I suspect is that during merge I might loose some informations.<br />
<br />
Any suggestions are apprieciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-graphhopper" rel="tag" title="see questions tagged &#39;graphhopper&#39;">graphhopper</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Dec '20, 14:09</strong></p>
<img src="https://secure.gravatar.com/avatar/735ed8c1abf1a1f7b907b78d9594303c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="engopy&#39;s gravatar image" />
<p><span>engopy</span><br />
<span class="score" title="126 reputation points">126</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="engopy has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-77936" class="comments-container">
&#10;</div>
<div id="comment-tools-77936" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77936-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

