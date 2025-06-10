+++
type = "question"
title = "Invisible Islands"
description = '''I stumbled upon an island not rendering properly. I have made several attempts to correct this by trying something a little different with each of the three islands that don&#x27;t seem to appear on the map. If anyone could take a look and let me know what is wrong it surely would be appreciated. http://...'''
date = "2017-03-18T14:17:00Z"
lastmod = "2017-03-22T12:40:00Z"
weight = 55174
keywords = [ "invisible", "island" ]
aliases = [ "/questions/55174" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Invisible Islands](/questions/55174/invisible-islands)

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
<span id="post-55174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55174-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I stumbled upon an island not rendering properly. I have made several attempts to correct this by trying something a little different with each of the three islands that don't seem to appear on the map.</p>
<p>If anyone could take a look and let me know what is wrong it surely would be appreciated.</p>
<p><a href="http://www.openstreetmap.org/#map=15/49.0719/-53.5678">http://www.openstreetmap.org/#map=15/49.0719/-53.5678</a></p>
<p>On OpenStreetMap Greenspond Island, Pig Island and Ship Island are invisible.</p>
<p>On my tablet using OsmAnd+ Greenspond and Pig islands are visible but Ship Island is invisible.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-invisible" rel="tag" title="see questions tagged &#39;invisible&#39;">invisible</span> <span class="post-tag tag-link-island" rel="tag" title="see questions tagged &#39;island&#39;">island</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Mar '17, 14:17</strong></p>
<img src="https://secure.gravatar.com/avatar/66003cc3c05c6ccf2a407ee22c124285?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Drew_NL&#39;s gravatar image" />
<p><span>Drew_NL</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Drew_NL has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55174" class="comments-container">
<span id="55225"></span>
<div id="comment-55225" class="comment">
<div id="post-55225-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You could try this: remove all tags except the coastline and make sure the ways' orientation is ccw (land to the left). Tags like place... are unnecessary (many sw-s create see/water instead of lan). If you want the same geometry for other object classes just insert there a new object and refer to the already uploaded geometry by its id.</p>
</div>
<div id="comment-55225-info" class="comment-info">
<span class="comment-age">(22 Mar '17, 08:58)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
</div>
<div id="comment-tools-55174" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55174-form-container" class="comment-form-container">
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

<span id="55175"></span>

<div id="answer-container-55175" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55175-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-55175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's because Ship Island is only a boundary way, it has no coastline. Notice the lines surrounding the other islands, the ones that render (show up). On JOSM they show up as a heavy black line. Ship Island doesn't have it. If you trace the outline of the island and tag it natural=coastline it will show up as an island. You need to trace it in a counterclockwise fashion.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '17, 14:41</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-55175" class="comments-container">
<span id="55177"></span>
<div id="comment-55177" class="comment not_top_scorer">
<div id="post-55177-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, I hopefully just did what you said on the two smaller islands and will wait and see how that renders.</p>
</div>
<div id="comment-55177-info" class="comment-info">
<span class="comment-age">(18 Mar '17, 15:29)</span> <span class="comment-user userinfo">Drew_NL</span>
</div>
</div>
<span id="55181"></span>
<div id="comment-55181" class="comment">
<div id="post-55181-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When I looked again after your edits Ship Island still wasn't visible on the OSM slippy map either as a boundary or as an island. That's probably because you used the same way twice, once as a boundary, and again as coastline.</p>
<p>I would duplicate the boundary, delete the existing tags, adjust it so it fits the contours of the water line better, then add the tag natural=coastline to the new way. Alternatively, seeing as the island is small, you could just draw a new coastline from scratch.</p>
<p>Pig Island has the same problem. The boundary is there, the name is there, but there is no coastline to define the enclosed area as an island in the sea. It displays as an administrative unit with name=Pig Island but without a coastline is otherwise invisible.</p>
</div>
<div id="comment-55181-info" class="comment-info">
<span class="comment-age">(19 Mar '17, 03:08)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="55182"></span>
<div id="comment-55182" class="comment">
<div id="post-55182-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I thought the coastline is not updated frequently. Only when all the coastlines are OK, i.e. none is broken so that land would be coloured blue.</p>
</div>
<div id="comment-55182-info" class="comment-info">
<span class="comment-age">(19 Mar '17, 06:37)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="55184"></span>
<div id="comment-55184" class="comment">
<div id="post-55184-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5390/escada"></a><a href="https://help.openstreetmap.org/users/5390/escada">@escada</a>, yes, that's a factor I forgot about. In JOSM, newly added coastlines appear right away but they take a while to propagate to the slippy map display. I'm not sure how long before they do. Coastlines don't appear on the slippy map as black lines, they are merely a place where land coloration changes to blue.</p>
<p><a href="https://help.openstreetmap.org/users/9888/drew_nl"></a><a href="https://help.openstreetmap.org/users/9888/drew_nl">@Drew</a>, considering this it's probably best to give your edits some more time to become visible. I have used a coastline way and a boundary way together in Alaska and on the slippy map only the boundary is visible as a separate entity. Here is a part of that way: <a href="http://www.openstreetmap.org/search?query=67.63419%2C%20-164.1889#map=16/67.6336/-164.1851">http://www.openstreetmap.org/search?query=67.63419%2C%20-164.1889#map=16/67.6336/-164.1851</a></p>
<p>Changes to this boundary show up right away but maybe that's because it marks a nature_reserve, which gets special treatment. Are administrative boundaries rendered differently?</p>
</div>
<div id="comment-55184-info" class="comment-info">
<span class="comment-age">(19 Mar '17, 07:26)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="55185"></span>
<div id="comment-55185" class="comment">
<div id="post-55185-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Another interesting part of this puzzle is that Greenspond Island does show up. It is tagged as natural=coastline and boundary=adminstrative. However, it is also tagged with admin_level=8 while neither Ship or Pig Islands have an admin_level tag.</p>
<p>Could this be the reason they don't render?</p>
</div>
<div id="comment-55185-info" class="comment-info">
<span class="comment-age">(19 Mar '17, 07:47)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="55186"></span>
<div id="comment-55186" class="comment not_top_scorer">
<div id="post-55186-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The islands do show, please refresh/reload your display.</p>
</div>
<div id="comment-55186-info" class="comment-info">
<span class="comment-age">(19 Mar '17, 08:03)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
<span id="55188"></span>
<div id="comment-55188" class="comment">
<div id="post-55188-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>We're talking about visibility on the OSM slippy map. I just cleared my image cache, reloaded the page, and except for the administrative boundary around Pig Island, both islands are still invisible in both Chrome and Firefox.</p>
</div>
<div id="comment-55188-info" class="comment-info">
<span class="comment-age">(19 Mar '17, 08:31)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="55189"></span>
<div id="comment-55189" class="comment not_top_scorer">
<div id="post-55189-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>At first I couldn't see Greenspond, a refresh and it showed. But Pig and Ship I can't see except as said the admin boundary round Pig</p>
</div>
<div id="comment-55189-info" class="comment-info">
<span class="comment-age">(19 Mar '17, 08:45)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
<span id="55190"></span>
<div id="comment-55190" class="comment not_top_scorer">
<div id="post-55190-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As I wrote in the other cross-post in the OpenStreetMap Forum: I made both some corrections yesterday (removal of duplicated ways and adding of missing tags), and advice you to wait several weeks before reviewing this. Honestly, I have seen it take up to a month for a similar issue related to coastline and islands to show up properly on the slippy map.</p>
</div>
<div id="comment-55190-info" class="comment-info">
<span class="comment-age">(19 Mar '17, 10:44)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
<span id="55227"></span>
<div id="comment-55227" class="comment not_top_scorer">
<div id="post-55227-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I plan on waiting until the month end updates, I would appreciate, however, that no one else go in and make changes as mboeringa took away the changes I made on the smaller islands. I made changes on the larger Green Island which seem to have worked unless some one else had made other changes. I will then correct the smaller two islands after the March update in early April. I'll then post back here with an update of what worked and what never. Thanks everyone.</p>
</div>
<div id="comment-55227-info" class="comment-info">
<span class="comment-age">(22 Mar '17, 09:18)</span> <span class="comment-user userinfo">Drew_NL</span>
</div>
</div>
<span id="55228"></span>
<div id="comment-55228" class="comment not_top_scorer">
<div id="post-55228-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, you should really wait. After pressing F5, I now see all my corrections and the islands properly rendered at Z14 and Z15, but not yet at higher zooms (&gt;=Z16). But this is probably an indication that all is fine now, and you just need to have some patience for the updates to appear at higher zooms.</p>
</div>
<div id="comment-55228-info" class="comment-info">
<span class="comment-age">(22 Mar '17, 10:52)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
<span id="55229"></span>
<div id="comment-55229" class="comment not_top_scorer">
<div id="post-55229-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sounds good. Please post a comment when you learn anything new.</p>
</div>
<div id="comment-55229-info" class="comment-info">
<span class="comment-age">(22 Mar '17, 12:40)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-55175" class="comment-tools">
<span class="comments-showing"> showing 5 of 12 </span> <a href="#" class="show-all-comments-link">show 7 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-55175-form-container" class="comment-form-container">
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

