+++
type = "question"
title = "Namedetails parameter not working on own nominatim installation"
description = '''I&#x27;ve installed Nominatim on a local server of ours, and it seems to work fine, except for one minor (major for me unfortunatly) problem. It is not returning the different naming of a specific location, on different languages. For example, let&#x27;s take this query:  http://nominatim.openstreetmap.org/re...'''
date = "2016-05-08T02:01:00Z"
lastmod = "2016-05-08T13:05:00Z"
weight = 49616
keywords = [ "nominatim", "language" ]
aliases = [ "/questions/49616" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Namedetails parameter not working on own nominatim installation](/questions/49616/namedetails-parameter-not-working-on-own-nominatim-installation)

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
<span id="post-49616-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49616-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49616-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've installed Nominatim on a local server of ours, and it seems to work fine, except for one minor (major for me unfortunatly) problem. It is not returning the different naming of a specific location, on different languages.</p>
<p>For example, let's take this query:</p>
<pre><code> http://nominatim.openstreetmap.org/reverse?format=json&amp;osm_type=R&amp;osm_id=146656&amp;namedetails=1</code></pre>
<p>This query returns a json array, with a "namedetails" parameter, containing the different names on different languages. When I make the same query, on my own nominatim installation, it returns the same data, but with no namedetails parameter. otherwise, the data matches on both queries. Any ideas what could be the problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 May '16, 02:01</strong></p>
<img src="https://secure.gravatar.com/avatar/8d611d043d7267073e41089a5283fbe1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Adam%20Baranyai&#39;s gravatar image" />
<p><span>Adam Baranyai</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Adam Baranyai has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49616" class="comments-container">
&#10;</div>
<div id="comment-tools-49616" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49616-form-container" class="comment-form-container">
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

<span id="49620"></span>

<div id="answer-container-49620" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49620-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>namedetails were introduced in Nominatim version 2.5.0, released February 2016. <a href="https://github.com/twain47/Nominatim/wiki/Release-Notes-2.5.0">https://github.com/twain47/Nominatim/wiki/Release-Notes-2.5.0</a> I see you asked your first question "How to use address lookup when nominatim is installed on own server" on Feb/21st. It is possible you still run version 2.4.0?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 May '16, 12:57</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-49620" class="comments-container">
<span id="49621"></span>
<div id="comment-49621" class="comment">
<div id="post-49621-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No, I've already installed the 2.5.0 version, but I think I know what the problem is. It seems that to get the namedetails, I would need PostgreSQL 9.3 at least, and with my base CentOS installation, only PostgreSQL 9.2 came:| Now I am trying to figure out a way, to upgrade my PostgreSQL without having to redo the whole Nominatim installation from the start, cause it took quite long time to finish(2 weeks). Any ideas on a possible solution with PostgreSQL 9.2.15?</p>
</div>
<div id="comment-49621-info" class="comment-info">
<span class="comment-age">(08 May '16, 13:05)</span> <span class="comment-user userinfo">Adam Baranyai</span>
</div>
</div>
</div>
<div id="comment-tools-49620" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49620-form-container" class="comment-form-container">
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

