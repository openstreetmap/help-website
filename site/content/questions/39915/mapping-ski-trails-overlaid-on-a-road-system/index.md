+++
type = "question"
title = "Mapping ski trails overlaid on a road system"
description = '''Im mapping a cross country ski area. The trails are mostly on roads that are already mapped, but most trails are made up of segments of multiple roads, a few contain segments on a road and a segment that is off a road, and sometimes 2 adjacent segments of a road can be different trails. If each trai...'''
date = "2014-12-29T20:26:00Z"
lastmod = "2014-12-30T19:38:00Z"
weight = 39915
keywords = [ "pistemap", "tagging" ]
aliases = [ "/questions/39915" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping ski trails overlaid on a road system](/questions/39915/mapping-ski-trails-overlaid-on-a-road-system)

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
<span id="post-39915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39915-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-39915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Im mapping a cross country ski area. The trails are mostly on roads that are already mapped, but most trails are made up of segments of multiple roads, a few contain segments on a road and a segment that is off a road, and sometimes 2 adjacent segments of a road can be different trails.</p>
<p>If each trail was exactly one road I would add the piste:* tags to the existing ways for the roads.</p>
<p>It seems like the easiest way is to create new ways, that have piste tags, but do not have highway tags. But this seems like it's probably the wrong way to go, as it create multiple ways that are largely the same, but I don't know of a better way to do it.</p>
<p>What is the proper way to map/tag this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pistemap" rel="tag" title="see questions tagged &#39;pistemap&#39;">pistemap</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Dec '14, 20:26</strong></p>
<img src="https://secure.gravatar.com/avatar/495ca47f3e54f74a414401c3d47d9257?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="datamongers&#39;s gravatar image" />
<p><span>datamongers</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="datamongers has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Dec '14, 20:28</strong> </span></p>
</div>
</div>
<div id="comments-container-39915" class="comments-container">
&#10;</div>
<div id="comment-tools-39915" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39915-form-container" class="comment-form-container">
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

<span id="39921"></span>

<div id="answer-container-39921" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39921-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-39921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you'd want to use is a <a href="https://wiki.openstreetmap.org/wiki/Relation:route">route relation</a>, specifically <code>route=ski</code>. You'd want to map the off-road sections as what they best represent (ie. are they hiking trails in the summer?), then add those sections and the relevant pieces of roads as members of a relation. You could then add the piste-specific tags to the relation and this object would represent the entire ski trail. Ways can also be members of multiple relations, so if there's a section that's used by more than one ski trail, it can be added to any relevant relations.</p>
<p>As for the specifics on how to create the relation, that will vary depending on which editor you're using. There should be plenty of information already available around here on creating route relations in the most popular editors.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '14, 00:11</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-39921" class="comments-container">
&#10;</div>
<div id="comment-tools-39921" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39921-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="39916"></span>

<div id="answer-container-39916" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39916-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi datamonger, this Q&amp;A came up by adding 'ski' to the white window above, read these lines <a href="/questions/32084/how-to-tag-something-that-is-a-ski-piste-in-winter-and-a-hiking-trail-in-summer">https://help.openstreetmap.org/questions/32084/how-to-tag-something-that-is-a-ski-piste-in-winter-and-a-hiking-trail-in-summer</a> And more if you want it the next one is useable as well, <a href="/questions/409/how-do-i-tag-a-way-where-there-is-a-cross-country-ski-track-in-winter-only">https://help.openstreetmap.org/questions/409/how-do-i-tag-a-way-where-there-is-a-cross-country-ski-track-in-winter-only</a> . Happy spur</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Dec '14, 20:31</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Dec '14, 20:34</strong> </span></p>
</div>
</div>
<div id="comments-container-39916" class="comments-container">
<span id="39917"></span>
<div id="comment-39917" class="comment">
<div id="post-39917-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hello, and thanks for the answer. Unfortunately I have already looked at the answer you linked to, and it does not provide and answer to my question.</p>
<p>Maybe I should have been more clear.</p>
<p>My question is really about the proper way to map a Way that is made up of segments of several other Ways, and may have segments that are not on an existing Way.</p>
</div>
<div id="comment-39917-info" class="comment-info">
<span class="comment-age">(29 Dec '14, 20:41)</span> <span class="comment-user userinfo">datamongers</span>
</div>
</div>
<span id="39918"></span>
<div id="comment-39918" class="comment">
<div id="post-39918-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi its cross country land ? Just add the ski_trail to a section of the track. If you want to add a route follow the route guide at help and tag all segments together. And if your on the track, thats no conflict, its just another tag on a way.</p>
</div>
<div id="comment-39918-info" class="comment-info">
<span class="comment-age">(29 Dec '14, 22:36)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="39923"></span>
<div id="comment-39923" class="comment">
<div id="post-39923-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd split the road where the piste enters it and/or leaves it. Then the part(s) that are pistes can be so tagged.</p>
<p>Nothing wrong in splitting ways. Done all the time when something changes (bridge, tunnel, paving surface, number of lanes, etc.) Just as there is no issue spitting highway=* ways there is no problem splitting pistes too. For example, I've seen one area where a ungroomed backcountry trail was split several times based on the difficulty of each section.</p>
</div>
<div id="comment-39923-info" class="comment-info">
<span class="comment-age">(30 Dec '14, 06:03)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
</div>
<div id="comment-tools-39916" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39916-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="39937"></span>

<div id="answer-container-39937" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39937-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Simply look here for an example: <a href="http://www.opensnowmap.org/?zoom=16&amp;lat=46.6399&amp;lon=6.16946&amp;layers=&amp;marker=false">http://www.opensnowmap.org/?zoom=16&amp;lat=46.6399&amp;lon=6.16946&amp;layers=&amp;marker=false</a></p>
<p>You can perfectly create a way with piste tags and no highway tag. What you are looking at is not a <strong>way</strong>, but a <strong>route</strong>. In OSM, routes are described with <strong>relation</strong>.</p>
<p>For <a href="https://wiki.openstreetmap.org/wiki/Tag:route%3Dpiste">route=piste</a> (or route=ski, it's about the same) relations, you may want to use <a href="https://wiki.openstreetmap.org/wiki/JOSM">JOSM</a> editor.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '14, 19:38</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-39937" class="comments-container">
&#10;</div>
<div id="comment-tools-39937" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39937-form-container" class="comment-form-container">
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

