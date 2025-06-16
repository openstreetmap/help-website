+++
type = "question"
title = "How to tag a presence or flashing light based restrictions for School Zone?"
description = '''In my area of the world (the US state of Vermont), some school zones don’t have time-based restrictions (esp. maxspeed), but instead a flashing light or sign specifying “When children are present.” I’m familiar with conditional restrictions as advised in the answer to the aforelinked question regard...'''
date = "2018-04-27T19:07:00Z"
lastmod = "2021-02-19T08:07:00Z"
weight = 63194
keywords = [ "variable", "speedlimit", "school", "maxspeed", "restrictions" ]
aliases = [ "/questions/63194" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag a presence or flashing light based restrictions for School Zone?](/questions/63194/how-to-tag-a-presence-or-flashing-light-based-restrictions-for-school-zone)

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
<span id="post-63194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63194-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In my area of the world (the US state of Vermont), some school zones don’t have <a href="/questions/15399/how-to-tag-a-time-based-maxspeed-for-school-zone">time-based restrictions (esp. maxspeed)</a>, but instead a flashing light or sign specifying “When children are present.” I’m familiar with <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions">conditional restrictions</a> as advised in the answer to the aforelinked question regarding time-based restrictions, but I’m not sure how to appropriately designate “presence” or a flashing signal. How should one do so?</p>
<p>Also included in the examples below is a strange one: a street is one-way when a signal is flashing.</p>
<p>Examples:</p>
<ol>
<li>Saint Peter St, Winooski, VT, US, between North St &amp; Weaver St (<a href="https://www.openstreetmap.org/#map=18/44.49619/-73.18824">OSM</a>): Street is one-way only when a signal light is flashing at the North St end (do-not-enter signs w/flashing signals at North St).</li>
<li>VT-100, Duxbury, VT, US, near entrance to Crossett Brook Middle School (<a href="https://www.openstreetmap.org/#map=17/44.32255/-72.75481">OSM</a>): VT-100 has maxspeed of 40 mph, but signs with signal lights at either side of the entrance to crossett Brook specify maxspeed of 35 mph when signals are flashing.</li>
<li>VT-100, South Duxbury, VT, US, near entrance to Harwood Union High School (<a href="https://www.openstreetmap.org/#map=15/44.2543/-72.7874">OSM</a>): VT-100 has maxspeed of 40 mph, but signs at either side of entrance to Harwood denote a maxspeed of 35 mph “When children are present” (<a href="http://www.mapillary.com/map/im/FIVb9W4123bFgEB3vz4A1Q/photo">Mapillary</a>).</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-variable" rel="tag" title="see questions tagged &#39;variable&#39;">variable</span> <span class="post-tag tag-link-speedlimit" rel="tag" title="see questions tagged &#39;speedlimit&#39;">speedlimit</span> <span class="post-tag tag-link-school" rel="tag" title="see questions tagged &#39;school&#39;">school</span> <span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-restrictions" rel="tag" title="see questions tagged &#39;restrictions&#39;">restrictions</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '18, 19:07</strong></p>
<img src="https://secure.gravatar.com/avatar/b2217a363e0648dd23614752b0de75bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="linetrace&#39;s gravatar image" />
<p><span>linetrace</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="linetrace has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63194" class="comments-container">
<span id="78936"></span>
<div id="comment-78936" class="comment">
<div id="post-78936-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to bump this, because speed limit signs with "when children are present" are all over Humboldt, CA. And I have found no guidance on how to map this VERY common sign / speed limit.</p>
<p>I've been getting by with traffic_sign=maxspeed and maxspeed:conditional=15 mph @ "When Children are Present"</p>
<p>However, I'd LOVE to make sure I'm using something that'll be accepted by renderers, navigation programs, etc, if possible? And when I try applying maxspeed:conditional=15 mph @ "When Children are Present" to a street, my editing program, Vespucci, says it's wrong.</p>
</div>
<div id="comment-78936-info" class="comment-info">
<span class="comment-age">(19 Feb '21, 08:07)</span> <span class="comment-user userinfo">JesseAKARaccoon</span>
</div>
</div>
</div>
<div id="comment-tools-63194" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63194-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

