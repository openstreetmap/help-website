+++
type = "question"
title = "Why does construction=motorway need highway=construction?"
description = '''Hello guys, I often make the motorways or expressways open, and here is my question: what for should I have highway=construction if I already have construction=motorway which is already a highway? It looks as if I put 2 tags: highway=construction and construction=highway, which is self-understanding...'''
date = "2016-07-18T05:53:00Z"
lastmod = "2016-07-21T16:46:00Z"
weight = 50960
keywords = [ "construction", "tagging", "highway" ]
aliases = [ "/questions/50960" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why does construction=motorway need highway=construction?](/questions/50960/why-does-constructionmotorway-need-highwayconstruction)

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
<span id="post-50960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50960-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-50960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello guys, I often make the motorways or expressways open, and here is my question: what for should I have highway=construction if I already have construction=motorway which is already a highway? It looks as if I put 2 tags: highway=construction and construction=highway, which is self-understanding that they are equal. It just fills OSM with additional memory and so it loads computers too much. Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-construction" rel="tag" title="see questions tagged &#39;construction&#39;">construction</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jul '16, 05:53</strong></p>
<img src="https://secure.gravatar.com/avatar/77dac03ece963907ee777ed23befd7bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ukraroad&#39;s gravatar image" />
<p><span>Ukraroad</span><br />
<span class="score" title="76 reputation points">76</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ukraroad has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50960" class="comments-container">
&#10;</div>
<div id="comment-tools-50960" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50960-form-container" class="comment-form-container">
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

<span id="50961"></span>

<div id="answer-container-50961" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50961-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-50961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In OSM, "highway" means "any road, street or path" - the meaning is specified by highway=motorway, or highway=-residential, or even highway=footway. Construction is designated by highway=construction , with <code>construction=</code> specifying the <em>type</em> of construction. "construction=highway" does <em>not</em> add any extra info on <em>what</em> is being constructed; "construction=motorway" does.</p>
<p>I think you might be confused by the "motorway" meaning of the <em>word</em> "highway" - in OSM, <code>highway</code> is a keyword, not a road type.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jul '16, 07:53</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jul '16, 08:06</strong> </span></p>
</div>
</div>
<div id="comments-container-50961" class="comments-container">
<span id="50963"></span>
<div id="comment-50963" class="comment">
<div id="post-50963-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>As an example, consider "residential" - that's valid both as a highway type and as a landuse - "landuse=construction; construction=residential" is different to "highway=construction; construction=residential".</p>
</div>
<div id="comment-50963-info" class="comment-info">
<span class="comment-age">(18 Jul '16, 08:03)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50964"></span>
<div id="comment-50964" class="comment">
<div id="post-50964-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>The wiki article (<span>wiki.openstreetmap.org/wiki/Key:construction</span>) also does a fairly good job of explaining why both tags are needed.</p>
</div>
<div id="comment-50964-info" class="comment-info">
<span class="comment-age">(18 Jul '16, 09:47)</span> <span class="comment-user userinfo">Lightsider</span>
</div>
</div>
<span id="50973"></span>
<div id="comment-50973" class="comment">
<div id="post-50973-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The tagging combination also makes it a lot easier to disseminate when rendering if you've ever tried to use QGIS to create a map using OSM data.</p>
</div>
<div id="comment-50973-info" class="comment-info">
<span class="comment-age">(19 Jul '16, 02:31)</span> <span class="comment-user userinfo">Longhorn256</span>
</div>
</div>
<span id="51008"></span>
<div id="comment-51008" class="comment">
<div id="post-51008-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did not mean I am confused that motorway is the same as highway, I just don't understand why don't just put construction=motorway</p>
</div>
<div id="comment-51008-info" class="comment-info">
<span class="comment-age">(21 Jul '16, 05:11)</span> <span class="comment-user userinfo">Ukraroad</span>
</div>
</div>
<span id="51039"></span>
<div id="comment-51039" class="comment">
<div id="post-51039-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>For a data consumer, what is described by an object with only the tag "construction=motorway"? Is it a highway? Is it an area of land where a motorway is being constructed (ie. "landuse=construction")? Is it something else? That tag alone doesn't sufficiently describe what the object is. Using "highway=construction" clearly indicates that it's a highway under construction, and the "construction=motorway" tag expands on that by stating that the type of highway under construction is a motorway.</p>
</div>
<div id="comment-51039-info" class="comment-info">
<span class="comment-age">(21 Jul '16, 16:46)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-50961" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50961-form-container" class="comment-form-container">
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

