+++
type = "question"
title = "Retrieving emptied relations"
description = '''Hi List, by chance I came across an empty cycling relation which I know it was full of members. Sadly, the user who removed all members also deleted his/her account, so I couldn&#x27;t ask for explanations. OSM relation history isn&#x27;t particularly useful, since the information is 363 members in previous v...'''
date = "2021-01-21T11:08:00Z"
lastmod = "2021-01-21T12:55:00Z"
weight = 78432
keywords = [ "revert", "route", "relation" ]
aliases = [ "/questions/78432" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Retrieving emptied relations](/questions/78432/retrieving-emptied-relations)

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
<span id="post-78432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78432-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi List,</p>
<p>by chance I came across an empty cycling <a href="https://www.openstreetmap.org/relation/6798010/history">relation</a> which I know it was full of members. Sadly, the user who removed all members also deleted his/her account, so I couldn't ask for explanations.</p>
<p>OSM <a href="https://www.openstreetmap.org/relation/6798010/history">relation history</a> isn't particularly useful, since the information is 363 members in previous version #77 and no mention of members in latest #78. <a href="https://osmlab.github.io/osm-deep-history/">Deep history</a> tool isn't useful either, since it reports only tags changes. Eventually, I've found useful <a href="http://osm.mapki.com/history/relation.php?id=6798010">Deep Diff</a> tool, which reports the full history of members in's and out's.</p>
<p><strong>How can I restore the relation to version #77?</strong></p>
<p>I tried JOSM changeset reverter without success. Maybe I did something wrong, or there's something I cannot understand: I expected that reverting <a href="http://osm.org/browse/changeset/92624763">changeset</a> where members were removed, should rebuild the members list, but reverter wasn't able to, returning only relation with zero members.</p>
<p>Since it is rather easy rewrite relation in a textual form, can I upload someway the below text instead? In case, are there some bad side effects?</p>
<pre><code>relation 6798010
name:it=Mobilità ciclabile tra Italia e Slovenia
name:sl=Kolesarska mobilnost med Slovenijo in Italijo
network=icn
ref=bimobis
route=bicycle
type=route
&#10;wy 109568228
wy 107298107
[...]
wy 165283326</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '21, 11:08</strong></p>
<img src="https://secure.gravatar.com/avatar/d33efa30f05d8f3604e7210c48b24a8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cascafico&#39;s gravatar image" />
<p><span>Cascafico</span><br />
<span class="score" title="283 reputation points">283</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cascafico has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78432" class="comments-container">
<span id="78434"></span>
<div id="comment-78434" class="comment">
<div id="post-78434-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Take a look at <a href="https://wiki.openstreetmap.org/wiki/Level0">https://wiki.openstreetmap.org/wiki/Level0</a></p>
</div>
<div id="comment-78434-info" class="comment-info">
<span class="comment-age">(21 Jan '21, 11:49)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="78435"></span>
<div id="comment-78435" class="comment">
<div id="post-78435-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Not sure what to do if reverter has failed but for future reference you should be able to retrieve previous versions of objects following pattern for <a href="/questions/20506/overpass-get-older-version">this question</a>.</p>
</div>
<div id="comment-78435-info" class="comment-info">
<span class="comment-age">(21 Jan '21, 12:46)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="78436"></span>
<div id="comment-78436" class="comment">
<div id="post-78436-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks! I often use Level0. I tried to upload relation text, resulting in a very long list of warnings... I just had to scroll to the bottom line to see what was wrong: 2 ways not existing anymore. I removed them from the 363 member list and changeset was correctly stored :-)</p>
</div>
<div id="comment-78436-info" class="comment-info">
<span class="comment-age">(21 Jan '21, 12:55)</span> <span class="comment-user userinfo">Cascafico</span>
</div>
</div>
</div>
<div id="comment-tools-78432" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78432-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

