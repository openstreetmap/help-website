+++
type = "question"
title = "How to setup PostGIS server and import .osm-file on Windows"
description = '''Hi guys, I spent the whole day trying to import a .osm-file into a database on Windows 7. I read many many pages about how to do this, but still I didn&#x27;t succeed. :-( The problem is that there are so many different tools available and as a newbie I just can&#x27;t decide which to use. I would be so happy...'''
date = "2011-10-08T18:24:00Z"
lastmod = "2012-11-25T19:21:00Z"
weight = 8363
keywords = [ "windows", "import", "postgis", "database" ]
aliases = [ "/questions/8363" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to setup PostGIS server and import .osm-file on Windows](/questions/8363/how-to-setup-postgis-server-and-import-osm-file-on-windows)

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
<span id="post-8363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8363-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys,</p>
<p>I spent the whole day trying to import a .osm-file into a database on Windows 7. I read many many pages about how to do this, but still I didn't succeed. :-(</p>
<p>The problem is that there are so many different tools available and as a newbie I just can't decide which to use.</p>
<p>I would be so happy, if you could give a step by step instruction on how to do it. It must be possible somehow! ;-) There is no need to be too detailed right now, I will try to follow your steps as good as possible and will just ask if more detail is needed for me.</p>
<p>Thank you so much in advance!</p>
<p>drummer</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Oct '11, 18:24</strong></p>
<img src="https://secure.gravatar.com/avatar/eec6214146fb12e56a8866dab146feac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="drummer83&#39;s gravatar image" />
<p><span>drummer83</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="drummer83 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8363" class="comments-container">
&#10;</div>
<div id="comment-tools-8363" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8363-form-container" class="comment-form-container">
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

<span id="8364"></span>

<div id="answer-container-8364" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8364-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Once you have set up PostGIS on Windows (which is outside the scope of OSM and you should find information about this elsewhere), <a href="http://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a> can be used to import data. You will not get a database that is fit for standard rendering with Mapnik, but if all you need is to <em>somehow</em> get the data into PostGIS, that might be the easiest way. Osmosis can write different data schemas and which one you choose depends on what you want to do with the data.</p>
<p>You could also choose an even simpler path and download a set of shape files for your region from the <a href="http://download.geofabrik.de/osm">Geofabrik download server</a>, then use the shp2pgsql that comes with PostGIS to load the shape files into a database. Note however that in contrast to the Osmosis approach, this will not give you the complete set of OSM data - just the stuff that the Geofabrik people chose to export in their shape file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '11, 18:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-8364" class="comments-container">
<span id="8370"></span>
<div id="comment-8370" class="comment">
<div id="post-8370-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>thanks for your answer. I decided to go for your second approach, as it seems to be easier. So I set up PostgreSQL 9.1 and PostGIS 1.5.3 using all the standard settings. I didn't choose to create a spatial database during the PostGIS setup.</p>
<p>When I try to import the shapefile (hamburg.shp -&gt; roads.shp) using shp2pgsql it says the connection succeeded, but I get the following error:</p>
<blockquote>
<p>Failed in pgui_exec(): FEHLER: Funktion addgeometrycolumn(unknown, unknown, unknown, unknown, unknown, integer) existiert nicht LINE 12: SELECT AddGeometryColumn('public','roads','the_geom','-1','M... ^ HINT: Keine Funktion stimmt mit dem angegebenen Namen und den Argumenttypen überein. Sie müssen möglicherweise ausdrückliche Typumwandlungen hinzufügen. Shapefile import failed.</p>
</blockquote>
<p>What is the problem here?</p>
<p>Thanks for any suggestions.</p>
<p>Using your first approach (osmosis) I guess I have to set up a database with the correct structure first. Is any of the files in this folder doing it for me?</p>
<p>C:Program Filesosmosis-0.39scriptcontrib</p>
<p>apidb_0.6.sql maybe? But what do I have to do to execute the script? I tried pasting the code in the SQL part of pgAdmin but which database has to be selected: postgres? template_postgis? a new one?</p>
<p>Thanks for any help!</p>
</div>
<div id="comment-8370-info" class="comment-info">
<span class="comment-age">(09 Oct '11, 10:33)</span> <span class="comment-user userinfo">drummer83</span>
</div>
</div>
</div>
<div id="comment-tools-8364" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8364-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8443"></span>

<div id="answer-container-8443" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8443-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8443-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8443-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, you have to do some tweaking to your postgis database to make it work with osm. If you understand German, look at my wiki-Page: <a href="http://wiki.openstreetmap.org/wiki/User:Ajoessen/Postgis">http://wiki.openstreetmap.org/wiki/User:Ajoessen/Postgis</a></p>
<p>Greetings, ajoessen</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Oct '11, 07:45</strong></p>
<img src="https://secure.gravatar.com/avatar/baddeab22266e1533be4ba4c9f3deb49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajoessen&#39;s gravatar image" />
<p><span>ajoessen</span><br />
<span class="score" title="168 reputation points">168</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajoessen has one accepted answer">9%</span></p>
</div>
</div>
<div id="comments-container-8443" class="comments-container">
<span id="17971"></span>
<div id="comment-17971" class="comment">
<div id="post-17971-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Any chance you'd know of an english version of that?</p>
</div>
<div id="comment-17971-info" class="comment-info">
<span class="comment-age">(25 Nov '12, 19:21)</span> <span class="comment-user userinfo">JuZeeMan</span>
</div>
</div>
</div>
<div id="comment-tools-8443" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8443-form-container" class="comment-form-container">
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

