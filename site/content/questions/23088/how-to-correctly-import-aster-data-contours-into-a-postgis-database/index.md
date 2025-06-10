+++
type = "question"
title = "How to correctly import ASTER data (contours) into a PostGIS database"
description = '''I&#x27;ve got a tile-server up and running on an Ubuntu 12.04 VM (I followed this guide exactly to create this: http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/) I tried to add contours following the http://wiki.openstreetmap.org/wiki/Contours guide. I downloaded the area of int...'''
date = "2013-06-07T02:55:00Z"
lastmod = "2013-06-20T13:10:00Z"
weight = 23088
keywords = [ "osm", "contours", "mapnik", "tileserver" ]
aliases = [ "/questions/23088" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to correctly import ASTER data (contours) into a PostGIS database](/questions/23088/how-to-correctly-import-aster-data-contours-into-a-postgis-database)

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
<span id="post-23088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23088-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've got a tile-server up and running on an Ubuntu 12.04 VM (I followed this guide exactly to create this: <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/</a>)</p>
<p>I tried to add contours following the <a href="http://wiki.openstreetmap.org/wiki/Contours">http://wiki.openstreetmap.org/wiki/Contours</a> guide.</p>
<p>I downloaded the area of interest as ASTER Global Digital Elevation Model V002 data and imported this into the database as described - no errors were encountered during this process.</p>
<p>I then added the styles and layers listed under the "For mapnik version 2.1 the xml changed a little bit, so I added this in osm.xml" section into my osm.xml file.</p>
<p>Now I cannot render any tiles. If I remove the added stuff from the osm.xml file then it all works again. (This is repeatable).</p>
<p>If I run the tile server interactively via the console with the command renderd -f -c /usr/local/etc/renderd.conf then errors parsing the sql in the style rules appear:</p>
<pre><code>column &quot;way&quot; does not exist.</code></pre>
<p>Which it doesn't - the script "import_ASTGTM2.sh" on the contours page does not include this column - the contours table has the columns gid, Id, height and geometry.</p>
<p>The deprecated script for importing the SRTM3 data DOES contain this column so I'm guessing it's an oversight in the ASTER script? I have no idea how to adapt it though to include this column.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-contours" rel="tag" title="see questions tagged &#39;contours&#39;">contours</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '13, 02:55</strong></p>
<img src="https://secure.gravatar.com/avatar/d0323e670bafa590ec131e5d08f1b85e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tangotonyb&#39;s gravatar image" />
<p><span>Tangotonyb</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tangotonyb has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jun '13, 16:29</strong> </span></p>
</div>
</div>
<div id="comments-container-23088" class="comments-container">
<span id="23091"></span>
<div id="comment-23091" class="comment">
<div id="post-23091-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There's a bit of the "manually building a tile server" guide that says "We’ll run it interctively first...". That causes renderd output to appear interactively instead of in a system log file /var/log/syslog.<br />
</p>
<p>Perhaps try that and edit your question to include any errors listd in there, if you see any?</p>
</div>
<div id="comment-23091-info" class="comment-info">
<span class="comment-age">(07 Jun '13, 09:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="23092"></span>
<div id="comment-23092" class="comment">
<div id="post-23092-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks - good call I should have seen that - question updated.</p>
</div>
<div id="comment-23092-info" class="comment-info">
<span class="comment-age">(07 Jun '13, 09:48)</span> <span class="comment-user userinfo">Tangotonyb</span>
</div>
</div>
</div>
<div id="comment-tools-23088" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23088-form-container" class="comment-form-container">
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

<span id="23114"></span>

<div id="answer-container-23114" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23114-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-23114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tangotonyb has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the Aster script, the column is named 'geometry' instead of way. Change the script or Mapnik postgis request accordingly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '13, 19:06</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span> </br></p>
</div>
</div>
<div id="comments-container-23114" class="comments-container">
<span id="23156"></span>
<div id="comment-23156" class="comment">
<div id="post-23156-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thankyou - works nicely</p>
</div>
<div id="comment-23156-info" class="comment-info">
<span class="comment-age">(09 Jun '13, 17:25)</span> <span class="comment-user userinfo">Tangotonyb</span>
</div>
</div>
<span id="23161"></span>
<div id="comment-23161" class="comment">
<div id="post-23161-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Have added a note to the talk page of <span>the wiki page contours</span>. If someone here can, please add this info to the relevant section of the manual.</p>
</div>
<div id="comment-23161-info" class="comment-info">
<span class="comment-age">(09 Jun '13, 20:23)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="23554"></span>
<div id="comment-23554" class="comment">
<div id="post-23554-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Speaking entirely personally, I'd be worried that doing this would overcomplicate the "manually-building-a-tile-server-12-04" page. A "minutely mapnik" section of that would probably be a higher priority.</p>
</div>
<div id="comment-23554-info" class="comment-info">
<span class="comment-age">(20 Jun '13, 13:10)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23114" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23114-form-container" class="comment-form-container">
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

