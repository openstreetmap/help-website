+++
type = "question"
title = "Filter out data that have been edited after some timestamp"
description = '''I want to get data after some timestamp. I have downloaded the osm file of the area. I went through the osmosis documentation but could not find a way to filter it by time. The result should be same as when we use the timestamp:sometime in JOSM.   I could use JOSM but copy pasting in new layer remov...'''
date = "2013-11-15T04:54:00Z"
lastmod = "2015-08-10T00:46:00Z"
weight = 28117
keywords = [ "filter", "timestamps", "osmosis" ]
aliases = [ "/questions/28117" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Filter out data that have been edited after some timestamp](/questions/28117/filter-out-data-that-have-been-edited-after-some-timestamp)

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
<span id="post-28117-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28117-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-28117-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to get data after some <code>timestamp</code>. I have downloaded the osm file of the area. I went through the osmosis documentation but could not find a way to filter it by time.</p>
<p>The result should be same as when we use the <code>timestamp:sometime</code> in JOSM.</p>
<ol>
<li>I could use JOSM but copy pasting in new layer removes old id ad gives new id, also</li>
<li>i could use the overpass but the area is large and overpass timed out many times</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '13, 04:54</strong></p>
<img src="https://secure.gravatar.com/avatar/651103e616e49724bb139f1a3e0a1a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amritkarma&#39;s gravatar image" />
<p><span>amritkarma</span><br />
<span class="score" title="684 reputation points">684</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amritkarma has one accepted answer">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Nov '13, 04:41</strong> </span></p>
</div>
</div>
<div id="comments-container-28117" class="comments-container">
&#10;</div>
<div id="comment-tools-28117" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28117-form-container" class="comment-form-container">
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

<span id="28185"></span>

<div id="answer-container-28185" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28185-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In JOSM, instead of selecting new objects with "timestamp:sometime" and copy them to a new layer loosing their Id's, you could try the opposite: select old objects with "-timestamp:sometime" (the "-" is the reverse option) and delete all of them. Thus, only the most recent elements are staying and you preserve the Id's. But I'm not able to test this method right now, I'm not sure if it works.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '13, 14:47</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-28185" class="comments-container">
<span id="28188"></span>
<div id="comment-28188" class="comment">
<div id="post-28188-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>They would not be deleted immidiately. They would be marked for deletion and don't show up in josm but they will still exist in the osm file.</p>
</div>
<div id="comment-28188-info" class="comment-info">
<span class="comment-age">(18 Nov '13, 15:04)</span> <span class="comment-user userinfo">amritkarma</span>
</div>
</div>
<span id="28193"></span>
<div id="comment-28193" class="comment">
<div id="post-28193-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is this a problem? You could just ignore any element with <code>action='delete'</code> when parsing the XML file.</p>
</div>
<div id="comment-28193-info" class="comment-info">
<span class="comment-age">(18 Nov '13, 16:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="28221"></span>
<div id="comment-28221" class="comment">
<div id="post-28221-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>JOSM can also discard data altogehter ("purge") instead of flagging it as deleted.</p>
</div>
<div id="comment-28221-info" class="comment-info">
<span class="comment-age">(19 Nov '13, 13:33)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28185-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44681"></span>

<div id="answer-container-44681" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44681-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For anyone looking to do this on a larger dataset, my approach would be to load the data into PostgreSQL</p>
<pre><code>osmosis --rbf large.osm.pbf --wp database=osm</code></pre>
<p>Then drop everything that was last touched before / after your desired horizon:</p>
<pre><code>DELETE FROM nodes WHERE tstamp &lt; date &#39;2015-07-01;
DELETE FROM ways WHERE tstamp &lt; date &#39;2015-07-01;
DELETE FROM relations WHERE tstamp &lt; date &#39;2015-07-01;</code></pre>
<p>Then dump the data to PBF again:</p>
<pre><code>osmosis --rp database=osm --dd --wb after-20150701.osm.pbf</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '15, 00:46</strong></p>
<img src="https://secure.gravatar.com/avatar/acea3c9fd5908d7ff09596d16b8724d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mvexel&#39;s gravatar image" />
<p><span>mvexel</span><br />
<span class="score" title="762 reputation points">762</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mvexel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44681" class="comments-container">
&#10;</div>
<div id="comment-tools-44681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44681-form-container" class="comment-form-container">
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

