+++
type = "question"
title = "OSM not rendering all content"
description = '''I&#x27;m developing project with your osm soft.  Some months agora I was able to start a server of tiles using a docker (https://github.com/Overv/openstreetmap-tile-server) Now, on try to create a new server I am not able to render tiles with information about state, city and street.. all my tiles in a c...'''
date = "2019-10-03T15:00:00Z"
lastmod = "2019-12-26T11:12:00Z"
weight = 71022
keywords = [ "brazil", "tiles", "docker", "tileserver" ]
aliases = [ "/questions/71022" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM not rendering all content](/questions/71022/osm-not-rendering-all-content)

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
<span id="post-71022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71022-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm developing project with your osm soft.</p>
<p>Some months agora I was able to start a server of tiles using a docker (<a href="https://github.com/Overv/openstreetmap-tile-server)">https://github.com/Overv/openstreetmap-tile-server)</a></p>
<p>Now, on try to create a new server I am not able to render tiles with information about state, city and street.. all my tiles in a country are 'blank'</p>
<p>(northeastern Brazil) <img src="https://i.imgur.com/r5ILYW5.png" alt="alt text" /></p>
<h2 id="section">--</h2>
<p>The log of my docker can be find in : <a href="https://anotepad.com/notes/33n3c3c">https://anotepad.com/notes/33n3c3c</a></p>
<p>Data used: <a href="https://download.geofabrik.de/south-america/brazil.html">https://download.geofabrik.de/south-america/brazil.html</a></p>
<p>My question: Whats is the reason for my tiles be 'blank' ?</p>
<p>(Sorry if it is not the place to do this question)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-brazil" rel="tag" title="see questions tagged &#39;brazil&#39;">brazil</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-docker" rel="tag" title="see questions tagged &#39;docker&#39;">docker</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Oct '19, 15:00</strong></p>
<img src="https://secure.gravatar.com/avatar/7c1485a1adb683f4bab3c29a3d8283bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Diego&#39;s gravatar image" />
<p><span>Diego</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Diego has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Oct '19, 15:00</strong> </span></p>
</div>
</div>
<div id="comments-container-71022" class="comments-container">
<span id="71043"></span>
<div id="comment-71043" class="comment">
<div id="post-71043-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The log isn't visible in a web browser without adverts appearing over the top of it.</p>
<p>What have you looked at so far in order to investigate the problem?</p>
</div>
<div id="comment-71043-info" class="comment-info">
<span class="comment-age">(05 Oct '19, 11:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="71047"></span>
<div id="comment-71047" class="comment">
<div id="post-71047-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think something is breaking the thread of render of images</p>
<p>Monday, I will try to build a version using the data of a small country to test my theory</p>
</div>
<div id="comment-71047-info" class="comment-info">
<span class="comment-age">(05 Oct '19, 17:17)</span> <span class="comment-user userinfo">Diego</span>
</div>
</div>
<span id="72218"></span>
<div id="comment-72218" class="comment">
<div id="post-72218-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>AFAIK coastline rendering is normally special and done from a different file from the other data. Do you definitely have all the required data?</p>
</div>
<div id="comment-72218-info" class="comment-info">
<span class="comment-age">(26 Dec '19, 02:42)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="72219"></span>
<div id="comment-72219" class="comment">
<div id="post-72219-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do you have an extra colon in your first line <code>.../openmaptiles/brazil-latest.osm.pbf:/data.osm.pbf -v...</code>?</p>
</div>
<div id="comment-72219-info" class="comment-info">
<span class="comment-age">(26 Dec '19, 03:00)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-71022" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71022-form-container" class="comment-form-container">
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

<span id="72220"></span>

<div id="answer-container-72220" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72220-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://help.openstreetmap.org/users/4426/insertuser"></a><a href="https://help.openstreetmap.org/users/4426/insertuser">@insertUser</a></a></p>
<p>Yes, I had all required data.</p>
<p>I was able to render all content some weeks before the 'crash'</p>
<p>Current status:</p>
<ol>
<li>The OSM is working fine in the server of my client</li>
<li>I am using a public server, in some moment in the future I will recreate my OSM server</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Dec '19, 11:12</strong></p>
<img src="https://secure.gravatar.com/avatar/7c1485a1adb683f4bab3c29a3d8283bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Diego&#39;s gravatar image" />
<p><span>Diego</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Diego has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Dec '19, 11:14</strong> </span></p>
</div>
</div>
<div id="comments-container-72220" class="comments-container">
&#10;</div>
<div id="comment-tools-72220" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72220-form-container" class="comment-form-container">
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

