+++
type = "question"
title = "How to deal with GPS accuracy problems mapping in London"
description = '''A question a friend emailed me with recently: I was visiting the Chelsea Physic Gardens today, doing the tourist thing, and figured a bit of mapping might be in order... until the GPS lock put me consistently at least ten metres off point, in various directions. Given that the place is surrounded on...'''
date = "2015-09-03T11:54:00Z"
lastmod = "2015-09-03T12:05:00Z"
weight = 45039
keywords = [ "gps" ]
aliases = [ "/questions/45039" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to deal with GPS accuracy problems mapping in London](/questions/45039/how-to-deal-with-gps-accuracy-problems-mapping-in-london)

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
<span id="post-45039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45039-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-45039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><em>A question a friend emailed me with recently:</em></p>
<p>I was visiting the Chelsea Physic Gardens today, doing the tourist thing, and figured a bit of mapping might be in order... until the GPS lock put me consistently at least ten metres off point, in various directions. Given that the place is surrounded on three sides by medium rise blocks of flats, ten foot walls, and myriad trees, is it likely to be a forelorn hope to get any decent fixed lock signal there? Oh, and forget trying to map it manually, the place is an absolute nightmare to quarter on paper, GPS tracks are the only way I can see it being done with any reliability!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Sep '15, 11:54</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-45039" class="comments-container">
<span id="45041"></span>
<div id="comment-45041" class="comment">
<div id="post-45041-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also a very relevant question in places not covered by WAAS / EGNOS - GPS traces can be substantially further out there.</p>
</div>
<div id="comment-45041-info" class="comment-info">
<span class="comment-age">(03 Sep '15, 12:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45039" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45039-form-container" class="comment-form-container">
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

<span id="45040"></span>

<div id="answer-container-45040" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45040-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-45040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Different people will give you different advice and mapping techniques for this kind of thing. The way I would do it is basically walk around the park in some logical order, taking a load of photos, then when I get home, map the basic layout of the park based entirely on bing imagery. <a href="http://harrywood.co.uk/maps/bingosm.html?lat=51.48455434284196&amp;lon=-0.1620274900711153&amp;zoom=18&amp;bingopacity=58">We can see the paths etc in the imagery</a></p>
<p>but of course, surveying is still important. I'd use my photos to add details and typology of things which you would not be able to see from the imagery, and to double check things which might be out of date in the imagery.</p>
<p>...and normally I wouldn't bother to use GPS for anything at all (apart from placing the photos in vaguely the right place while I'm working in JOSM.</p>
<p>Now some might say this is cheating, but it's more accurate than GPS, as I will explain.</p>
<p>There is always the awkward question of imagery "offset". I think some OSM mappers are far too ready to assume that their GPS trace is accurate and everything else is wrong. As a result there's some patches of data in London with different offsets, as people have attempted to correct the imagery. My usual approach to these is to assume that previous mappers have known what they were doing with offsets. So I shift my imagery layer in JOSM to match the existing OSM data. Where that is not possible due to two competing offsets, I... try to pick an offset which is sort of half way between. You can see my vague hand-wavy demonstration of this at the <a href="https://vimeo.com/67201566">beginning of this video</a></p>
<p>But it is frustrating because (although I generally assume it) I actually consider it highly unlikely that prior mappers <em>did</em> know what they were doing with offsets. The imagery <em>does</em> have an incorrect offset from reality, and this varies from place to place in London, but a single GPS trace is definitely not sufficient to establish what the offset is (particularly if there's tall buildings around). To create a "ground reference point" is a lot of effort. You need to pick a clearly visible very precise point on the ground or something like a fountain in the middle of the park to walk around, and I would say you need to take <em>at least five</em> different GPS traces on different days to zero in on a correct offset.</p>
<p>I went through this process in the park outside my house. I had about seven different traces, but discarded two of them as being wildly wrong (must have just got a bad GPS fix that day for some reason), the remaining traces all seemed to agree within about a metre or two. The little loops as I walked around a statue in the middle of the park, were all looping in almost the same place. And taking the average positioning of those as ground truth, I established the exact offset of the bing imagery outside my house.</p>
<p>...A lot of effort. Which is why I consider it highly unlikely that mappers have gone to that level of hassle in many other parts of London. Most awkward offsets you see in the data in London, will be most likely somebody placing too much trust in a single GPS trace. The most correct thing we can realistically do, would actually be to abandon such efforts and shift all data to align with bing imagery, <em>unless</em> we have some sort of widely publicised procedure and a push to create lots of ground reference points. But it would be a lot of hassle.</p>
<p>But there's the "correct" offset, and then there's the best way to treat offsets in order to avoid annoying other mappers :-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '15, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Sep '15, 11:59</strong> </span></p>
</div>
</div>
<div id="comments-container-45040" class="comments-container">
&#10;</div>
<div id="comment-tools-45040" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45040-form-container" class="comment-form-container">
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

