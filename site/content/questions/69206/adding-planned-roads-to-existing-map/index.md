+++
type = "question"
title = "Adding planned roads to existing map"
description = '''Hello! I have to create a navigation system app for a piece of land (1km * 1km). Currently, the piece of land is empty but there are plans for adding roads.  My task is to add the planned roads onto an existing map. Navigation is also required for the added roads. Where do I start and what are the a...'''
date = "2019-05-16T10:03:00Z"
lastmod = "2019-05-21T03:21:00Z"
weight = 69206
keywords = [ "openstreetmap", "roads", "navigation", "josm", "tileserver" ]
aliases = [ "/questions/69206" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Adding planned roads to existing map](/questions/69206/adding-planned-roads-to-existing-map)

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
<span id="post-69206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69206-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello!</p>
<p>I have to create a navigation system app for a piece of land (1km * 1km). Currently, the piece of land is empty but there are plans for adding roads. My task is to add the planned roads onto an existing map. Navigation is also required for the added roads.</p>
<p>Where do I start and what are the applications I need to do this? Do I need to host my own tile server?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-navigation" rel="tag" title="see questions tagged &#39;navigation&#39;">navigation</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 May '19, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/75bfa1e4f41ffdd694ed68100d668b1b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Feruses&#39;s gravatar image" />
<p><span>Feruses</span><br />
<span class="score" title="15 reputation points">15</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Feruses has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69206" class="comments-container">
&#10;</div>
<div id="comment-tools-69206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69206-form-container" class="comment-form-container">
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

<span id="69207"></span>

<div id="answer-container-69207" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69207-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Creating a full OSM stack for this is likely far more work than you are willing to do.</p>
<p>The simplest way forward would likely be this:</p>
<ol>
<li>Obtain an OSM data file for the region of interest, e.g. by downloading it from OSM in JOSM.</li>
<li>Modify the file in the JOSM editor (you cannot use Id for this), adding the planned roads as if they were already there. Do <em>not</em> upload your changes to OSM! Save them to a file only.</li>
<li><em>perhaps</em> renumber the file to get rid of negative IDs - might not be necessary, depends on whether the tools below can work with negative IDs or not. The command-line "osmium" tool can renumber.</li>
<li>load the file into Maperitive and create a map, or map tiles, from there (alternatively, set up a tile server with osm2pgsql, mapnik, renderd, mod_tile as documented on switch2osm.org to get the "true" OSM look and feel but this is likely overkill)</li>
<li>for navigation, download Graphhopper and load the file into it</li>
</ol>
<p>Of course if you want a web site that shows your modified map and allows navigation, you'll have to code that yourself using your self-made tiles and your local Graphhopper service.</p>
<p>Please do not under any circumstances upload planned road data to the main OSM database. Firstly, we don't generally record planning data, and secondly, routers would not use these planned roads anyway. In your own local file you can act as if the planned roads were real, nobody cares, but you cannot do that on OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '19, 10:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 May '19, 10:19</strong> </span></p>
</div>
</div>
<div id="comments-container-69207" class="comments-container">
<span id="69208"></span>
<div id="comment-69208" class="comment">
<div id="post-69208-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I will try this out. Thank you very much!</p>
</div>
<div id="comment-69208-info" class="comment-info">
<span class="comment-age">(16 May '19, 10:24)</span> <span class="comment-user userinfo">Feruses</span>
</div>
</div>
<span id="69209"></span>
<div id="comment-69209" class="comment">
<div id="post-69209-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi! When I tried opening my OSM file (modified with JOSM) on Maperitive, I received this error "Script execution error (line 1): The file could not be loaded: Node <a href="https://help.openstreetmap.org/users/5110/latroc">@lat</a> attribute is missing." Do you know what the issue is?</p>
</div>
<div id="comment-69209-info" class="comment-info">
<span class="comment-age">(16 May '19, 10:49)</span> <span class="comment-user userinfo">Feruses</span>
</div>
</div>
<span id="69211"></span>
<div id="comment-69211" class="comment">
<div id="post-69211-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I guess you might have deleted a node, and JOSM perhaps leaves the deleted node in the file with an action=delete marker but drops lat/lon attributes, and then Maperitive is unhappy. You'd have to find the objects with action=delete in the XML file and remove them, OR you could use JOSM's "purge" function (instead of "delete") to get rid of them; "purge" does not leave a "deleted" object in the file.</p>
</div>
<div id="comment-69211-info" class="comment-info">
<span class="comment-age">(16 May '19, 12:18)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="69217"></span>
<div id="comment-69217" class="comment">
<div id="post-69217-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would also add that if you want to be able to do offline navigation on a phone, you can complete steps 1 and 2 and then run that osm file through <a href="https://wiki.openstreetmap.org/wiki/OsmAndMapCreator">OsmAndMapCreator</a> to give you a *.obf that can be sideloaded onto your mobile device.</p>
</div>
<div id="comment-69217-info" class="comment-info">
<span class="comment-age">(16 May '19, 19:57)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="69252"></span>
<div id="comment-69252" class="comment">
<div id="post-69252-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot for your help! I managed to modify my map via JOSM and created the map tiles through Maperitive. I would like to ask, how do I go about adding these map tiles into my web application?</p>
</div>
<div id="comment-69252-info" class="comment-info">
<span class="comment-age">(21 May '19, 03:21)</span> <span class="comment-user userinfo">Feruses</span>
</div>
</div>
</div>
<div id="comment-tools-69207" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69207-form-container" class="comment-form-container">
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

