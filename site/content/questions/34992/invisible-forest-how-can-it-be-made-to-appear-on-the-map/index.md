+++
type = "question"
title = "Invisible forest - how can it be made to appear on the map?"
description = '''Hi, some days ago I walked through a wooded area in Ireland, and noticed that the offline map downloaded to my Android device a week earlier didn&#x27;t show the northern half of that forest; when that night I logged in to openstreetmap.org to add it, it was already there. However, the next day, it still...'''
date = "2014-07-19T10:47:00Z"
lastmod = "2014-07-31T11:48:00Z"
weight = 34992
keywords = [ "not_shown", "forest", "multipolygon" ]
aliases = [ "/questions/34992" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Invisible forest - how can it be made to appear on the map?](/questions/34992/invisible-forest-how-can-it-be-made-to-appear-on-the-map)

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
<span id="post-34992-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34992-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34992-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>some days ago I walked through a wooded area in Ireland, and noticed that the offline map downloaded to my Android device a week earlier didn't show the northern half of that forest; when that night I logged in to openstreetmap.org to add it, it was already there.</p>
<p>However, the next day, it still didn't appear in the map - or rather, at different zoom levels, you could see all/nothing/the southern half/the western half.</p>
<p>I waited another day - no change.</p>
<p>So I looked (in Potlatch 2) at the entries for that forest and compared it to others in the area that did show on the map.</p>
<p>The only difference I could see was that the others had a relation Multipolygon/outer, and this one didn't.</p>
<p>So, I added that relation 14 hours ago; as a result, the forest vanished completely from the map at most zoom levels.</p>
<p>I deleted the relation (created with Potlatch) and created a new one in iD 10 hours ago.</p>
<p>This morning, the forest is still not there.</p>
<p>Can someone who knows OSM editing well (which I obviously don't) check what's wrong here?</p>
<p>My "Aenderungssatz" (changeset) is <a href="https://www.openstreetmap.org/changeset/24231492">#24231492</a>, and the northern end of the forest should be around the coordinates 52°03'47.2" (N), -09°32'12.2" (W).</p>
<p><a href="https://www.openstreetmap.org/edit?editor=id#map=16/52.0628/-9.5376">https://www.openstreetmap.org/edit?editor=id#map=16/52.0628/-9.5376</a></p>
<p>EDIT: I just cleared my browser's cache again and went through all zoom levels; the whole forest is visible at zoom level 14; I don't think it was before, so something may indeed be happening, just VERY slowly???</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-not_shown" rel="tag" title="see questions tagged &#39;not_shown&#39;">not_shown</span> <span class="post-tag tag-link-forest" rel="tag" title="see questions tagged &#39;forest&#39;">forest</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jul '14, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/06b2f5d4fa9884ae47333da22b6f2662?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marabu_Too&#39;s gravatar image" />
<p><span>Marabu_Too</span><br />
<span class="score" title="210 reputation points">210</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marabu_Too has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jul '14, 11:19</strong> </span></p>
</div>
</div>
<div id="comments-container-34992" class="comments-container">
<span id="34993"></span>
<div id="comment-34993" class="comment">
<div id="post-34993-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There's a long and detailed explanation of how and when edits show up <a href="/questions/102/i-have-made-edits-but-they-dont-show-up-on-the-map/104">here</a>.</p>
</div>
<div id="comment-34993-info" class="comment-info">
<span class="comment-age">(19 Jul '14, 11:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-34992" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34992-form-container" class="comment-form-container">
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

<span id="35004"></span>

<div id="answer-container-35004" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35004-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-35004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Marabu_Too has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First thing: Check how often the vector maps you use are updated and that you use one created some time <em>after</em> creating/changing a feature in OSM. Even when the vector map is created one or two days after your edit that doesn't mean that this map contains your edit due to possible delays in the tool chain of the map creator.</p>
<p>Second thing: I removed the forest in the south from the MP since there was no need to have it as "outer" in the MP. (<a href="https://www.openstreetmap.org/relation/3360464/history">changeset</a>)</p>
<p>Hint: The <a href="https://www.openstreetmap.org/way/249993611">wood I removed from the MP</a> overlaps lavishly with the landuse=residential North East of it. That's no good mapping style.</p>
<p>Else I didn't see anything which should make the forest disappear from maps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '14, 18:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jul '14, 19:49</strong> </span></p>
</div>
</div>
<div id="comments-container-35004" class="comments-container">
<span id="35029"></span>
<div id="comment-35029" class="comment">
<div id="post-35029-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks - seems to have been a lack of coordination here.</p>
<p>If I understand you correctly, the "southern half" that I saw was actually a second bit of forest in the same place as the one that was missing?</p>
<p>(I didn't draw either, by the way; just noticed that something was wrong.)</p>
<p>I suppose that - for what ever reason - this forest just takes time (electronic trees which will have to grow?) ;-)</p>
<p>On my Android device the forest ist now visible in the online maps provided by Mapquest as well as by Hike&amp;Bike, though not, strangely, in OSM (either on my PC or on my Android device).</p>
<p>We'll just have to wait and see, I suppose.</p>
<p>Kind regards,</p>
<p>Jochen</p>
</div>
<div id="comment-35029-info" class="comment-info">
<span class="comment-age">(20 Jul '14, 19:26)</span> <span class="comment-user userinfo">Marabu_Too</span>
</div>
</div>
<span id="35346"></span>
<div id="comment-35346" class="comment">
<div id="post-35346-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>I just checked again, and the forest which should just reach Victoria Lodge from the east in</p>
<p><a href="https://www.openstreetmap.org/changeset/24444512#map=18/52.06334/-9.53708">https://www.openstreetmap.org/changeset/24444512#map=18/52.06334/-9.53708</a></p>
<p>is STILL not visible.</p>
<p>Surely 12 days is excessively long for such a small area, and it SHOULD by now be visible?</p>
<p>When I noticed that it did not appear on the map 12 days ago (not having drawn it myself), I added a multipolygen relation; this has now been removed again by someone else, but surely that shouldn't prevent it from being visible?</p>
<p>Regards,</p>
<p>Jochen</p>
</div>
<div id="comment-35346-info" class="comment-info">
<span class="comment-age">(31 Jul '14, 10:20)</span> <span class="comment-user userinfo">Marabu_Too</span>
</div>
</div>
<span id="35347"></span>
<div id="comment-35347" class="comment">
<div id="post-35347-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to notice that in <a href="https://www.openstreetmap.org/#map=15/52.0584/-9.5237&amp;layers=Q">MapQuest Open</a> and <a href="https://www.openstreetmap.org/#map=15/52.0584/-9.5237&amp;layers=H">Humanitarian</a> layers the forest is well visible.</p>
</div>
<div id="comment-35347-info" class="comment-info">
<span class="comment-age">(31 Jul '14, 10:40)</span> <span class="comment-user userinfo">NonnEmilia</span>
</div>
</div>
<span id="35348"></span>
<div id="comment-35348" class="comment not_top_scorer">
<div id="post-35348-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Marabu_Too</span>: strange, indeed. It is a closed way (checked with JOSM's validator). It is shown by MQOpen and Humanitarian layers but not the standard one. I tried with <span>/dirty</span>, but no success. Not sure what's wrong here. At least I can confirm your observations. ;-)</p>
</div>
<div id="comment-35348-info" class="comment-info">
<span class="comment-age">(31 Jul '14, 10:44)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="35350"></span>
<div id="comment-35350" class="comment not_top_scorer">
<div id="post-35350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It coming back <a href="https://www.openstreetmap.org/#map=18/52.06341/-9.53747">https://www.openstreetmap.org/#map=18/52.06341/-9.53747</a></p>
</div>
<div id="comment-35350-info" class="comment-info">
<span class="comment-age">(31 Jul '14, 11:07)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="35351"></span>
<div id="comment-35351" class="comment not_top_scorer">
<div id="post-35351-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>at nevw:</p>
<p>you're right - it's there in several zoom levels; probably just wanted a bit of attention! ;-)</p>
</div>
<div id="comment-35351-info" class="comment-info">
<span class="comment-age">(31 Jul '14, 11:13)</span> <span class="comment-user userinfo">Marabu_Too</span>
</div>
</div>
<span id="35352"></span>
<div id="comment-35352" class="comment">
<div id="post-35352-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>....or is your "Added one node" responsible for this?</p>
</div>
<div id="comment-35352-info" class="comment-info">
<span class="comment-age">(31 Jul '14, 11:15)</span> <span class="comment-user userinfo">Marabu_Too</span>
</div>
</div>
<span id="35354"></span>
<div id="comment-35354" class="comment">
<div id="post-35354-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't know but the same thing happened to another mapper and I added a couple of nodes and saved and it did the trick then too. Sometimes things just get hung up for whatever reason I guess and just need an extra push. I don't know if I helped or it was just umpteen people dirtying the tiles that did the trick. ???</p>
</div>
<div id="comment-35354-info" class="comment-info">
<span class="comment-age">(31 Jul '14, 11:20)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="35359"></span>
<div id="comment-35359" class="comment not_top_scorer">
<div id="post-35359-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's certainly worth keeping in mind for a similar case; thanks anyhow!</p>
</div>
<div id="comment-35359-info" class="comment-info">
<span class="comment-age">(31 Jul '14, 11:48)</span> <span class="comment-user userinfo">Marabu_Too</span>
</div>
</div>
</div>
<div id="comment-tools-35004" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-35004-form-container" class="comment-form-container">
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

