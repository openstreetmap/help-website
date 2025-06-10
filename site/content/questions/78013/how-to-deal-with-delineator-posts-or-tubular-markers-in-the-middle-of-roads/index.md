+++
type = "question"
title = "How to deal with delineator posts or tubular markers in the middle of roads?"
description = '''I haven&#x27;t found these keywords used in the wiki when searching google and OSM. Here is an example: https://www.openstreetmap.org/way/344624044 On this way, the northbound and southbound lanes are separated by delineator posts similar to the ones seen here (https://pppcatalog.com/product/orca/). The ...'''
date = "2020-12-20T05:55:00Z"
lastmod = "2020-12-23T21:15:00Z"
weight = 78013
keywords = [ "turn_restrictions", "routing" ]
aliases = [ "/questions/78013" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to deal with delineator posts or tubular markers in the middle of roads?](/questions/78013/how-to-deal-with-delineator-posts-or-tubular-markers-in-the-middle-of-roads)

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
<span id="post-78013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78013-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I haven't found these keywords used in the wiki when searching google and OSM.</p>
<p>Here is an example: <a href="https://www.openstreetmap.org/way/344624044">https://www.openstreetmap.org/way/344624044</a></p>
<p>On this way, the northbound and southbound lanes are separated by delineator posts similar to the ones seen here (<a href="https://pppcatalog.com/product/orca/).">https://pppcatalog.com/product/orca/).</a></p>
<p>The effect of this is that southbound traffic cannot turn left into the safeway parking lot at either of the three little entrances and instead must turn left at the light to get to the parking lot.</p>
<p>For a while now maps.me has been telling folks to turn there where the posts are. This is partially due to the parking lot not being mapped (fixed that) but also it should not suggest a left turn when heading south until the stoplight. Since I just added the parking lot yesterday I'm not sure how the routing engines will handle it yet but I don't think they will have enough info right now.</p>
<p>I am thinking that it makes sense to use the <a href="https://wiki.openstreetmap.org/wiki/Key:turn#Turning_indications_per_lane">key:turn</a> and say that the lane next to the barriers is "through" until it gets to the next way and then set it to be a left turn only. However, that isn't an accurate description because it is a left turn only lane but you just can't turn left until the intersection.</p>
<p>Any tips or examples on how to handle this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Dec '20, 05:55</strong></p>
<img src="https://secure.gravatar.com/avatar/043d95939633cb3216e446401aee254a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ray331&#39;s gravatar image" />
<p><span>ray331</span><br />
<span class="score" title="120 reputation points">120</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ray331 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78013" class="comments-container">
&#10;</div>
<div id="comment-tools-78013" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78013-form-container" class="comment-form-container">
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

<span id="78016"></span>

<div id="answer-container-78016" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78016-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78016-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78016-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The delineators are a type of physical barrier, so it is appropriate to split the street into dual carriageways. It is also valid to use turn restrictions but the result can be more complicated to maintain.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '20, 13:17</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-78016" class="comments-container">
<span id="78031"></span>
<div id="comment-78031" class="comment">
<div id="post-78031-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Technically, non-permanent barriers (unlike land or fixed concrete walls) aren't considered "dual carriageway". This is akin to putting delineators on double solid white lines of a "single carriageway". Splitting any phyiscal barrier is an OSM practice.</p>
</div>
<div id="comment-78031-info" class="comment-info">
<span class="comment-age">(21 Dec '20, 06:25)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="78037"></span>
<div id="comment-78037" class="comment">
<div id="post-78037-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In our area, the delineators are installed to address traffic issues and remain until a permanent curb median can be installed, possibly a year or 2 later.</p>
</div>
<div id="comment-78037-info" class="comment-info">
<span class="comment-age">(21 Dec '20, 12:59)</span> <span class="comment-user userinfo">Mike N</span>
</div>
</div>
</div>
<div id="comment-tools-78016" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78016-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78034"></span>

<div id="answer-container-78034" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78034-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78034-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78034-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Pedestrians can still cross the street there, so I wouldn't re-model the street into a dual carriage way. Instead you should introduce <a href="https://wiki.openstreetmap.org/wiki/Relation:restriction">turn restrictions</a>. In the iD editor you can set restrictions by clicking on the intersection node and then applying the appropriate restrictions in the intersection schematics in the left hand panel.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Dec '20, 09:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-78034" class="comments-container">
<span id="78060"></span>
<div id="comment-78060" class="comment">
<div id="post-78060-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is it possible to do turn restrictions for just certain lanes?</p>
</div>
<div id="comment-78060-info" class="comment-info">
<span class="comment-age">(23 Dec '20, 00:46)</span> <span class="comment-user userinfo">ray331</span>
</div>
</div>
<span id="78065"></span>
<div id="comment-78065" class="comment">
<div id="post-78065-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is some old proposal in the Wiki (I'd have to look for it) that tried to do something like that if I remember correctly.</p>
<p>But why would you think that is necessary? Southbound on Ho'okele you are not allowed to turn left into the parking lot regardless on what lane you are. Coming from the parking lot you are only allowed to turn right. The fact that you are not allowed to turn into the far lane is not really necessary for routing engines and needs to be observed by the driver. But there is also a tagging scheme for <span>lane change restrictions</span> which you could use on the short stretches where the traffic from the marking lot eters Ho'okele.</p>
</div>
<div id="comment-78065-info" class="comment-info">
<span class="comment-age">(23 Dec '20, 21:15)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-78034" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78034-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78038"></span>

<div id="answer-container-78038" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78038-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78038-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78038-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi did you consider to use barrier=kerb, material composite ? Extra are the bollards on top. That could be caught with barrier=bollard (in line) flexible=yes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Dec '20, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-78038" class="comments-container">
&#10;</div>
<div id="comment-tools-78038" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78038-form-container" class="comment-form-container">
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

