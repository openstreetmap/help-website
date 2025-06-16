+++
type = "question"
title = "How to load Columns via hstore command in my database which are not included in the OSM Carto Style"
description = '''Hello, right now I am trying to make a touristic map for Abakan (the capital of the Republik of the Russian Republik Khakassia). So far I used the instruction on switch2osm to load OSM Data from Geofabrik into QGIS. I used the Carto stlye sheet. Now I would like to lable streets and touristic Object...'''
date = "2015-06-18T13:45:00Z"
lastmod = "2015-06-22T19:10:00Z"
weight = 43615
keywords = [ "qgis", "rendering", "osm2sql", "hstore", "postgis" ]
aliases = [ "/questions/43615" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How to load Columns via hstore command in my database which are not included in the OSM Carto Style](/questions/43615/how-to-load-columns-via-hstore-command-in-my-database-which-are-not-included-in-the-osm-carto-style)

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
<span id="post-43615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43615-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>right now I am trying to make a touristic map for Abakan (the capital of the Republik of the Russian Republik Khakassia). So far I used the instruction on <a href="https://switch2osm.org/?s=loading+osm+data&amp;lang=en">switch2osm</a> to load OSM Data from Geofabrik into QGIS. I used the Carto stlye sheet. Now I would like to lable streets and touristic Objects with the German or English names, but the columns for these tags are missing. I guess, I somehow could get the columns tobe created using the hstore extension, but I dont kno how to do this. Is it clear what I am asking for? Thanks alot</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-osm2sql" rel="tag" title="see questions tagged &#39;osm2sql&#39;">osm2sql</span> <span class="post-tag tag-link-hstore" rel="tag" title="see questions tagged &#39;hstore&#39;">hstore</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '15, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/e57fcc103053e5d009ad1cc0031d8d73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oohay&#39;s gravatar image" />
<p><span>oohay</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oohay has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '15, 15:07</strong> </span></p>
</div>
</div>
<div id="comments-container-43615" class="comments-container">
&#10;</div>
<div id="comment-tools-43615" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43615-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="43619"></span>

<div id="answer-container-43619" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43619-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please do not ask two questions in one (particularly when they are technically not related), can you open a seperate question for your 2nd part?</p>
<p>Wrt hstore I'm assuming that you are actually loading them in to Postgres/Postgis not qgis, and likely doing that with osm2pgsql? If that is the case you can follow <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql#hstore">https://wiki.openstreetmap.org/wiki/Osm2pgsql#hstore</a> and reimport.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '15, 15:28</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-43619" class="comments-container">
&#10;</div>
<div id="comment-tools-43619" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43619-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43636"></span>

<div id="answer-container-43636" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43636-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To import with hstore, you'll need to reimport. First run <code>CREATE EXTENSION hstore;</code> in the postgres database you want to use, then pass the <code>--hstore</code> option to osm2pgsql. <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql#hstore">Read more</a>.</p>
<p>I'm afraid I don't know how to style QGis in the way you want, perhaps someone else can help. (Though like <a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a>, I advise you to open another question)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '15, 08:41</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-43636" class="comments-container">
<span id="43645"></span>
<div id="comment-43645" class="comment">
<div id="post-43645-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answers! Simon Poole is right. I am working with Postgis. And I already activated the --hstore Extension:</p>
<p><code>sudo -u postgres createuser -s $USER createdb gis psql -d gis -c 'CREATE EXTENSION hstore; CREATE EXTENSION postgis;</code></p>
<p>Than I loaded the Database in osm2pgsql by typing:</p>
<p><code>osm2pgsql --create --slim \ --cache 1000 --number-processes 2 --hstore \ --style ~/osm/openstreetmap-carto/openstreetmap-carto.style --multi-geometry \ ~/osm/meineosmdatei.osm.pbf</code></p>
<p>I guess, I have to change something in this last command to get the english an german Names. On the [switch2osm] (<a href="https://switch2osm.org/?s=loading+osm+data)">https://switch2osm.org/?s=loading+osm+data)</a> page is written that:</p>
<blockquote>
<p>--hstore causes tags not in the .style file to be stored in a special “hstore” column. Hstore is a key-value store that supports arbitrary keys and values. Having other tags in hstore allows changes later on, like rendering names in a specific language and overall makes the database more flexible, giving you greater freedom to render interesting data on maps you create.</p>
</blockquote>
<p>But there is no special hstroe column in QGIS visble....</p>
</div>
<div id="comment-43645-info" class="comment-info">
<span class="comment-age">(19 Jun '15, 15:23)</span> <span class="comment-user userinfo">oohay</span>
</div>
</div>
<span id="43663"></span>
<div id="comment-43663" class="comment">
<div id="post-43663-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>According to this older issue tracker link (<a href="https://hub.qgis.org/issues/3989),">https://hub.qgis.org/issues/3989),</a> the latest versions of QGIS should display hstore columns as text (columns?). I guess it may be doing some "on-the-fly" conversion of the data to get in a more "GIS friendly" plain text column format, but since I don't have PostGIS installed, I can't tell you for sure.</p>
</div>
<div id="comment-43663-info" class="comment-info">
<span class="comment-age">(20 Jun '15, 13:51)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
</div>
<div id="comment-tools-43636" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43636-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43669"></span>

<div id="answer-container-43669" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43669-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks a lot I rechecked my data in QGIS and found out that the English and German Names of the touristic objects are stored within the last column, which is called "tags". So my question kind of changed: How can I get two single columns with the English and German Names out of the tag column in which seem to be stored all additional tags not used by the Cartho style? Should I open a new question for that and declare my question as solved?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '15, 22:02</strong></p>
<img src="https://secure.gravatar.com/avatar/e57fcc103053e5d009ad1cc0031d8d73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oohay&#39;s gravatar image" />
<p><span>oohay</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oohay has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jun '15, 22:02</strong> </span></p>
</div>
</div>
<div id="comments-container-43669" class="comments-container">
<span id="43675"></span>
<div id="comment-43675" class="comment">
<div id="post-43675-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Opening a new question can mean more visibility which can attract answers. To get the tags as separate columns, you can use the osm2pgsql style file to add <code>name:en</code> and <code>name:de</code> which means they'll be added as columns.</p>
</div>
<div id="comment-43675-info" class="comment-info">
<span class="comment-age">(21 Jun '15, 10:31)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
</div>
<div id="comment-tools-43669" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43669-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43708"></span>

<div id="answer-container-43708" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43708-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Okay thats the solution to the problem: I edited the openstreetmap-carto.style document to create separate columns for the tags name:en and the tag name:de. I just added the lines to the document:</p>
<pre><code>node,way   name:en  text         linear
&#10;node,way   name:de  text         linear</code></pre>
<p>Thanks for your help!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '15, 19:10</strong></p>
<img src="https://secure.gravatar.com/avatar/e57fcc103053e5d009ad1cc0031d8d73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oohay&#39;s gravatar image" />
<p><span>oohay</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oohay has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jun '15, 19:15</strong> </span></p>
</div>
</div>
<div id="comments-container-43708" class="comments-container">
&#10;</div>
<div id="comment-tools-43708" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43708-form-container" class="comment-form-container">
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

