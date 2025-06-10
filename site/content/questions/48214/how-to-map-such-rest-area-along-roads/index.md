+++
type = "question"
title = "How to map such rest area along roads?"
description = '''Hello, there. I was wondering: there are numerous examples of rest areas like the following, but how exactly to map them? The first example:  These are often only a stop area, sometimes with some trash cans, even less often with picnic tables; this one, apart from mapping cans and tables if present,...'''
date = "2016-02-19T07:37:00Z"
lastmod = "2020-04-15T14:12:00Z"
weight = 48214
keywords = [ "table", "trashcans", "rest", "road", "area" ]
aliases = [ "/questions/48214" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to map such rest area along roads?](/questions/48214/how-to-map-such-rest-area-along-roads)

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
<span id="post-48214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48214-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, there.</p>
<p>I was wondering: there are numerous examples of rest areas like the following, but how exactly to map them?</p>
<p>The first example: <img src="http://help.openstreetmap.org/upfiles/1_9EeNLNP.png" alt="first example" /></p>
<p>These are often only a stop area, sometimes with some trash cans, even less often with picnic tables; this one, apart from mapping cans and tables if present, I have no idea how to map it.</p>
<p>Second example: <img src="http://help.openstreetmap.org/upfiles/2.png" alt="second example" /></p>
<p>These are bigger, and the ones without tables and trash cans are not the predominant type. There, I would say to map the highway, maybe as <code>highway=service</code>, and the tables and cans, but there may be a better modelling; if so, how?</p>
<p>I must add that I expect a mean to explicitly map them as rest areas, as it's their use, and consumers like road GPS receivers often use these areas to help their users by saying "Hey, you didn't take a rest during the past 3 hours, you could rest here, 5 minutes ahead.". I don't know if such a modelling exists, though.</p>
<p>Awaiting your answers,</p>
<p>Regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-table" rel="tag" title="see questions tagged &#39;table&#39;">table</span> <span class="post-tag tag-link-trashcans" rel="tag" title="see questions tagged &#39;trashcans&#39;">trashcans</span> <span class="post-tag tag-link-rest" rel="tag" title="see questions tagged &#39;rest&#39;">rest</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '16, 07:37</strong></p>
<img src="https://secure.gravatar.com/avatar/03b6014ac927da400a55374bbbe5152a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Penegal&#39;s gravatar image" />
<p><span>Penegal</span><br />
<span class="score" title="631 reputation points">631</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Penegal has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-48214" class="comments-container">
&#10;</div>
<div id="comment-tools-48214" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48214-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="48215"></span>

<div id="answer-container-48215" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48215-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48215-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48215-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Penegal has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Drest_area">highway=rest_area</a> is pretty popular. It has currently around 13k usages, half of them as nodes, the other half as ways/areas.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '16, 07:49</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</img>
</div>
</div>
<div id="comments-container-48215" class="comments-container">
<span id="48216"></span>
<div id="comment-48216" class="comment">
<div id="post-48216-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I think of a rest_area as someplace where there are toilets and perhaps picnic tables. I map objects in the illustration as highway=service and a node (or an area) as amenity=parking. Add nodes for drinking water and waste baskets or tourism=viewpoint when appropriate.</p>
</div>
<div id="comment-48216-info" class="comment-info">
<span class="comment-age">(19 Feb '16, 09:24)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="48218"></span>
<div id="comment-48218" class="comment">
<div id="post-48218-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>According to the current wiki description rest areas <em>may</em> have picnic tables, garbage bins and toilets. If they have these features then they can be mapped either separately or with an additional tag like toilets=yes/no. This way a router can decide whether to show these places or not.</p>
</div>
<div id="comment-48218-info" class="comment-info">
<span class="comment-age">(19 Feb '16, 09:37)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="48234"></span>
<div id="comment-48234" class="comment">
<div id="post-48234-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I'd agree with AlaskaDave - the top example isn't really a rest_area because it has no facilities at all. I'd just tag it as "amenity=parking; parking=layby". The second one might just qualify as a rest_area if it had some facilities, but if not I'd just tag the service road, and then the parking area as "amenity=parking; parking=layby".</p>
<p>It is unhelpful to tag things that are "on the way to X but not actually X" as "X" because it means there's then no way to tell them from the <em>real</em> "Xs" that have been mapped.</p>
<p>There are other examples of this within OSM - the use of "natural=peak" is (at least in England and Wales) one; "natural=tree" also was (not helped by the English English definition of "tree" not matching the original OSM definition of "significant tree"). Here at least "rest_area" does have an English definition, and the first example above definitely isn't one, and the second probably isn't. Both are laybies.</p>
</div>
<div id="comment-48234-info" class="comment-info">
<span class="comment-age">(20 Feb '16, 11:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="48238"></span>
<div id="comment-48238" class="comment">
<div id="post-48238-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/387/someoneelse"></a><a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> then our wiki pages need to be fixed. The English version even lists lay-bys as examples for highway=rest_area. The German page suggests to use it also for places to make driver changes etc.</p>
</div>
<div id="comment-48238-info" class="comment-info">
<span class="comment-age">(20 Feb '16, 12:46)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="74204"></span>
<div id="comment-74204" class="comment">
<div id="post-74204-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Completely agree with SomeoneElse here: both are lay-bys and not rest areas. Many lay-bys, such as the first example, are unsuitable for wandering away from the car. Note in the UK some lay-bys have cafes or similar in portacabins but are still lay-bys (I've never quite understood the planning basis for such locations)</p>
</div>
<div id="comment-74204-info" class="comment-info">
<span class="comment-age">(15 Apr '20, 14:12)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48215" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48215-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48228"></span>

<div id="answer-container-48228" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48228-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is one here <a href="http://www.openstreetmap.org/#map=18/52.31442/-0.14199">http://www.openstreetmap.org/#map=18/52.31442/-0.14199</a> It is just a parking node, and is used mainly by HGVs ( heavy goods vehicles ) so the drivers can comply with law that they have rest stops. Cars can use them but adding the number of spaces wouldn't make sense. I my opinion a parking node is the best way to map them, if there are other facilities add them. It is useful that these parking spots are mapped. They are called laybys in GB.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '16, 17:22</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-48228" class="comments-container">
<span id="48231"></span>
<div id="comment-48231" class="comment">
<div id="post-48231-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I agree that these areas can be considered as parking, but with a specific usage, that <code>highway=rest_area</code> models better than just <code>amenity=parking</code>, which serves a different purpose IMHO. Thanks anyway.</p>
</div>
<div id="comment-48231-info" class="comment-info">
<span class="comment-age">(20 Feb '16, 09:09)</span> <span class="comment-user userinfo">Penegal</span>
</div>
</div>
<span id="48236"></span>
<div id="comment-48236" class="comment">
<div id="post-48236-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If I was looking for a highway rest area I'd feel very short-changed if a search came up with Andy Mackey's example on the A14. It's just a service road separated from an almost-motorway by a bit of armco. Rest areas on the Australian model (the wiki page was created by an Australian) are pretty rare in the southern UK, as the distances don't require it. Unfortunately the wiki page was edited by someone from the southern UK who it appears has never seen a rest area and assumed that a layby was one.</p>
</div>
<div id="comment-48236-info" class="comment-info">
<span class="comment-age">(20 Feb '16, 11:10)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48228" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48228-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74202"></span>

<div id="answer-container-74202" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74202-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Question is pretty old, but for the first picture I would use <a href="https://wiki.openstreetmap.org/wiki/Key:parking:lane">parking:lane</a> - for parking alongside a highway. Also you can add some restrictions if apply. <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity=parking">amenity:parking</a> assumes some bigger facility.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '20, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/d1495190e346c0c530fd7205883b55c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Plamen&#39;s gravatar image" />
<p><span>Plamen</span><br />
<span class="score" title="151 reputation points">151</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Plamen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74202" class="comments-container">
<span id="74203"></span>
<div id="comment-74203" class="comment">
<div id="post-74203-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not really; the first sentence says just "Use amenity=parking to tag a facility used by the public, customers, or other authorised users for parking motor vehicles, such as cars and trucks" and there's no use of "big" or "large" on that page.</p>
</div>
<div id="comment-74203-info" class="comment-info">
<span class="comment-age">(15 Apr '20, 12:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74202-form-container" class="comment-form-container">
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

