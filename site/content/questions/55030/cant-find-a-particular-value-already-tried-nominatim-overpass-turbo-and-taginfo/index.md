+++
type = "question"
title = "Can&#x27;t find a particular value (already tried Nominatim, Overpass Turbo and TagInfo)"
description = '''Please, have a look at the center of this map. Turs out someone added &quot;plantel dr. ángel ma. garibay kintana&quot; to something that apparently has some inherent admin_level value that makes it show up at zoom 10, blocking out the name of the city below it (&quot;Toluca de Lerdo&quot;), which happens to be a capit...'''
date = "2017-03-13T06:34:00Z"
lastmod = "2017-03-13T17:38:00Z"
weight = 55030
keywords = [ "search" ]
aliases = [ "/questions/55030" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't find a particular value (already tried Nominatim, Overpass Turbo and TagInfo)](/questions/55030/cant-find-a-particular-value-already-tried-nominatim-overpass-turbo-and-taginfo)

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
<span id="post-55030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55030-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Please, have a look at the center of <a href="https://www.openstreetmap.org/#map=12/19.2881/-99.6518">this map</a>. Turs out someone added "plantel dr. ángel ma. garibay kintana" to <em>something</em> that apparently has some inherent admin_level value that makes it show up at zoom 10, blocking out the name of the city below it ("Toluca de Lerdo"), which happens to be a capital city.</p>
<p>This is flat-out wrong but for the love of me, I can't find the element that has such value in order to fix it. I have already tried Nominatim, Overpass Turbo and TagInfo, but they don't return any results if I query the whole string.</p>
<p>If I split the string, say, "garibay kintana", they do return a couple of elements but they seem to have correct information, or at least neither of them appear to be the element I look for. If I try to search for "plantel dr.", nothing comes up.</p>
<p>What's a good way to find out what element is causing this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Mar '17, 06:34</strong></p>
<img src="https://secure.gravatar.com/avatar/37882972d0db7a93230b8e5e7fdbabc3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Absay&#39;s gravatar image" />
<p><span>Absay</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Absay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55030" class="comments-container">
&#10;</div>
<div id="comment-tools-55030" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55030-form-container" class="comment-form-container">
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

<span id="55035"></span>

<div id="answer-container-55035" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55035-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A couple of months ago someone (probably accidentally) changed the name of the node for the city of Toluca de Lerdo to "plantel dr. ángel ma. garibay kintana". This was spotted and corrected a while back: however the relevant tiles (levels 12 and lower) have not yet been re-rendered. A reasonable way to cross-check is to view other available renderings on the main OSM site. If they all show something then it's likely to still be in the database; if they show different things then one is probably looking at artefacts associated with the different re-rendering algorithms.</p>
<p>You can see the change in the history here: <a href="https://www.openstreetmap.org/node/269914302/history#map=11/19.2925/-99.6569">https://www.openstreetmap.org/node/269914302/history#map=11/19.2925/-99.6569</a></p>
<p>So no need to tear your hair out continuing to look for it!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '17, 14:10</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-55035" class="comments-container">
<span id="55040"></span>
<div id="comment-55040" class="comment">
<div id="post-55040-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I knew it couldn't be there anymore if the DB searchers where not returning relevant results and other renderers weren't showing it, but I couldn't explain the fact the map was still rendering such information. A follow-up question: when are those tiles going to re-render?</p>
</div>
<div id="comment-55040-info" class="comment-info">
<span class="comment-age">(13 Mar '17, 17:38)</span> <span class="comment-user userinfo">Absay</span>
</div>
</div>
</div>
<div id="comment-tools-55035" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55035-form-container" class="comment-form-container">
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

