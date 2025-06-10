+++
type = "question"
title = "Watershed basin limits in OSM?"
description = '''Hello everyone. Yesterday I noticed a strange very big lake in the center of Madagascar [this polygon]. When inspecting the data, I found that it was supposed to be a watershed basin but was wrongly tagged as landuse=basin. To avoid the rendering of the whole area as a lake/basin, I immediately remo...'''
date = "2017-12-20T05:19:00Z"
lastmod = "2017-12-21T08:51:00Z"
weight = 61281
keywords = [ "basin", "tagging", "watershed", "relations" ]
aliases = [ "/questions/61281" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Watershed basin limits in OSM?](/questions/61281/watershed-basin-limits-in-osm)

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
<span id="post-61281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61281-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone.</p>
<p>Yesterday I noticed a strange very big lake in the center of Madagascar [<a href="http://www.openstreetmap.org/way/547294938">this polygon</a>]. When inspecting the data, I found that it was supposed to be a watershed basin but was wrongly tagged as <code>landuse=basin</code>. To avoid the rendering of the whole area as a lake/basin, I immediately removed the <code>landuse=basin</code> tag and replaced it with a fixme note.</p>
<ul>
<li>By the way I was wondering if there was really a way to add watershed basin limits to OpenStreetMap? (<a href="http://wiki.openstreetmap.org/wiki/Relation:watershed">This proposed relation type</a> takes in waterways (main stream + tributaries) instead of limits)</li>
<li>What do I do with this polygon: should I let it there as it is or delete it?</li>
</ul>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-basin" rel="tag" title="see questions tagged &#39;basin&#39;">basin</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-watershed" rel="tag" title="see questions tagged &#39;watershed&#39;">watershed</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Dec '17, 05:19</strong></p>
<img src="https://secure.gravatar.com/avatar/15d45a99f101e06c9e79916af33f8336?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Privatemajory&#39;s gravatar image" />
<p><span>Privatemajory</span><br />
<span class="score" title="1125 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Privatemajory has 4 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Dec '17, 05:20</strong> </span></p>
</div>
</div>
<div id="comments-container-61281" class="comments-container">
<span id="61283"></span>
<div id="comment-61283" class="comment">
<div id="post-61283-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's a good question (and not one that has been asked directly before, although people have asked about watersheds <a href="https://help.openstreetmap.org/search/?q=watershed&amp;Submit=search&amp;t=question">https://help.openstreetmap.org/search/?q=watershed&amp;Submit=search&amp;t=question</a> )</p>
</div>
<div id="comment-61283-info" class="comment-info">
<span class="comment-age">(20 Dec '17, 10:24)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="61284"></span>
<div id="comment-61284" class="comment">
<div id="post-61284-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A web search of "watershed site:<a href="https://lists.openstreetmap.org/pipermail/">https://lists.openstreetmap.org/pipermail/"</a> finds mailing list discussions in the US about it, but surprisingly few.</p>
</div>
<div id="comment-61284-info" class="comment-info">
<span class="comment-age">(20 Dec '17, 10:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="61306"></span>
<div id="comment-61306" class="comment">
<div id="post-61306-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think in general we should not try to map them. It is possible to find all waterways draining a given basin (either through explicit tags or finding discrete graphs of waterways) and draw a concave hull to create a polygon which will approximate the drainage basin. It should also be possible to post-process these to tessellate the drainage basins over the area.</p>
</div>
<div id="comment-61306-info" class="comment-info">
<span class="comment-age">(20 Dec '17, 22:26)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="61312"></span>
<div id="comment-61312" class="comment">
<div id="post-61312-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But well, natural landscape elements and natural boundaries could also be part of OSM, just like other boundaries, right? Then watersheds can't be separate from hydrography, waterways + springs + watershed limits would be a more complete hydrographic data.</p>
<p>Using the search suggested by <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> above, I found a 2009 topic on OSM-Talk-fr (<a href="https://lists.openstreetmap.org/pipermail/talk-fr/2009-September/014241.html)">https://lists.openstreetmap.org/pipermail/talk-fr/2009-September/014241.html)</a> about adding ridge and thalweg lines to OSM but no one showed interest. This could match here as watersheds follow ridge lines. But I guess it's not interesting enough amongst the OSM community.</p>
</div>
<div id="comment-61312-info" class="comment-info">
<span class="comment-age">(21 Dec '17, 08:51)</span> <span class="comment-user userinfo">Privatemajory</span>
</div>
</div>
</div>
<div id="comment-tools-61281" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61281-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

