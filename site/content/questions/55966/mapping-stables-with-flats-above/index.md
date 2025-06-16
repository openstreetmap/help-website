+++
type = "question"
title = "Mapping stables with flats above"
description = '''I would like to map a building which is a stables with 2 flats above. What&#x27;s the best way of doing this? I was going to map the whole building as stables, and then use nodes for the 2 flats, but then you can&#x27;t see what areas the flats cover. Is that the best way of doing it? Or should I do the stabl...'''
date = "2017-05-01T08:47:00Z"
lastmod = "2017-05-01T11:01:00Z"
weight = 55966
keywords = [ "buildings", "stables" ]
aliases = [ "/questions/55966" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Mapping stables with flats above](/questions/55966/mapping-stables-with-flats-above)

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
<span id="post-55966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55966-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to map a building which is a stables with 2 flats above. What's the best way of doing this?</p>
<p>I was going to map the whole building as stables, and then use nodes for the 2 flats, but then you can't see what areas the flats cover. Is that the best way of doing it? Or should I do the stables and flats all as overlapping building ways?</p>
<p>The stables are currently mapped as a node, but I don't like that as it doesn't show the whole area that the stables cover: <a href="https://www.openstreetmap.org/node/1011636463">https://www.openstreetmap.org/node/1011636463</a></p>
<p>You can see a <a href="http://www.thisispaddington.com/cms/images/articles/thumbnails/Hyde-Park-and-area-31.jpg">photo here</a> - the stables are on the ground floor and the 2 flats are the first floor.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-stables" rel="tag" title="see questions tagged &#39;stables&#39;">stables</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 May '17, 08:47</strong></p>
<img src="https://secure.gravatar.com/avatar/112b44f8f07f00d309f2b49a7c3a65aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abeverley&#39;s gravatar image" />
<p><span>abeverley</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abeverley has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55966" class="comments-container">
&#10;</div>
<div id="comment-tools-55966" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55966-form-container" class="comment-form-container">
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

<span id="55969"></span>

<div id="answer-container-55969" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55969-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="abeverley has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've heard that the building tag should reflect the style or type of the building, not the usage. E.g. we still map a church that is turned into lofts as building=church.</p>
<p>This does not look to me like a typical stable, more like a residential building. But it has to be compared with the style of residential buildings in the area, if this is the case, map the building with building=residential</p>
<p>The tag <a href="https://wiki.openstreetmap.org/wiki/Key:building:use">building:use</a> can be added to reflect the current use. Since there are 2 uses in this case, you could add building:use=stable;residential</p>
<p>If you want to add more detail, you can start thinking to using some aspects of <a href="https://wiki.openstreetmap.org/wiki/Indoor_Mapping">indoor mapping</a>.</p>
<p>I would always keep the POI for the company operating the stables.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '17, 11:01</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-55969" class="comments-container">
&#10;</div>
<div id="comment-tools-55969" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55969-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55967"></span>

<div id="answer-container-55967" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55967-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, you should not split a building so leave it just as building=yes. The users as stable and households should get a node with the special items as addresses and the use as stable with its special tags. There is a node stable but there seems to be no building, start adding the building and its neighbours and add the separate nodes to it the building with the stable inside, but don’t map for the renderer. By the way the whole Bathurst Mews seems likely to be residential as well and some building seems to be missing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '17, 10:53</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 May '17, 10:59</strong> </span></p>
</div>
</div>
<div id="comments-container-55967" class="comments-container">
&#10;</div>
<div id="comment-tools-55967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55967-form-container" class="comment-form-container">
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

