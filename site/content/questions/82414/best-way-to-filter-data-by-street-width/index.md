+++
type = "question"
title = "Best way to filter data by street width?"
description = '''I&#x27;m new to working with OSM data and there seem to be a few different ways to download it. I&#x27;m looking to download road vector data (ideally globally but a small region works as well) filtered by width such that only large roads wider than a certain threshold (like highways) are included. Which is t...'''
date = "2021-10-29T20:22:00Z"
lastmod = "2021-10-30T13:15:00Z"
weight = 82414
keywords = [ "filter", "width", "download", "road" ]
aliases = [ "/questions/82414" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Best way to filter data by street width?](/questions/82414/best-way-to-filter-data-by-street-width)

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
<span id="post-82414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82414-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to working with OSM data and there seem to be a few different ways to download it. I'm looking to download road vector data (ideally globally but a small region works as well) filtered by width such that only large roads wider than a certain threshold (like highways) are included. Which is the best option for this -- the Overpass API? Others?</p>
<p>Thoughts on how to write the query for this are greatly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-width" rel="tag" title="see questions tagged &#39;width&#39;">width</span> <span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Oct '21, 20:22</strong></p>
<img src="https://secure.gravatar.com/avatar/91145d5cf6d21231451e6e4a78b846cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krt333&#39;s gravatar image" />
<p><span>krt333</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krt333 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82414" class="comments-container">
<span id="82415"></span>
<div id="comment-82415" class="comment">
<div id="post-82415-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't know how to help you with your query but as a long-time OSM mapper, I can say that most highways in OSM don't have a defined width associated with them. That is, most of the mappers I know don't use the tag width=*. It's a level of detail that isn't critical for the type of mapping many of us do.</p>
<p>So, while you will certainly get some help in developing a working query here, I doubt whether it will be very useful.</p>
</div>
<div id="comment-82415-info" class="comment-info">
<span class="comment-age">(29 Oct '21, 21:05)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="82423"></span>
<div id="comment-82423" class="comment">
<div id="post-82423-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><em>"such that only large roads wider than a certain threshold (like highways) are included"</em> makes me wonder if you are not in fact looking for a highway classification. At least in more developed regions there is a quite differentiated system of highway classification mapped in OSM. Probably your best bet is to filter by the <a href="https://wiki.openstreetmap.org/wiki/Key:highway"><code>highway</code></a> tag then.</p>
</div>
<div id="comment-82423-info" class="comment-info">
<span class="comment-age">(30 Oct '21, 13:15)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-82414" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82414-form-container" class="comment-form-container">
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

<span id="82420"></span>

<div id="answer-container-82420" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82420-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>width=</code> is not usually tagged, although one may easily measure it on imagery. Even if it is, there are many measures of it (ie whether to include parking and hard shoulder), that not even the uncommonly (at this scale) used <code>width:carriageway=</code> may be reliable enough. Width of carriageway (meaning the traveled lanes only) for a certain number of lanes (lanes=) depends on the design speed (reflected in the legal <code>maxspeed=</code> in operation). The entire roadway (whole paved area) needs to include hard shoulder, which although often assumed in highway=motorway (will need to exclude those without by <code>shoulder!=no</code>) may be under-tagged in other roads as <code>shoulder=</code>. You may also want to think about whether to include short sections of widening for turn lanes at intersections if this detail is present at your country being worked on, or evaluate a continuous length of main lanes only (this is better pre-processed afterwards I guess, as an outsider).</p>
<p>Overpass is obviously easier when working with small areas, or if you don't want to download and set up a local data file. The Overpass query would include combinations of <code>[highway=motorway]</code> (think you want to separately query for <code>=trunk</code> and <code>=primary</code> using different criteria), <code>(if:t[lanes]&gt;=3)</code>, <code>(if:t[maxspeed]&gt;=100)</code> (need to use <code>(if:number(t[maxspeed])&gt;65)</code> for mph units in USA), etc.</p>
<p>One official blog post: <a href="https://dev.overpass-api.de/blog/numbers.html">https://dev.overpass-api.de/blog/numbers.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '21, 08:04</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Oct '21, 08:10</strong> </span></p>
</div>
</div>
<div id="comments-container-82420" class="comments-container">
&#10;</div>
<div id="comment-tools-82420" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82420-form-container" class="comment-form-container">
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

