+++
type = "question"
title = "How should the turn restrictions be added to this junction?"
description = '''Red is not allowed because after the turn it&#x27;s restricted to the 1st lane until it passes the yellow entrance. Only green is allowed. How should the turn restrictions be added to this junction?  '''
date = "2021-07-05T17:55:00Z"
lastmod = "2021-07-06T15:38:00Z"
weight = 80833
keywords = [ "junction", "turn_restrictions" ]
aliases = [ "/questions/80833" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How should the turn restrictions be added to this junction?](/questions/80833/how-should-the-turn-restrictions-be-added-to-this-junction)

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
<span id="post-80833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80833-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Red is not allowed because after the turn it's restricted to the 1st lane until it passes the yellow entrance. Only green is allowed. How should the turn restrictions be added to this junction?</p>
<p><img src="/upfiles/route_ECRGfuO.png" alt="Route" /> <img src="https://i.imgur.com/gqa6G7V.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-junction" rel="tag" title="see questions tagged &#39;junction&#39;">junction</span> <span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jul '21, 17:55</strong></p>
<img src="https://secure.gravatar.com/avatar/5251709eae3d3cb648f498bbd4af06dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rafaelmartinsrm&#39;s gravatar image" />
<p><span>rafaelmartinsrm</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rafaelmartinsrm has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jul '21, 19:26</strong> </span></p>
</div>
</div>
<div id="comments-container-80833" class="comments-container">
&#10;</div>
<div id="comment-tools-80833" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80833-form-container" class="comment-form-container">
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

<span id="80834"></span>

<div id="answer-container-80834" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80834-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80834-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-80834-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The best way to do this may depend on what you mean by "it's restricted to the 1st lane until it passes the yellow entrance".</p>
<p>If you mean there is a physical barrier between the lanes then it may be acceptable to re-work the junction to attach the yellow slipway east of the route in red.</p>
<p>If there is no physical barrier then you will need to use a <a href="https://wiki.openstreetmap.org/wiki/Relation:restriction">turn restriction relation</a>. To me this looks like it would be a <code>restriction=no_left_turn</code> relation between the road segment just after 1 to the road segment 2 is on <code>via</code> the curve shown in red and the section shown between the prohibited U and the yellow.</p>
<p>If the distance was small enough you would be able to edit this using iD's built in turn restriction editor by selecting the node where the illegal turn begins, increasing the 'distance' and 'via' sliders to show the full turn and selecting the origin and prohibited destination.</p>
<p>If the distance is too big you will have to split the ways and create the relation manually. This is a bit tricky in the 'default' iD editor as the way it presents them is reversed for the way they are actually stored. It is workable with a bit of persistence, but they are much easier to edit in something like JOSM (see <a href="https://wiki.openstreetmap.org/wiki/JOSM_Relations_and_Turn_Based_Restrictions">this page</a> for guidance).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jul '21, 19:05</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</img>
</div>
</div>
<div id="comments-container-80834" class="comments-container">
<span id="80835"></span>
<div id="comment-80835" class="comment">
<div id="post-80835-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I added a photo showing the phisical barrier between the lanes, preventing the driver from turning right on the yellow entrance.</p>
</div>
<div id="comment-80835-info" class="comment-info">
<span class="comment-age">(05 Jul '21, 19:27)</span> <span class="comment-user userinfo">rafaelmartinsrm</span>
</div>
</div>
<span id="80836"></span>
<div id="comment-80836" class="comment">
<div id="post-80836-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If this barrier exists all the way back to the U loop then it is <a href="https://wiki.openstreetmap.org/wiki/Editing_Standards_and_Conventions#Divided_highways">probably</a> OK to disconnect the way and reconnect it after the yellow turnoff. The posts being in a continuous stretch of asphalt makes it a little arguable, but I think it's reasonable here unless there is a local convention to do otherwise. It may be worth mapping the <a href="https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dbollard">barrier</a> separately as a signal to other mappers not to revert the change on the basis of a blurry satellite view.</p>
</div>
<div id="comment-80836-info" class="comment-info">
<span class="comment-age">(05 Jul '21, 20:25)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="80838"></span>
<div id="comment-80838" class="comment">
<div id="post-80838-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note: I like iD editor for mapping turn restrictions. It is simple, I find other editors difficult for this task.</p>
</div>
<div id="comment-80838-info" class="comment-info">
<span class="comment-age">(06 Jul '21, 09:34)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="80840"></span>
<div id="comment-80840" class="comment">
<div id="post-80840-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I realised that InsertUser's the answer was the correct one. I wanted to point other mappers struggling with turn restrictions that iD is easy to use. If they did a search for a solution my comment may help them.</p>
</div>
<div id="comment-80840-info" class="comment-info">
<span class="comment-age">(06 Jul '21, 13:58)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="80842"></span>
<div id="comment-80842" class="comment">
<div id="post-80842-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14350/jmapb"></a><a href="https://help.openstreetmap.org/users/14350/jmapb">@jmapb</a> iD has a slider to allow you to use up to 2 <code>via</code> <em>ways</em> if needed. You do need to initiate the turns restrictions interface by selecting the first node of the turn though.</p>
<p>@<a href="https://help.openstreetmap.org/users/644/andy-mackey">andy</a> I was able to find this junction in OSM, unfortunately iD's max search radius (50m) is too small to use their rather neat interface at this location.</p>
</div>
<div id="comment-80842-info" class="comment-info">
<span class="comment-age">(06 Jul '21, 14:44)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="80843"></span>
<div id="comment-80843" class="comment not_top_scorer">
<div id="post-80843-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a> Oh, news to me! I'll try it sometime. Zapped my comment to avoid any confusion.</p>
</div>
<div id="comment-80843-info" class="comment-info">
<span class="comment-age">(06 Jul '21, 15:38)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-80834" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-80834-form-container" class="comment-form-container">
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

