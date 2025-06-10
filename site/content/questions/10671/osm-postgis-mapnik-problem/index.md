+++
type = "question"
title = "OSM – PostGIS – Mapnik problem!"
description = '''Hello,  I have to learn how to make maps using OSM data. The data will be in held in a PostGIS database and my role in the project is to learn how to take this data and make pretty maps using Mapnik, store the tiles and use something to make slippy maps that can be accessed by the public for free vi...'''
date = "2012-02-20T11:34:00Z"
lastmod = "2012-02-20T21:04:00Z"
weight = 10671
keywords = [ "mapnik", "postgresql", "postgres", "postgis" ]
aliases = [ "/questions/10671" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OSM – PostGIS – Mapnik problem!](/questions/10671/osm-postgis-mapnik-problem)

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
<span id="post-10671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10671-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I have to learn how to make maps using OSM data. The data will be in held in a PostGIS database and my role in the project is to learn how to take this data and make pretty maps using Mapnik, store the tiles and use something to make slippy maps that can be accessed by the public for free via a web server. In order to fully understand / get to grips with my end I thought I had better learn / get familiar with the whole process. To the end I have done the following: - I have installed the OSGeo live version 5 bundle on a virtual machine on my PC. I believe this means it is running in ubuntu. - Then downloaded United_Kingdom.shapefiles.zip, unzipped and used QGIS to make the shape file go into an sql database (PostGIS). - I think I then access mapnik through a terminal thing a bit like when you want to run command lines through dos. There doesn’t seem to be another way that I could see? I am sorry if I sound like a bit of an idiot, but I don’t really understand what Mapnik is, I thought it was going to be something like ArcGIS or Mapinfo, both of which I’ve seen before. Anyway, I followed some instructions using something they called “python bindings” and managed to get my .shp files to make maps in the .png format. I have some instructions on how I can make that ‘executable’ – whatever that means?</p>
<p>But I need to be able to make these maps from data in the PostGIS database, and I can’t seem to figure out how to do that. I have tried some code copied off OSMwiki, but that didn’t work. Someone has suggested that Mapnik maybe doesn’t know how to read from PostGIS and told me to type ‘registered datasource : postgis’ but I got ‘registered : command not found’ and I don’t even know what that means!</p>
<p>I have been using this OSGeo thing as it came; I have not installed or uninstalled anything else. I am sorry if I am asking help on something really basic and potentially obvious, I don’t come from a computer background and I think I am out of my depth!!</p>
<p>Manythanks TM</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '12, 11:34</strong></p>
<img src="https://secure.gravatar.com/avatar/534850577a0dcc6c2ab4dc987b5ee6a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OSM-GB&#39;s gravatar image" />
<p><span>OSM-GB</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OSM-GB has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-10671" class="comments-container">
&#10;</div>
<div id="comment-tools-10671" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10671-form-container" class="comment-form-container">
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

<span id="10674"></span>

<div id="answer-container-10674" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10674-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-10674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are asking many things at the same time. A single answer in this forum will probably not elevate you from your current position ("not from a computer background and out of your depth") to where you would like to be ("take this data and make pretty maps"). I see a serious learning curve ahead of you that will definitely include some study of our <a href="http://www.openstreetmap.org">wiki</a>!</p>
<p>A few pointers:</p>
<ul>
<li>Serious OSM map makers never use shape files; they use osm2pgsql or imposm to convert OSM data directly to PostGIS (see wiki for both).</li>
<li>Don't start out with the whole of the UK. Download a county only and play with that: <a href="http://download.geofabrik.de/osm/europe/great_britain/england/">http://download.geofabrik.de/osm/europe/great_britain/england/</a></li>
<li>If you are looking for a large area and/or lot of detail then you will not be able to simply "produce and store tiles"; you will have to set up a "tile server" that computes them on demand.</li>
<li>If your intent is to create your own map style, then you might want to have a look at the TileMill software which simplifies the round-trip times during style development, and which is capable of producing a Mapnik style file at the end.</li>
<li>Some software installation is very likely required so at the very least you will have to install that OSGeo DVD in a way that allows you to add packages.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '12, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-10674" class="comments-container">
<span id="10675"></span>
<div id="comment-10675" class="comment">
<div id="post-10675-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'd also suggest reading some linux primer if you've only ever used Windows or MacOSX. A quick googling gave me <a href="http://lifehacker.com/5633909/who-needs-a-mouse-learn-to-use-the-command-line-for-almost-anything">http://lifehacker.com/5633909/who-needs-a-mouse-learn-to-use-the-command-line-for-almost-anything</a> but googling for "linux", "command-line", "ubuntu", "primer", "tutorial" etc will give you more.</p>
<p>Approach your problem in separate phases, not worrying about the next phase until you've got the current foundation right :</p>
<ul>
<li><p>understand the VM you've downloaded</p></li>
<li><p>get some osm data into a postgres db</p></li>
<li><p>setup mapnik to render the data</p></li>
<li><p>setup a slippymap to display the rendered data</p></li>
</ul>
</div>
<div id="comment-10675-info" class="comment-info">
<span class="comment-age">(20 Feb '12, 12:16)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-10674" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10674-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10683"></span>

<div id="answer-container-10683" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10683-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd suggest that the best tutorial if you want to understand the process of creating an OSM-style slippy map like the <a href="http://www.openstreetmap.org/">main page</a> based on data in a local PostGIS database is probably <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server/">this one</a>. The reason why I'd recommend it is that it starts with a standard download of Ubuntu Linux, and goes through the process of installing and configuring the necessary software until you've got a working tile server.<br />
</p>
<p>Most of the instructions are copy-and-pasteable from the page, but they still do require some familarity with Linux (particularly Ubuntu Linux) - how to install it into a virtual machine, how to stop it and start it, how to edit files, etc. Ubuntu's a good choice to base this tutorial around as it's probably the best documented Linux distribution out there - if you do a web search for "ubuntu edit file" you'll get half a dozen HOWTOs on the first page.</p>
<p>So, I'd get started and then when you have a specific problem (e.g. "I'm following XYZ instructions when I type ABC it gives me an error message DEF instead of the desired result") ask back here (or perhaps on <a href="http://wiki.openstreetmap.org/wiki/Irc">IRC</a>) - someone will be able to help.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '12, 21:04</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></br></p>
</div>
</div>
<div id="comments-container-10683" class="comments-container">
&#10;</div>
<div id="comment-tools-10683" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10683-form-container" class="comment-form-container">
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

