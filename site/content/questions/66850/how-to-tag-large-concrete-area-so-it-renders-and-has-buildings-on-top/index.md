+++
type = "question"
title = "How to tag large concrete area so it renders and has buildings on top?"
description = '''Hi All, I&#x27;m having some issues getting disused airfield runways to show in the renderer. They are often used as highways, footpaths or are used for various sundry other uses. Being large visible areas I want to include them in the map but simply tag them in a way that has the map render them but acc...'''
date = "2018-11-19T16:13:00Z"
lastmod = "2023-02-07T14:29:00Z"
weight = 66850
keywords = [ "concrete", "runway", "disused", "area" ]
aliases = [ "/questions/66850" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag large concrete area so it renders and has buildings on top?](/questions/66850/how-to-tag-large-concrete-area-so-it-renders-and-has-buildings-on-top)

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
<span id="post-66850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66850-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I'm having some issues getting disused airfield runways to show in the renderer. They are often used as highways, footpaths or are used for various sundry other uses. Being large visible areas I want to include them in the map but simply tag them in a way that has the map render them but accurately reflects the fact they are just big areas of open concrete.</p>
<p>I originally tired marking them as disused:aeroway=runway but anything disused doesn't get rendered so I reverted to simply adding a centre line marking it as such and then defining the area the concrete takes up. <a href="https://www.openstreetmap.org/way/645833648#map=17/51.67018/-1.83741&amp;layers=D">(Area in Question)</a></p>
<p>I tried tagging them as area=yes/area:highway=unclassified/highway=unclassified to denote the fact they are used for vehicular access but as a "road" don't fit any pre-defined classification.</p>
<p>This works, but the buildings that are build upon part render below the concrete area which I understand it because it's defined as a a highway and thus always gets rendered on top.</p>
<p>So my question is:</p>
<p>a) Is there a better set of area:* tags I can use to define large areas of concrete that should be rendered on the map? b) If I should use area:highway, I believe I can make the buldings "part" of the area so they rendered above? How should I set-up the relationship?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-concrete" rel="tag" title="see questions tagged &#39;concrete&#39;">concrete</span> <span class="post-tag tag-link-runway" rel="tag" title="see questions tagged &#39;runway&#39;">runway</span> <span class="post-tag tag-link-disused" rel="tag" title="see questions tagged &#39;disused&#39;">disused</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '18, 16:13</strong></p>
<img src="https://secure.gravatar.com/avatar/e29180eb0eab5eeee15ab4cbf0d3bfd5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NeilJed&#39;s gravatar image" />
<p><span>NeilJed</span><br />
<span class="score" title="96 reputation points">96</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NeilJed has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66850" class="comments-container">
&#10;</div>
<div id="comment-tools-66850" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66850-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="66859"></span>

<div id="answer-container-66859" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66859-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-66859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="NeilJed has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You probably need to flip around your thinking. Rather than focusing on the way you want things to look in one particular rendering and trying to find tags that get you the look you want (known in the OSM community as "<a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">tagging for the renderer</a>"), you should be focusing on finding the most appropriate tags to represent reality and leaving it up to each data consumer/renderer to determine how they want to show things. Otherwise, you may get things to look the way you want in the one rendering, but the underlying data may cause unexpected rendering issues for other renderers or be unusable by some data consumers.</p>
<p>As for the best tags to use, disused:aeroway=runway is most likely the best tag for the entire runway. If there are parts of it now being used for other purposes like roads or footpaths, you could map those as distinct objects over the disused:aeroway object or break that object up and tag the pieces separately.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '18, 23:00</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-66859" class="comments-container">
<span id="66865"></span>
<div id="comment-66865" class="comment">
<div id="post-66865-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks for the response.</p>
<p>Yes, I was aware I may have fallen foul of "tagging for the renderer". I have placed a centre line down the path of each runway and marked it as disused:aeroway=runway and done similar for the entire area around the airfield. Naturally neither of these show up in the default map view.</p>
<p>The issue is that there is no hard boundary as to which areas are used for what and sometimes it varies on events. So basically it's multipurpose. In some ways I wish there was a generic "paved area" type that covers this.</p>
<p>I'll have a think and try to come up with solution that works but abides by the tagging schema. Mostly this was prompted by someone I know was organising an event on an old runway and was trying to show the location on an embedded map and the fact the runways weren't shown was causing some problems for people getting there.</p>
</div>
<div id="comment-66865-info" class="comment-info">
<span class="comment-age">(20 Nov '18, 14:03)</span> <span class="comment-user userinfo">NeilJed</span>
</div>
</div>
<span id="66886"></span>
<div id="comment-66886" class="comment">
<div id="post-66886-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Since you are talking about disused airstrips and touristic? / hobby? events taking place there - I guess things like drag races or a big outdoor book or art market? - I think tagging them as highway=pedestrian, area=yes is the most appropriate. People are likely walking around a lot on the former tarmac, and it is likely used as just one big plaza or square.</p>
<p>Tagging them with anything suggesting they are "normal" roads for cars (e.g. highway=unclassified/tertiary/secondary) is thus not sensible.</p>
</div>
<div id="comment-66886-info" class="comment-info">
<span class="comment-age">(21 Nov '18, 20:52)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
<span id="86640"></span>
<div id="comment-86640" class="comment">
<div id="post-86640-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The problem with highway=pedestrian, area=yes is that any buildings on top of the runway then don't render. I've got that issue as well, as a TV studio has been built on top of part of the runway</p>
<p>I've ended up just drawing the runways as an area and calling them a "commercial area", as at least that way they're highlighted, and other building and activities (like a go-cart track) can be placed on top.</p>
<p>The problem here is that the available tagging doesn't represent "reality", as the landuse options are all for natural uses, and the landcover tag doesn't render. And rendering, especially the standard option, does matter as that is what so many organisations link to, to show where they are. Without posting an area, the former runways just wouldn't show up on nearly all renders, making the map unhelpful.</p>
</div>
<div id="comment-86640-info" class="comment-info">
<span class="comment-age">(07 Feb '23, 14:29)</span> <span class="comment-user userinfo">Mikey Co</span>
</div>
</div>
</div>
<div id="comment-tools-66859" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66859-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85307"></span>

<div id="answer-container-85307" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85307-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On the former airport "Berlin-Tempelhof", it is tagged as "highway=footway" and "area=yes" and partly "bicycle=yes": <a href="https://www.openstreetmap.org/way/58696735#map=16/52.4751/13.4050">https://www.openstreetmap.org/way/58696735#map=16/52.4751/13.4050</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '22, 16:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a83854e9475736603fbe89e556f9930b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="osmidal&#39;s gravatar image" />
<p><span>osmidal</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="osmidal has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-85307" class="comments-container">
&#10;</div>
<div id="comment-tools-85307" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85307-form-container" class="comment-form-container">
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

