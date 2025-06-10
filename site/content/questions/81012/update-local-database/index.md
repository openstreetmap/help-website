+++
type = "question"
title = "Update local Database?"
description = '''I have an overpass server setup locally, which is working, but there&#x27;s still one more issue I have with it. Some results are different from my server to the public one, and I want to know what the best way of fixing that is? Should I just scrap the whole database and re-download it, following this? ...'''
date = "2021-07-16T19:07:00Z"
lastmod = "2021-07-16T19:07:00Z"
weight = 81012
keywords = [ "overpass", "update", "database" ]
aliases = [ "/questions/81012" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Update local Database?](/questions/81012/update-local-database)

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
<span id="post-81012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81012-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have an overpass server setup locally, which is working, but there's still one more issue I have with it. Some results are different from my server to the public one, and I want to know what the best way of fixing that is? Should I just scrap the whole database and re-download it, following <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Installation#Populating_the_DB">this</a>?</p>
<p>I posted about this previously, and from that I setup daily diffs on my database which solved some of the issues that I had. This was a few days ago, but clearly has not solved all of my problems.</p>
<p>Here's an example query that is producing different results for me:</p>
<pre><code>nwr[&quot;name:en&quot;=&quot;Warsaw Chopin Airport&quot;];
out geom;</code></pre>
My result (only the first three lines are shown here, and preceding "&lt;" omitted in xml output):
<pre><code>way id=&quot;237594029&quot;&gt;
bounds minlat=&quot;52.1419630&quot; minlon=&quot;20.9393671&quot; maxlat=&quot;52.1842563&quot; maxlon=&quot;20.9878821&quot;/&gt;
nd ref=&quot;8857075938&quot;/&gt;</code></pre>
Public server's result:
<pre><code>way id=&quot;237594029&quot;&gt;
bounds minlat=&quot;52.1419630&quot; minlon=&quot;20.9393671&quot; maxlat=&quot;52.1842522&quot; maxlon=&quot;20.9878821&quot;/&gt;
nd ref=&quot;8857075938&quot; lat=&quot;52.1731347&quot; lon=&quot;20.9770425&quot;/&gt;</code></pre>
<p>The difference here is that the node (and many other nodes in this way) do not have a lat / lon in my results. I'm pretty sure this is also the cause of the center of this way being calculated <em>very</em> wrong.</p>
<p>My center:</p>
<pre><code>way id=&quot;237594029&quot;&gt;
center lat=&quot;-19.4078719&quot; lon=&quot;-96.8802413&quot;/&gt;</code></pre>
<p>Public server's center:</p>
<pre><code>way id=&quot;237594029&quot;&gt;
center lat=&quot;52.1631076&quot; lon=&quot;20.9636246&quot;/&gt;</code></pre>
<p>Any ideas on the best way to update/change/fixing my local database would be very appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '21, 19:07</strong></p>
<img src="https://secure.gravatar.com/avatar/90c1a2a6f8b3789f0622ae27f3d92bd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nbreden&#39;s gravatar image" />
<p><span>nbreden</span><br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nbreden has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81012" class="comments-container">
&#10;</div>
<div id="comment-tools-81012" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81012-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

