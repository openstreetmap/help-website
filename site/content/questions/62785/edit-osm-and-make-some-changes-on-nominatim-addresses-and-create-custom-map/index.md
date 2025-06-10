+++
type = "question"
title = "Edit OSM and make some changes on nominatim addresses and create custom map"
description = '''I did create a local map render virtual machine with mapnik, postgis and osm2postgis. (switch2osm article). Also I did import whole of country OSM file into Postgis and Nominatim too. So i have 2 databases. Now i need to correct my local data like streets and do some changes on names and etc (create...'''
date = "2018-03-22T21:32:00Z"
lastmod = "2018-03-23T12:24:00Z"
weight = 62785
keywords = [ "carto", "nominatim", "osm", "postgis", "mapnik" ]
aliases = [ "/questions/62785" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Edit OSM and make some changes on nominatim addresses and create custom map](/questions/62785/edit-osm-and-make-some-changes-on-nominatim-addresses-and-create-custom-map)

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
<span id="post-62785-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62785-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62785-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I did create a local map render virtual machine with mapnik, postgis and osm2postgis. (switch2osm article). Also I did import whole of country OSM file into Postgis and Nominatim too. So i have 2 databases. Now i need to correct my local data like streets and do some changes on names and etc (create custom map). The question is what i should to do? open the huge country OSM file in a OSM editor and change it? or i can do changes quick in a new OSM blank file and import it into database and replace data with my changes. Is there any tool for that? What is the solution?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '18, 21:32</strong></p>
<img src="https://secure.gravatar.com/avatar/976e165a9bd4b1aaf035f790545a0776?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cybercoder&#39;s gravatar image" />
<p><span>cybercoder</span><br />
<span class="score" title="36 reputation points">36</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cybercoder has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62785" class="comments-container">
<span id="62790"></span>
<div id="comment-62790" class="comment">
<div id="post-62790-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>any reason why you wouldn't apply those changes to the "central" OSM database and apply updates (diffs) to your DB afterwards ?</p>
</div>
<div id="comment-62790-info" class="comment-info">
<span class="comment-age">(23 Mar '18, 11:46)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="62791"></span>
<div id="comment-62791" class="comment">
<div id="post-62791-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5390/escada">@escada</a> It may we have daily changes in local data in our project which is unusable for others.</p>
</div>
<div id="comment-62791-info" class="comment-info">
<span class="comment-age">(23 Mar '18, 11:55)</span> <span class="comment-user userinfo">cybercoder</span>
</div>
</div>
</div>
<div id="comment-tools-62785" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62785-form-container" class="comment-form-container">
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

<span id="62793"></span>

<div id="answer-container-62793" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62793-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It sounds like what you want to do is to import OSM data, and then apply a bunch of changes that don't belong in OSM on top of that. Depending on what you're doing there might be licence implications with that, but I'll let others comment on that aspect.</p>
<p>A technical solution might be to prepare your changes in OSMChange format for the rendering server and adapt the process described <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap">here</a> to apply your changes to your local rendering database. You'd need to adapt the script to <em>not</em> download a "minutely diff" from OSM and instead load your changes instead. It's likely that you won't find an off-the-shelf solution for what you want to do so some coding and experimentation at your end will be needed.</p>
<p>Nominatim probably has a similar process but it's not one that I'm familiar with.</p>
<p>Also note that if you're applying <em>local</em> changes then you won't be able to apply changes from OSM itself any more; you'd need to reload your database from OSM and then reload the composite of your local changes over the top.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '18, 12:24</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-62793" class="comments-container">
&#10;</div>
<div id="comment-tools-62793" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62793-form-container" class="comment-form-container">
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

