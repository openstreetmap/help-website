+++
type = "question"
title = "Render Maps with English Street Labels"
description = '''Hi, We would like to render our own map tiles for an iOS app in an offline mode. The main motivation for rendering our own map tiles is to have street labels in both local language and English. The app is now using map tiles from Cloudmade with street labels in local language by default. I have a fe...'''
date = "2014-03-18T13:19:00Z"
lastmod = "2014-03-18T15:10:00Z"
weight = 31659
keywords = [ "tilemill", "labels", "osm", "english" ]
aliases = [ "/questions/31659" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Render Maps with English Street Labels](/questions/31659/render-maps-with-english-street-labels)

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
<span id="post-31659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31659-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>We would like to render our own map tiles for an iOS app in an offline mode. The main motivation for rendering our own map tiles is to have street labels in both local language and English. The app is now using map tiles from Cloudmade with street labels in local language by default. I have a few questions.</p>
<ol>
<li>Is it possible to render map with street labels in more than one language? In our case we want the street lable to be local language + English.</li>
<li>What tools should I use? I have heard about Mapnik and TileMill, but don't know much about them. Are they the right tools for this and are there other tools that I should also investigate?</li>
<li>For a few large cities (mostly in Asia) where few street names are in English, we would like to translate the names of major streets into English on our own before we do the map rendering. How can this be done?</li>
</ol>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-english" rel="tag" title="see questions tagged &#39;english&#39;">english</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Mar '14, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/24a65fe96f0cbd267a761e4bfabbaa25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jwt8070&#39;s gravatar image" />
<p><span>jwt8070</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jwt8070 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31659" class="comments-container">
<span id="31668"></span>
<div id="comment-31668" class="comment">
<div id="post-31668-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Forgetting about the technicalities for a second.</p>
<p>The language tags are for non-local language names that are in use for the road, something which is rather rare (for roads). Please do not add "translations" of street names to OSM, in general they will simply be nonsense.</p>
</div>
<div id="comment-31668-info" class="comment-info">
<span class="comment-age">(18 Mar '14, 15:10)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31659" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31659-form-container" class="comment-form-container">
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

<span id="31664"></span>

<div id="answer-container-31664" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31664-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-31664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Carto/Mapnik style sheets for use with OSM - whether in TileMill or a standalone rendering server as described on switch2osm.org - depend on a database from where they load their data from. In one of the style config files you'll find SQL SELECT queries for that. These can be modified to take other names into account, e.g. instead of</p>
<pre><code>SELECT name, ...</code></pre>
<p>you would write (a very simplistic approach)</p>
<pre><code>SELECT name || &#39; (&#39; || &quot;name:en&quot; || &#39;)&#39; AS name, ...</code></pre>
<p>This would then put the English name in parentheses. More complex queries - that only insert parentheses where an English name is present, or where it is present and different from the local name, or somesuch - are just a matter of more SQL.</p>
<p>For this to work, your database must of course <em>have</em> the <code>name:en</code> column, which you would request when running osm2pgsql to populate it, either by creating a proper style file or by using "hstore" (the above query would then use <code>tags-&gt;'name:en'</code> instead of just <code>name:en</code>).</p>
<p>Since SQL queries are used, you could trivially also retrieve a translation of the name from a different table by joining that into the query.</p>
<p>Of course it would be even better if you just added the appropriate <code>name:en</code> tags into OpenStreetMap!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '14, 14:43</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-31664" class="comments-container">
&#10;</div>
<div id="comment-tools-31664" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31664-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31660"></span>

<div id="answer-container-31660" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31660-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-31660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As a quick and dirty solution to the "languages" part of the problem, I'd do the same as I suggested in <a href="https://help.openstreetmap.org/questions/31351/translating-all-place-names-beginner?page=1&amp;focusedAnswerId=31354#31354">a previous answer to a different question</a> - use a lua script to combine the names any way that you want, and use the standard <a href="https://github.com/gravitystorm/openstreetmap-carto">openstreetmap-carto</a> stylesheet (modified with TileMill if you prefer) to render tiles. You can, of course use a different stylesheet, or create your own.</p>
<p>Another thought might be not to restrict yourself to tiles. I'm aware of at least one iOS renderer project (<a href="https://github.com/beelsebob/OpenStreetPad">OpenStreetPad</a>), although it's not been updated for a while.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '14, 13:35</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-31660" class="comments-container">
&#10;</div>
<div id="comment-tools-31660" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31660-form-container" class="comment-form-container">
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

