+++
type = "question"
title = "After I import a new area to my postgresql, Why cannot I see my new imported data?"
description = '''Hello, I bulid my own tile server using mod_tile, mapnik, PostgreSql, osm2psql, Apache2, leaflet based on ubuntu16.04. But after I used the command &quot;osm2pgsql --slim -d gis -C 3600 --hstore -S openstreetmap-carto-2.41.0/openstreetmap-carto.style chongqing_china.osm.pbf&quot; to update my database. I was ...'''
date = "2017-11-25T04:43:00Z"
lastmod = "2017-11-25T13:08:00Z"
weight = 60770
keywords = [ "new", "see", "cannot", "mapdata" ]
aliases = [ "/questions/60770" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [After I import a new area to my postgresql, Why cannot I see my new imported data?](/questions/60770/after-i-import-a-new-area-to-my-postgresql-why-cannot-i-see-my-new-imported-data)

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
<span id="post-60770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60770-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I bulid my own tile server using mod_tile, mapnik, PostgreSql, osm2psql, Apache2, leaflet based on ubuntu16.04. But after I used the command "osm2pgsql --slim -d gis -C 3600 --hstore -S openstreetmap-carto-2.41.0/openstreetmap-carto.style chongqing_china.osm.pbf" to update my database. I was sure that the database was updated. But when I typed my ip in my broswer, what I could see wes my previous mapdata not my new data. What should I do to see my new imported mapdata?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-new" rel="tag" title="see questions tagged &#39;new&#39;">new</span> <span class="post-tag tag-link-see" rel="tag" title="see questions tagged &#39;see&#39;">see</span> <span class="post-tag tag-link-cannot" rel="tag" title="see questions tagged &#39;cannot&#39;">cannot</span> <span class="post-tag tag-link-mapdata" rel="tag" title="see questions tagged &#39;mapdata&#39;">mapdata</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Nov '17, 04:43</strong></p>
<img src="https://secure.gravatar.com/avatar/66e4305afae2faf808a2b600525c4cc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gleide&#39;s gravatar image" />
<p><span>gleide</span><br />
<span class="score" title="79 reputation points">79</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gleide has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-60770" class="comments-container">
<span id="60775"></span>
<div id="comment-60775" class="comment">
<div id="post-60775-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>First time I use the command I can see the map that is what i imported, But when I use the command to import a different area to the same database, I still only see the previous map. I did renderded again and restarted apache. Hope someone could help me! Thanks very much.</p>
</div>
<div id="comment-60775-info" class="comment-info">
<span class="comment-age">(25 Nov '17, 11:55)</span> <span class="comment-user userinfo">gleide</span>
</div>
</div>
</div>
<div id="comment-tools-60770" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60770-form-container" class="comment-form-container">
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

<span id="60776"></span>

<div id="answer-container-60776" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60776-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60776-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60776-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'll need to stop and restart renderd and apache</p>
<pre><code>sudo /etc/init.d/renderd restart
sudo /etc/init.d/apache2 restart</code></pre>
<p>you'll want to remove old tiles:</p>
<pre><code>sudo rm -rf /var/lib/mod_tiles/wherever/?
sudo rm -rf /var/lib/mod_tiles/wherever/??</code></pre>
<p>and the first time you view the new area in a web browser you'll need to clear-cache or "shift-refresh" to force load a new tile.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '17, 12:02</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-60776" class="comments-container">
<span id="60777"></span>
<div id="comment-60777" class="comment">
<div id="post-60777-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thank you very much. That solved my problem!</p>
</div>
<div id="comment-60777-info" class="comment-info">
<span class="comment-age">(25 Nov '17, 13:08)</span> <span class="comment-user userinfo">gleide</span>
</div>
</div>
</div>
<div id="comment-tools-60776" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60776-form-container" class="comment-form-container">
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

