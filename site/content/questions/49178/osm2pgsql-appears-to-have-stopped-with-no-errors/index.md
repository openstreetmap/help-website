+++
type = "question"
title = "osm2pgsql appears to have stopped with no errors"
description = '''Hi there, I am trying to import an osm planet file in .pbf format into PostGIS and it appears to have just stopped after about 5 days of running. I&#x27;ve read through quite a few of the posts in this forum and not found an answer that seems to explain what has happened. As far as I understand it I shou...'''
date = "2016-04-11T12:54:00Z"
lastmod = "2016-04-27T14:29:00Z"
weight = 49178
keywords = [ "windows", "osm2pgsql", "postgis" ]
aliases = [ "/questions/49178" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql appears to have stopped with no errors](/questions/49178/osm2pgsql-appears-to-have-stopped-with-no-errors)

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
<span id="post-49178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49178-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>I am trying to import an osm planet file in .pbf format into PostGIS and it appears to have just stopped after about 5 days of running. I've read through quite a few of the posts in this forum and not found an answer that seems to explain what has happened. As far as I understand it I should get some information about how long it has taken once it has finished but the last thing it shows me is:</p>
<p>'Processing: Node&lt;1929394k 225.9k/s&gt; Way&lt;186904k 1.37k/s&gt; Relation&lt;477740 9.65/s&gt;'</p>
<p>I've checked the event logs and I can't see anything that says I've run out of memory or space and when I look in PostgreSQL there is only one table called spatial_ref_sys. I also read somewhere that PostgreSQL has to run indexing and what not, so I'm not sure if that is what is happening at the moment.</p>
<p>My server set up is thus:</p>
<ul>
<li>Windows Server 2008 R2 - 64bit</li>
<li>2.00Ghz Dual Core</li>
<li>24 GB RAM</li>
<li>350GB HDD</li>
</ul>
<p>The command I used to set osm2pgsql running was:</p>
<p>osm2pgsql -S "C:/Program Files/cygwin-package/default.style" -U postgres -d maps C:/Users/jordane/Desktop/Maps/planet-130614.osm.pbf -W --port 5432 --host localhost -s --flat-nodes flat-nodes.bin</p>
<p>Can anyone tell me what happened and how to fix it or is it still running in the background?</p>
<p>UPDATE: So, I figured I may as well run it again and see what happens, in case a process had stopped last time and so killed it. I got exactly the same issue happen again and it stopped at exactly the same point. I was keeping an eye on how much space I had available as it was running and it didn't come anywhere close to filling my disk. It finished overnight so I can't say how much space it was taking up when it stopped but I got no warnings to say it ran out of space. I have however noticed that the used space on my disk has gone down by about 40-50GB since it stopped running, so I can only assume that it has hit a problem and cleaned up the partially converted data.</p>
<p>Am I missing something obvious here? Is there a load of data that it has dumped somewhere other than PostgreSQL? I would really appreciate some pointers as I am all out of ideas bar downloading a new planet file and just trying it again.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '16, 12:54</strong></p>
<img src="https://secure.gravatar.com/avatar/b75302f1065a5eca0c63dcb6f3b51ea7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Elea%20J&#39;s gravatar image" />
<p><span>Elea J</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Elea J has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '16, 09:38</strong> </span></p>
</div>
</div>
<div id="comments-container-49178" class="comments-container">
&#10;</div>
<div id="comment-tools-49178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49178-form-container" class="comment-form-container">
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

<span id="49462"></span>

<div id="answer-container-49462" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49462-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49462-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49462-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think that it's fair to say that there are far fewer people using osm2pgsql on Windows than on e.g. Linux - that's probably why you didn't get any answers here.</p>
<p>There has been some Windows activity at <a href="https://github.com/openstreetmap/osm2pgsql/issues?utf8=%E2%9C%93&amp;q=is%3Aissue+is%3Aopen+windows">https://github.com/openstreetmap/osm2pgsql/issues?utf8=%E2%9C%93&amp;q=is%3Aissue+is%3Aopen+windows</a> (your question there is at the top of the list).</p>
<p>My first thought is "are you running out of memory?". Have you tried a much smaller data extract (a city or very small country)?</p>
<p>My second is "what do you want to do with the data afterwards"? Your question at <a href="https://help.openstreetmap.org/questions/49457/ways-of-loading-a-planet-file-into-a-gui-and-exporting-tiles-from-it">https://help.openstreetmap.org/questions/49457/ways-of-loading-a-planet-file-into-a-gui-and-exporting-tiles-from-it</a> suggests that you want to generate tiles. I'm unaware of a well-documented software stack that will do this on Windows.</p>
<p>My suggestions are:</p>
<ol>
<li>Use Ubuntu Linux 14.04 LTS as the base OS, and follow <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a></li>
<li>Initially use a very small data extract, not a full planet.</li>
<li>When you're happy that you can generate tiles successfully, consider changing to larger data extracts or to a different platform, but bear in mind that for Windows you may need to write something that doesn't exist currently (even if it's only documentation).</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '16, 14:14</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-49462" class="comments-container">
<span id="49464"></span>
<div id="comment-49464" class="comment">
<div id="post-49464-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks I'll try those. Could I really be running out memory with 24GB of RAM? I kept an eye on it (during the days) and I only ever used about 10-15% of the available RAM.</p>
</div>
<div id="comment-49464-info" class="comment-info">
<span class="comment-age">(27 Apr '16, 14:21)</span> <span class="comment-user userinfo">Elea J</span>
</div>
</div>
<span id="49467"></span>
<div id="comment-49467" class="comment">
<div id="post-49467-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Depending on where you got osm2pgsql from, I wouldn't assume that it could address all 24Gb of RAM on Windows.</p>
</div>
<div id="comment-49467-info" class="comment-info">
<span class="comment-age">(27 Apr '16, 14:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-49462" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49462-form-container" class="comment-form-container">
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

