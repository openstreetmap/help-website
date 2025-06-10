+++
type = "question"
title = "osmfilter increases output file tenfold"
description = '''I&#x27;m using osmfilter for the first time to filter to a .osm file containing only railway=station nodes.  It increases the output file tenfold.  I downloaded great-britain-latest.osm.pbf (~1.2Gb) from Geofabrik  Converted it to .o5m using: osmconvert64-0.8.8p great-britain-latest.osm.pbf -o=great-brit...'''
date = "2020-11-09T00:53:00Z"
lastmod = "2020-11-09T20:52:00Z"
weight = 77452
keywords = [ "osmfilter" ]
aliases = [ "/questions/77452" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osmfilter increases output file tenfold](/questions/77452/osmfilter-increases-output-file-tenfold)

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
<span id="post-77452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77452-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using osmfilter for the first time to filter to a .osm file containing only railway=station nodes.</p>
<p>It increases the output file tenfold.</p>
<p>I downloaded great-britain-latest.osm.pbf (~1.2Gb) from Geofabrik Converted it to .o5m using:</p>
<pre><code>osmconvert64-0.8.8p great-britain-latest.osm.pbf -o=great-britain-latest.osm.o5m</code></pre>
<p>(~2.5Gb)</p>
<pre><code>osmfilter great-britain-latest.osm.o5m --keep-nodes=&quot;railway=station&quot; -o=osmfilter_railway_station.osm</code></pre>
<p>(~23 Gb!) Taking ~5mins to complete. It's too large to open.</p>
<p>I'm expecting a file of about 1.8Mb as from Overpass.</p>
<p>I've read the help documentation, can't see anything obvious. What am i doing wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Nov '20, 00:53</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Nov '20, 01:02</strong> </span></p>
</div>
</div>
<div id="comments-container-77452" class="comments-container">
<span id="77482"></span>
<div id="comment-77482" class="comment">
<div id="post-77482-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>May be the issue is here: <a href="https://wiki.openstreetmap.org/wiki/Osmfilter#Keep_specific_Object_Type">https://wiki.openstreetmap.org/wiki/Osmfilter#Keep_specific_Object_Type</a> (looks like you need additional filters, either a --keep= before or --keep-ways= <em>and --keep-relations=</em> after).</p>
</div>
<div id="comment-77482-info" class="comment-info">
<span class="comment-age">(09 Nov '20, 20:52)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-77452" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77452-form-container" class="comment-form-container">
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

<span id="77456"></span>

<div id="answer-container-77456" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77456-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looks like osmfilter put all the data into the output file, not only the railway nodes. A 10x factor compared to the .pbf file is about what's expected in that case.</p>
<p>I am using <a href="https://osmcode.org/osmium-tool">osmium</a> for these kinds of things (I am the author, so that's no wonder...). You don't need the intermediate o5m file and the whole thing is faster:</p>
<pre><code>osmium tags-filter great-britain-latest.osm.pbf n/railway=station -o railway_stations.osm</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Nov '20, 08:11</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-77456" class="comments-container">
<span id="77472"></span>
<div id="comment-77472" class="comment">
<div id="post-77472-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, but unfortunately it doesn't run on Windows, unless I've missed some documentation(?).</p>
<hr />
<p>I've also tried Osmosis, (osmosis --rbf great-britain-latest.osm.pbf --nkv keyValueList="railway.station" --wx railway_station.osm ) which worked, but took 4 times as long (65 secs) to complete as using Overpass. It surprises me that a remote server was much quicker than a local drive. Given the info I provided above, is this the expected time for such a routine?</p>
</div>
<div id="comment-77472-info" class="comment-info">
<span class="comment-age">(09 Nov '20, 12:25)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="77478"></span>
<div id="comment-77478" class="comment">
<div id="post-77478-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Osmium runs on Windows. But there are no prepacked binaries. So you have to compile it yourself.</p>
<p>The 65 secs for Osmosis sounds abound right. Osmosis has to read all the data and throw most of it away, that takes a lot of time. Overpass doesn't have to do this, because it has a specialized database behind it with indexes. (Osmium still has to do the same work as Osmosis, but will be noticably faster.)</p>
</div>
<div id="comment-77478-info" class="comment-info">
<span class="comment-age">(09 Nov '20, 13:30)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="77480"></span>
<div id="comment-77480" class="comment">
<div id="post-77480-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are there any instructions on how/what to compile or know if anyone has completed the task?</p>
</div>
<div id="comment-77480-info" class="comment-info">
<span class="comment-age">(09 Nov '20, 15:56)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-77456" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77456-form-container" class="comment-form-container">
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

