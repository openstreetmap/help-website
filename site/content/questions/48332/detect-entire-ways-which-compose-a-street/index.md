+++
type = "question"
title = "Detect entire &#x27;ways&#x27; which compose a street"
description = '''Hi!! I am a student of Engineering and I&#x27;m using OSM data for my final university project. My problem is this: Let us place ourselves in Madrid, Serrano street is defined by various &#x27;ways&#x27; and I wonder if anyone knows any way to detect ALL Serrano street at once, without having to resort to differen...'''
date = "2016-02-24T15:51:00Z"
lastmod = "2016-02-29T14:36:00Z"
weight = 48332
keywords = [ "ways", "project", "street" ]
aliases = [ "/questions/48332" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Detect entire 'ways' which compose a street](/questions/48332/detect-entire-ways-which-compose-a-street)

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
<span id="post-48332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48332-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!! I am a student of Engineering and I'm using OSM data for my final university project.</p>
<p>My problem is this: Let us place ourselves in Madrid, Serrano street is defined by various 'ways' and I wonder if anyone knows any way to detect ALL Serrano street at once, without having to resort to different 'ways' that compose this street.</p>
<p>Currently, I have downloaded the data from Madrid in SQL .</p>
<p>THANKS!!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-project" rel="tag" title="see questions tagged &#39;project&#39;">project</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '16, 15:51</strong></p>
<img src="https://secure.gravatar.com/avatar/c989cd61fa91d018771a24c482310df3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eleena18&#39;s gravatar image" />
<p><span>eleena18</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eleena18 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '16, 20:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-48332" class="comments-container">
<span id="48340"></span>
<div id="comment-48340" class="comment">
<div id="post-48340-score" class="comment-score">
3
</div>
<div class="comment-text">
<p><a href="/questions/48331/detectar-ways-completos-para-trabajo-fin-de-carrera">This question in Spanish</a>.</p>
</div>
<div id="comment-48340-info" class="comment-info">
<span class="comment-age">(24 Feb '16, 20:16)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48332-form-container" class="comment-form-container">
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

<span id="48337"></span>

<div id="answer-container-48337" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48337-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-48337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to get a combined geometry out of your SQL database, you could do something like this. Instead of</p>
<pre><code>SELECT name, highway, way FROM planet_osm_line</code></pre>
<p>write</p>
<pre><code>SELECT name, highway, ST_UNION(way) AS way FROM planet_osm_line GROUP BY name, highway</code></pre>
<p>This will combine all objects that have the same name and highway type into single lines (where possible).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '16, 19:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-48337" class="comments-container">
<span id="48347"></span>
<div id="comment-48347" class="comment">
<div id="post-48347-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Aha, good point. Note that some streets change type, so this heuristic still won't be 100%. See this - the street "Kochanova" starts from south as <code>residential</code>, continues north as <code>steps</code>, and then again as <code>residential</code>: <a href="http://www.openstreetmap.org/way/32024324">http://www.openstreetmap.org/way/32024324</a> (just an example I found by casually glancing at the map; probably a more common occurence would be <code>residential</code>-<code>tertiary</code>-<code>secondary</code>)</p>
</div>
<div id="comment-48347-info" class="comment-info">
<span class="comment-age">(25 Feb '16, 09:46)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
<span id="48351"></span>
<div id="comment-48351" class="comment">
<div id="post-48351-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Also beware of streets with the same name but in different parts of a city. Using st_intersects and a rather more complicated query gets round this issue. You will also probably need to cast your st_union() with st_multi() so that everything becomes a multilinestring.</p>
</div>
<div id="comment-48351-info" class="comment-info">
<span class="comment-age">(25 Feb '16, 11:15)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="48361"></span>
<div id="comment-48361" class="comment">
<div id="post-48361-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't have ways defined as geometric...</p>
<p>I have a table with the characteristics of the way, another one with the nodes that compose it and another with its tags..</p>
</div>
<div id="comment-48361-info" class="comment-info">
<span class="comment-age">(25 Feb '16, 16:13)</span> <span class="comment-user userinfo">eleena18</span>
</div>
</div>
<span id="48388"></span>
<div id="comment-48388" class="comment">
<div id="post-48388-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>well that doesn't technically matter: in this case you are searching for connected graphs which share the same name attribute. You may find something I wrote about building such a graph from open data for streetlights describes a solution to a similar problem: <a href="http://sk53-osm.blogspot.co.uk/2013/04/maps-for-dogs-or-lamp-posts-in-chains.html.">http://sk53-osm.blogspot.co.uk/2013/04/maps-for-dogs-or-lamp-posts-in-chains.html.</a> So use your way_nodes table to find 1) all interconnected ways, and 2) build graphs from this.</p>
</div>
<div id="comment-48388-info" class="comment-info">
<span class="comment-age">(27 Feb '16, 19:09)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="48416"></span>
<div id="comment-48416" class="comment">
<div id="post-48416-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>THANK YOU!! :)</p>
</div>
<div id="comment-48416-info" class="comment-info">
<span class="comment-age">(29 Feb '16, 14:36)</span> <span class="comment-user userinfo">eleena18</span>
</div>
</div>
</div>
<div id="comment-tools-48337" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48337-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48333"></span>

<div id="answer-container-48333" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48333-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No. You could theoretically map a street as a relation consisting of the various ways, but this is rare. Most streets are indeed mapped as multiple segments with the same <code>name</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '16, 16:03</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-48333" class="comments-container">
&#10;</div>
<div id="comment-tools-48333" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48333-form-container" class="comment-form-container">
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

