+++
type = "question"
title = "Best practices for querying natural geographical features"
description = '''Hi all! I&#x27;m developing a mobile app that will need the natural geographical data (mountains, lakes, rivers, and so on) present in OSM, just the POIs (coords and features), not the tiles. If I&#x27;m not mistaken, I must deploy my own database, to avoid excessive access to OSM systems. Right? Can I (and i...'''
date = "2013-10-10T10:32:00Z"
lastmod = "2013-10-10T16:33:00Z"
weight = 27069
keywords = [ "query", "natural", "lakes", "mountains", "database" ]
aliases = [ "/questions/27069" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Best practices for querying natural geographical features](/questions/27069/best-practices-for-querying-natural-geographical-features)

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
<span id="post-27069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27069-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all! I'm developing a mobile app that will need the natural geographical data (mountains, lakes, rivers, and so on) present in OSM, just the POIs (coords and features), not the tiles.</p>
<p>If I'm not mistaken, I must deploy my own database, to avoid excessive access to OSM systems. Right?</p>
<p>Can I (and if so, how?) download just the data i need from OSM, avoiding roads, cities, and tiles?</p>
<p>Thanks a lot!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-natural" rel="tag" title="see questions tagged &#39;natural&#39;">natural</span> <span class="post-tag tag-link-lakes" rel="tag" title="see questions tagged &#39;lakes&#39;">lakes</span> <span class="post-tag tag-link-mountains" rel="tag" title="see questions tagged &#39;mountains&#39;">mountains</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Oct '13, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/881f8582154691efa29c7fbe91c7279d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ubik15&#39;s gravatar image" />
<p><span>ubik15</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ubik15 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27069" class="comments-container">
<span id="27070"></span>
<div id="comment-27070" class="comment">
<div id="post-27070-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A couple of questions - do you want it to be worldwide or regional, and do you need it to be able to work offline or would online access be OK?</p>
</div>
<div id="comment-27070-info" class="comment-info">
<span class="comment-age">(10 Oct '13, 10:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-27069" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27069-form-container" class="comment-form-container">
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

<span id="27074"></span>

<div id="answer-container-27074" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27074-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-27074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ubik15 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You don't necessarily need to deploy your own database. You can use the <a href="http://wiki.osm.org/wiki/Overpass_API">Overpass API</a> for that purpose. As <a href="http://overpass-turbo.eu/s/1e5">an example in Overpass Turbo</a>,</p>
<pre><code>node(46,8,47,9)[natural=peak];out;</code></pre>
<p>gives you all peaks within a quite large area. If you want to deploy yourown database, you can get a data extract in the same way from the Overpass API.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '13, 11:57</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-27074" class="comments-container">
<span id="27081"></span>
<div id="comment-27081" class="comment">
<div id="post-27081-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the answer!</p>
<p>So, it's impossible to download just the geo features with, eg, Planet OSM?</p>
</div>
<div id="comment-27081-info" class="comment-info">
<span class="comment-age">(10 Oct '13, 13:50)</span> <span class="comment-user userinfo">ubik15</span>
</div>
</div>
<span id="27082"></span>
<div id="comment-27082" class="comment">
<div id="post-27082-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Using overpass-api is already a filtered download.</p>
<p>Alternatively, download the whole complete raw OSM data for a specific region from any source listed at <a href="https://wiki.openstreetmap.org/wiki/Planet.osm">https://wiki.openstreetmap.org/wiki/Planet.osm</a> ... and do a filtering via <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">https://wiki.openstreetmap.org/wiki/Osmfilter</a></p>
</div>
<div id="comment-27082-info" class="comment-info">
<span class="comment-age">(10 Oct '13, 16:28)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="27083"></span>
<div id="comment-27083" class="comment">
<div id="post-27083-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, many thanks.</p>
</div>
<div id="comment-27083-info" class="comment-info">
<span class="comment-age">(10 Oct '13, 16:33)</span> <span class="comment-user userinfo">ubik15</span>
</div>
</div>
</div>
<div id="comment-tools-27074" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27074-form-container" class="comment-form-container">
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

