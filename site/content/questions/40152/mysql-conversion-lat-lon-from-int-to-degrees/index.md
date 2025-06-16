+++
type = "question"
title = "MySQL - conversion lat lon from int to degrees"
description = '''Hello, In the MySQL database I have the following data: node id lat lon 2094180296 349660688 336654980 667088997 349663935 336658237 667089013 349667613 336661316 701333196 349670314 336663369 2094180312 349672919 336665248  How to convert latitude and longitude from integers to degrees (float / dou...'''
date = "2015-01-08T17:13:00Z"
lastmod = "2015-01-08T17:41:00Z"
weight = 40152
keywords = [ "mysql" ]
aliases = [ "/questions/40152" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [MySQL - conversion lat lon from int to degrees](/questions/40152/mysql-conversion-lat-lon-from-int-to-degrees)

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
<span id="post-40152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40152-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>In the MySQL database I have the following data:</p>
<pre><code>node id     lat             lon
2094180296  349660688   336654980
667088997   349663935   336658237
667089013   349667613   336661316
701333196   349670314   336663369
2094180312  349672919   336665248</code></pre>
<p>How to convert latitude and longitude from integers to degrees (float / double)?</p>
<p>How does this algorithm?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jan '15, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/874f428b539f501361c6a9947fe859f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rysiu&#39;s gravatar image" />
<p><span>Rysiu</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rysiu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40152" class="comments-container">
<span id="40153"></span>
<div id="comment-40153" class="comment">
<div id="post-40153-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A better forum for a question such as this that isn't OpenStreetMap related might be <a href="http://stackoverflow.com/">http://stackoverflow.com/</a> or <a href="http://gis.stackexchange.com/">http://gis.stackexchange.com/</a> (although actually I'm sure a quick web search will find the answer without even having to ask again).</p>
</div>
<div id="comment-40153-info" class="comment-info">
<span class="comment-age">(08 Jan '15, 17:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="40156"></span>
<div id="comment-40156" class="comment">
<div id="post-40156-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If the bit that you're missing is "what do these numbers mean in OpenStreetMap" than have a read of these two wiki sections:</p>
<p><a href="http://wiki.osm.org/wiki/Beginners%27_guide">http://wiki.osm.org/wiki/Beginners%27_guide</a></p>
<p><a href="http://wiki.osm.org/wiki/Elements">http://wiki.osm.org/wiki/Elements</a></p>
</div>
<div id="comment-40156-info" class="comment-info">
<span class="comment-age">(08 Jan '15, 17:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40152" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40152-form-container" class="comment-form-container">
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

<span id="40155"></span>

<div id="answer-container-40155" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40155-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rysiu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looking at your <a href="https://www.openstreetmap.org/node/2094180296">first example</a> which is at 34.9660688, 33.665498 it suggests you divide by 10,000,000</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '15, 17:38</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-40155" class="comments-container">
&#10;</div>
<div id="comment-tools-40155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40155-form-container" class="comment-form-container">
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

