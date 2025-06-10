+++
type = "question"
title = "Get all tags overpass api to display in a html file."
description = '''Hello everyone again. I would like to know how its possible to use the overpass api of OSM to get all tags of one node (by searching the id of the node) and display in a html file. Thank you for all the help. Francisco Costa'''
date = "2016-04-19T11:09:00Z"
lastmod = "2016-04-19T17:09:00Z"
weight = 49295
keywords = [ "newbie", "overpass-api", "tags" ]
aliases = [ "/questions/49295" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get all tags overpass api to display in a html file.](/questions/49295/get-all-tags-overpass-api-to-display-in-a-html-file)

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
<span id="post-49295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49295-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone again.</p>
<p>I would like to know how its possible to use the overpass api of OSM to get all tags of one node (by searching the id of the node) and display in a html file.</p>
<p>Thank you for all the help.</p>
<p>Francisco Costa</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '16, 11:09</strong></p>
<img src="https://secure.gravatar.com/avatar/2d5201d8b00ecd21e515f37b627df3b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FrancisCosta&#39;s gravatar image" />
<p><span>FrancisCosta</span><br />
<span class="score" title="0 reputation points">0</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FrancisCosta has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49295" class="comments-container">
&#10;</div>
<div id="comment-tools-49295" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49295-form-container" class="comment-form-container">
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

<span id="49296"></span>

<div id="answer-container-49296" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49296-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Take a look at this page, especially the custom and popup stuff:</p>
<p><a href="http://overpass-api.de/output_formats.html">http://overpass-api.de/output_formats.html</a></p>
<p>So you can have a link like <a href="http://overpass-api.de/api/interpreter?data=%5Bout:popup%5D;node%2818994998%29;out;">http://overpass-api.de/api/interpreter?data=[out:popup];node%2818994998%29;out;</a> and it will display a simple html page.</p>
<p>I think a lot of the time caching the result of a query on a server will be a better approach.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '16, 17:09</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Apr '16, 19:21</strong> </span></p>
</div>
</div>
<div id="comments-container-49296" class="comments-container">
&#10;</div>
<div id="comment-tools-49296" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49296-form-container" class="comment-form-container">
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

