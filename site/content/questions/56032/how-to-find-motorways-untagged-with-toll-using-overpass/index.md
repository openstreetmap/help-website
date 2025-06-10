+++
type = "question"
title = "How to find motorways untagged with toll=* using Overpass?"
description = '''There&#x27;s a set of motorways surrounding a city. All motorways for the country are either paid (default), or toll-free (where explicitly marked). Therefore, it makes sense to mark the toll-free motorways as toll=no, as no tagging implies toll=yes in the general area. Now, I can query Overpass API (fro...'''
date = "2017-05-04T16:04:00Z"
lastmod = "2017-05-05T13:31:00Z"
weight = 56032
keywords = [ "overpass", "tagging", "overpass-api", "toll" ]
aliases = [ "/questions/56032" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to find motorways untagged with toll=\* using Overpass?](/questions/56032/how-to-find-motorways-untagged-with-toll-using-overpass)

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
<span id="post-56032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56032-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There's a set of motorways surrounding a city. All motorways for the country are either paid (default), or toll-free (where explicitly marked).</p>
<p>Therefore, it makes sense to mark the toll-free motorways as <code>toll=no</code>, as no tagging implies <code>toll=yes</code> in the general area.</p>
<p>Now, I can query Overpass API (from JOSM) - filtering <code>way["highway"="motorway"]</code> gives me all motorways; filtering <code>way["highway"="motorway"]["toll"=*]</code> gives me motorways with explicit toll info. I'm interested in the opposite: in motorways which are <em>not</em> tagged with <code>toll</code>. I haven't found that anywhere in the examples, here, or on the Internet at large.</p>
<p>Is there a way do find "ways that have <em>this tag</em> but <em>not that tag</em>"?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span> <span class="post-tag tag-link-toll" rel="tag" title="see questions tagged &#39;toll&#39;">toll</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '17, 16:04</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-56032" class="comments-container">
&#10;</div>
<div id="comment-tools-56032" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56032-form-container" class="comment-form-container">
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

<span id="56033"></span>

<div id="answer-container-56033" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56033-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Piskvor has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is possible by using regular expressions and querying for <code>["highway"="motorway"]["toll"!~".*"]</code>.</p>
<p>However it sounds like you are about to perform an <a href="https://wiki.openstreetmap.org/wiki/Automated_edits">automated edit</a>. Can you be really sure that all highways without a toll tag require a fee? I guess there is still a chance that some motorways are missing a toll=yes tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '17, 16:50</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-56033" class="comments-container">
<span id="56034"></span>
<div id="comment-56034" class="comment">
<div id="post-56034-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's what I am looking for, thank you. And on second look, my wording does sound suspicious :) Do not worry, I am not about to mass-edit: I am looking for a tool to check for missing spots. I have recently driven one part of the city's ring road, so now I'm comparing my notes with the DB to see if all the places around the city that are enumerated in a city bylaw and <em>physically</em> marked as "toll not required" are marked as such in OSM. Have been using two JOSM layers, one for toll=yes, other for toll=no, and checking for gaps visually; wondered if there was an easier way.</p>
</div>
<div id="comment-56034-info" class="comment-info">
<span class="comment-age">(04 May '17, 16:57)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
<span id="56036"></span>
<div id="comment-56036" class="comment">
<div id="post-56036-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>A recent update added a nicer syntax for missing tags, <code>["highway"="motorway"][!toll]</code>.</p>
</div>
<div id="comment-56036-info" class="comment-info">
<span class="comment-age">(04 May '17, 20:19)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="56046"></span>
<div id="comment-56046" class="comment">
<div id="post-56046-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(btw yes, all motorways without a specific physical tag are toll roads here, by law. What I'm checking is that OSM tagging matches the physical tagging)</p>
</div>
<div id="comment-56046-info" class="comment-info">
<span class="comment-age">(05 May '17, 10:48)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
<span id="56053"></span>
<div id="comment-56053" class="comment">
<div id="post-56053-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And it seems that, in the area I visited, <em>all</em> toll roads have already been correctly tagged as toll=yes; there were some parts left untagged where toll=no was the OTG situation.</p>
</div>
<div id="comment-56053-info" class="comment-info">
<span class="comment-age">(05 May '17, 13:31)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
</div>
<div id="comment-tools-56033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56033-form-container" class="comment-form-container">
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

