+++
type = "question"
title = "How to retrieve official boundaries of rural lots?"
description = '''It is not about OSM tag place=plot but about type=boundary and boundary=?... Because the OSM&#x27;s plot concept is very restrictive. In rural area (geographic area that is not urban) there are no city_block or neighbourhood, all are &quot;lots&quot;.  There are a mosaic of nature reserve, parcel of lands for crop...'''
date = "2018-08-17T16:09:00Z"
lastmod = "2018-08-17T17:52:00Z"
weight = 65405
keywords = [ "retrieve" ]
aliases = [ "/questions/65405" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to retrieve official boundaries of rural lots?](/questions/65405/how-to-retrieve-official-boundaries-of-rural-lots)

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
<span id="post-65405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65405-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>It is not about OSM tag <code>place=plot</code> but about <code>type=boundary</code> and <code>boundary=?</code>... Because the OSM's <em>plot</em> concept is very restrictive. In <em>rural area</em> (geographic area that is not urban) there are no <code>city_block</code> or <code>neighbourhood</code>, all are "lots".</p>
<p>There are a mosaic of <a href="https://www.wikidata.org/wiki/Q179049">nature reserve</a>, parcel of lands for crop, etc. Each <em>lot of rural area</em> is an <strong>"official boundary"</strong> (but it is not a <code>boundary=administrative</code>).</p>
<p>So, how to, the best manner to retrieve that class of elements from OSM?</p>
<hr />
<p><strong>NOTES</strong></p>
<p>With Overpass perhaps we can use a logic <em>OR</em> as filter, something as: <a href="https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dfarmland"><code>landuse=farmland</code></a> <em>or</em> nature reserve <em>or</em> <code>landuse=meadow</code> ...<br />
But I not found a <em>standardized</em> or "endorsed query" to retrieve "official boundaries of rural lots", that will be the answer of this question.</p>
<p>It is not a <code>place=plot</code> because by the Wiki "plot's boundaries are recorded by visual observation on the ground", and here we talking about "official boundaries" with no visual observation on the ground, like the country and city boundaries. It is not a <code>place=plot</code> also because in rural region it is not "a subdivision at a level lower than place=neighbourhood or place=city_block" (Wiki). In rural region of a country like Brazil, the <em>rural lot</em> have also the function of a "rural neighbourhood" or a "rural block".</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-retrieve" rel="tag" title="see questions tagged &#39;retrieve&#39;">retrieve</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Aug '18, 16:09</strong></p>
<img src="https://secure.gravatar.com/avatar/6963015ca2c3146e2a2a348b7fcb793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppKrauss&#39;s gravatar image" />
<p><span>ppKrauss</span><br />
<span class="score" title="95 reputation points">95</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppKrauss has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '18, 16:43</strong> </span></p>
</div>
</div>
<div id="comments-container-65405" class="comments-container">
&#10;</div>
<div id="comment-tools-65405" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65405-form-container" class="comment-form-container">
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

<span id="65406"></span>

<div id="answer-container-65406" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65406-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There basically isn't any such data in OSM, so the answer is to get it from official sources rather than from OSM.</p>
<p>I guess there lots of reasons it isn't in OSM, but 2 big ones are that it would be an awful lot of data, and any edits would be likely to decrease the utility of the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '18, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-65406" class="comments-container">
<span id="65407"></span>
<div id="comment-65407" class="comment">
<div id="post-65407-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Max, thanks the explanations. There are an obvious scale difference (and the cost associated to it), but today OSM is managing addresses points and urban lots... Can you explain the differences between <em>rural lots</em>, as an "official boundary" polygon, and the other classic OSM "official boundary" polygons, like the country and city boundaries?</p>
</div>
<div id="comment-65407-info" class="comment-info">
<span class="comment-age">(17 Aug '18, 16:50)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
<span id="65409"></span>
<div id="comment-65409" class="comment">
<div id="post-65409-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think I don't understand "rural lot" well enough to say something. We certainly do not map <em>plots</em> as they are just private boundaries between one person's land and another person's land. But if a <em>rural lot</em> is something like a city neighbourhood, and also used by people on the ground ("I live in lot X") then maybe there are ways to record them. I suggest researching past discussions about "neighbourhoods" on the mailing lists, especially regarding their fuzziness. Unsure if that applies to rural lots as well.</p>
</div>
<div id="comment-65409-info" class="comment-info">
<span class="comment-age">(17 Aug '18, 17:52)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65406" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65406-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

