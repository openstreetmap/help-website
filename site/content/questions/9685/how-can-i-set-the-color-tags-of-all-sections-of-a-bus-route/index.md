+++
type = "question"
title = "How can I set the color tags of all sections of a bus route ?"
description = '''I missed the color tag. Is there a way to apply the color tag to the whole bus route ? '''
date = "2011-12-29T17:06:00Z"
lastmod = "2012-01-03T14:30:00Z"
weight = 9685
keywords = [ "color", "bus" ]
aliases = [ "/questions/9685" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I set the color tags of all sections of a bus route ?](/questions/9685/how-can-i-set-the-color-tags-of-all-sections-of-a-bus-route)

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
<span id="post-9685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9685-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I missed the color tag. Is there a way to apply the color tag to the whole bus route ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-color" rel="tag" title="see questions tagged &#39;color&#39;">color</span> <span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Dec '11, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/1fb9da36bbe8817c461df33d395ee413?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gerdami&#39;s gravatar image" />
<p><span>gerdami</span><br />
<span class="score" title="696 reputation points">696</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="46 badges"><span class="bronze">●</span><span class="badgecount">46</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gerdami has 2 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-9685" class="comments-container">
&#10;</div>
<div id="comment-tools-9685" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9685-form-container" class="comment-form-container">
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

<span id="9689"></span>

<div id="answer-container-9689" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9689-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-9689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gerdami has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a Public Transport scheme created last April that you should digest if you're interested - see <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Public_Transport">Public Transport</a></p>
<p>You only need to add it once per route.</p>
<p>EITHER add the <strong>colour</strong> key to your <em>route_master</em> relation; OR add the <strong>colour</strong> key to the <em>route</em> relation if you're not using a <em>route_master</em>.</p>
<p>Note the British spelling of this key: <strong>colour</strong></p>
<p>The allowed values are either HTML named colour, or HEX colour. E.g. <strong>colour=#00FF00</strong> gives you green. There are resources on the internet to help you with colour codes.</p>
<p>The specific information you want relates to public transport <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Public_Transport#Route">route</a>, and <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Public_Transport#Route_master">route_master</a></p>
<p>Please note that the Public Transport maps layer that you're probably familiar with does not actually render these colours. From my experience, it just makes all bus routes red, all rail lines black, etc... but I believe there are other systems out there that will use the value of the colour tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Dec '11, 19:34</strong></p>
<img src="https://secure.gravatar.com/avatar/4200f1aaa4fa9ccd4d02db2e8e670de1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wolftracker&#39;s gravatar image" />
<p><span>wolftracker</span><br />
<span class="score" title="475 reputation points">475</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wolftracker has 2 accepted answers">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Dec '11, 10:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-9689" class="comments-container">
<span id="9705"></span>
<div id="comment-9705" class="comment">
<div id="post-9705-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"Note the British spelling of this key: colour." I think there should be an alias color - colour to avoid mistakes, because you all know that the HTML tag is color, not colour.</p>
</div>
<div id="comment-9705-info" class="comment-info">
<span class="comment-age">(30 Dec '11, 10:30)</span> <span class="comment-user userinfo">gerdami</span>
</div>
</div>
<span id="9706"></span>
<div id="comment-9706" class="comment">
<div id="post-9706-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Whether or not something is an "alias" for something else lies in the hands of whoever renders the map. It is possible to make a map that honours the "color" tag, or the "colour" tag, or both, or neither. To the central database, all tags are just key/value combinations and color/colour are as similar as apples/oranges!</p>
</div>
<div id="comment-9706-info" class="comment-info">
<span class="comment-age">(30 Dec '11, 10:33)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="9707"></span>
<div id="comment-9707" class="comment">
<div id="post-9707-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for this explanation on 'route_master'. Is there a chance that it would be integrated within Potlatch2 ?</p>
</div>
<div id="comment-9707-info" class="comment-info">
<span class="comment-age">(30 Dec '11, 10:33)</span> <span class="comment-user userinfo">gerdami</span>
</div>
</div>
<span id="9719"></span>
<div id="comment-9719" class="comment">
<div id="post-9719-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't use Potlatch when working with relations, so the short answer is, I don't know... but you may already be able to do it. Suggest you raise a new question about setting up a public transport route_master in Potlatch so the Potlatch experts can help! Thanks Frederik for your excellent alias response.</p>
</div>
<div id="comment-9719-info" class="comment-info">
<span class="comment-age">(31 Dec '11, 00:19)</span> <span class="comment-user userinfo">wolftracker</span>
</div>
</div>
<span id="9774"></span>
<div id="comment-9774" class="comment not_top_scorer">
<div id="post-9774-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://3liz.fr/public/osmtransport/">http://3liz.fr/public/osmtransport/</a> renders colored bus relations... ;-)</p>
</div>
<div id="comment-9774-info" class="comment-info">
<span class="comment-age">(03 Jan '12, 12:27)</span> <span class="comment-user userinfo">gerdami</span>
</div>
</div>
<span id="9776"></span>
<div id="comment-9776" class="comment">
<div id="post-9776-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The route_master relation type is very rarely used (in just one city so far), has not been discussed widely, and is not in good English. It is very unlikely to be added as a preset in P2 until this changes.</p>
</div>
<div id="comment-9776-info" class="comment-info">
<span class="comment-age">(03 Jan '12, 14:30)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-9689" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-9689-form-container" class="comment-form-container">
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

