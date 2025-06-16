+++
type = "question"
title = "Duplicate Town names"
description = '''Hi installed OSM via the guide you prove and I am using the British Isles pack from geofabrick.  I have an issue where duplicate town names appear on different levels of zoom, please seem below for an example. Anyone seen this before? '''
date = "2016-06-24T14:01:00Z"
lastmod = "2016-06-24T17:23:00Z"
weight = 50435
keywords = [ "duplicate" ]
aliases = [ "/questions/50435" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicate Town names](/questions/50435/duplicate-town-names)

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
<span id="post-50435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50435-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi installed OSM via the guide you prove and I am using the British Isles pack from geofabrick.</p>
<p>I have an issue where duplicate town names appear on different levels of zoom, please seem below for an example. Anyone seen this before?</p>
<p><img src="http://i64.tinypic.com/24m7whi.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jun '16, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/3148bcd7e636cb9da66405667a29691c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike1704&#39;s gravatar image" />
<p><span>Mike1704</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike1704 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jun '16, 14:17</strong> </span></p>
</div>
</div>
<div id="comments-container-50435" class="comments-container">
<span id="50436"></span>
<div id="comment-50436" class="comment">
<div id="post-50436-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain which "guide" and which "British Isles pack"?</p>
</div>
<div id="comment-50436-info" class="comment-info">
<span class="comment-age">(24 Jun '16, 14:22)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50439"></span>
<div id="comment-50439" class="comment">
<div id="post-50439-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This guide</p>
<p><a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a></p>
<p>Then the british isle map pack on this page</p>
<p><a href="http://download.geofabrik.de/europe.html">http://download.geofabrik.de/europe.html</a></p>
</div>
<div id="comment-50439-info" class="comment-info">
<span class="comment-age">(24 Jun '16, 14:49)</span> <span class="comment-user userinfo">Mike1704</span>
</div>
</div>
<span id="50441"></span>
<div id="comment-50441" class="comment">
<div id="post-50441-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The word "pack" does not appear on <a href="http://download.geofabrik.de/europe.html">http://download.geofabrik.de/europe.html</a> . Do you mean you downloaded <a href="http://download.geofabrik.de/europe/british-isles-latest.osm.pbf">http://download.geofabrik.de/europe/british-isles-latest.osm.pbf</a> ?</p>
<p>What "osm2pgsql" command did you use and what were the last 5 or so lines of output?</p>
</div>
<div id="comment-50441-info" class="comment-info">
<span class="comment-age">(24 Jun '16, 14:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50442"></span>
<div id="comment-50442" class="comment">
<div id="post-50442-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes that's correct, the following command was used.</p>
<p>osm2pgsql --slim -d gis -C 10000 --number-processes 3 /usr/local/share/maps/planet/british-isles-latest.osm.pbf</p>
<p>Thanks</p>
</div>
<div id="comment-50442-info" class="comment-info">
<span class="comment-age">(24 Jun '16, 15:08)</span> <span class="comment-user userinfo">Mike1704</span>
</div>
</div>
<span id="50443"></span>
<div id="comment-50443" class="comment">
<div id="post-50443-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Since you were loading "british-isles-latest.osm.pbf" not "planet-latest.osm.pbf" at least the last part of the command would have been different.</p>
<p>What were the last 5 or so lines of output?</p>
</div>
<div id="comment-50443-info" class="comment-info">
<span class="comment-age">(24 Jun '16, 15:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50444"></span>
<div id="comment-50444" class="comment not_top_scorer">
<div id="post-50444-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't have a copy of the last 5 or so line of output, unless osm2pgsql has a history option?</p>
</div>
<div id="comment-50444-info" class="comment-info">
<span class="comment-age">(24 Jun '16, 15:35)</span> <span class="comment-user userinfo">Mike1704</span>
</div>
</div>
<span id="50445"></span>
<div id="comment-50445" class="comment not_top_scorer">
<div id="post-50445-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was just trying to figure out whether it had actually completed successfully.</p>
</div>
<div id="comment-50445-info" class="comment-info">
<span class="comment-age">(24 Jun '16, 15:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50446"></span>
<div id="comment-50446" class="comment not_top_scorer">
<div id="post-50446-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah okay, wondering if it's worth trying to use a different style sheet? That could be the issue.</p>
</div>
<div id="comment-50446-info" class="comment-info">
<span class="comment-age">(24 Jun '16, 16:16)</span> <span class="comment-user userinfo">Mike1704</span>
</div>
</div>
<span id="50448"></span>
<div id="comment-50448" class="comment not_top_scorer">
<div id="post-50448-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You're right - the stylesheet seems to be rendering everything with a name. I've put this in a separate answer to try and avoid confusion.</p>
</div>
<div id="comment-50448-info" class="comment-info">
<span class="comment-age">(24 Jun '16, 17:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50435" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-50435-form-container" class="comment-form-container">
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

<span id="50447"></span>

<div id="answer-container-50447" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50447-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's a stylesheet problem. I've loaded the data I've got here into OSMBright and I'm seeing extra Warringtons too. I'm guessing one might be the <a href="https://www.openstreetmap.org/way/38387597">NaPTAN pay scale area</a>. There are 5 names in that area - <a href="http://overpass-turbo.eu/s/gXV">this query</a> shows them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '16, 17:16</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-50447" class="comments-container">
&#10;</div>
<div id="comment-tools-50447" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50447-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50437"></span>

<div id="answer-container-50437" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50437-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From a <a href="https://www.openstreetmap.org/search?query=warrington%2C%20uk#map=12/53.4017/-2.5616">search on the main osm site</a>, there appear to be a few Warringtons that may appear at different zoom levels in the area:<br />
<a href="https://www.openstreetmap.org/relation/147278">Relation: Warrington (147278)</a><br />
<a href="https://www.openstreetmap.org/node/17409843#map=15/53.3906/-2.5942">Node: Warrington (17409843)</a><br />
<a href="https://www.openstreetmap.org/node/3123294008#map=15/53.3944/-2.5972">Railway Station Node: Warrington (3123294008)</a><br />
and two Results from GeoNames<br />
<a href="https://www.openstreetmap.org/#map=12/53.39254/-2.58024">Warrington</a> , United Kingdom<br />
<a href="https://www.openstreetmap.org/#map=12/53.41667/-2.58333">Warrington</a> , United Kingdom.<br />
[edit] ... but the main osm site shows one Warrington, so not normal to show several.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '16, 14:37</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jun '16, 15:08</strong> </span></p>
</div>
</div>
<div id="comments-container-50437" class="comments-container">
<span id="50438"></span>
<div id="comment-50438" class="comment">
<div id="post-50438-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is an issue for other areas also, are you saying this is normal?</p>
<p>Thanks</p>
</div>
<div id="comment-50438-info" class="comment-info">
<span class="comment-age">(24 Jun '16, 14:41)</span> <span class="comment-user userinfo">Mike1704</span>
</div>
</div>
<span id="50440"></span>
<div id="comment-50440" class="comment">
<div id="post-50440-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's not normal. "british-isles-latest.osm.pbf" will have the Relation, Node and Railway Station in it - it's the same data that's used to create the "standard" stle on OpenStreetMap.Org, where only one Warrington appears, as per:</p>
<p><a href="https://a.tile.openstreetmap.org/12/2018/1326.png">https://a.tile.openstreetmap.org/12/2018/1326.png</a></p>
<p>The "osmbright" stylesheet is different, and will cause a different rendering, but I can't explain the extra Warringtons.</p>
</div>
<div id="comment-50440-info" class="comment-info">
<span class="comment-age">(24 Jun '16, 14:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50437" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50437-form-container" class="comment-form-container">
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

