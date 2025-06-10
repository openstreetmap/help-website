+++
type = "question"
title = "OSM vs OSM names vs Nominatim"
description = '''Hi, i found these 4 query services   https://osmnames.org/ https://nominatim.openstreetmap.org/ https://www.openstreetmap.org/ https://www.openstreetmap.de/karte.html  My questions are:  What are the differences between them ? All of them are based on OSM planet data! How do they exactly sort their ...'''
date = "2020-01-23T13:38:00Z"
lastmod = "2020-01-23T18:57:00Z"
weight = 72640
keywords = [ "search", "nominatim", "osm" ]
aliases = [ "/questions/72640" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [OSM vs OSM names vs Nominatim](/questions/72640/osm-vs-osm-names-vs-nominatim)

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
<span id="post-72640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72640-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>i found these 4 query services</p>
<ul>
<li><a href="https://osmnames.org/">https://osmnames.org/</a></li>
<li><a href="https://nominatim.openstreetmap.org/">https://nominatim.openstreetmap.org/</a></li>
<li><a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a></li>
<li><a href="https://www.openstreetmap.de/karte.html">https://www.openstreetmap.de/karte.html</a></li>
</ul>
<p>My questions are:</p>
<ul>
<li>What are the differences between them ? All of them are based on OSM planet data!</li>
<li>How do they exactly sort their search results ?</li>
</ul>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jan '20, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/5bf224d0c0866e72c7539d5e9551c46a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Omar%20Oghli&#39;s gravatar image" />
<p><span>Omar Oghli</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Omar Oghli has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72640" class="comments-container">
&#10;</div>
<div id="comment-tools-72640" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72640-form-container" class="comment-form-container">
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

<span id="72647"></span>

<div id="answer-container-72647" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72647-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-72647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Omar Oghli has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osmnames uses a a full-text search engine. It's good at partial queries like typing in "Pari" and getting "Paris" as result. The database build needs to pre-prepare all addresses (e.g. valid street and city combinations) and often that means the database only contains one or few languages.</p>
<p>nominatim uses a structured data schema. It's better at determining the relationship between places (e.g. which street belongs to which city) and can match many/all languages. But is more strict in matching the user's query to data.</p>
<p>Both are valid approaches to search for places (<a href="https://wiki.openstreetmap.org/wiki/Search_engines),">https://wiki.openstreetmap.org/wiki/Search_engines),</a> the best engine is probably one that combines both.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jan '20, 18:57</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-72647" class="comments-container">
&#10;</div>
<div id="comment-tools-72647" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72647-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72641"></span>

<div id="answer-container-72641" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72641-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The last 2 use Nominatim behind the scenes.</p>
<p>More information about Nominatim can be found on the <a href="https://wiki.openstreetmap.org/wiki/Nominatim">wiki</a> and <a href="https://wiki.openstreetmap.org/wiki/Nominatim/FAQ">FAQ</a> (also on the wiki) and the <a href="https://github.com/openstreetmap/Nominatim">Github repository</a>. Nominatim.openstreetmap.org uses OSM Planet data and some external data sources (Tiger address data).</p>
<p>I don't know about osmnames.org</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jan '20, 15:02</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-72641" class="comments-container">
<span id="72642"></span>
<div id="comment-72642" class="comment">
<div id="post-72642-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great!</p>
<p>Do you know why the results of nominatim.openstreetmap.org and openstreetmap.org are differently sorted ?</p>
<p>You can try with the query "della vostra" to reproduce the issue.</p>
</div>
<div id="comment-72642-info" class="comment-info">
<span class="comment-age">(23 Jan '20, 15:17)</span> <span class="comment-user userinfo">Omar Oghli</span>
</div>
</div>
<span id="72646"></span>
<div id="comment-72646" class="comment">
<div id="post-72646-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>openstreetmap.org takes the current map position into consideration. For example if the map shows France it can then assume what you look for is nearby and sort those results higher. On nominatim.openstreetmap.org that is switched off by default, you can click the 'apply viewbox' to enable it.</p>
</div>
<div id="comment-72646-info" class="comment-info">
<span class="comment-age">(23 Jan '20, 18:42)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-72641" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72641-form-container" class="comment-form-container">
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

