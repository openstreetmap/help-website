+++
type = "question"
title = "Anybody else experienced a suddenly slower and more disk consuming planet import with osm2pgsql?"
description = '''Since two years or more I do from time to time a planet import into my postgresql databases on two servers because I needed additional tags by ways of the style sheet. Last successful one was in mid-December. When doing an import in January with just a few new tags, I recognized the import rate of n...'''
date = "2021-02-17T10:24:00Z"
lastmod = "2021-02-17T11:10:00Z"
weight = 78891
keywords = [ "disk_usage", "slow", "osm2pgsql" ]
aliases = [ "/questions/78891" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Anybody else experienced a suddenly slower and more disk consuming planet import with osm2pgsql?](/questions/78891/anybody-else-experienced-a-suddenly-slower-and-more-disk-consuming-planet-import-with-osm2pgsql)

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
<span id="post-78891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78891-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Since two years or more I do from time to time a planet import into my postgresql databases on two servers because I needed additional tags by ways of the style sheet. Last successful one was in mid-December. When doing an import in January with just a few new tags, I recognized the import rate of nodes/second was only half of what I was used to. When I let it run through, my usually sufficient 2TB disk wasn't large enough. Replaced it with a 4TB disk but also this one ran out of disk space. Tried it with newest and some older osm2pgsql versions to no avail. As usual I think I haven't changed anything on the servers (Debian Buster)... Has anyone else every saw such a behaviour and figured out what was screwed up? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-disk_usage" rel="tag" title="see questions tagged &#39;disk_usage&#39;">disk_usage</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '21, 10:24</strong></p>
<img src="https://secure.gravatar.com/avatar/948de5eff339ee8b78f38591334f05ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hkucharek&#39;s gravatar image" />
<p><span>hkucharek</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hkucharek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78891" class="comments-container">
&#10;</div>
<div id="comment-tools-78891" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78891-form-container" class="comment-form-container">
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

<span id="78892"></span>

<div id="answer-container-78892" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78892-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Noticed in Osmose that the update backlog went from 0.4 days gradually towards the evening to 0.6 days yesterday. Just now it dropped to 0.4 days again, suspecting the US went to sleep. Rendering refreshes in ID editor carto and carto-fr is also very slow, some elements wont show for multiple days to a week. I guess that with everyone/many/most being cooked up in house due COVID-19, the use of OSM has gone up exponentially at times 'the site is under heavy load' popping up at times. In short, yes things seem under duress.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '21, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/ed39ace8cbefe3b5c45da98f60f5e34c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SekeRob&#39;s gravatar image" />
<p><span>SekeRob</span><br />
<span class="score" title="211 reputation points">211</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SekeRob has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Feb '21, 11:12</strong> </span></p>
</div>
</div>
<div id="comments-container-78892" class="comments-container">
&#10;</div>
<div id="comment-tools-78892" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78892-form-container" class="comment-form-container">
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

