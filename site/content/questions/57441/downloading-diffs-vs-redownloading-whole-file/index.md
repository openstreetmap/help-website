+++
type = "question"
title = "Downloading diffs vs Redownloading whole file"
description = '''I have only roads data from US, Canada and Mexico in my DB imported using osm2pgsql.  As it is mentioned in the osmupdate wiki page here You need to update the OSM file of a small geographical region every other week. Do not use osmupdate. Redownload the file from one of the OSM file services, e.g. ...'''
date = "2017-08-03T17:28:00Z"
lastmod = "2017-08-04T11:55:00Z"
weight = 57441
keywords = [ "diffs", "osm", "osm2pgsql", "update" ]
aliases = [ "/questions/57441" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Downloading diffs vs Redownloading whole file](/questions/57441/downloading-diffs-vs-redownloading-whole-file)

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
<span id="post-57441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57441-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have only roads data from US, Canada and Mexico in my DB imported using osm2pgsql. As it is mentioned in the osmupdate wiki page <a href="http://wiki.openstreetmap.org/wiki/Osmupdate">here</a></p>
<p><code>You need to update the OSM file of a small geographical region every other week. Do not use osmupdate. Redownload the file from one of the OSM file services, e.g. geofabrik.de.</code></p>
<p>Since I want to keep my db size as small as possible. will it be a good idea to do the following on a weekly basis</p>
<p>1 - Download the osm.pbf file</p>
<p>2 - convert to o5m (this step is for osm filter)</p>
<p>3 - filter for only road data</p>
<p>4 - import using osm2pgsql in slim mode using --drop</p>
<p>Any feedback will be highly appreciated</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-diffs" rel="tag" title="see questions tagged &#39;diffs&#39;">diffs</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Aug '17, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/24fb9e633cb135d94e6a9b4cc4fc6d1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aitizazk&#39;s gravatar image" />
<p><span>aitizazk</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aitizazk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Aug '17, 17:29</strong> </span></p>
</div>
</div>
<div id="comments-container-57441" class="comments-container">
&#10;</div>
<div id="comment-tools-57441" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57441-form-container" class="comment-form-container">
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

<span id="57449"></span>

<div id="answer-container-57449" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57449-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure why you don't simply change your default.style file to only import road data, the main issue that even with that your database will grow due to edits outside of the area you imported (there are however a couple of ways to work around that).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '17, 19:08</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-57449" class="comments-container">
<span id="57458"></span>
<div id="comment-57458" class="comment">
<div id="post-57458-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you guide me regarding the work around?</p>
</div>
<div id="comment-57458-info" class="comment-info">
<span class="comment-age">(04 Aug '17, 10:46)</span> <span class="comment-user userinfo">aitizazk</span>
</div>
</div>
<span id="57459"></span>
<div id="comment-57459" class="comment">
<div id="post-57459-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>One possible workaround is to use <a href="https://github.com/zverik/regional">https://github.com/zverik/regional</a> from Zverik . That's really simple to use (just call it with the parameters you need to trim the update file down). There's an example of its use described at <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap">https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap</a> .</p>
</div>
<div id="comment-57459-info" class="comment-info">
<span class="comment-age">(04 Aug '17, 11:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-57449" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57449-form-container" class="comment-form-container">
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

