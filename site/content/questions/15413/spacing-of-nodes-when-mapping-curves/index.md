+++
type = "question"
title = "Spacing of nodes when mapping curves"
description = '''Are there any guidelines for how far apart nodes should be spaced when mapping a smooth curve in a road? Given that our source data is accurate to about the nearest metre at best, I would have thought that a node every three or four metres would be adequate for any curve likely to be found on a road...'''
date = "2012-08-22T21:48:00Z"
lastmod = "2012-08-24T20:09:00Z"
weight = 15413
keywords = [ "spacing", "nodes", "curve" ]
aliases = [ "/questions/15413" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Spacing of nodes when mapping curves](/questions/15413/spacing-of-nodes-when-mapping-curves)

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
<span id="post-15413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15413-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-15413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Are there any guidelines for how far apart nodes should be spaced when mapping a smooth curve in a road? Given that our source data is accurate to about the nearest metre at best, I would have thought that a node every three or four metres would be adequate for any curve likely to be found on a road. To take just one example, Wild Ridings and Thornbury Close (<a href="https://www.openstreetmap.org/?lat=50.848497&amp;lon=-1.217579&amp;zoom=18&amp;layers=M)">https://www.openstreetmap.org/?lat=50.848497&amp;lon=-1.217579&amp;zoom=18&amp;layers=M)</a> have nodes spaced much more closely. These nodes seem to contribute little to the map, and when zoomed in just a little further than the OSM web site permits (e.g. in MapSource or on a GPSr), the rendering engines seem to be defeated, and the smooth curve breaks up into a series of sharp corners. Potlatch 2 offers a shortcut ('Y') that removes some of the nodes; if anything it can be a little too enthusiastic. I would like to remove some apparently unnecessary nodes, but I hesitate to 'improve' the style of other people's work without some backup from the OSM community.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-spacing" rel="tag" title="see questions tagged &#39;spacing&#39;">spacing</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-curve" rel="tag" title="see questions tagged &#39;curve&#39;">curve</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '12, 21:48</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-15413" class="comments-container">
<span id="15416"></span>
<div id="comment-15416" class="comment">
<div id="post-15416-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>The Potlatch 2 shortcut is mostly there for when you bring in data from an external source (e.g. alt-clicking a GPS track), rather than working with existing data. You can adjust how brutal it is in the Options dialogue.</p>
<p>But by and large, I think OSMers tend to put not enough points in curves, rather than too many. I've seen one guy in Ireland who puts (IMO) too many in; otherwise it's pretty rare.</p>
</div>
<div id="comment-15416-info" class="comment-info">
<span class="comment-age">(22 Aug '12, 22:42)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-15413" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15413-form-container" class="comment-form-container">
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

<span id="15414"></span>

<div id="answer-container-15414" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15414-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-15414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I like the curves in the example and would not change it. I often add nodes to improve the sweep of curves. The nodes in the example appear to be about a car length,from the Bing image, which is about 4 metres anyway. If you draw a small roundabout they will need nodes closer than 3 metres, in fact the auto circle will generate them more dense than that anyway. The magnification on some devices will reveal the series of straight lines but all digital curves will be like that I would think if magnified enough. edit update This is a very good question and highlights the feelings we all have. Change or not, If the map is improved by our edits it must be OK. The points about straight lining ways (there is a tool in potlatch2) and creating smooth curves with even nodes are the way to go. I suppose even good work can be improved.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '12, 22:22</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Aug '12, 10:54</strong> </span></p>
</div>
</div>
<div id="comments-container-15414" class="comments-container">
<span id="15417"></span>
<div id="comment-15417" class="comment">
<div id="post-15417-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I too have added nodes to smooth the line of a curve, and I accept that a digital representation of a curve necessarily becomes a series of short lines when zoomed, but at each node the line should change direction just a little. The nodes in the example do not quite form a smooth curve, and some commonly used rendering engines seem to make it worse, giving a very jagged result. Is there any tool that can smooth out a curve, perhaps by imposing a minimum radius of curvature? The Potlatch 2 'circle' tool does a wonderful job on closed ways such as roundabouts.</p>
</div>
<div id="comment-15417-info" class="comment-info">
<span class="comment-age">(22 Aug '12, 23:45)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
<span id="15419"></span>
<div id="comment-15419" class="comment">
<div id="post-15419-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If some renderers can't handle accurate data, then the toolchain feeding those renderers needs fixing. We shouldn't map less accurate for them.</p>
</div>
<div id="comment-15419-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 00:13)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="15420"></span>
<div id="comment-15420" class="comment">
<div id="post-15420-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Madryn I generally agree but curves should match what is on the ground or Bing first and foremost, not always a computer generated curve, although a assume new roads are designed with such tools anyway.</p>
</div>
<div id="comment-15420-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 06:10)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="15436"></span>
<div id="comment-15436" class="comment">
<div id="post-15436-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>"how close together are the nodes" is not the right metric. You instead want to look at "what is the angle between two segments" and "how far is each segment's midpoint from the center of the road". The position and closeness of osm nodes is just a derived property.</p>
</div>
<div id="comment-15436-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 10:29)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="15440"></span>
<div id="comment-15440" class="comment">
<div id="post-15440-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Vincent, I agree completely. Accuracy requires that the digital representation of a way should not misrepresent the position of any part of the way by more than about half of the accuracy of the source data. Aesthetics require that a curve on the rendered map should look like a curve, not a series of corners.</p>
</div>
<div id="comment-15440-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 12:54)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
</div>
<div id="comment-tools-15414" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15414-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15418"></span>

<div id="answer-container-15418" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15418-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Madryn, I dont support Andy and would change the curves. Too a smoother looking road in the middle of the arial pic. But I dont count nodes, just look at the curves. When theyre getting very close youll have to make the editing area smaller to get a greater scale. But generally youll be able to see a nice curve, it needs practice. Keep up the good work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '12, 23:57</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-15418" class="comments-container">
<span id="15421"></span>
<div id="comment-15421" class="comment">
<div id="post-15421-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>see this Q and more importantly the Answer and the links in it. <a href="/questions/2197/drawing-over-traces">https://help.openstreetmap.org/questions/2197/drawing-over-traces</a></p>
</div>
<div id="comment-15421-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 06:42)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="15435"></span>
<div id="comment-15435" class="comment">
<div id="post-15435-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Although I think the spacing of general nodes is good, there are some nodes that can be deleted.</p>
<p>First of all, the nodes on a straight line (if there is no curve, there is no need for a node): <a href="https://www.openstreetmap.org/browse/node/1697642915">https://www.openstreetmap.org/browse/node/1697642915</a></p>
<p>And next to that, nodes very close to a crossing: <a href="https://www.openstreetmap.org/browse/node/1697630103">https://www.openstreetmap.org/browse/node/1697630103</a></p>
</div>
<div id="comment-15435-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 09:54)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
<span id="15491"></span>
<div id="comment-15491" class="comment">
<div id="post-15491-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Andy, thanks for your comment. The question that you mentioned, and the links in the answer to that question, have made very interesting reading.</p>
</div>
<div id="comment-15491-info" class="comment-info">
<span class="comment-age">(24 Aug '12, 20:09)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
</div>
<div id="comment-tools-15418" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15418-form-container" class="comment-form-container">
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

