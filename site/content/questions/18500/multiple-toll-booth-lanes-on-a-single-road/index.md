+++
type = "question"
title = "Multiple toll booth lanes on a single road"
description = '''Hi, I&#x27;m looking for what is considered best practice for a 2 lane road, splitting up to 11 lanes, each with toll booth and gate, just to combine into 2 lanes again. Currently, the toll boths at the Oresund bridge between Sweden and Denmark is created by splitting into multiple roads. I guess that is...'''
date = "2012-12-16T22:24:00Z"
lastmod = "2012-12-17T15:42:00Z"
weight = 18500
keywords = [ "booth", "toll", "lanes", "bestpractice", "splitting" ]
aliases = [ "/questions/18500" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Multiple toll booth lanes on a single road](/questions/18500/multiple-toll-booth-lanes-on-a-single-road)

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
<span id="post-18500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18500-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm looking for what is considered best practice for a 2 lane road, splitting up to 11 lanes, each with toll booth and gate, just to combine into 2 lanes again.</p>
<p>Currently, the <a href="https://www.openstreetmap.org/?lat=55.565834&amp;lon=12.913597&amp;zoom=18&amp;layers=M">toll boths</a> at the Oresund bridge between Sweden and Denmark is created by splitting into multiple roads. I guess that is technically true, but when using GPS and routing, you are told to turn left (depending on routing preferences), which in this case doesn't make sense and would take you to a customer service road. <a href="https://www.openstreetmap.org/?lat=55.3496&amp;lon=11.110139&amp;zoom=18&amp;layers=M">Another place with, similar scenario,</a> the road is just created as a single road.</p>
<p>So I'm a little curious as to what is considered the best way of doing it?</p>
<p>Thanks,</p>
<p>Jesper</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-booth" rel="tag" title="see questions tagged &#39;booth&#39;">booth</span> <span class="post-tag tag-link-toll" rel="tag" title="see questions tagged &#39;toll&#39;">toll</span> <span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-bestpractice" rel="tag" title="see questions tagged &#39;bestpractice&#39;">bestpractice</span> <span class="post-tag tag-link-splitting" rel="tag" title="see questions tagged &#39;splitting&#39;">splitting</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Dec '12, 22:24</strong></p>
<img src="https://secure.gravatar.com/avatar/21fdb756f12afa15f29ba3a25f32619b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jesperd&#39;s gravatar image" />
<p><span>jesperd</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jesperd has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18500" class="comments-container">
&#10;</div>
<div id="comment-tools-18500" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18500-form-container" class="comment-form-container">
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

<span id="18502"></span>

<div id="answer-container-18502" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18502-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jesperd has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Normally, when you can freely switch between the lanes (there are no barriers), a single way is drawn for all lanes together. Of course, here you have these very small toll booths which are barriers between the lanes, so both choices can be argued.</p>
<p>You should note that the navigation device you use is wrong when it says to turn left in the first scenario. It should just say to take a certain lane (keep left or keep right). So you can't use that argument to defend the second way of tagging.</p>
<p>I would (but this is purely personal) draw a single line like in your second example. The part of the lanes that has a barrier between it is too short for me to separate the lanes into multiple ways. Naturally, tags such as width= <em>and lanes=</em> should be provided.</p>
<p>It would also be a great use of the <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/area:highway">area:highway</a> proposal.</p>
<p>As you know, this last part was a personal tagging style I would use, if you want more certainty, contact the <a href="http://lists.openstreetmap.org/listinfo/tagging">tagging mailing list</a> as this has not been really discussed before.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '12, 22:58</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-18502" class="comments-container">
<span id="18529"></span>
<div id="comment-18529" class="comment">
<div id="post-18529-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would also go for a single line and only make seperate ways if access restrictions exist (e.g. seperate toll lanes for cars, trucks, buses). If there is a generally accepted solution for this question, it would be cool to document it somewhere in the Wiki, as this problem occurs more often (e.g. big border crossings).</p>
</div>
<div id="comment-18529-info" class="comment-info">
<span class="comment-age">(17 Dec '12, 13:42)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
<span id="18531"></span>
<div id="comment-18531" class="comment">
<div id="post-18531-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would consider to add the border crossing with the same multiple lanes. But different lane descriptions for a bus, hgv, nothing to declare aso. Or UK residents here.</p>
</div>
<div id="comment-18531-info" class="comment-info">
<span class="comment-age">(17 Dec '12, 15:42)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-18502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18502-form-container" class="comment-form-container">
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

