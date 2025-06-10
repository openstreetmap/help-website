+++
type = "question"
title = "Start JOSM with imagery layers already loaded"
description = '''Every time I invoke JOSM to begin an editing session I must manually load some satellite imagery. I use the same satellite imagery every time; Maxar-Premium, Maxar-Standard, ESRI Clarity, and USGS Topos. Is there a way to start JOSM perhaps with a command string containing these choices as parameter...'''
date = "2020-08-18T05:07:00Z"
lastmod = "2020-08-26T09:16:00Z"
weight = 76176
keywords = [ "josm", "imagery", "startup", "parameters" ]
aliases = [ "/questions/76176" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Start JOSM with imagery layers already loaded](/questions/76176/start-josm-with-imagery-layers-already-loaded)

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
<span id="post-76176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76176-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Every time I invoke JOSM to begin an editing session I must manually load some satellite imagery. I use the same satellite imagery every time; Maxar-Premium, Maxar-Standard, ESRI Clarity, and USGS Topos.</p>
<p>Is there a way to start JOSM perhaps with a command string containing these choices as parameters? I think I've seen the answer to this question in this forum a while ago but cannot find it right now.</p>
<p>Dave</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span> <span class="post-tag tag-link-startup" rel="tag" title="see questions tagged &#39;startup&#39;">startup</span> <span class="post-tag tag-link-parameters" rel="tag" title="see questions tagged &#39;parameters&#39;">parameters</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '20, 05:07</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Aug '20, 05:07</strong> </span></p>
</div>
</div>
<div id="comments-container-76176" class="comments-container">
&#10;</div>
<div id="comment-tools-76176" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76176-form-container" class="comment-form-container">
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

<span id="76177"></span>

<div id="answer-container-76177" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76177-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ah, yes, that is one of the annoying "why was it ever done this way?" things about JOSM.</p>
<p>See <a href="https://labs.mapbox.com/mapping/becoming-a-power-mapper/editing-saving-and-loading-josm-session/">https://labs.mapbox.com/mapping/becoming-a-power-mapper/editing-saving-and-loading-josm-session/</a> for how to create a session configuration file (relatively new feature).</p>
<p>And, found after some experimenting, the session file can be specified on the command line with</p>
<p><code>--download &lt;session file&gt;</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '20, 08:23</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Aug '20, 08:49</strong> </span></p>
</div>
</div>
<div id="comments-container-76177" class="comments-container">
<span id="76178"></span>
<div id="comment-76178" class="comment">
<div id="post-76178-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I thought for a minute this might have answered another JOSM layers question. How to stop JOSM automatically loading the OpenStreetCam and OneWay layers? Anyone have a way to stop the orange spots?</p>
<p>As an addition to the above answer I found that if you centre your JOSM map on your area of interest before saving the session JOSM will next open at that place and zoom level.</p>
</div>
<div id="comment-76178-info" class="comment-info">
<span class="comment-age">(18 Aug '20, 09:14)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
<span id="76179"></span>
<div id="comment-76179" class="comment">
<div id="post-76179-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2925/bcnorwich">@BCNorwich</a> according to the answer to <a href="https://help.openstreetmap.org/questions/70538/disable-josm-overlay-layers">this</a> you need to close the layer using the right click menu rather than the button below the layer list.</p>
</div>
<div id="comment-76179-info" class="comment-info">
<span class="comment-age">(18 Aug '20, 09:49)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="76180"></span>
<div id="comment-76180" class="comment">
<div id="post-76180-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh so easy, I'd just been clicking the trash can/delete button. Many Thanks!</p>
</div>
<div id="comment-76180-info" class="comment-info">
<span class="comment-age">(18 Aug '20, 09:57)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
<span id="76232"></span>
<div id="comment-76232" class="comment">
<div id="post-76232-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry to be so late to reply. I forgot to subscribe.</p>
<p>It looks like it's possible to do what I want but I would prefer to not have the viewport showing any particular area. I want JOSM to open with only the imagery layers loaded and the viewport in the same location as when I quit JOSM in the previous session, which is what it normally does now.</p>
<p>I haven't experimented with this yet but wanted to let you know I'm still interested.</p>
<p>Thank you....</p>
</div>
<div id="comment-76232-info" class="comment-info">
<span class="comment-age">(20 Aug '20, 09:42)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="76308"></span>
<div id="comment-76308" class="comment">
<div id="post-76308-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Strange, my JOSM doesn't have a Sessions submenu in the File menu. It has a Save Session As option but not Load Session. I can still load it by right clicking the session file and using Open With -&gt; JOSM, or passing it as an argument when launching from the shell though.</p>
</div>
<div id="comment-76308-info" class="comment-info">
<span class="comment-age">(26 Aug '20, 08:55)</span> <span class="comment-user userinfo">tguen</span>
</div>
</div>
<span id="76309"></span>
<div id="comment-76309" class="comment not_top_scorer">
<div id="post-76309-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16647/tguen">@tguen</a>: You can use the standard Open dialogue to open sessions. The same you use for opening images, tracks, data files, ...</p>
</div>
<div id="comment-76309-info" class="comment-info">
<span class="comment-age">(26 Aug '20, 09:16)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-76177" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-76177-form-container" class="comment-form-container">
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

