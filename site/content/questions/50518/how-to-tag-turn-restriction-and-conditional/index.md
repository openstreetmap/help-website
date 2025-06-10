+++
type = "question"
title = "How to tag turn restriction and conditional ?"
description = '''Hi ! I have a traffic_sign which describe:  No left_turn for hgv except for delivery. (in french, sauf livraisons)   My relation start with these tags: type=restriction restriction:hgv=no_left_turn Perhaps i should add restriction:hgv:conditional=none @ delivery What is your opinion about this ?'''
date = "2016-06-29T14:10:00Z"
lastmod = "2016-07-07T14:32:00Z"
weight = 50518
keywords = [ "delivery", "conditional", "turn_restrictions" ]
aliases = [ "/questions/50518" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag turn restriction and conditional ?](/questions/50518/how-to-tag-turn-restriction-and-conditional)

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
<span id="post-50518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50518-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi !</p>
<p>I have a traffic_sign which describe:</p>
<ul>
<li>No left_turn for hgv</li>
<li>except for delivery. (in french, sauf livraisons)</li>
</ul>
<p><img src="http://help.openstreetmap.org/upfiles/no_left_turn.jpg" alt="alt text" /></p>
<p>My relation start with these tags: type=restriction restriction:hgv=no_left_turn</p>
<p>Perhaps i should add restriction:hgv:conditional=none @ delivery</p>
<p>What is your opinion about this ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-delivery" rel="tag" title="see questions tagged &#39;delivery&#39;">delivery</span> <span class="post-tag tag-link-conditional" rel="tag" title="see questions tagged &#39;conditional&#39;">conditional</span> <span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jun '16, 14:10</strong></p>
<img src="https://secure.gravatar.com/avatar/2702b1238bf746bb2e5fa89dfb0fe88c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StephaneP&#39;s gravatar image" />
<p><span>StephaneP</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StephaneP has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jun '16, 14:24</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-50518" class="comments-container">
<span id="50521"></span>
<div id="comment-50521" class="comment">
<div id="post-50521-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>don't know the situation, but wouldn't it be easier to map the restriction on the street? of course this is only possible when the same restriction holds for traffic coming from any side.</p>
</div>
<div id="comment-50521-info" class="comment-info">
<span class="comment-age">(29 Jun '16, 15:21)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="50522"></span>
<div id="comment-50522" class="comment">
<div id="post-50522-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In this case, you're right, it's easier and valid (there is a turn restriction for the backward traffic). On the highway i've added: - hgv=no - hgv:conditional=yes @ delivery</p>
<p>But I'm still curious to know how to map it when there is only one side with this restriction.</p>
</div>
<div id="comment-50522-info" class="comment-info">
<span class="comment-age">(29 Jun '16, 15:29)</span> <span class="comment-user userinfo">StephaneP</span>
</div>
</div>
</div>
<div id="comment-tools-50518" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50518-form-container" class="comment-form-container">
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

<span id="50705"></span>

<div id="answer-container-50705" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50705-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to tag that then the solution is indeed what you wrote, supported by the wiki page <a href="http://wiki.openstreetmap.org/wiki/Conditional_restrictions#Condition">Conditional_restrictions</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '16, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/543f907c30de5772ec0625b82264c188?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grin&#39;s gravatar image" />
<p><span>grin</span><br />
<span class="score" title="158 reputation points">158</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50705" class="comments-container">
&#10;</div>
<div id="comment-tools-50705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50705-form-container" class="comment-form-container">
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

