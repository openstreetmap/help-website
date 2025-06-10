+++
type = "question"
title = "Different amount of features displayed at different zoom levels"
description = '''I can see the map get more and more detailed when zooming in, while only a selected number of features displayed when zooming out. May I ask how the selection was made by OSM server? Is there a tag explicitly saying which feature should be displayed at which zoom level? '''
date = "2017-08-25T12:37:00Z"
lastmod = "2017-08-26T12:41:00Z"
weight = 58816
keywords = [ "zoomlevel", "level_of_detail" ]
aliases = [ "/questions/58816" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Different amount of features displayed at different zoom levels](/questions/58816/different-amount-of-features-displayed-at-different-zoom-levels)

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
<span id="post-58816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58816-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I can see the map get more and more detailed when zooming in, while only a selected number of features displayed when zooming out. May I ask how the selection was made by OSM server? Is there a tag explicitly saying which feature should be displayed at which zoom level?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-level_of_detail" rel="tag" title="see questions tagged &#39;level_of_detail&#39;">level_of_detail</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '17, 12:37</strong></p>
<img src="https://secure.gravatar.com/avatar/4c6b1343c60b83eaa6e7114be590837d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Digmaa&#39;s gravatar image" />
<p><span>Digmaa</span><br />
<span class="score" title="100 reputation points">100</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Digmaa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58816" class="comments-container">
&#10;</div>
<div id="comment-tools-58816" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58816-form-container" class="comment-form-container">
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

<span id="58817"></span>

<div id="answer-container-58817" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58817-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-58817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming you are referring to the standard style on opensreetmap.org: the rendering of individual elements colour, patterns, labels etc. is defined in a static style file, that contains rules for each zoom level. See <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a> for the source code.</p>
<p>You cannot influence the cartographic decisions by object tagging, nor would that be a sensible thing to implement.</p>
<p>If should be noted that with so called "vector tiles" which are rendered in your browser instead of as bitmaps on a central server, there is a bit more flexibility. However for practical reasons there is still a zoom level based object selection for the contents of the vector tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '17, 12:58</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Aug '17, 12:59</strong> </span></p>
</div>
</div>
<div id="comments-container-58817" class="comments-container">
<span id="58819"></span>
<div id="comment-58819" class="comment">
<div id="post-58819-score" class="comment-score">
-1
</div>
<div class="comment-text">
<p>Interesting question and answers! The question is initially about map generalization. May I get to know map generalization was achieved? Or how to determine which map objects should be removed, or which map objects should be retained?</p>
</div>
<div id="comment-58819-info" class="comment-info">
<span class="comment-age">(25 Aug '17, 15:19)</span> <span class="comment-user userinfo">binjiang</span>
</div>
</div>
<span id="58823"></span>
<div id="comment-58823" class="comment">
<div id="post-58823-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Basically what I wondered is how OSM community deals the issue of automated map generalization from a single largest scale of database. Or just like many mapping agencies, OSM community maintains multiple databases for creating different scales of tiles. Any comments are highly anticipated. Thanks!</p>
</div>
<div id="comment-58823-info" class="comment-info">
<span class="comment-age">(26 Aug '17, 11:23)</span> <span class="comment-user userinfo">binjiang</span>
</div>
</div>
<span id="58824"></span>
<div id="comment-58824" class="comment">
<div id="post-58824-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you have a proper question please ask in in a separate question and neither a comment or an answer.</p>
</div>
<div id="comment-58824-info" class="comment-info">
<span class="comment-age">(26 Aug '17, 11:36)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="58828"></span>
<div id="comment-58828" class="comment">
<div id="post-58828-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To see the discussion that happens about "what gets displayed at what zoom level", have a look at the discussion that takes place on the issues and pull requests over at <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a> . That's just one renderer though.</p>
<p>An example of the actual code that results from this is <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/power.mss#L4">https://github.com/gravitystorm/openstreetmap-carto/blob/master/power.mss#L4</a> - that says "show this at zoom level 14 and higher".</p>
</div>
<div id="comment-58828-info" class="comment-info">
<span class="comment-age">(26 Aug '17, 12:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-58817" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58817-form-container" class="comment-form-container">
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

