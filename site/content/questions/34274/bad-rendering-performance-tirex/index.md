+++
type = "question"
title = "Bad Rendering Performance (Tirex)"
description = '''We have set up a rendering server with a Intel(R) Xeon(R) CPU E5-1620 v2 @ 3.70GHz, 32 GB RAM and SSD discs for the database storage. Import was done using osm2pgsql -C14G --number-processes 8 -v --slim planet-latest.osm.pbf and postgresql 9.3 and the settings as suggested by Frederik Ramm. But the ...'''
date = "2014-06-24T13:22:00Z"
lastmod = "2014-07-05T13:14:00Z"
weight = 34274
keywords = [ "performance", "tirex", "mapnik" ]
aliases = [ "/questions/34274" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Bad Rendering Performance (Tirex)](/questions/34274/bad-rendering-performance-tirex)

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
<span id="post-34274-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34274-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34274-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We have set up a rendering server with a Intel(R) Xeon(R) CPU E5-1620 v2 @ 3.70GHz, 32 GB RAM and SSD discs for the database storage.</p>
<p>Import was done using <code>osm2pgsql -C14G --number-processes 8 -v --slim planet-latest.osm.pbf</code> and postgresql 9.3 and the settings as <a href="http://www.geofabrik.de/media/2012-09-08-osm2pgsql-performance.pdf">suggested by Frederik Ramm</a>.</p>
<p>But the performance on low zoom levels is worse than what Frederik gets in his talk. Maybe because of additional map data in the past 2 years?</p>
<p>Some extreme examples:</p>
<pre><code>Map                           X          Y   Z Prio   Age
example                      32         16   6    1   486
&#10;Currently rendering: (num=4)
Map                           X          Y   Z Prio   Age
example                     136         80   8    1   295
example                     128         80   8    1   295
example                     264        168   9    1   285
example                     528        352  10    1   260</code></pre>
<p>I am using the standard osm.xml (mapnik-osm-carto).</p>
<p><code>generate_image.py</code> with the standard bounding box (GB) takes 6m10.450s.</p>
<p>Is this normal?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-tirex" rel="tag" title="see questions tagged &#39;tirex&#39;">tirex</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jun '14, 13:22</strong></p>
<img src="https://secure.gravatar.com/avatar/7651f7a3094f0a39b51630214fe9c94d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alex_AddisMap&#39;s gravatar image" />
<p><span>Alex_AddisMap</span><br />
<span class="score" title="189 reputation points">189</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alex_AddisMap has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jun '14, 13:31</strong> </span></p>
</div>
</div>
<div id="comments-container-34274" class="comments-container">
&#10;</div>
<div id="comment-tools-34274" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34274-form-container" class="comment-form-container">
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

<span id="34307"></span>

<div id="answer-container-34307" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34307-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Alex_AddisMap has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You've already partially answered your own question: two years ago we had roughly half the data we currently have in the database see for example <a href="http://osmstats.altogetherlost.com/index.php?item=nodes">http://osmstats.altogetherlost.com/index.php?item=nodes</a> (I'm actually surprised that you are not still importing given that the cache value you used is far too small for a current planet).</p>
<p>However the queries for low zoom tile data tend to already substantially reduce the ammout of data, so that is likely not to be a major factor. Frederiks numbers seem to be very good, I've not actually ever seen low zoom tiles render as fast as his numbers show. IIRC for the standard style we pre-render down to zoom level 14 to work around that.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '14, 09:24</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '14, 09:35</strong> </span></p>
</div>
</div>
<div id="comments-container-34307" class="comments-container">
<span id="34652"></span>
<div id="comment-34652" class="comment">
<div id="post-34652-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Even on zoom level 15 I have the problem that tiles take too long.</p>
</div>
<div id="comment-34652-info" class="comment-info">
<span class="comment-age">(05 Jul '14, 13:14)</span> <span class="comment-user userinfo">Alex_AddisMap</span>
</div>
</div>
</div>
<div id="comment-tools-34307" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34307-form-container" class="comment-form-container">
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

