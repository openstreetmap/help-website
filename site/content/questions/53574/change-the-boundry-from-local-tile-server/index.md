+++
type = "question"
title = "Change the boundry from local tile server"
description = '''Hi, I am running a local tile server. For India Map, I want to remove the current boundary of India and insert Administrative boundary which is available with me in shape file format. How can I do that?'''
date = "2016-12-16T09:22:00Z"
lastmod = "2016-12-27T12:02:00Z"
weight = 53574
keywords = [ "admin_boundary", "change" ]
aliases = [ "/questions/53574" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Change the boundry from local tile server](/questions/53574/change-the-boundry-from-local-tile-server)

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
<span id="post-53574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53574-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am running a local tile server. For India Map, I want to remove the current boundary of India and insert Administrative boundary which is available with me in shape file format.</p>
<p>How can I do that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-change" rel="tag" title="see questions tagged &#39;change&#39;">change</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Dec '16, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/1a9eea008bc0c9a26985aa042d9b8ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reshma%20Maner&#39;s gravatar image" />
<p><span>Reshma Maner</span><br />
<span class="score" title="235 reputation points">235</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reshma Maner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53574" class="comments-container">
&#10;</div>
<div id="comment-tools-53574" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53574-form-container" class="comment-form-container">
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

<span id="53586"></span>

<div id="answer-container-53586" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53586-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is some information in <a href="https://www.openstreetmap.org/user/PlaneMad/diary/38176">this diary entry</a> that might help. If the results of the Overpass query don't get exactlly what you want then you should be able to infer something from the tags it's looking for, and fill in the gaps yourself.</p>
<p>Then, depending on what sort of tile server you're running and how it displays boundary data, update OSM's on-the-ground boundary data with the claim of a particular country.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '16, 12:14</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-53586" class="comments-container">
<span id="53603"></span>
<div id="comment-53603" class="comment">
<div id="post-53603-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is not much detail on the link you gave.</p>
<p>I am running a local OSM server and imported data using osm2pgsql script. How can I remove a state or a country boundary and upload new boundary from a shape file?</p>
</div>
<div id="comment-53603-info" class="comment-info">
<span class="comment-age">(19 Dec '16, 06:01)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="53734"></span>
<div id="comment-53734" class="comment">
<div id="post-53734-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How can I remove a state or a country boundary and upload new boundary from a shape file?</p>
</div>
<div id="comment-53734-info" class="comment-info">
<span class="comment-age">(27 Dec '16, 09:05)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="53735"></span>
<div id="comment-53735" class="comment">
<div id="post-53735-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's actually going to depend on which map style you're using currently. You'll need to understand how that currently displays admin boundaries (at various levels) now, and how the style works (how data is extracted from the rendering database for display).</p>
<p>Which map style are you using?</p>
</div>
<div id="comment-53735-info" class="comment-info">
<span class="comment-age">(27 Dec '16, 09:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="53741"></span>
<div id="comment-53741" class="comment">
<div id="post-53741-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What exactly you want to know by map style?</p>
<p>I have referred below link and set up OSM map server using osm2pgsql. Downloaded osm.pbf file and extracted data in PostGresql.</p>
<p><a href="https://seshagiriprabhu.wordpress.com/2013/07/21/building-an-openstreetmap-tile-server-on-ubuntu-12-04-lts/">https://seshagiriprabhu.wordpress.com/2013/07/21/building-an-openstreetmap-tile-server-on-ubuntu-12-04-lts/</a></p>
</div>
<div id="comment-53741-info" class="comment-info">
<span class="comment-age">(27 Dec '16, 11:18)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="53742"></span>
<div id="comment-53742" class="comment not_top_scorer">
<div id="post-53742-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am using Mod-Tile, renderd, Mapnik and OSM2pgsql tools for running the map server</p>
</div>
<div id="comment-53742-info" class="comment-info">
<span class="comment-age">(27 Dec '16, 11:26)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="53743"></span>
<div id="comment-53743" class="comment">
<div id="post-53743-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Somewhere you'll have a file "renderd.conf". In there there will probably be a line "XML=" that points to a file like "mapnik.xml". That probably came from from the PPA that you used to set up the server. If you're lucky, you'll also have a file "project.mml" or "project.yaml" that is part of the source of that style (from which mapnik.xml is created).</p>
<p>If you don't have that, I wouldn't recommend trying to edit mapnik.xml manually - I'd download a different map style, install it as per its installation instructions, and have "renderd.conf" point at that.</p>
<p>I wrote a guide <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load">here</a> that goes through the process for one map style. You may be able to use some of that to help set up a map style of your choice (see the sections below <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load#Setting_up_a_stylesheet">here</a> particularly). If you want to install a version of the "standard" map style used at openstreetmap.org read <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md">this</a>, but do check that the pre-requisites for that (e.g mapnik version).</p>
</div>
<div id="comment-53743-info" class="comment-info">
<span class="comment-age">(27 Dec '16, 12:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53586" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-53586-form-container" class="comment-form-container">
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

