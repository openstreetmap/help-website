+++
type = "question"
title = "Download a map and extract position from places like schools, hospitals, etc."
description = '''Hi everyone, my situation is the following:  I&#x27;m starting to develop an Iphone application which deals a lot with the position of the user. The idea is that, when he is at certain positions, he receives different kinds of files, somehow related to that position.  I&#x27;ve got no problem with unique posi...'''
date = "2012-03-06T11:17:00Z"
lastmod = "2012-03-06T17:45:00Z"
weight = 11004
keywords = [ "download", "extract", "newbie", "opendata" ]
aliases = [ "/questions/11004" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Download a map and extract position from places like schools, hospitals, etc.](/questions/11004/download-a-map-and-extract-position-from-places-like-schools-hospitals-etc)

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
<span id="post-11004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11004-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone, my situation is the following:</p>
<p>I'm starting to develop an Iphone application which deals a lot with the position of the user. The idea is that, when he is at certain positions, he receives different kinds of files, somehow related to that position. I've got no problem with unique positions which are "detected" by the GPS, but it's important for me that I'm able to allow that the user receives files also when he is near from, for example, a hospital, any hospital in germany. And here is where OSM comes. I already downloaded the map from Germany (germany.osm.pbf [1.12 GB]) but I could not really open it, because I have problems using Osmosis. Right now I'm questioning myself if I even need Osmosis or there are other ways to obtain that data.</p>
<p>So, my actual question is; having the map from Germany, how can I see the information that is inside and extract the position of all the hospitals (for example) that it contains?</p>
<p>As you can see, I'm quite lost, so any kind of help would be really appreciate it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-opendata" rel="tag" title="see questions tagged &#39;opendata&#39;">opendata</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '12, 11:17</strong></p>
<img src="https://secure.gravatar.com/avatar/1a2aa68f1a6a2f5e892e320f1edcf8a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlvaroSantisteban&#39;s gravatar image" />
<p><span>AlvaroSantis...</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlvaroSantisteban has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11004" class="comments-container">
&#10;</div>
<div id="comment-tools-11004" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11004-form-container" class="comment-form-container">
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

<span id="11005"></span>

<div id="answer-container-11005" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11005-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11005-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-11005-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AlvaroSantisteban has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use one of the APIs to only get the data you need.</p>
<p>With Overpass API you can do something like this:</p>
<pre><code>&lt;query type=&quot;node&quot;&gt;
  &lt;has-kv k=&quot;amenity&quot; v=&quot;school&quot;/&gt;
  &lt;bbox-query e=&quot;7.25&quot; n=&quot;50.8&quot; s=&quot;50.7&quot; w=&quot;7.1&quot;/&gt;
&lt;/query&gt;
&lt;print/&gt;</code></pre>
<p>you can test on <a href="http://www.overpass-api.de/query_form.html">http://www.overpass-api.de/query_form.html</a></p>
<p>There is more info on Overpass on <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">https://wiki.openstreetmap.org/wiki/Overpass_API</a></p>
<p>You can also try XAPI: <a href="https://wiki.openstreetmap.org/wiki/Xapi">https://wiki.openstreetmap.org/wiki/Xapi</a></p>
<p>The Overpass server also supports XAPI and is usually very fast.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '12, 11:47</strong></p>
<img src="https://secure.gravatar.com/avatar/b9a8b8a3b1418b4b0bb41041555b18a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dymo12&#39;s gravatar image" />
<p><span>Dymo12</span><br />
<span class="score" title="796 reputation points">796</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dymo12 has 2 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '12, 17:41</strong> </span></p>
</div>
</div>
<div id="comments-container-11005" class="comments-container">
<span id="11006"></span>
<div id="comment-11006" class="comment">
<div id="post-11006-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, it looks exactly like what I needed. :) Just more thing: where can I find the meaning from each possible condition (e, into, n, etc)? I understand that in the query you wrote it's searching for all the schools inside a certain range, but I'm not sure which one. The query returns something like 29 Schools, inside two or three cities.</p>
</div>
<div id="comment-11006-info" class="comment-info">
<span class="comment-age">(06 Mar '12, 12:20)</span> <span class="comment-user userinfo">AlvaroSantis...</span>
</div>
</div>
<span id="11015"></span>
<div id="comment-11015" class="comment">
<div id="post-11015-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"into" is actually not necessary in this case, so i have removed it from the example. You can find info on the wiki and on <a href="http://www.overpass-api.de/">http://www.overpass-api.de/</a> about how to make more advanced queries and in several different ways depending on your needs.</p>
</div>
<div id="comment-11015-info" class="comment-info">
<span class="comment-age">(06 Mar '12, 17:45)</span> <span class="comment-user userinfo">Dymo12</span>
</div>
</div>
</div>
<div id="comment-tools-11005" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11005-form-container" class="comment-form-container">
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

