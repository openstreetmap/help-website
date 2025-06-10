+++
type = "question"
title = "How to filter or shrink .osm.pbf size for planet map"
description = '''Hi everyone! First of all, I am a beginner at using OpenStreetMap for development purposes. Now, I am being involved in a project where we would like to have the planet map for offline usage due to limited or no internet connection. So, we are considering to self-host an OpenStreetMap Tile Server lo...'''
date = "2021-06-25T12:48:00Z"
lastmod = "2021-06-28T13:16:00Z"
weight = 80710
keywords = [ "docker", "switch2osm", "osm", "tiles", "tileserver" ]
aliases = [ "/questions/80710" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter or shrink .osm.pbf size for planet map](/questions/80710/how-to-filter-or-shrink-osmpbf-size-for-planet-map)

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
<span id="post-80710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80710-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone!</p>
<p>First of all, I am a beginner at using OpenStreetMap for development purposes. Now, I am being involved in a project where we would like to have the planet map for offline usage due to limited or no internet connection.</p>
<p>So, we are considering to self-host an OpenStreetMap Tile Server locally on our HMI touchscreen device using this approach described <a href="https://switch2osm.org/serving-tiles/using-a-docker-container/">here</a>, by running a docker image. And feed our Qt application on a touchscreen device with map data through the local self-hosted tile server and update data when it's possible with a better internet connection.</p>
<p>However, our HMI touchscreen device has limited hardware capabilities and I am really concerned about this <a href="https://github.com/Overv/openstreetmap-tile-server#setting-up-the-server">step</a> where we have to import .osm.pbf raw data into PostgreSQL. Since we want to load the planet map the importing time and resources can be extremely high and this is a big problem during first-time device installation.</p>
<p>Is there a tool to filter or shrink the planet map .osm.pbf file size? For example to discard information about places, streets, and side roads, since we are mainly interested in cities, ports, airports, and highways? And also apply a range of specific zoom levels to be exported? Or do you have any idea for a different strategy, such as first-time importing data into PostgreSQL on a more powerful machine and then copy final docker volume on target devices?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-docker" rel="tag" title="see questions tagged &#39;docker&#39;">docker</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jun '21, 12:48</strong></p>
<img src="https://secure.gravatar.com/avatar/f60805c350f89d4e73a57be60624454e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pc_pacman&#39;s gravatar image" />
<p><span>pc_pacman</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pc_pacman has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80710" class="comments-container">
<span id="80711"></span>
<div id="comment-80711" class="comment">
<div id="post-80711-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A bit more info on the specifications of the "HMI touchscreen device" you're trying to use would be helpful, and also what zoom levels, what geographical area you want to cover and what map style you're planning to use.</p>
<p>If it's really limited then a different approach (perhaps using vector tiles, as is often done for phone-based map apps) might be a better one.</p>
</div>
<div id="comment-80711-info" class="comment-info">
<span class="comment-age">(25 Jun '21, 13:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="80715"></span>
<div id="comment-80715" class="comment">
<div id="post-80715-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A different approach using vector tiles how it can be achieved? Any helpful guide and initial reference?</p>
<p>Below you can find more info about the device and specs.</p>
<p>Hardware Requirements of our HMI touchscreen device:</p>
<p>CPU: Intel® Pentium® QuadCore N4200 GPU Graphics: Intel® HD Graphics Memory 4GB DDR4 non-ECC (max. 8GB) Storage: Industrial 128GB SSD</p>
<p>Geographical area: the whole planet since we may need to display points anywhere in the planet map</p>
<p>Zoom Level: Preferred range of zoom levels from 2 to 16.</p>
<p>Map Style: we can start with the basic style and later it's under discussion to select a different map style</p>
</div>
<div id="comment-80715-info" class="comment-info">
<span class="comment-age">(25 Jun '21, 14:40)</span> <span class="comment-user userinfo">pc_pacman</span>
</div>
</div>
<span id="80720"></span>
<div id="comment-80720" class="comment">
<div id="post-80720-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If you need the planet in z2-16, that hardware specs is nowhere able to help you out with raster tiles.</p>
<p>You may have a look at openmaptiles.org for vector tiles but I'd strongly recommend to not render anything on that hardware, be it vector or raster.</p>
<p>And even if you would render the raster tiles elsewhere, 128gb is not sufficient to save all those tiles. That might be different with vector tiles w/ reduced data/information and overzooming used.</p>
</div>
<div id="comment-80720-info" class="comment-info">
<span class="comment-age">(25 Jun '21, 19:08)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-80710" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80710-form-container" class="comment-form-container">
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

<span id="80721"></span>

<div id="answer-container-80721" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80721-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Is there a tool to filter or shrink the planet map .osm.pbf file size? For example to discard information about places, streets, and side roads, since we are mainly interested in cities, ports, airports, and highways?</p>
</blockquote>
<p>You can use <code>osmium</code> for this, using the <code>tags-filter</code> <a href="https://docs.osmcode.org/osmium/latest/osmium-tags-filter.html">option</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '21, 22:20</strong></p>
<img src="https://secure.gravatar.com/avatar/acea3c9fd5908d7ff09596d16b8724d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mvexel&#39;s gravatar image" />
<p><span>mvexel</span><br />
<span class="score" title="762 reputation points">762</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mvexel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80721" class="comments-container">
<span id="80760"></span>
<div id="comment-80760" class="comment">
<div id="post-80760-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I started working with osmium using the tags-filter and it seems that can help me shrinking the planet map file size. Now, I am trying to find all the suitable filter expressions for what should be excluded. Do you think by shrinking the .osm.pbf and using vector tiles instead of raster that it could be possible to load the planet map in offline mode on the device specs mentioned?</p>
</div>
<div id="comment-80760-info" class="comment-info">
<span class="comment-age">(28 Jun '21, 13:16)</span> <span class="comment-user userinfo">pc_pacman</span>
</div>
</div>
</div>
<div id="comment-tools-80721" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80721-form-container" class="comment-form-container">
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

