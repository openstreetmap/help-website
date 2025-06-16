+++
type = "question"
title = "how to add artificial nodes to OSM map?"
description = '''Hello, I&#x27;m looking for the fastest way that I could add some artificial nodes between available nodes (maybe at certain interval) in OSM map file. actually &quot;osmosis-srtm-plugin&quot; use these nodes and update the OSM map file with elevation data. I want to increase the resolution of elevation data by ad...'''
date = "2019-07-12T21:58:00Z"
lastmod = "2019-07-20T13:04:00Z"
weight = 70013
keywords = [ "nodes", "artificial", "osmosis-srtm-plugin" ]
aliases = [ "/questions/70013" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [how to add artificial nodes to OSM map?](/questions/70013/how-to-add-artificial-nodes-to-osm-map)

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
<span id="post-70013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70013-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,<br />
I'm looking for the fastest way that I could add some artificial nodes between available nodes (maybe at certain interval) in OSM map file.<br />
actually "<strong><a href="https://github.com/locked-fg/osmosis-srtm-plugin">osmosis-srtm-plugin</a></strong>" use these nodes and update the OSM map file with elevation data. I want to increase the resolution of elevation data by adding some artificial nodes between available nodes in the OSM map file.<br />
are there any tools to do that?<br />
</p>
<p>With Best Regards,<br />
Mohsen</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-artificial" rel="tag" title="see questions tagged &#39;artificial&#39;">artificial</span> <span class="post-tag tag-link-osmosis-srtm-plugin" rel="tag" title="see questions tagged &#39;osmosis-srtm-plugin&#39;">osmosis-srtm-plugin</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '19, 21:58</strong></p>
<img src="https://secure.gravatar.com/avatar/17223d085c9c027032156c5349916e7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mohsen%20Rahmati&#39;s gravatar image" />
<p><span>Mohsen Rahmati</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mohsen Rahmati has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '19, 14:58</strong> </span></p>
</div>
</div>
<div id="comments-container-70013" class="comments-container">
<span id="70031"></span>
<div id="comment-70031" class="comment">
<div id="post-70031-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>by the way, I want to use this updated OSM map file offline, in a traffic simulation software.</p>
</div>
<div id="comment-70031-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 09:21)</span> <span class="comment-user userinfo">Mohsen Rahmati</span>
</div>
</div>
<span id="70040"></span>
<div id="comment-70040" class="comment">
<div id="post-70040-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It would help if you could explain what you're actually doing in a bit more detail, and also describe what you've tried already.</p>
</div>
<div id="comment-70040-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 11:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70043"></span>
<div id="comment-70043" class="comment">
<div id="post-70043-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your participation <a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@someoneelse</a>.<br />
There are many ways to create a network in traffic simulation software, but importing the OSM map file of the interested area is more convenient. Also, I want to see the effect of elevation in my simulation model. so, now I'm looking for the fastest way that I could add some artificial nodes into edges or links (i.e. those links that are related to roads or highways), in order to increase the resolution of the elevation data that produced by "<a href="https://github.com/locked-fg/osmosis-srtm-plugin">osmosis-srtm-plugin</a>".</p>
</div>
<div id="comment-70043-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 14:30)</span> <span class="comment-user userinfo">Mohsen Rahmati</span>
</div>
</div>
<span id="70044"></span>
<div id="comment-70044" class="comment">
<div id="post-70044-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So you're actually looking to add extra nodes to existing ways in your download (and presumably only some existing ways, perhaps corresponding with certain highway types)?</p>
<p>I'm not aware of anything that already does that, but that doesn't mean that it doesn't exist. On the other hand of course it doesn't sound that hard to write some code yourself to do that.</p>
</div>
<div id="comment-70044-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 14:38)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-70013" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70013-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="70039"></span>

<div id="answer-container-70039" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70039-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Does it matter that your new nodes are "between other nodes" (i.e. along a long straight way already in OSM) or can they just fill in the areas where there are no nodes to allow you to add elevations to them to process later?</p>
<p>If it's the latter, I'd just programmatically create a regular grid of nodes in an external .osm file a certain difference apart and merge that with the existing .osm data that you have. I'd then combine the resulting files with osmosis or similar.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '19, 11:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></br></p>
</div>
</div>
<div id="comments-container-70039" class="comments-container">
<span id="70045"></span>
<div id="comment-70045" class="comment">
<div id="post-70045-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your participation <a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@someoneelse</a>.<br />
Well, artificial nodes must be added into edges or links that are related to roads or highways. it doesn't matter how it should be added, just every edge or link should have enough number of artificial nodes to be ensured that elevation data are usefulness in the simulated network.<br />
I can do this manually in JOSM, but this is not applicable for large networks.<br />
To view the sample, see attached files that are manually created. (<span>Before</span> | <span>After</span>)</p>
</div>
<div id="comment-70045-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 14:46)</span> <span class="comment-user userinfo">Mohsen Rahmati</span>
</div>
</div>
</div>
<div id="comment-tools-70039" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70039-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70064"></span>

<div id="answer-container-70064" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70064-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have a chance to put your data in Postgis, then this function may help:</p>
<p><a href="https://postgis.net/docs/ST_Segmentize.html">https://postgis.net/docs/ST_Segmentize.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '19, 15:27</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span> </br></br></p>
</div>
</div>
<div id="comments-container-70064" class="comments-container">
<span id="70140"></span>
<div id="comment-70140" class="comment">
<div id="post-70140-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your participation <a href="https://help.openstreetmap.org/users/5587/yvecai"></a><a href="https://help.openstreetmap.org/users/5587/yvecai">@yvecai</a>.<br />
I've written a python script that uses the same underlying of what you've shared.<br />
I will share the script here, hope to be helpful.</p>
</div>
<div id="comment-70140-info" class="comment-info">
<span class="comment-age">(20 Jul '19, 12:53)</span> <span class="comment-user userinfo">Mohsen Rahmati</span>
</div>
</div>
</div>
<div id="comment-tools-70064" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70064-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70141"></span>

<div id="answer-container-70141" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70141-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As I mentioned above, I was looking for a tool that could add some artificial nodes into the ways of the OSM map file. my goal was to increase the resolution of the elevation data that was later added with the "<a href="https://github.com/locked-fg/osmosis-srtm-plugin">Osmosis-SRTM-Plugin</a>".<br />
<br />
I've written a python script which creates artificial nodes till all segments lengths in the OSM map file become lower than the predefined threshold. then the appropriate patch file will be created to patch the input OSM map file with "<a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a>".<br />
<br />
<strong>Programming Language:</strong><br />
- Python 3.3+ (tested on python 3.7.3)<br />
<br />
</p>
<p><strong>Required Packages:</strong><br />
- osmread==0.2<br />
- numpy==1.16.4<br />
- pandas==0.24.2<br />
- shapely==1.6.4.post1<br />
- osgeo==2.3.3<br />
- geopandas==0.5.0<br />
</p>
<p><strong>Python Script Repository (OSMEditor):</strong><br />
- <a href="https://github.com/Mohsen-eng74/OSMEditor">https://github.com/Mohsen-eng74/OSMEditor</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jul '19, 13:04</strong></p>
<img src="https://secure.gravatar.com/avatar/17223d085c9c027032156c5349916e7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mohsen%20Rahmati&#39;s gravatar image" />
<p><span>Mohsen Rahmati</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mohsen Rahmati has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jul '19, 13:14</strong> </span></p>
</div>
</div>
<div id="comments-container-70141" class="comments-container">
&#10;</div>
<div id="comment-tools-70141" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70141-form-container" class="comment-form-container">
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

