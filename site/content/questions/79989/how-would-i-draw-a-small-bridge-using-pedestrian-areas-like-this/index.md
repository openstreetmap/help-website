+++
type = "question"
title = "How would I draw a small bridge using pedestrian areas like this?..."
description = '''I&#x27;m at a bit of a loss for how to draw this feature correctly...   I have been using highway=pedestrian area=yes to draw a promenade area because that seemed like the semantically correct method for a wide pedestrian space, but now I&#x27;m wondering if that was a mistake? I&#x27;m fairly new to this so any a...'''
date = "2021-05-04T18:13:00Z"
lastmod = "2021-05-05T20:21:00Z"
weight = 79989
keywords = [ "bridge", "pedestrian", "layer", "area" ]
aliases = [ "/questions/79989" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How would I draw a small bridge using pedestrian areas like this?...](/questions/79989/how-would-i-draw-a-small-bridge-using-pedestrian-areas-like-this)

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
<span id="post-79989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79989-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm at a bit of a loss for how to draw this feature correctly...</p>
<p><img src="/upfiles/bandstand_AqRD44U.png" title="multi-level area" alt="multi-level area" /></p>
<p>I have been using <code>highway=pedestrian area=yes</code> to draw a promenade area because that seemed like the semantically correct method for a wide pedestrian space, but now I'm wondering if that was a mistake? I'm fairly new to this so any advice would be very welcome.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '21, 18:13</strong></p>
<img src="https://secure.gravatar.com/avatar/cdd55e49ba7330a60898d23d12de9f13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Foomandoonian&#39;s gravatar image" />
<p><span>Foomandoonian</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Foomandoonian has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-79989" class="comments-container">
&#10;</div>
<div id="comment-tools-79989" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79989-form-container" class="comment-form-container">
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

<span id="79990"></span>

<div id="answer-container-79990" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79990-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm guessing this is the Brighton Bandstand at <a href="https://www.openstreetmap.org/way/96655710">https://www.openstreetmap.org/way/96655710</a>? (Full disclosure -- this building was a little jagged and I just uploaded a changeset to make it into a regular octogon.)</p>
<p><em>[Answer has been edited to reflect info from the comments below -- thanks <a href="https://help.openstreetmap.org/users/8189/alester"></a><a href="https://help.openstreetmap.org/users/8189/alester">@alester</a></a> <a href="https://help.openstreetmap.org/users/16887/kovoschiz"></a><a href="https://help.openstreetmap.org/users/16887/kovoschiz">@Kovoschiz</a></a> and <a href="https://help.openstreetmap.org/users/647/sk53"></a><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a></a> for the insights!]</em></p>
<p>For the bridge, I'd probably use a linear <code>highway=footway</code> + <code>bridge=yes</code> + <code>layer=1</code> without any area tags. I don't think it's necessary to map the exact extent of the bridge, but if I wanted to I'd add a separate polygon tagged with <code>man_made=bridge</code> and <code>layer=1</code>. If <a href="https://live.staticflickr.com/8338/8186906204_0602cf87f7_b.jpg">this picture</a> is correct, it looks like there are steps leading up to the bridge, so I'd add a short way from the upper promenade to the <code>highway=footway</code> bridge and tag that with <code>highway=steps</code> + <code>incline=up</code> + <code>layer=1</code>. (You might even consider the steps part of the bridge, and if so they'd get the <code>bridge=yes</code> tag as well.)</p>
<p>I'd also use an octagonal linear footway to indicate the walking area around the bandstand, on the cafe roof. Mapping this as an area in addition or instead would also be possible, but I don't feel that it qualifies for <code>highway=pedestrian</code> since it doesn't appear suitable for any kind of emergency or delivery vehicular traffic.</p>
<p>As discussed in the comments below, it's possible to map a 2-D "foot area" as either <code>=footway</code> or <code>=pedestrian</code>, and one might well be more correct than the other in a particular situation, but <code>pedestrian</code> has long had a leg up (heh) because it's a programmed preset in iD.</p>
<p>Furthermore, there's a distinction between <strong>omnidirectional highway areas</strong> for mapping plazas and other situations where traffic can go anywhere and might enter and exit at a variety of locations, and <strong>linear highway areas</strong> for adding shape and width details to an already-mapped one-way or two-way linear highway. The omnidirectional areas should get two tags -- <code>highway=*</code> + <code>area=yes</code> -- and the linear areas should be drawn around the existing <code>highway=*</code> way and just be tagged <code>area:highway=*</code>. IMO either of these area methods could be used for the cafe roof, but neither is necessary. The area around the lower cafe level looks like omnidirectional pedestrian to me, and the bridge and upper promenade look like linear ways that could optionally be augmented with a separate <code>area:highway=*</code> way.</p>
<p>Whatever method you ultimately choose, take care that your upper and lower highways don't share any nodes, or routing software might send people jumping off the bandstand level to the cafe below instead of using the steps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '21, 20:43</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 May '21, 15:17</strong> </span></p>
</div>
</div>
<div id="comments-container-79990" class="comments-container">
<span id="79992"></span>
<div id="comment-79992" class="comment">
<div id="post-79992-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, thank you. I will try to make sense of that when I get back to my drawing tonight.</p>
<p>And yeah, my work that I haven't uploaded yet already includes a better octagon, so it'll be interesting to see what happens when I save! Most of the building shapes have been very rough and I'm improving them all as I progress east.</p>
</div>
<div id="comment-79992-info" class="comment-info">
<span class="comment-age">(04 May '21, 21:34)</span> <span class="comment-user userinfo">Foomandoonian</span>
</div>
</div>
<span id="79994"></span>
<div id="comment-79994" class="comment">
<div id="post-79994-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A foot area where vehicle traffic never travels (or is only accessed rarely by authorized service vehicles) could be mapped as <code>highway=footway</code> + <code>area=yes</code></p>
</div>
<div id="comment-79994-info" class="comment-info">
<span class="comment-age">(04 May '21, 23:56)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="79995"></span>
<div id="comment-79995" class="comment">
<div id="post-79995-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/20163/foomandoonian">@Foomandoonian</a> Ah sorry about that, my octagon compulsive disorder got the best of me. I didn't add or delete anything, just re-aligned the nodes, so it shouldn't be too much of a pain. It looks like you're mapping with iD, so you should just be able to select "Keep mine" (mine meaning yours) to overwrite my changes when you save.</p>
<p><a href="https://help.openstreetmap.org/users/8189/alester">@alester</a> Yep that makes sense. Haven't seen it used much but scouting around on Overpass I see that it's actually more common than I thought. But highway=pedestrian still appears to be far more common. I think one reason is that polygonal footway areas are very often called "pedestrian areas" IRL, and another is that it's rare to find one that doesn't have <em>some</em> allowance for emergency or delivery traffic.</p>
</div>
<div id="comment-79995-info" class="comment-info">
<span class="comment-age">(05 May '21, 01:11)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="79998"></span>
<div id="comment-79998" class="comment">
<div id="post-79998-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We have linear <code>area:highway=footway</code> and omnidirectional <code>highway=footway</code> + <code>area=yes</code>. "Pedestrian area" is caused by the ambiguous iD preset name seemingly not considering the definition of <code>=pedestrian</code>.</p>
</div>
<div id="comment-79998-info" class="comment-info">
<span class="comment-age">(05 May '21, 08:52)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="80000"></span>
<div id="comment-80000" class="comment">
<div id="post-80000-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16887/kovoschiz">@Kovoschiz</a> highway=pedestrian + area=yes has a long usage for mapping the areas of footways. I would agree this is not absolutely correct, and at a minimum they can be changed to highway=footway + area=yes without losing their ability to be rendered.</p>
</div>
<div id="comment-80000-info" class="comment-info">
<span class="comment-age">(05 May '21, 10:35)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="80008"></span>
<div id="comment-80008" class="comment not_top_scorer">
<div id="post-80008-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks folks, I've edited my answer to incorporate your insights.</p>
</div>
<div id="comment-80008-info" class="comment-info">
<span class="comment-age">(05 May '21, 15:07)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="80013"></span>
<div id="comment-80013" class="comment not_top_scorer">
<div id="post-80013-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53"></a><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a> At the very least, the situation is worsened by using a preset name not carefully thought about, regardless of what common terminology may be. When created in 2007, <a href="https://wiki.openstreetmap.org/w/index.php?title=Tag:highway=pedestrian&amp;oldid=55318">https://wiki.openstreetmap.org/w/index.php?title=Tag:highway=pedestrian&amp;oldid=55318</a> already has "Vehicles may be allowed in", "The "footpath" tag seems a bit inappropriate for such things.", and "a pedestrianised road".</p>
</div>
<div id="comment-80013-info" class="comment-info">
<span class="comment-age">(05 May '21, 19:16)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="80014"></span>
<div id="comment-80014" class="comment not_top_scorer">
<div id="post-80014-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@Kovoshiz I happen to agree with you, I am merely commenting on what actually happens, not what I would like to happen :-)</p>
</div>
<div id="comment-80014-info" class="comment-info">
<span class="comment-age">(05 May '21, 20:21)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-79990" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-79990-form-container" class="comment-form-container">
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

