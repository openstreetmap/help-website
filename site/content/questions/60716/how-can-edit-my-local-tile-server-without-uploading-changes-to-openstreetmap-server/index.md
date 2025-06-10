+++
type = "question"
title = "How can edit my local tile server without uploading changes to openstreetmap server?"
description = '''I build a local tile server using mapnik, PostgreSql, mod_tile, Apache based on Ubuntu16.04. I want to edit my local tile server online just like openstreetmap.org. But I don&#x27;t want to upload my changes to openstreetmap server.How can I do this? I really need your help!!!'''
date = "2017-11-20T14:53:00Z"
lastmod = "2017-11-25T14:05:00Z"
weight = 60716
keywords = [ "tile", "local" ]
aliases = [ "/questions/60716" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can edit my local tile server without uploading changes to openstreetmap server?](/questions/60716/how-can-edit-my-local-tile-server-without-uploading-changes-to-openstreetmap-server)

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
<span id="post-60716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60716-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I build a local tile server using mapnik, PostgreSql, mod_tile, Apache based on Ubuntu16.04. I want to edit my local tile server online just like openstreetmap.org. But I don't want to upload my changes to openstreetmap server.How can I do this? I really need your help!!!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Nov '17, 14:53</strong></p>
<img src="https://secure.gravatar.com/avatar/66e4305afae2faf808a2b600525c4cc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gleide&#39;s gravatar image" />
<p><span>gleide</span><br />
<span class="score" title="79 reputation points">79</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gleide has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-60716" class="comments-container">
&#10;</div>
<div id="comment-tools-60716" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60716-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="60778"></span>

<div id="answer-container-60778" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60778-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I finally solved this problem as follows: Firstly, I import a .osm file to openstreetmap database which used by Rails port. Then I can edit map online with iD editor. After doing some change, I uploaded changes to openstreetmap database. Then I import the databese to a .osm file. Using osm2psql import this .osm file to my local gis atabase. Hope can help someone who met the same question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '17, 14:05</strong></p>
<img src="https://secure.gravatar.com/avatar/66e4305afae2faf808a2b600525c4cc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gleide&#39;s gravatar image" />
<p><span>gleide</span><br />
<span class="score" title="79 reputation points">79</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gleide has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-60778" class="comments-container">
&#10;</div>
<div id="comment-tools-60778" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60778-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60718"></span>

<div id="answer-container-60718" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60718-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-60718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you just want to make a few minor changes, it might be easiest to make changes directly to your PostgreSQL database, using either an SQL tool like pgsql or pgadmin or a GIS editor like QGIS.</p>
<p>If you have bigger plans - more people editing, using ID/JOSM, making more edits - then things become complicated; in addition to what you have already set up, you must then set up the <a href="https://github.com/openstreetmap/openstreetmap-website">OpenStreetMap web site</a> which, despite its name, also contains the API used by these editors. This comes with its <em>own</em> database which holds OpenStreetMap data, just in a different format. You will need to import existing OpenStreetMap data into that database using Osmosis (<code>--read-pbf --write-apidb</code>), and then you can make changes on that database with standard OSM editors. You will further have to ensure the changes made in that database find their way into your rendering database, either by doing regular exports (from API database into PBF with Osmosis, from PBF to PostGIS with osm2pgsql), or by configuring change replication with Osmosis.</p>
<p>Note that no matter which of these ways you choose, any edits you make could be overwritten by future updates from OSM, so this will cut you off from OSM updates.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Nov '17, 16:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-60718" class="comments-container">
<span id="60732"></span>
<div id="comment-60732" class="comment">
<div id="post-60732-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer.I have set up OpenStreetMap web site.In order to see my own map not openstreetmap's , I changed the file vendor/assets/openlayers/OpenStreetMap.js, adding "http://localhost/osm_tiles/${z}/${x}/${y}.png".Finally I could sign up and login to my localhost:3000 page.But when I edit something, the save button says my changes will upload to openstreetmap server.Could you speak more specifically how can I import existing OpenStreetMap data into that database using Osmosis and make changes on that database with standard OSM editors. I really need your help!!!This question has bothered me for a long time.Thank you very very much!!!</p>
</div>
<div id="comment-60732-info" class="comment-info">
<span class="comment-age">(21 Nov '17, 16:22)</span> <span class="comment-user userinfo">gleide</span>
</div>
</div>
<span id="60734"></span>
<div id="comment-60734" class="comment">
<div id="post-60734-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think you don't have to be bothered by the "will be uploaded to OpenStreetMap" message - surely you are using a different account/password with your local server than with OpenStreetMap, so even if you did something wrong, it will not be able to upload anything because the password is wrong. -- For loading OSM data into your local database, see <a href="https://help.openstreetmap.org/questions/50109/loading-data-to-apidb">https://help.openstreetmap.org/questions/50109/loading-data-to-apidb</a> and make sure to start with a very small amount of data first, to get an idea how long it takes.</p>
</div>
<div id="comment-60734-info" class="comment-info">
<span class="comment-age">(21 Nov '17, 16:26)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="60739"></span>
<div id="comment-60739" class="comment">
<div id="post-60739-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Firstly,thanks for your help.But I met new problem.I use this command "osmosis --read-pbf /home/yeager/Downloads/beijing_china.osm.pbf --write-apidb host="localhost" database="openstreetmap" user="openstreetmap" password="openstreetmap" validateSchemaVersion="no"" But it failed says that "org.postgresql.util.PSQLException: FATAL: password authentication failed for user "openstreetmap"".I just follow the guide on openstreetmapwebsite install.md. after I installed it I could find two new database one called openstreetmap the other osm_test. these two databases's initial owner is my username. Then I creat a new user named openstreetmap and set the unix password "openstreetmap".Then I alter the two databases' owner to new owner openstreetmap. So is there somewhere wrong?</p>
</div>
<div id="comment-60739-info" class="comment-info">
<span class="comment-age">(22 Nov '17, 17:12)</span> <span class="comment-user userinfo">gleide</span>
</div>
</div>
<span id="60740"></span>
<div id="comment-60740" class="comment">
<div id="post-60740-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Try this:</p>
<pre><code>sudo -u postgres psql openstreetmap -c &quot;alter user openstreetmap with password &#39;openstreetmap&#39;&quot;</code></pre>
<p>I find it strange that you have only two databases, and not a third called "openstreetmap_dev" which used to be created also. If you stumble over the lack of this database later, you might have to debug why it wasn't created, and maybe created that by hand (it has the same structure as the openstreetmap database).</p>
</div>
<div id="comment-60740-info" class="comment-info">
<span class="comment-age">(22 Nov '17, 18:27)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="60751"></span>
<div id="comment-60751" class="comment">
<div id="post-60751-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much. With your help I successfully import my osm data to my openstreetmap database. I was very glad. But afer I opened my browser and typed localhost:3000, I saw the slippy map, not only my new database,but all over the world, Could you please tell me why this happened? I just cannot see any differences between importing data to database openstreetmap with not importing data to database. Another thing is strange, when I click "edit" button ,I did some changes to my map and saved it, But I can only see changes in edit page, In my initial log in page I cannot see any change.</p>
</div>
<div id="comment-60751-info" class="comment-info">
<span class="comment-age">(23 Nov '17, 16:38)</span> <span class="comment-user userinfo">gleide</span>
</div>
</div>
<span id="60759"></span>
<div id="comment-60759" class="comment not_top_scorer">
<div id="post-60759-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello, did you see my question, I would be grateful if you could help me. Thanks for your help.</p>
</div>
<div id="comment-60759-info" class="comment-info">
<span class="comment-age">(24 Nov '17, 08:54)</span> <span class="comment-user userinfo">gleide</span>
</div>
</div>
</div>
<div id="comment-tools-60718" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-60718-form-container" class="comment-form-container">
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

