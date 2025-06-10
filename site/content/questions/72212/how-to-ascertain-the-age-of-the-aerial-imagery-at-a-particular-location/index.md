+++
type = "question"
title = "How to ascertain the age of the aerial imagery at a particular location?"
description = '''Oftentimes, there are several aerial imagery sources available for any particular location. When I want to trace the newest features, it is helpful to know which source is the newest one. However, my particular use case is that I want to check if a particular feature that was added by a new user doe...'''
date = "2019-12-23T10:41:00Z"
lastmod = "2019-12-27T19:39:00Z"
weight = 72212
keywords = [ "aerial_imagery", "tiles", "quality_assurance", "update" ]
aliases = [ "/questions/72212" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to ascertain the age of the aerial imagery at a particular location?](/questions/72212/how-to-ascertain-the-age-of-the-aerial-imagery-at-a-particular-location)

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
<span id="post-72212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72212-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Oftentimes, there are several aerial imagery sources available for any particular location. When I want to trace the newest features, it is helpful to know which source is the newest one.</p>
<p>However, my particular use case is that I want to check if a particular feature that was added by a new user does really exist. If I knew the date or year at which the different satellite pictures were made, I would be able to tell whether the feature is simply not visible yet because the map tiles are too old, or if it was an act of vandalism.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-aerial_imagery" rel="tag" title="see questions tagged &#39;aerial_imagery&#39;">aerial_imagery</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-quality_assurance" rel="tag" title="see questions tagged &#39;quality_assurance&#39;">quality_assurance</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Dec '19, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/806355bb02bf30d4d2da55b8d23dafce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="westnordost&#39;s gravatar image" />
<p><span>westnordost</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="westnordost has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72212" class="comments-container">
<span id="72236"></span>
<div id="comment-72236" class="comment">
<div id="post-72236-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have this same question. How can I figure out what the age of a sat image was?</p>
</div>
<div id="comment-72236-info" class="comment-info">
<span class="comment-age">(27 Dec '19, 19:39)</span> <span class="comment-user userinfo">nater111</span>
</div>
</div>
</div>
<div id="comment-tools-72212" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72212-form-container" class="comment-form-container">
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

<span id="72213"></span>

<div id="answer-container-72213" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72213-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Some imagery tiles provide metadata, including date of acquisition, for each tile. This information is available in both JOSM and iD (Shift-Ctrl-B) for at least ESRI layers.</p>
<p>In some countries there are also other historical layers which may help. For instance <a href="http://os.openstreetmap.org">os.openstreetmap.org</a> shows various issues of Ordnance Survey StreetView Open Data from 2010-2016. This can assist in more accurate ageing of imagery layers. When one of Bing Streetside, Mapillary or OpenStreetCam imagery is available these can also help.</p>
<p>Most of the time relative age needs to be inferred from imagery itself. In many places this is self-evident, for instance, buildings on what was farmland, but in town centres and long-standing residential suburbs the signs are more subtle. One clue I'm aware of is presence of rooftop solar installations can be a good guide at present because many of these have been put in since 2010 and in many areas there are enough to discriminate between other very similar imagery.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Dec '19, 14:33</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Dec '19, 10:24</strong> </span></p>
</div>
</div>
<div id="comments-container-72213" class="comments-container">
<span id="72214"></span>
<div id="comment-72214" class="comment">
<div id="post-72214-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Bing usually has information available on "vintage" in a similar way.</p>
</div>
<div id="comment-72214-info" class="comment-info">
<span class="comment-age">(24 Dec '19, 00:25)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-72213" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72213-form-container" class="comment-form-container">
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

