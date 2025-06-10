+++
type = "question"
title = "Map offset values for Kuala Terengganu, Malaysia? Nothing lines up!"
description = '''Hi, I&#x27;m new to OSM, as you might have seen from my other recent post. I&#x27;m really keen on mapping the city of Kuala Terengganu, Malaysia, as there are a surprisingly large number of roads that are missing. The only up to date and reliable imagery for that area seems to be Esri World (not the Clarity ...'''
date = "2018-04-30T17:02:00Z"
lastmod = "2018-05-06T05:06:00Z"
weight = 63242
keywords = [ "aerial_imagery", "beginner", "offset" ]
aliases = [ "/questions/63242" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Map offset values for Kuala Terengganu, Malaysia? Nothing lines up!](/questions/63242/map-offset-values-for-kuala-terengganu-malaysia-nothing-lines-up)

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
<span id="post-63242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63242-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm new to OSM, as you might have seen from my other recent post. I'm really keen on mapping the city of Kuala Terengganu, Malaysia, as there are a surprisingly large number of roads that are missing. The only up to date and reliable imagery for that area seems to be Esri World (not the Clarity Beta version) Imagery and Digital Globe Standard Imagery. The others are either too old (&gt;5 years old, airport is different) or too low res.</p>
<p>I'm having trouble finding the correct offset to use with the Esri World Imagery. If I line up the main roads near the coast, then the roads west of it seem to be not lining up. If I line up the minor roads towards the south of the city, then the main roads and the buildings at the city centre don't line up exactly. What should I do? Could someone please take a look?</p>
<p>Here is the location: <a href="https://www.openstreetmap.org/#map=14/5.3080/103.1432">https://www.openstreetmap.org/#map=14/5.3080/103.1432</a></p>
<p>Thanks for the help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-aerial_imagery" rel="tag" title="see questions tagged &#39;aerial_imagery&#39;">aerial_imagery</span> <span class="post-tag tag-link-beginner" rel="tag" title="see questions tagged &#39;beginner&#39;">beginner</span> <span class="post-tag tag-link-offset" rel="tag" title="see questions tagged &#39;offset&#39;">offset</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Apr '18, 17:02</strong></p>
<img src="https://secure.gravatar.com/avatar/7d96e20c0642af8e402224dda4bee21d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aaronshenhao&#39;s gravatar image" />
<p><span>aaronshenhao</span><br />
<span class="score" title="66 reputation points">66</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aaronshenhao has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Apr '18, 17:03</strong> </span></p>
</div>
</div>
<div id="comments-container-63242" class="comments-container">
&#10;</div>
<div id="comment-tools-63242" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63242-form-container" class="comment-form-container">
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

<span id="63244"></span>

<div id="answer-container-63244" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63244-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-63244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aaronshenhao has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are some GPX tracks available in the area and a superficial check would indicate that they line up quite good with the existing OSM data (turn on the GPS layer in iD if you are using iD to edit).</p>
<p>Varying offsets in the couple of meters range are normal and now and then you will find an "imagery boundary" with different offsets going right through the area you are trying to map. It's a pain but can't be avoided.</p>
<p>In your case I would use the most current imagery and adjust to the GPX tracks (you can easily improve and generate more of those naturally).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Apr '18, 19:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-63244" class="comments-container">
<span id="63245"></span>
<div id="comment-63245" class="comment">
<div id="post-63245-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>just want to add on this: the offsets in aerial imagery could change continuously (not a hard boundary) over an area. Mostly if there are mountains. Just always use the nearest gps traces and check the alignment.</p>
</div>
<div id="comment-63245-info" class="comment-info">
<span class="comment-age">(30 Apr '18, 21:51)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="63247"></span>
<div id="comment-63247" class="comment">
<div id="post-63247-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Simon for your advice. I aligned the aerial map to the GPS traces within the area, and the majority of OSM roads in the area seem to line up decently. The GPS traces actually lines up quite nicely with the aerial imagery (offset -0.45; 0.60) overall, however there are a number of existing OSM roads (some quite long) that seem misaligned, even though the GPS traces are aligned. Perhaps they were created a long time ago with different imagery sources, so I might try correcting them (hope I'm right).</p>
<p>Luckily, all the OSM data in my hometown in Australia seem to be aligned perfectly to the GPS traces and the aerial map. That city in Malaysia is not a hilly area at all (coastline city), I'm guessing the misaligned roads were done a long time ago.</p>
</div>
<div id="comment-63247-info" class="comment-info">
<span class="comment-age">(01 May '18, 08:17)</span> <span class="comment-user userinfo">aaronshenhao</span>
</div>
</div>
<span id="63339"></span>
<div id="comment-63339" class="comment">
<div id="post-63339-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also take note that the usual practice to map structures - for example, the buildings - are mapped with respect to their bases (which touches the ground), not their roofs.</p>
<p>Confusing, isn't it?</p>
<p>Shameless plug for the Malaysian community forum: <a href="https://forum.openstreetmap.org/viewforum.php?id=60">https://forum.openstreetmap.org/viewforum.php?id=60</a></p>
</div>
<div id="comment-63339-info" class="comment-info">
<span class="comment-age">(06 May '18, 05:06)</span> <span class="comment-user userinfo">AkuAnakTimur</span>
</div>
</div>
</div>
<div id="comment-tools-63244" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63244-form-container" class="comment-form-container">
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

