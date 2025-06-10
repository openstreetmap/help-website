+++
type = "question"
title = "Circular river-lines vs. river-/lake-areas"
description = '''River-lines (waterway=river), per definition, should never be circular (simple closed polygons). Yet, there are thousands of them in some strange combination with river and lake areas. These lines usually form a long thin polygonal shape, sometimes overlapping lake and/or river area borders but ofte...'''
date = "2015-05-10T20:05:00Z"
lastmod = "2015-05-29T18:14:00Z"
weight = 43003
keywords = [ "river", "lines", "circular" ]
aliases = [ "/questions/43003" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Circular river-lines vs. river-/lake-areas](/questions/43003/circular-river-lines-vs-river-lake-areas)

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
<span id="post-43003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43003-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>River-lines (waterway=river), per definition, should never be circular (simple closed polygons). Yet, there are thousands of them in some strange combination with river and lake areas. These lines usually form a long thin polygonal shape, sometimes overlapping lake and/or river area borders but often with no matching objects in the mentioned area classes. While in the raster map-making these lines doesn’t matter too much (eventually some area brakes, strange name positioning…) in the vector map-making it does. Note that a very similar case we have with the canal-lines vs. canal areas. So, my question is:<br />
Is there any OSM data preparation tool that uses these circular river-/canal-lines for (vector) data corrections?<br />
I would be thankful for any references. Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span> <span class="post-tag tag-link-lines" rel="tag" title="see questions tagged &#39;lines&#39;">lines</span> <span class="post-tag tag-link-circular" rel="tag" title="see questions tagged &#39;circular&#39;">circular</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 May '15, 20:05</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-43003" class="comments-container">
<span id="43006"></span>
<div id="comment-43006" class="comment">
<div id="post-43006-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Do you have any examples</p>
</div>
<div id="comment-43006-info" class="comment-info">
<span class="comment-age">(10 May '15, 23:11)</span> <span class="comment-user userinfo">DaCor</span>
</div>
</div>
<span id="43009"></span>
<div id="comment-43009" class="comment">
<div id="post-43009-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Of course. Otherwise I would never write/asked something like I did. If you want, you can get the shp files with large number of cases (7536) from the dump from some weeks ago. In my experience, changes/corrections there go pretty slow.</p>
</div>
<div id="comment-43009-info" class="comment-info">
<span class="comment-age">(11 May '15, 09:55)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
<span id="43010"></span>
<div id="comment-43010" class="comment">
<div id="post-43010-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>A link to a circular river way in OSM would be useful.</p>
</div>
<div id="comment-43010-info" class="comment-info">
<span class="comment-age">(11 May '15, 09:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="43037"></span>
<div id="comment-43037" class="comment">
<div id="post-43037-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If I understand correctly, the question is about what Osmosis calls "Closed waterways":</p>
<p><a href="http://osmose.openstreetmap.fr/en/errors/?item=1220&amp;class=12200">http://osmose.openstreetmap.fr/en/errors/?item=1220&amp;class=12200</a></p>
<p>Some are just bad NHD imports:</p>
<p><a href="http://www.openstreetmap.org/way/38672004#map=18/34.32973/-77.71119">http://www.openstreetmap.org/way/38672004#map=18/34.32973/-77.71119</a></p>
<p>A few I looked at were ditches:</p>
<p><a href="http://www.openstreetmap.org/way/238797117">http://www.openstreetmap.org/way/238797117</a></p>
</div>
<div id="comment-43037-info" class="comment-info">
<span class="comment-age">(12 May '15, 22:13)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="43038"></span>
<div id="comment-43038" class="comment not_top_scorer">
<div id="post-43038-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not quite. The question was about using these anomalies to correct the vector data in a data preparation chain. There were questions about examples. Your list shows many, thanks. I have also uploaded many thousands to my G-repository for the interested here: <a href="https://drive.google.com/open?id=0B6qGm3k2qWHqflNLZmFhN1diUW5uTkphSVM5aUFnX2lsZUJpcVplT29aaEQwMkFjMWJZbkk&amp;authuser=0.">https://drive.google.com/open?id=0B6qGm3k2qWHqflNLZmFhN1diUW5uTkphSVM5aUFnX2lsZUJpcVplT29aaEQwMkFjMWJZbkk&amp;authuser=0.</a> If interested, please start with the "Circular_river_lines.docx". Thanks.</p>
</div>
<div id="comment-43038-info" class="comment-info">
<span class="comment-age">(13 May '15, 07:22)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
<span id="43046"></span>
<div id="comment-43046" class="comment">
<div id="post-43046-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/3194/sanser">@sanser</a> that document has lots of text and pictures but no links. Can you provide a link to a circular waterway=river in OSM (preferably to the one of the ways, like maxerickson did above)? The "osmose" issues seem to be a mix of false positives (osmose not understanding the tagging), circular parts of drainage networks with no obvious direction, and simple tagging errors.</p>
</div>
<div id="comment-43046-info" class="comment-info">
<span class="comment-age">(13 May '15, 15:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="43059"></span>
<div id="comment-43059" class="comment not_top_scorer">
<div id="post-43059-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>one of the first in the document is the river ways around the island linked in maxerickson's answer (<a href="http://www.openstreetmap.org/way/89569937)">http://www.openstreetmap.org/way/89569937)</a></p>
</div>
<div id="comment-43059-info" class="comment-info">
<span class="comment-age">(13 May '15, 16:26)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="43067"></span>
<div id="comment-43067" class="comment not_top_scorer">
<div id="post-43067-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's a riverbank, not a river. One of the river ways there is not circular:</p>
<p><a href="http://www.openstreetmap.org/way/30587867">http://www.openstreetmap.org/way/30587867</a></p>
</div>
<div id="comment-43067-info" class="comment-info">
<span class="comment-age">(13 May '15, 17:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="43070"></span>
<div id="comment-43070" class="comment not_top_scorer">
<div id="post-43070-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>which is why I said "river ways around the island". sorry, should've not been lazy and linked directly to those ways (3215427 and 48856760 on the north side, 30587867 on the south)</p>
</div>
<div id="comment-43070-info" class="comment-info">
<span class="comment-age">(13 May '15, 18:45)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-43003" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-43003-form-container" class="comment-form-container">
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

<span id="43042"></span>

<div id="answer-container-43042" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43042-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>waterway=riverbank should generally be an area tag, here is the missing island from one of your early examples:</p>
<p><a href="http://www.openstreetmap.org/way/89569937">http://www.openstreetmap.org/way/89569937</a></p>
<p>It appears to be the same object as your anomaly.</p>
<p>The riverbank has the tags on the outer part of the multipolygon, which is maybe deprecated, but you will want to interpret it correctly:</p>
<p><a href="http://www.openstreetmap.org/relation/1321026">http://www.openstreetmap.org/relation/1321026</a></p>
<p>The surrounding waterway=river ways look like they make sense.</p>
<p>It is also the case that a long thin area might be correctly tagged as natural=water.</p>
<p>I think if you account for waterway=riverbank being an area, many of your anomalies will go away. I fear many of the remaining anomalies will be more nonsense than anything else (of course depending on what you have included as anomalous).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 May '15, 13:07</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-43042" class="comments-container">
<span id="43296"></span>
<div id="comment-43296" class="comment">
<div id="post-43296-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What makes sense or don't depend on the criteria and criteria is subjective (somebodies). When a river-line is circular, surrounding a lake area object, between two river-area sections (even aving "river" in the name) to me makes sense to call it for anomaly but probably not to you. But my question/help-request was something totally different. If you have time, you can find some more/new notes under P.S. in the referenced document.</p>
</div>
<div id="comment-43296-info" class="comment-info">
<span class="comment-age">(28 May '15, 23:11)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
</div>
<div id="comment-tools-43042" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43042-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43043"></span>

<div id="answer-container-43043" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43043-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you're misunderstanding <a href="http://wiki.openstreetmap.org/wiki/Tag:waterway%3Driver">waterway=river</a>. These are vector lines representing the channel of a waterway, so they might be traced to go on both sides of an island. If the direction of one of these ways was opposite, I could understand thinking of them as circular, but since they both head "downstream," that makes topological sense and follows OSM practice.</p>
<p>As pointed out separately, the island is accurately modeled in the waterway=riverbank version of the Thames.</p>
<p>I'm not sure how you're doing your analysis, but it might be convenient to use river's waterway relations when they exist, such as <a href="https://www.openstreetmap.org/relation/2263653">https://www.openstreetmap.org/relation/2263653</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 May '15, 15:13</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-43043" class="comments-container">
<span id="43297"></span>
<div id="comment-43297" class="comment">
<div id="post-43297-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I believe it is more a misunderstanding between us than what you have suggested about such a simple/basic notion as the riverline. Essentially, my question was related to something else, as you could see. But, you have a point regarding the analyses and the riverline relations. I have added some more/new notes under P.S. in the referenced document. These notes are related to your two points but also to some earlier useful comments. If you or others are still interested in the circular river-/canal-lines you are welcome to revisit the document.</p>
</div>
<div id="comment-43297-info" class="comment-info">
<span class="comment-age">(28 May '15, 23:11)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
<span id="43313"></span>
<div id="comment-43313" class="comment">
<div id="post-43313-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Your document is really long and dense--I think you'll have better luck getting help if you can summarize your issue so that it is clear. For example, "the data seems incorrect at this place for this reason". Or, "when I try to render the data at this place in this way, I am having these problems". I'm sorry but I'm not going to read pages and pages.</p>
</div>
<div id="comment-43313-info" class="comment-info">
<span class="comment-age">(29 May '15, 16:15)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="43315"></span>
<div id="comment-43315" class="comment">
<div id="post-43315-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>FWIW I tried reading "pages and pages" but communication did not occur.</p>
</div>
<div id="comment-43315-info" class="comment-info">
<span class="comment-age">(29 May '15, 16:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="43320"></span>
<div id="comment-43320" class="comment">
<div id="post-43320-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I just tried reading the "pages and pages" again, and I think the question is really, "How should my vector renderer deal with incorrectly-mapped waterways?" There's a ton of other stuff in there, though, so it's nearly impossible to decipher an actual question.</p>
</div>
<div id="comment-43320-info" class="comment-info">
<span class="comment-age">(29 May '15, 18:14)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-43043" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43043-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43319"></span>

<div id="answer-container-43319" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43319-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It still isn't clear what exactly you're asking. If you're asking if closed-way waterway=river is correct tagging or not, the answer is that in most cases (if not all) it would not be correct tagging. The same would apply to the other waterway classes which are assumed to always flow in a single direction (stream, brook). If you know of incorrectly mapped waterway=river, stream, or brook, the answer is to fix the data. If there are a lot of them, it could be a candidate for a <a href="http://maproulette.org/">MapRoulette</a> challenge.</p>
<p>Drains and ditches often don't have a flow-direction and mapping them as closed ways is common.</p>
<p>Canals are a grey area that could go either way but could conceivably exist in a closed loop.</p>
<p>A closed way of any of the above waterway=* values should never be interpreted as an area. They are always vector ways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '15, 17:11</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-43319" class="comments-container">
&#10;</div>
<div id="comment-tools-43319" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43319-form-container" class="comment-form-container">
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

