+++
type = "question"
title = "How to determine if a road is outside or inside place?"
description = '''I&#x27;m interesting in estimating the best speed limit for each road in my app. Most of the roads do not have a maxspeed tag, therefore the default per-country rules should be applied: http://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Maxspeed A lot of these rules are supposing we know if a road i...'''
date = "2017-07-04T10:39:00Z"
lastmod = "2017-07-04T10:51:00Z"
weight = 56876
keywords = [ "inside", "maxspeed", "place", "outside" ]
aliases = [ "/questions/56876" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to determine if a road is outside or inside place?](/questions/56876/how-to-determine-if-a-road-is-outside-or-inside-place)

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
<span id="post-56876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56876-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm interesting in estimating the best speed limit for each road in my app. Most of the roads do not have a <code>maxspeed</code> tag, therefore the default per-country rules should be applied: <a href="http://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Maxspeed">http://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Maxspeed</a> A lot of these rules are supposing we know if a road is inside or outside place, which sounds to me that is inside or outside a city area.</p>
<p>But I can't figure out how to determine this case. On which tag could I rely to know this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-inside" rel="tag" title="see questions tagged &#39;inside&#39;">inside</span> <span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-outside" rel="tag" title="see questions tagged &#39;outside&#39;">outside</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jul '17, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/ed2b06be7765e94570ace8fb755b266c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fabien%20Rohrer&#39;s gravatar image" />
<p><span>Fabien Rohrer</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fabien Rohrer has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jul '17, 10:40</strong> </span></p>
</div>
</div>
<div id="comments-container-56876" class="comments-container">
&#10;</div>
<div id="comment-tools-56876" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56876-form-container" class="comment-form-container">
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

<span id="56877"></span>

<div id="answer-container-56877" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56877-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Legal rules vary in between countries. In Germany, there's special signage that tells you when you enter a populated place (and this is different from the administrative boundaries). These populated places ("geschlossene Ortschaft") are not explicitly mapped in OSM so you cannot find out which roads are inside and which are outside. Mappers in Germany tend to add explicit speed limits to roads inside.</p>
<p>I think your best bet might be to simply assume that anything that is a highway=residential or surrounded by highway=residential counts as part of a populated place. Of course this will lead to some errors both ways but it's the best I can come up with.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '17, 10:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-56877" class="comments-container">
<span id="56878"></span>
<div id="comment-56878" class="comment">
<div id="post-56878-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, it seems it's indeed a good rule.</p>
</div>
<div id="comment-56878-info" class="comment-info">
<span class="comment-age">(04 Jul '17, 10:51)</span> <span class="comment-user userinfo">Fabien Rohrer</span>
</div>
</div>
</div>
<div id="comment-tools-56877" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56877-form-container" class="comment-form-container">
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

