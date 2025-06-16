+++
type = "question"
title = "Tag / rendering problems..."
description = '''Hi, I&#x27;m new to OSM and still on a learning curve so please bear with me. I&#x27;ve been editing the Salcombe Estuary area (South Devon, UK). The tidal area north of Snapes Point has already been edited by another local user to denote it as mudflats. This area I&#x27;ve added in areas around Southpool Creek an...'''
date = "2015-10-06T18:48:00Z"
lastmod = "2015-10-06T21:34:00Z"
weight = 45758
keywords = [ "rendering", "tags" ]
aliases = [ "/questions/45758" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tag / rendering problems...](/questions/45758/tag-rendering-problems)

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
<span id="post-45758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45758-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm new to OSM and still on a learning curve so please bear with me.</p>
<p>I've been editing the Salcombe Estuary area (South Devon, UK). The tidal area north of Snapes Point has already been edited by another local user to denote it as mudflats. <a href="https://www.openstreetmap.org/#map=15/50.2331/-3.7489">This area</a></p>
<p>I've added in areas around Southpool Creek and Batson Creek to reflect the tidal mudflats there too. I used natural=mud and surface=mud, plus tidal=yes for the area, and it shows up in the OSM viewer as dark blue dashes over light blue water, which is what I was expecting. (It looks different than the previous areas north of Snapes Point because the other chap put his riverbank at the low tide mark, and I left mine at the high tide mark, but that's not too important right now.)</p>
<p>So far so good. So then I tried to add in the sandy tidal area south of Ditch End (east bank) and Fort Charles (west bank). I created areas up as far as the existing beaches and set natural=beach and surface=sand, plus tidal=yes. I generally used the Administrative Boundary as a decent approximation of the low tide line, and the riverbank as an approximation of the high tide line.</p>
<p>However, these areas still render just as water. Not only that, but the existing beaches (North Sands, Mill Bay, Smalls Cove etc), which WERE rendering as yellow sand, are now rendering as water. I can't understand this as I haven't changed the riverbank at all.</p>
<p>I'd be grateful if somebody could point me in the right direction on this one as I can't work out how to fix it! It <em>should</em> show the beaches as sand up from the high tide mark, and ideally something to denote tidal sand below the high tide mark. That's what I was trying to achieve, anyway.</p>
<p>Thanks, David</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Oct '15, 18:48</strong></p>
<img src="https://secure.gravatar.com/avatar/76659c40e70586672ac3c1dd625fec94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20R%20French&#39;s gravatar image" />
<p><span>David R French</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David R French has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Oct '15, 18:52</strong> </span></p>
</div>
</div>
<div id="comments-container-45758" class="comments-container">
&#10;</div>
<div id="comment-tools-45758" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45758-form-container" class="comment-form-container">
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

<span id="45762"></span>

<div id="answer-container-45762" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45762-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>David, it helps when you give a particular polygon as below, you can click these if you switch on the data layer on the main website. It seems you refer to ways like this: <a href="https://www.openstreetmap.org/way/156118757">https://www.openstreetmap.org/way/374132785</a> which is tagged natural=beach, surface=sand, and a bit of the beach rendering is lurking at the eastern side. It is also tagged type=multipolygon which only belongs on relations, not on ways.</p>
<p>This beach area is mostly overlapped with this way <a href="https://www.openstreetmap.org/way/146605238">https://www.openstreetmap.org/way/146605238</a> tagged as riverbank.</p>
<p>The renderer paints the map in layers, so apparently the natural tag first, the waterway later, thus most of your beach gets covered by the water. Symbols and names follow on top.</p>
<p>Another of your beaches has a name, so you see 'North sands' named on the map, but only a tiny stripe lurking north-east.</p>
<p>The solution for you should probably be to separate (i.e. not overlap) the polygons and tag them individually.</p>
<p>Please also note that not everything that can be tagged is also rendered, for technical and style reasons.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Oct '15, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/2d01b00413bb205c1735dde9a3b32c4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="P24&#39;s gravatar image" />
<p><span>P24</span><br />
<span class="score" title="154 reputation points">154</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="P24 has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-45762" class="comments-container">
<span id="45764"></span>
<div id="comment-45764" class="comment">
<div id="post-45764-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi. Thanks for taking the time to look into this. Your answer mostly makes sense, but I'm left wondering why the beaches were rendering OK before I added the tidal polygon adjacent to it, but adding the polygon seems to have made the water render over the beach up to the riverbank.</p>
<p>So I need to move the riverbank way; procedurally how do I do this in iD given it shares dozens of nodes with the beach and other features? I'm familiar with clicking on a node and selecting "Separate these lines / areas from each other", but presumably there's a faster way of doing this than repeating that for each of the shared nodes?</p>
<p>In a way I'd rather leave the riverbank where it was; it marks the high tide point, and some of the beaches (e.g. North Sands) are covered at high water, but traditionally are shown in their low tide state on maps (otherwise there would be no beach on the map!) If I could go back to having the beach render over the water I'd like to do that, which it was doing before I added the adjacent intertidal area.</p>
<p>My type=multipolygon arose from copying tags from similar areas elsewhere... I won't do that again without knowing what they mean :)</p>
<p>Thanks again for your help. David</p>
</div>
<div id="comment-45764-info" class="comment-info">
<span class="comment-age">(06 Oct '15, 21:34)</span> <span class="comment-user userinfo">David R French</span>
</div>
</div>
</div>
<div id="comment-tools-45762" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45762-form-container" class="comment-form-container">
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

