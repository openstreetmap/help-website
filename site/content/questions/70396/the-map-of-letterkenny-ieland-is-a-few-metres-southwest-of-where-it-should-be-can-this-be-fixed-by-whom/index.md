+++
type = "question"
title = "The map of Letterkenny, Ieland, is a few metres southwest of where it should be. Can this be fixed? By whom?"
description = '''Hi, when I drove through Letterkenny, County Donegal, on the Irish north coast a few days ago, I noticed that GPS appeared to have a bit of a problem, because my track was consistently a few metres north north east of the map. Just now I wanted to enter a few things I had found missing when I was th...'''
date = "2019-08-15T23:36:00Z"
lastmod = "2019-08-16T23:41:00Z"
weight = 70396
keywords = [ "offset" ]
aliases = [ "/questions/70396" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [The map of Letterkenny, Ieland, is a few metres southwest of where it should be. Can this be fixed? By whom?](/questions/70396/the-map-of-letterkenny-ieland-is-a-few-metres-southwest-of-where-it-should-be-can-this-be-fixed-by-whom)

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
<span id="post-70396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70396-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>when I drove through Letterkenny, County Donegal, on the Irish north coast a few days ago, I noticed that GPS appeared to have a bit of a problem, because my track was consistently a few metres north north east of the map.</p>
<p>Just now I wanted to enter a few things I had found missing when I was there (using Potlatch 2), and saw that my track fits perfectly not just for Bing, but also for Mapbox and Maxar Premium, so it must surely be the map that is "off".</p>
<p>(How) can this be fixed?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-offset" rel="tag" title="see questions tagged &#39;offset&#39;">offset</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Aug '19, 23:36</strong></p>
<img src="https://secure.gravatar.com/avatar/06b2f5d4fa9884ae47333da22b6f2662?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marabu_Too&#39;s gravatar image" />
<p><span>Marabu_Too</span><br />
<span class="score" title="210 reputation points">210</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marabu_Too has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Aug '19, 23:46</strong> </span></p>
</div>
</div>
<div id="comments-container-70396" class="comments-container">
<span id="70398"></span>
<div id="comment-70398" class="comment">
<div id="post-70398-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Interestingly at <a href="https://www.openstreetmap.org/#map=19/54.94726/-7.73106">https://www.openstreetmap.org/#map=19/54.94726/-7.73106</a> there's a visible offset between various imagery resources. at that roundabout, OSM data is offset to the southwest compared to both Bing imagery and GPS traces. ESRI is offset a few meters to the northwest, Maxar premium and standard slightly to the south. The offset of different imagery sources may vary as you move around; where were you looking?</p>
</div>
<div id="comment-70398-info" class="comment-info">
<span class="comment-age">(16 Aug '19, 00:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70400"></span>
<div id="comment-70400" class="comment">
<div id="post-70400-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> I panned the map to Donegal, zoomed in onto that roundabout, because around it a number of shops have changed since someone put them on the map, opened Potlatch 2, saw the offset to Bing, loaded my track with its annotations, saw that it fitted Bing, tried some of the other satellite imagery.</p>
<p>I loaded some older tracks from journey to that Retail Park and saw that all were nearly identical around the roundabout, at at any Letterkenny street that extends more or less east/west, all ran a bit to the north of thos streets.</p>
</div>
<div id="comment-70400-info" class="comment-info">
<span class="comment-age">(16 Aug '19, 09:52)</span> <span class="comment-user userinfo">Marabu_Too</span>
</div>
</div>
<span id="70401"></span>
<div id="comment-70401" class="comment">
<div id="post-70401-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>In general I wouldn't bother. It's really tedious realigning objects like this, and there is a possibility of making things worse. We mapped a lot of Nottingham from Yahoo imagery years ago which turned out to be displaced about 10 m N of true (accurately located street lamp data helped show this). The problem is that a mass realignment is unlikely to be correct (adjacent map tiles will have different offsets &amp; different zoom levels will have different offsets), and partially corrected stuff just looks awful. If you do want to correct something choose an area with 'give' at the edges (major roads, parks etc) so that the differences are not too jarring.</p>
</div>
<div id="comment-70401-info" class="comment-info">
<span class="comment-age">(16 Aug '19, 15:56)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="70405"></span>
<div id="comment-70405" class="comment">
<div id="post-70405-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>In this particular case I agree that there is a correction-worthy offset, but just to prevent over-eager correction: Be careful to not trust a single GPS trace, even if it shows a consistent offset compared to OSM data. GPS receiver errors can be self-consistent and last for hours. Only trust a cloud of dozens of GPS traces.</p>
</div>
<div id="comment-70405-info" class="comment-info">
<span class="comment-age">(16 Aug '19, 23:41)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-70396" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70396-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

