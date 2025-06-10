+++
type = "question"
title = "How to keep local database in sync with OSM?"
description = '''Hi There - I&#x27;m new to OSM and I&#x27;m trying to figure out the best way to keep a local PostGIS version of OSM (one country) in sync with OSM main. I&#x27;m using OSM data to as one input into some road verification work. So where a road in my copy is modified, I&#x27;d like to keep that modification (it mighten&#x27;...'''
date = "2020-03-03T01:23:00Z"
lastmod = "2020-03-05T04:50:00Z"
weight = 73318
keywords = [ "osmosis", "road", "sync", "postgis", "database" ]
aliases = [ "/questions/73318" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to keep local database in sync with OSM?](/questions/73318/how-to-keep-local-database-in-sync-with-osm)

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
<span id="post-73318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73318-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi There - I'm new to OSM and I'm trying to figure out the best way to keep a local PostGIS version of OSM (one country) in sync with OSM main. I'm using OSM data to as one input into some road verification work. So where a road in my copy is modified, I'd like to keep that modification (it mighten't be relevant to anyone else) but where new features exist or features changed in OSM (that have not been modified locally) I'd like to bring them into my local copy. Can anyone give some pointers or links to the best way to approach this?</p>
<p>Thanks for any help</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-sync" rel="tag" title="see questions tagged &#39;sync&#39;">sync</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Mar '20, 01:23</strong></p>
<img src="https://secure.gravatar.com/avatar/c3ff4a6fb6c4ca04f44e328fc275404c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quannah&#39;s gravatar image" />
<p><span>Quannah</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quannah has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73318" class="comments-container">
&#10;</div>
<div id="comment-tools-73318" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73318-form-container" class="comment-form-container">
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

<span id="73353"></span>

<div id="answer-container-73353" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73353-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would read <a href="https://ircama.github.io/osm-carto-tutorials/updating-data/">this</a> for an introduction to the process of syncing. Then I'd check <a href="http://download.openstreetmap.fr/">OSM FR</a> to see if the country you want is in their list, as this will simply the process of dealing with only your area of interest.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '20, 04:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a22e0d8d83a5f9fe7ca0e51f61f77da0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheSwavu&#39;s gravatar image" />
<p><span>TheSwavu</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheSwavu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '20, 04:42</strong> </span></p>
</div>
</div>
<div id="comments-container-73353" class="comments-container">
<span id="73379"></span>
<div id="comment-73379" class="comment">
<div id="post-73379-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks - using that page and a couple others I think the process goes like this:</p>
<ol>
<li>Get the latest timestamp of the OSM main data</li>
<li>Create the configuration, download.lock and state.txt files</li>
<li>Generate a change (.osc diff file)of the database changes</li>
<li>Apply the change file/s to the database.</li>
</ol>
<p>Is that how its supposed to work?</p>
<p>Once I have the state file for my country <a href="https://download.geofabrik.de/australia-oceania-updates/">https://download.geofabrik.de/australia-oceania-updates/</a> and a configuration file in a working directory my osmosis command looks like this</p>
<pre><code>osmosis --rri workingDirectory=%WORKOSM% --simc --wxc - | osm2pgsql -a -S &quot;C:\Program Files\osm2pgsql-latest-x64\osm2pgsql-bin\default.style&quot; -d dbasename -U username -H localhost --slim -k --flat-nodes c:\temp\fl -r xml -</code></pre>
<p>which generates a file - but I can't figure out what it is? I was going to check a change inside the file and then verify that changes is applied in postgis but I can't open the downloaded file. Any tips on what kind of binary it is or where I'm going wrong are much appreciated.</p>
<p>I think I'm gettings somewhere (just really slowly...)</p>
</div>
<div id="comment-73379-info" class="comment-info">
<span class="comment-age">(05 Mar '20, 04:50)</span> <span class="comment-user userinfo">Quannah</span>
</div>
</div>
</div>
<div id="comment-tools-73353" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73353-form-container" class="comment-form-container">
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

