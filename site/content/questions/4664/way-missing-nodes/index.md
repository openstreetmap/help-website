+++
type = "question"
title = "Way missing nodes"
description = '''Hello, I wonder if someone can explain the following: if you inspect the way id 34342449 you should find a part of the Belgium / French border with 92 Nodes. Looking at Potlatch 1 or 2 this number seems to match roughly. Now if you download the latest planet dump extract for Belgium from GeoFabrik i...'''
date = "2011-04-20T11:53:00Z"
lastmod = "2011-04-20T13:59:00Z"
weight = 4664
keywords = [ "geofabrik", "nodes", "osmosis", "way", "missing" ]
aliases = [ "/questions/4664" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Way missing nodes](/questions/4664/way-missing-nodes)

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
<span id="post-4664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4664-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I wonder if someone can explain the following: if you inspect the way id 34342449 you should find a part of the Belgium / French border with 92 Nodes. Looking at Potlatch 1 or 2 this number seems to match roughly.</p>
<p>Now if you download the latest planet dump extract for Belgium from GeoFabrik it contains the way, but only 26 of the 92 nodes are included - which makes me wonder what I am doing wrong??</p>
<p>Any advice?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Apr '11, 11:53</strong></p>
<img src="https://secure.gravatar.com/avatar/e931b50ab8bee152dde0c68748911508?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ralf71&#39;s gravatar image" />
<p><span>Ralf71</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ralf71 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>07 Sep '12, 14:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a1156d45a55699715b80fc3cadd0c8d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmehl&#39;s gravatar image" />
<p><span>mmehl</span><br />
<span class="score" title="565 reputation points">565</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span></p>
</div>
</div>
<div id="comments-container-4664" class="comments-container">
&#10;</div>
<div id="comment-tools-4664" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4664-form-container" class="comment-form-container">
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

<span id="4666"></span>

<div id="answer-container-4666" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4666-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4666-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4666-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Also note the boundaries of the Geofabrik extracts do not match the country borders mapped in OSM. I think Geofabrik use a somewhat simplified polygon. So in some places, it can have extra bits outside the border, in other places, it can cut bits off inside.</p>
<p>Its usually close enough, you will probably only notice this if trying to use a complete boundary relation, or mapping very close to the borders.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '11, 13:14</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-4666" class="comments-container">
<span id="4667"></span>
<div id="comment-4667" class="comment">
<div id="post-4667-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OSM boundary polygons are often broken so it would not be sensible to rely on them for a daily process. AFAIK France has been broken for the past week, perhaps far longer.</p>
</div>
<div id="comment-4667-info" class="comment-info">
<span class="comment-age">(20 Apr '11, 13:59)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-4666" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4666-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4665"></span>

<div id="answer-container-4665" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4665-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4665-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4665-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are not doing anything wrong: it's a result of the way crossing the border.</p>
<p>Osmosis (the tool used to produce country extracts) gives the option to include either the complete way, or only those nodes which are part of the country in question. It sounds like the extract that you are downloading has been produced using the latter option.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '11, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-4665" class="comments-container">
&#10;</div>
<div id="comment-tools-4665" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4665-form-container" class="comment-form-container">
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

