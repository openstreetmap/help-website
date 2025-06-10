+++
type = "question"
title = "Help: I have made the coastline of Tonga unrenderable!"
description = '''Last night I tried to get advanced by creating a series of relationships to better define a coastline and some corresponding tidal flats/mangroves and now none of it is rendering in the Mapnik. The area is here: http://www.openstreetmap.org/#map=15/-21.1465/-175.1545 I started by making a relation b...'''
date = "2014-11-15T05:18:00Z"
lastmod = "2014-11-24T20:51:00Z"
weight = 38569
keywords = [ "tonga", "wetlands", "coastline", "tongatapu" ]
aliases = [ "/questions/38569" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Help: I have made the coastline of Tonga unrenderable!](/questions/38569/help-i-have-made-the-coastline-of-tonga-unrenderable)

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
<span id="post-38569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38569-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Last night I tried to get advanced by creating a series of relationships to better define a coastline and some corresponding tidal flats/mangroves and now none of it is rendering in the Mapnik. The area is here: <a href="http://www.openstreetmap.org/#map=15/-21.1465/-175.1545">http://www.openstreetmap.org/#map=15/-21.1465/-175.1545</a></p>
<p>I started by making a relation between the mainland and the nearby islet since they are locally regarded as one in the same, being separated only by the tidal mudflats. After this, I tried to replicate some tagging/relationships I had seen in Australia where one boundary of the mangroves is defined by the coastline way and the other by a wetland way. Somewhere along the way, this hasn't worked out properly and I'm not sure the right way to fix it and get the result I was looking for.</p>
<p>If someone can have a look at this for me and point out where I went wrong and how I can fix it I would be very happy.</p>
<p>Malo</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tonga" rel="tag" title="see questions tagged &#39;tonga&#39;">tonga</span> <span class="post-tag tag-link-wetlands" rel="tag" title="see questions tagged &#39;wetlands&#39;">wetlands</span> <span class="post-tag tag-link-coastline" rel="tag" title="see questions tagged &#39;coastline&#39;">coastline</span> <span class="post-tag tag-link-tongatapu" rel="tag" title="see questions tagged &#39;tongatapu&#39;">tongatapu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '14, 05:18</strong></p>
<img src="https://secure.gravatar.com/avatar/ce32dca798cb9a859435d42700c4b880?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Loau&#39;s gravatar image" />
<p><span>Loau</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Loau has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38569" class="comments-container">
&#10;</div>
<div id="comment-tools-38569" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38569-form-container" class="comment-form-container">
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

<span id="38572"></span>

<div id="answer-container-38572" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38572-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have made an attempt at fixing the errors by reviewing the data and introducing a number of multipolygons, and removing some spurious multipolygon relations with JOSM validation errors (e.g. unclosed). I hope I did this correct, but it may take some while before the new rendering shows up and it can be verified. There were still a lot of JOSM validation errors for features on the Tonga island, a few of which I have fixed, but no errors for the coastline if I am right.</p>
<p>For the type of edits you attempt to do, you really need JOSM and its build in validator. In addition, if you want to "re-use" a coastline as part of a wetland, you will need to split the coastline where the wetland polygon outline touches the coastline (use the "P" letter shortcut for this, you need to select the two nodes first at both ends of the "wetland" outline where it touches the coastline, then hit "P" on your keyboard). You can then define multipolygons for BOTH the coastline AND the wetland, both of which should incorporate the single split line of the coastline.</p>
<p>After defining the multipolygon relations and adding the line elements to it, it is good practice to remove the tags from the outer ways, and only add them to the multipolygon. So the multipolygon should have the "natural=wetland", "wetland=tidalflat" tags, not the outer ways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '14, 09:06</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Nov '14, 13:43</strong> </span></p>
</div>
</div>
<div id="comments-container-38572" class="comments-container">
<span id="38573"></span>
<div id="comment-38573" class="comment">
<div id="post-38573-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>A quick reminder that coastline changes don't take effect as quickly as other ones. I believe they now update daily. You can check the land polygon dates at <a href="http://tile.openstreetmap.org/cgi-bin/debug">http://tile.openstreetmap.org/cgi-bin/debug</a> to see how recently they were updated (not sure how long before the time shown the files are generated though).</p>
</div>
<div id="comment-38573-info" class="comment-info">
<span class="comment-age">(15 Nov '14, 09:51)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="38589"></span>
<div id="comment-38589" class="comment">
<div id="post-38589-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/339/edloach">@EdLoach</a>: from <a href="/questions/38437/lost-image-of-bengkalis-island">there</a> I know that it took from 11 Nov, 12:29 to about 15 Nov 13:45 to show a coastline change (on tiles zoom level 13+ – smaller is not updated yet).</p>
</div>
<div id="comment-38589-info" class="comment-info">
<span class="comment-age">(16 Nov '14, 00:39)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="38590"></span>
<div id="comment-38590" class="comment">
<div id="post-38590-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the help. It might be time to upgrade to the more powerful editor in JOSM. The simplicity of iD got me into it in the first place. According the the link <a href="http://help.openstreetmap.org/users/339/edloach">@EdLoach</a> it looks like coastlines haven't been rendered since Friday sometime, I'm still waiting for the island to return to the mapnik, but will advise when if it doesn't return. I must have made the changes right before render time since it disappeared pretty soon after.</p>
<p>Thanks again.</p>
<p>Malo.</p>
</div>
<div id="comment-38590-info" class="comment-info">
<span class="comment-age">(16 Nov '14, 03:43)</span> <span class="comment-user userinfo">Loau</span>
</div>
</div>
<span id="38738"></span>
<div id="comment-38738" class="comment">
<div id="post-38738-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="http://help.openstreetmap.org/users/9580/mboeringa">@mboeringa</a></p>
<p>I see your extra work to get the tags right and the coastline rendering, thanks very much. It was rendering properly at some of the larger zoom levels, I guess it's a matter of time before the others render properly now too.</p>
<p>Is it possible that coastlines made up of relations take significantly longer to render than those that are made up of just a closed way?</p>
<p>Malo.</p>
</div>
<div id="comment-38738-info" class="comment-info">
<span class="comment-age">(24 Nov '14, 05:43)</span> <span class="comment-user userinfo">Loau</span>
</div>
</div>
<span id="38757"></span>
<div id="comment-38757" class="comment">
<div id="post-38757-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Malo,</p>
<p>Actually, I was starting to doubt my own work. At first, after my edits, I actually saw the remainders of the tiles showing the island disappearing... Only now, 8(!) days after edits, seem new tiles to come up at zoomlevels 13 and 14, like you also noted. So yes, I think we still need to wait longer for proper rendering. You may be right the coastlines based on relationships taking longer, but I am not sure, it may be just a cause of the general backlog in rendering.</p>
<p>Marco</p>
</div>
<div id="comment-38757-info" class="comment-info">
<span class="comment-age">(24 Nov '14, 20:51)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
</div>
<div id="comment-tools-38572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38572-form-container" class="comment-form-container">
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

