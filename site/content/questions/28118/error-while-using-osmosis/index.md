+++
type = "question"
title = "Error while using osmosis"
description = '''I was trying to filter openstreet map data using osmosis. I used the following osmosis --read-xml city.osm --tf accept-ways highway=* --used-node --write-xml highways.osm But while i run this command in osmosis with osm file &quot;city.osm&quot; it throws run time exception SEVERE: Thread for task 1-read-xml ...'''
date = "2013-11-15T06:13:00Z"
lastmod = "2013-11-17T04:07:00Z"
weight = 28118
keywords = [ "osmosis" ]
aliases = [ "/questions/28118" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Error while using osmosis](/questions/28118/error-while-using-osmosis)

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
<span id="post-28118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28118-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-28118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was trying to filter openstreet map data using osmosis. I used the following</p>
<p><code>osmosis --read-xml city.osm --tf accept-ways highway=* --used-node --write-xml highways.osm</code></p>
<p>But while i run this command in osmosis with osm file "city.osm" it throws run time exception</p>
<p><code>SEVERE: Thread for task 1-read-xml failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: Cannot represent 2169105896 as an integer. at org.openstreetmap.osmosis.core.util.LongAsInt.longToInt(LongAsInt.java:33)</code></p>
<p>What could be the problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '13, 06:13</strong></p>
<img src="https://secure.gravatar.com/avatar/331eecd6ec3fc7984bb8797bb17de4bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Poshan&#39;s gravatar image" />
<p><span>Poshan</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Poshan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28118" class="comments-container">
<span id="28126"></span>
<div id="comment-28126" class="comment">
<div id="post-28126-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Where did "city.osm" come from? Knowing that may help people understand the missing data (mentioned in the comment).</p>
</div>
<div id="comment-28126-info" class="comment-info">
<span class="comment-age">(15 Nov '13, 10:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="28162"></span>
<div id="comment-28162" class="comment">
<div id="post-28162-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it seems i had error with my osm file city.osm. Everything worked fine after i downloaded and used another file from metroextract metro.teczno.com. Thanks.</p>
</div>
<div id="comment-28162-info" class="comment-info">
<span class="comment-age">(17 Nov '13, 04:07)</span> <span class="comment-user userinfo">Poshan</span>
</div>
</div>
</div>
<div id="comment-tools-28118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28118-form-container" class="comment-form-container">
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

<span id="28120"></span>

<div id="answer-container-28120" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28120-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-28120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Poshan has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Which version of osmosis are you using? Update your osmosis and see if it works. The node id of OSM has exceeded the 2^32 - 1 so you might be using order version of osmosis which might be giving you this error.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '13, 08:03</strong></p>
<img src="https://secure.gravatar.com/avatar/a812981e0d01bb368aeb92536183d9e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nirab%20Pudasaini&#39;s gravatar image" />
<p><span>Nirab Pudasaini</span><br />
<span class="score" title="556 reputation points">556</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nirab Pudasaini has 2 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Nov '13, 08:15</strong> </span></p>
</div>
</div>
<div id="comments-container-28120" class="comments-container">
<span id="28121"></span>
<div id="comment-28121" class="comment">
<div id="post-28121-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>i have updated osmosis to 0.43.1 version but new kind of error shows <code>SEVERE: Thread for task 1-read-xml failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: The entity timestamp att ribute is missing. at org.openstreetmap.osmosis.core.domain.common.UnparsedTimestampContain er.&lt;init&gt;(UnparsedTimestampContainer.java:34)</code></p>
</div>
<div id="comment-28121-info" class="comment-info">
<span class="comment-age">(15 Nov '13, 08:13)</span> <span class="comment-user userinfo">Poshan</span>
</div>
</div>
</div>
<div id="comment-tools-28120" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28120-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28119"></span>

<div id="answer-container-28119" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28119-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It could be because you have an old version of osmosis that don't <a href="https://wiki.openstreetmap.org/wiki/64-bit_Identifiers">support 64 bit id's</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '13, 06:37</strong></p>
<img src="https://secure.gravatar.com/avatar/b9a8b8a3b1418b4b0bb41041555b18a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dymo12&#39;s gravatar image" />
<p><span>Dymo12</span><br />
<span class="score" title="796 reputation points">796</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dymo12 has 2 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-28119" class="comments-container">
&#10;</div>
<div id="comment-tools-28119" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28119-form-container" class="comment-form-container">
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

