+++
type = "question"
title = "Error reading style file when loading osm data into postgis using osm2pgsql"
description = '''When I used osm2pgsql to load OpenStreetMap data into my postgis, I got the error message:Error reading style file line 1(fields = 1). I really don&#x27;t know how to deal with it. Beg your help! Thanks very much!'''
date = "2015-10-12T03:46:00Z"
lastmod = "2018-07-04T09:41:00Z"
weight = 45844
keywords = [ "default.style", "osm2pgsql", "postgis" ]
aliases = [ "/questions/45844" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error reading style file when loading osm data into postgis using osm2pgsql](/questions/45844/error-reading-style-file-when-loading-osm-data-into-postgis-using-osm2pgsql)

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
<span id="post-45844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45844-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I used osm2pgsql to load OpenStreetMap data into my postgis, I got the error message:Error reading style file line 1(fields = 1). I really don't know how to deal with it. Beg your help! Thanks very much!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-default.style" rel="tag" title="see questions tagged &#39;default.style&#39;">default.style</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Oct '15, 03:46</strong></p>
<img src="https://secure.gravatar.com/avatar/b8177741baf1dfabbe85b830c5c9efce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kandifa&#39;s gravatar image" />
<p><span>kandifa</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kandifa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45844" class="comments-container">
<span id="45845"></span>
<div id="comment-45845" class="comment">
<div id="post-45845-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It would help if you could add the full line of the osm2pgsql command you're using (and on what OS).</p>
</div>
<div id="comment-45845-info" class="comment-info">
<span class="comment-age">(12 Oct '15, 08:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45844" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45844-form-container" class="comment-form-container">
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

<span id="64524"></span>

<div id="answer-container-64524" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64524-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have the same problem. I tried to load *.pbf file via osm2pgsql. I copied the command from site, but when I replaced filename, I deleted one parametr.</p>
<p>Commnd from site:</p>
<p>C:&gt;osm2pgsql -d gis -U postgres -W -H localhost -P 5432 -s -S C:\osm2pgsql\default.style RU-MOW.osm.pbf</p>
<p>My command:</p>
<p>osm2pgsql -d gis -U postgres -W -H localhost -P 5432 -s -S C:\RU-MOW.osm.pbf<br />
Instead of style-file I specify pbf, and get the error:<br />
Osm2pgsql Error reading style file line 2 (fields=1)</p>
<p>correct command:</p>
<p>C:&gt;osm2pgsql -d gis -U postgres -W -H localhost -P 5432 -s -S C:\osm2pgsql-bin\default.style C:\osm.pbf</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '18, 09:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0057104086ce3464c15c1291a4338827?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vladimir-554455&#39;s gravatar image" />
<p><span>Vladimir-554455</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vladimir-554455 has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jul '18, 09:46</strong> </span></p>
</div>
</div>
<div id="comments-container-64524" class="comments-container">
&#10;</div>
<div id="comment-tools-64524" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64524-form-container" class="comment-form-container">
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

