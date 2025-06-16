+++
type = "question"
title = "mapping houses with yards"
description = '''Generally, In my region, houses consist of a building and a yard in front/back of that building. how can I map these houses and which tags must I use? Is it Ok using wall for outer range of house and a building within? How can I address them (complete house? wall?!!)'''
date = "2013-06-01T21:23:00Z"
lastmod = "2021-01-18T01:13:00Z"
weight = 22943
keywords = [ "courtyard", "house", "yard" ]
aliases = [ "/questions/22943" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [mapping houses with yards](/questions/22943/mapping-houses-with-yards)

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
<span id="post-22943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22943-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Generally, In my region, houses consist of a building and a yard in front/back of that building. how can I map these houses and which tags must I use? Is it Ok using wall for outer range of house and a building within? How can I address them (complete house? wall?!!)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-courtyard" rel="tag" title="see questions tagged &#39;courtyard&#39;">courtyard</span> <span class="post-tag tag-link-house" rel="tag" title="see questions tagged &#39;house&#39;">house</span> <span class="post-tag tag-link-yard" rel="tag" title="see questions tagged &#39;yard&#39;">yard</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '13, 21:23</strong></p>
<img src="https://secure.gravatar.com/avatar/20a1823ecb217eaea15b2c6827b4cc54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kesler&#39;s gravatar image" />
<p><span>kesler</span><br />
<span class="score" title="86 reputation points">86</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kesler has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22943" class="comments-container">
<span id="22944"></span>
<div id="comment-22944" class="comment">
<div id="post-22944-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>does this give you any ideas <a href="https://www.openstreetmap.org/?lat=52.216143&amp;lon=-0.067283&amp;zoom=18&amp;layers=M">https://www.openstreetmap.org/?lat=52.216143&amp;lon=-0.067283&amp;zoom=18&amp;layers=M</a></p>
</div>
<div id="comment-22944-info" class="comment-info">
<span class="comment-age">(01 Jun '13, 22:57)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-22943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22943-form-container" class="comment-form-container">
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

<span id="22946"></span>

<div id="answer-container-22946" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22946-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-22946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See the page for tagging buildings (with addresses) on the wiki: <a href="https://wiki.openstreetmap.org/wiki/Building">https://wiki.openstreetmap.org/wiki/Building</a></p>
<p>Yards are generally separated by fences, hedges, etc: <a href="https://wiki.openstreetmap.org/wiki/Key:barrier">https://wiki.openstreetmap.org/wiki/Key:barrier</a></p>
<p>For mapping the yards themselves there seem to be three schools of thought (apart from not mapping that much detail at all). The first is most numerous. Mainly because people think the default map becomes too "messy" when tagging that way, the other options were invented.</p>
<ol>
<li><a href="http://taginfo.openstreetmap.org/tags/?key=leisure&amp;value=garden#combinations">Combine leisure=garden with access=private</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Talk:Tag:leisure%3Dgarden">Use residential=garden with or within landuse=residential</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Garden_specification">Combine leisure=garden with garden:type=residential</a></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '13, 23:06</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-22946" class="comments-container">
<span id="78375"></span>
<div id="comment-78375" class="comment">
<div id="post-78375-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I map it if it sticks out from the rest. but good point about it being crowded map, not necessary to have that much detail.</p>
</div>
<div id="comment-78375-info" class="comment-info">
<span class="comment-age">(16 Jan '21, 01:34)</span> <span class="comment-user userinfo">mtbboy1993</span>
</div>
</div>
<span id="78376"></span>
<div id="comment-78376" class="comment">
<div id="post-78376-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>mtbboy, remember not to tag for the renderer. Every detail counts and could be found in the database. Making a map is always a choice for whom its made. A hiker expects other details than a driver, the last wants ways suitable to drive.</p>
</div>
<div id="comment-78376-info" class="comment-info">
<span class="comment-age">(16 Jan '21, 10:55)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="78388"></span>
<div id="comment-78388" class="comment">
<div id="post-78388-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I prioritise the big and noticeable stuff and stuff that stand out when it comes to grass and areas like that.</p>
</div>
<div id="comment-78388-info" class="comment-info">
<span class="comment-age">(18 Jan '21, 01:04)</span> <span class="comment-user userinfo">mtbboy1993</span>
</div>
</div>
<span id="78389"></span>
<div id="comment-78389" class="comment">
<div id="post-78389-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I forgot to mention the map does not show it all, you need to zoom in, so I don't think adding too much detail is an issue. also there are several types of open maps, showing different things. so I add all I can see, but only priority bigger areas first. unless it's a new area then I add all I can.</p>
</div>
<div id="comment-78389-info" class="comment-info">
<span class="comment-age">(18 Jan '21, 01:13)</span> <span class="comment-user userinfo">mtbboy1993</span>
</div>
</div>
</div>
<div id="comment-tools-22946" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22946-form-container" class="comment-form-container">
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

