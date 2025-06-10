+++
type = "question"
title = "Rendering of protected areas"
description = '''Seems like there is a serious issue with rendering of protected areas. I often see people tagging various protected areas as &quot;boundary=national park&quot; even if those areas are not national parks but are of lower protection level, because they simply want the areas to render. I made some research on re...'''
date = "2012-02-25T20:38:00Z"
lastmod = "2012-02-26T12:24:00Z"
weight = 10790
keywords = [ "national_park", "rendering", "protected_area", "mapnik" ]
aliases = [ "/questions/10790" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering of protected areas](/questions/10790/rendering-of-protected-areas)

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
<span id="post-10790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10790-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Seems like there is a serious issue with rendering of protected areas. I often see people tagging various protected areas as "boundary=national park" even if those areas are not national parks but are of lower protection level, because they simply want the areas to render. I made some research on rendering of "boundary=protected area" with various "protect id" and "protection class" and found out some of those do not render at all (even at max zoom levels). It seems mapnik setting does not even follow <a href="http://wiki.openstreetmap.org/wiki/Protected_Area_Rendering#Protected_Areas">Protected Area Rendering#Protected Areas</a> wiki page... while the setting proposed on this page could use some tweaks too. Where should I start trying to sort this out?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-national_park" rel="tag" title="see questions tagged &#39;national_park&#39;">national_park</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-protected_area" rel="tag" title="see questions tagged &#39;protected_area&#39;">protected_area</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Feb '12, 20:38</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-10790" class="comments-container">
&#10;</div>
<div id="comment-tools-10790" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10790-form-container" class="comment-form-container">
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

<span id="10807"></span>

<div id="answer-container-10807" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10807-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"Where should I start trying to sort this out?". I think locally. Make some test renderings and tweak your rules until you are satisfied.</p>
<p>The page you are linking to contains rendering rules for the Kosmos rendering engine, they have to be modified to work with mapnik (this is not a big deal, but it's worth to point it out).</p>
<p>When you come to a point where you are satisfied with your rendering rules and respective zoom factors, open a ticket in trac, component <code>mapnik</code>, and paste your patch. I think that this has a good chance to get implemented in the near future (because usage of <code>boundary=protected_area</code> is recently growing rapidly. Some time ago when I last checked for it on taginfo it wasn't yet used a lot.).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '12, 12:24</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-10807" class="comments-container">
&#10;</div>
<div id="comment-tools-10807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10807-form-container" class="comment-form-container">
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

