+++
type = "question"
title = "Adding relations by using a GPX-file"
description = '''Hi I have some GPX-files (official local MTB-tracks) that I want to import in OSM. Therefore I&#x27;m looking for a way to select the roads that overlap with the GPX-route so I can add a relation to them. Any suggestions on how I could do this easily? Kind regards Yves'''
date = "2020-11-27T10:12:00Z"
lastmod = "2020-11-27T11:36:00Z"
weight = 77745
keywords = [ "routes", "import", "gpx", "relations" ]
aliases = [ "/questions/77745" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Adding relations by using a GPX-file](/questions/77745/adding-relations-by-using-a-gpx-file)

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
<span id="post-77745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77745-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I have some GPX-files (official local MTB-tracks) that I want to import in OSM. Therefore I'm looking for a way to select the roads that overlap with the GPX-route so I can add a relation to them.</p>
<p>Any suggestions on how I could do this easily?</p>
<p>Kind regards Yves</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routes" rel="tag" title="see questions tagged &#39;routes&#39;">routes</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Nov '20, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/9929a4545d147980d053515b44f5e0fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yves%20Mu&#39;s gravatar image" />
<p><span>Yves Mu</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yves Mu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77745" class="comments-container">
&#10;</div>
<div id="comment-tools-77745" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77745-form-container" class="comment-form-container">
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

<span id="77746"></span>

<div id="answer-container-77746" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77746-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Yves Mu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Given that you will likely have to split roads along the way I don't believe that there is currently any fully automatic way to do this. Your best bet on a desktop is to use JOSM to display the track over the data and then just split the ways where necessary and add them to the route relation.</p>
<p>A bit more luxurious would be what we are doing in <a href="https://twitter.com/vespucci_editor/status/1305863889607852032">https://twitter.com/vespucci_editor/status/1305863889607852032</a> which automatically splits and adds route segments,and would work with a GPX overlay too, maybe there is a JOSM plugin that does the same.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Nov '20, 11:36</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-77746" class="comments-container">
&#10;</div>
<div id="comment-tools-77746" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77746-form-container" class="comment-form-container">
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

