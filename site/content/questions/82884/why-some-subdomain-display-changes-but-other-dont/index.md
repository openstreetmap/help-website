+++
type = "question"
title = "Why some subdomain display changes but other dont?"
description = '''Hello, I edit the OSM main map,  and some subdomain display my changes but other dont. I can see the changes in:  https://tile.openstreetmap.org/17/78489/52924.png https://a.tile.openstreetmap.org/17/78489/52924.png  but not in the following subdomains:  https://b.tile.openstreetmap.org/17/78489/529...'''
date = "2021-12-21T12:00:00Z"
lastmod = "2021-12-23T14:13:00Z"
weight = 82884
keywords = [ "leaflet", "duration", "edits", "subdomain" ]
aliases = [ "/questions/82884" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why some subdomain display changes but other dont?](/questions/82884/why-some-subdomain-display-changes-but-other-dont)

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
<span id="post-82884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82884-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I edit the OSM main map, and some subdomain display my changes but other dont.</p>
<p>I can see the changes in:</p>
<ul>
<li><a href="https://tile.openstreetmap.org/17/78489/52924.png">https://tile.openstreetmap.org/17/78489/52924.png</a></li>
<li><a href="https://a.tile.openstreetmap.org/17/78489/52924.png">https://a.tile.openstreetmap.org/17/78489/52924.png</a></li>
</ul>
<p>but not in the following subdomains:</p>
<ul>
<li><a href="https://b.tile.openstreetmap.org/17/78489/52924.png">https://b.tile.openstreetmap.org/17/78489/52924.png</a></li>
<li><a href="https://c.tile.openstreetmap.org/17/78489/52924.png">https://c.tile.openstreetmap.org/17/78489/52924.png</a></li>
</ul>
<p>How long does it take to the servers b,c to recived the updates?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-duration" rel="tag" title="see questions tagged &#39;duration&#39;">duration</span> <span class="post-tag tag-link-edits" rel="tag" title="see questions tagged &#39;edits&#39;">edits</span> <span class="post-tag tag-link-subdomain" rel="tag" title="see questions tagged &#39;subdomain&#39;">subdomain</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Dec '21, 12:00</strong></p>
<img src="https://secure.gravatar.com/avatar/8e74d0c6b5a110c712e5abc1982a98d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DAN&#39;s gravatar image" />
<p><span>DAN</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DAN has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82884" class="comments-container">
&#10;</div>
<div id="comment-tools-82884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82884-form-container" class="comment-form-container">
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

<span id="82893"></span>

<div id="answer-container-82893" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82893-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>these addresses (a,b,c) are here only for historical reasons, so that older browsers would load more tiles in parallel but they all point to the same server. Nowadays (especially with HTTP/2 IIRC), it is not needed. And they all point to a CDN now. Behind the CDN there are a few rendering servers, but they should be in sync mostly. Some <a href="https://prometheus.openstreetmap.org/d/wyyzhZKMk/tile-rendering?orgId=1&amp;refresh=1m">statistics</a> about that. A lot of information is on the <a href="https://wiki.openstreetmap.org/wiki/Servers">wiki</a>, some of it is outdated though.</p>
<p>It might be a trouble of cache on your side. Try Ctrl+Shift+R. Just in case, I've checked, they all look the same to me now.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Dec '21, 14:13</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-82893" class="comments-container">
&#10;</div>
<div id="comment-tools-82893" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82893-form-container" class="comment-form-container">
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

