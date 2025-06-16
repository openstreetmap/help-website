+++
type = "question"
title = "Point rails port to different tile server"
description = '''I have setup the RailsPort according to https://wiki.openstreetmap.org/wiki/Rails_port and now can access it through http://localhost:3000/. The tiles are being accessed from tile.openstreetmap.org. However I want it to point to tile.localhost where I&#x27;ve already setup apache with mod_tile. Where do I...'''
date = "2012-11-04T09:01:00Z"
lastmod = "2014-11-14T02:31:00Z"
weight = 17450
keywords = [ "custom_tiles", "railsport" ]
aliases = [ "/questions/17450" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Point rails port to different tile server](/questions/17450/point-rails-port-to-different-tile-server)

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
<span id="post-17450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17450-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have setup the RailsPort according to <a href="https://wiki.openstreetmap.org/wiki/Rails_port">https://wiki.openstreetmap.org/wiki/Rails_port</a> and now can access it through <a href="http://localhost:3000/.">http://localhost:3000/.</a> The tiles are being accessed from tile.openstreetmap.org. However I want it to point to tile.localhost where I've already setup apache with mod_tile.</p>
<p>Where do I change the configuration in the RailsPort for this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-custom_tiles" rel="tag" title="see questions tagged &#39;custom_tiles&#39;">custom_tiles</span> <span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Nov '12, 09:01</strong></p>
<img src="https://secure.gravatar.com/avatar/fce9c9c5dc42d98e71856d166e984e96?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bibstha&#39;s gravatar image" />
<p><span>bibstha</span><br />
<span class="score" title="76 reputation points">76</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bibstha has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17450" class="comments-container">
&#10;</div>
<div id="comment-tools-17450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17450-form-container" class="comment-form-container">
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

<span id="17451"></span>

<div id="answer-container-17451" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17451-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think I got the answer for this. I changed the lines in file /&lt;path&gt;/openstreetmap-website/vendor/assets/openlayers/OpenStreetMap.js</p>
<pre><code>initialize: function(name, options) {
    var url = [
        &quot;http://a.tile.openstreetmap.org/${z}/${x}/${y}.png&quot;,
        &quot;http://b.tile.openstreetmap.org/${z}/${x}/${y}.png&quot;,
        &quot;http://c.tile.openstreetmap.org/${z}/${x}/${y}.png&quot;
    ];</code></pre>
<p>and it works great.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Nov '12, 09:24</strong></p>
<img src="https://secure.gravatar.com/avatar/fce9c9c5dc42d98e71856d166e984e96?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bibstha&#39;s gravatar image" />
<p><span>bibstha</span><br />
<span class="score" title="76 reputation points">76</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bibstha has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17451" class="comments-container">
<span id="36887"></span>
<div id="comment-36887" class="comment">
<div id="post-36887-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>what exactly you replace to make it work?</p>
</div>
<div id="comment-36887-info" class="comment-info">
<span class="comment-age">(17 Sep '14, 19:35)</span> <span class="comment-user userinfo">eyemax</span>
</div>
</div>
<span id="36894"></span>
<div id="comment-36894" class="comment">
<div id="post-36894-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess he replaced <code>tile.openstreetmap.org</code> with <code>tile.localhost:3000</code>.</p>
</div>
<div id="comment-36894-info" class="comment-info">
<span class="comment-age">(18 Sep '14, 07:52)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="38550"></span>
<div id="comment-38550" class="comment">
<div id="post-38550-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, this localhost:3000 is the url of the same rails port, not tile server.</p>
<p>I have been changing <a href="http://a.tile.openstreetmap.org">http://a.tile.openstreetmap.org</a> for <a href="http://localhost/osm">http://localhost/osm</a> in every file I found in /&lt;path&gt;/openstreetmap-website/ but it looks like has not effect, I keep getting always the tiles from openstreetmap.org.</p>
<p>I need to see and edit my tile server info. please help.</p>
</div>
<div id="comment-38550-info" class="comment-info">
<span class="comment-age">(14 Nov '14, 02:31)</span> <span class="comment-user userinfo">eyemax</span>
</div>
</div>
</div>
<div id="comment-tools-17451" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17451-form-container" class="comment-form-container">
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

