+++
type = "question"
title = "How do I tag a skywalk / skyway / sky bridge?"
description = '''How do you tag a skywalk / skyway / sky bridge. This is a bridge connecting two buildings usually covered and for pedestrians only. For references please read: http://en.wikipedia.org/wiki/Skywalk Regards'''
date = "2010-11-24T23:25:00Z"
lastmod = "2018-08-27T21:41:00Z"
weight = 1623
keywords = [ "building", "bridge", "tagging" ]
aliases = [ "/questions/1623" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How do I tag a skywalk / skyway / sky bridge?](/questions/1623/how-do-i-tag-a-skywalk-skyway-sky-bridge)

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
<span id="post-1623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1623-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-1623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
3
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do you tag a skywalk / skyway / sky bridge. This is a bridge connecting two buildings usually covered and for pedestrians only.</p>
<p>For references please read: <a href="http://en.wikipedia.org/wiki/Skywalk">http://en.wikipedia.org/wiki/Skywalk</a></p>
<p>Regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Nov '10, 23:25</strong></p>
<img src="https://secure.gravatar.com/avatar/3f398da25e1453020723c955139a4ec7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ALE&#39;s gravatar image" />
<p><span>ALE</span><br />
<span class="score" title="1943 reputation points"><span>1.9k</span></span><span title="41 badges"><span class="badge1">●</span><span class="badgecount">41</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ALE has 4 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Nov '10, 09:11</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-1623" class="comments-container">
&#10;</div>
<div id="comment-tools-1623" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1623-form-container" class="comment-form-container">
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

<span id="2107"></span>

<div id="answer-container-2107" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2107-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-2107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ALE has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For substantial structures over narrower spans, like the ones in your link, I'd suggest</p>
<pre><code>building=yes   # or better still: the same as an adjoining building
level=1
bridge=yes</code></pre>
<p>and be sure to share 2 nodes or more in common with the adjoining buildings on each side. Here's one of the examples from the wikipedia link in OSM: <a href="https://www.openstreetmap.org/browse/way/62333303">"Bridge of Sighs", Oxford</a>.</p>
<hr />
<p>For lighter, longer constructions of metal, say - "raised covered pedestrian walkways", "<a href="http://en.wikipedia.org/wiki/Pedway">pedways</a>" such as they have in big cities in very cold or very wet places, I would suggest</p>
<pre><code>highway=pedestrian
bridge=yes   # if/where goes over something
level=1
covered=yes   # idea stolen from bicycle parking :)</code></pre>
<p>Add in steps leading up to them as necessary, connect to neighbouring buildings at doorway points.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '11, 17:12</strong></p>
<img src="https://secure.gravatar.com/avatar/b4a99bb74962d3cedff3e6d591847852?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrew%20Chadwick&#39;s gravatar image" />
<p><span>Andrew Chadwick</span><br />
<span class="score" title="1129 reputation points"><span>1.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrew Chadwick has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-2107" class="comments-container">
<span id="49568"></span>
<div id="comment-49568" class="comment">
<div id="post-49568-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>shoudn't it be <code>layer=1</code>, rather?</p>
</div>
<div id="comment-49568-info" class="comment-info">
<span class="comment-age">(04 May '16, 09:53)</span> <span class="comment-user userinfo">stephane-gui...</span>
</div>
</div>
<span id="65591"></span>
<div id="comment-65591" class="comment">
<div id="post-65591-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>yeah I think this works the best</p>
</div>
<div id="comment-65591-info" class="comment-info">
<span class="comment-age">(27 Aug '18, 19:48)</span> <span class="comment-user userinfo">jeff0launch</span>
</div>
</div>
<span id="65593"></span>
<div id="comment-65593" class="comment">
<div id="post-65593-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It should be noted that highway=pedestrian is the wrong tag for one of these walkways, because that tag describes a pedestrianized-street. highway=footway would be more appropriate.</p>
</div>
<div id="comment-65593-info" class="comment-info">
<span class="comment-age">(27 Aug '18, 21:41)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-2107" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2107-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1624"></span>

<div id="answer-container-1624" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1624-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>FWIW, I'm very new at this, but the way I've seen it done and how I've been doing it is setting with the following:</p>
<p>highway=footway bridge=yes layer=1</p>
<p>I'm not entirely happy with this method, since it doesn't really render as a "building" on the maps.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '10, 02:46</strong></p>
<img src="https://secure.gravatar.com/avatar/b3ed3a2cce7a1365cbe2d81d5662808c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="txaggie90&#39;s gravatar image" />
<p><span>txaggie90</span><br />
<span class="score" title="186 reputation points">186</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="txaggie90 has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-1624" class="comments-container">
<span id="1656"></span>
<div id="comment-1656" class="comment">
<div id="post-1656-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In reality it is a building and therefore IMHO it should be tagged as such and not as a highway. Is there no other way to tag a sky bridge?</p>
</div>
<div id="comment-1656-info" class="comment-info">
<span class="comment-age">(27 Nov '10, 22:36)</span> <span class="comment-user userinfo">ALE</span>
</div>
</div>
<span id="1657"></span>
<div id="comment-1657" class="comment">
<div id="post-1657-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You could also use building=yes level=1.</p>
</div>
<div id="comment-1657-info" class="comment-info">
<span class="comment-age">(28 Nov '10, 10:10)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="35548"></span>
<div id="comment-35548" class="comment">
<div id="post-35548-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think I may have done such taging for what was a wide corridor suspended between two buildings. and on another one close by, I added them as steps and deferent level tag values to each side [the floors between the two were a matching levelscheme]. The problem is when you try to transition between indoor and outdoor mapping and in larger spaces it can blured to which is which [outside fire escapes and large covered plazas etc]. What is needed is a indoor form of routing line to work like a highway way that isn't a highway because its just space inside part of a building. Tillonecomes we fudge</p>
</div>
<div id="comment-35548-info" class="comment-info">
<span class="comment-age">(05 Aug '14, 18:34)</span> <span class="comment-user userinfo">Govanus</span>
</div>
</div>
</div>
<div id="comment-tools-1624" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1624-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2074"></span>

<div id="answer-container-2074" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2074-score" class="post-score" title="current number of votes">
-5
</div>
<span id="post-2074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you go the the OSM wiki and search for "skywalk", you find:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Talk:Proposed_features/Escalator">https://wiki.openstreetmap.org/wiki/Talk:Proposed_features/Escalator</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '11, 15:00</strong></p>
<img src="https://secure.gravatar.com/avatar/cb9e3487765b1e13e3fd6ebb00fdcac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kartograefin&#39;s gravatar image" />
<p><span>Kartograefin</span><br />
<span class="score" title="592 reputation points">592</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kartograefin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2074" class="comments-container">
&#10;</div>
<div id="comment-tools-2074" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2074-form-container" class="comment-form-container">
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

