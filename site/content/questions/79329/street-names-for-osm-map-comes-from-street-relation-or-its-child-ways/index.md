+++
type = "question"
title = "Street names for osm map comes from street relation or its child ways?"
description = '''I&#x27;m extracting city streets by osm relation and ways. In common case street consists of relation as street which includes a list of its child way (or ways) as street. Both the relation as street and its way as street can be tagged with name.   My guess was that the name tag of relation as street has...'''
date = "2021-03-19T17:28:00Z"
lastmod = "2021-03-20T16:12:00Z"
weight = 79329
keywords = [ "openstreetmap", "street", "streetnames" ]
aliases = [ "/questions/79329" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Street names for osm map comes from street relation or its child ways?](/questions/79329/street-names-for-osm-map-comes-from-street-relation-or-its-child-ways)

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
<span id="post-79329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79329-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm extracting city streets by osm relation and ways. In common case street consists of relation as street which includes a list of its child way (or ways) as street. Both the relation as street and its way as street can be tagged with name.  My guess was that the name tag of relation as street has more higher priority then the name tag of its child way. But it looks like it is not a correct assumption.</p>
<p>Example: relation <a href="https://www.openstreetmap.org/relation/3431740/">3431740</a> tagged with "Дзержинського вулиця" as name, and its child way <a href="https://www.openstreetmap.org/way/147405229">147405229</a> tagged with "Благодатний провулок" as name and on the map I see the street name as "Благодатний провулок".</p>
<p>So my question is: Which way does the Osm define the name of the street if there are alternatives?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '21, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe9f92ff514336a321930f0755b67c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ozerovn&#39;s gravatar image" />
<p><span>Ozerovn</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ozerovn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79329" class="comments-container">
&#10;</div>
<div id="comment-tools-79329" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79329-form-container" class="comment-form-container">
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

<span id="79332"></span>

<div id="answer-container-79332" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79332-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-79332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A relation with <code>type=associatedStreet</code> is used for addressing, not for defining anything about the street itself. It just says that the members of the relation have an address on that street.</p>
<p>The longstanding standard is that the name of a street is in the <code>name</code> tag on the way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Mar '21, 18:05</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-79332" class="comments-container">
<span id="79333"></span>
<div id="comment-79333" class="comment">
<div id="post-79333-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I see, thanks</p>
</div>
<div id="comment-79333-info" class="comment-info">
<span class="comment-age">(19 Mar '21, 19:34)</span> <span class="comment-user userinfo">Ozerovn</span>
</div>
</div>
<span id="79343"></span>
<div id="comment-79343" class="comment">
<div id="post-79343-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also associatedStreet relations can be used to define addr:parentstreet (as this tag has only recently been proposed), so you could have &lt;street name=""&gt; on the ways and &lt;parent street="" name=""&gt; on the relation.</p>
</div>
<div id="comment-79343-info" class="comment-info">
<span class="comment-age">(20 Mar '21, 16:12)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-79332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79332-form-container" class="comment-form-container">
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

