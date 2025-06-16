+++
type = "question"
title = "How configure OSM in Oracle MapViewer 11g ?"
description = '''I can&#x27;t find information about configure OSM (openstreetmap.org) in Oracle MapViewer 11g ? Please some help me. Thank you.'''
date = "2014-03-11T07:18:00Z"
lastmod = "2014-03-11T10:07:00Z"
weight = 31436
keywords = [ "oracle" ]
aliases = [ "/questions/31436" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How configure OSM in Oracle MapViewer 11g ?](/questions/31436/how-configure-osm-in-oracle-mapviewer-11g)

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
<span id="post-31436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31436-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I can't find information about configure OSM (openstreetmap.org) in Oracle MapViewer 11g ?</p>
<p>Please some help me.</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-oracle" rel="tag" title="see questions tagged &#39;oracle&#39;">oracle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Mar '14, 07:18</strong></p>
<img src="https://secure.gravatar.com/avatar/5d765ad65d8a6de502908345944b6e73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gelek&#39;s gravatar image" />
<p><span>gelek</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gelek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31436" class="comments-container">
<span id="31442"></span>
<div id="comment-31442" class="comment">
<div id="post-31442-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Could you clarify whether you mean MapViewer (J2EE-based map rendering middleware) or Oracle Maps (JavaScript map viewer client)?</p>
</div>
<div id="comment-31442-info" class="comment-info">
<span class="comment-age">(11 Mar '14, 10:07)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
</div>
<div id="comment-tools-31436" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31436-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="31441"></span>

<div id="answer-container-31441" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31441-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, a quick web search found <a href="http://docs.oracle.com/cd/E14571_01/web.1111/e10145/vis_newfeat.htm">this</a> note about using external tile layers, <a href="http://docs.oracle.com/cd/E14571_01/web.1111/e10145/vis_omaps.htm#BACDBCBI">this</a> note about how you've got to configure your data before using an external spherical mercator tile layer (read the rest of that for more MVCustomMapTileLayer info) and and <a href="http://oraclemaps.blogspot.co.uk/2009/05/using-openstreetmap-tiles-with-oracle.html">this</a> example. If you haven't already done it, I'd check that you can display data over an external Bing or Google layer before switching to OSM tiles.</p>
<p>The usual OSM <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">tile usage caveats</a> apply of course, but using that last example you should be able to render your own and point Oracle Apps at that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '14, 09:57</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-31441" class="comments-container">
&#10;</div>
<div id="comment-tools-31441" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31441-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31438"></span>

<div id="answer-container-31438" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31438-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Oracle MapViewer is made by Oracle, not by OSM. You have to contact Oracle if you have questions about their software.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '14, 08:30</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-31438" class="comments-container">
&#10;</div>
<div id="comment-tools-31438" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31438-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31440"></span>

<div id="answer-container-31440" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31440-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>MapViewer appears to rely on Oracle Spatial as a back-end. There are no tools to import OpenStreetMap data directly into Oracle Spatial, but you may be able to use shapefiles created from OSM data. However, you would need to read the Oracle documentation to find out how to do this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '14, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-31440" class="comments-container">
&#10;</div>
<div id="comment-tools-31440" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31440-form-container" class="comment-form-container">
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

