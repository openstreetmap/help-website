+++
type = "question"
title = "Overpass area"
description = '''Hello, i am trying to get areas working on my overpass interpreter following this tutorial: http://wiki.openstreetmap.org/wiki/Overpass_API/Installation#Area_creation when i run the loop i get these errors in my nohup.out (many times) but the loop keeps running and the files are created. i can query...'''
date = "2017-04-27T13:02:00Z"
lastmod = "2017-10-22T18:54:00Z"
weight = 55910
keywords = [ "overpass" ]
aliases = [ "/questions/55910" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass area](/questions/55910/overpass-area)

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
<span id="post-55910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55910-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>i am trying to get areas working on my overpass interpreter following this tutorial: <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Installation#Area_creation">http://wiki.openstreetmap.org/wiki/Overpass_API/Installation#Area_creation</a></p>
<p>when i run the loop i get these errors in my nohup.out (many times) but the loop keeps running and the files are created. i can query the areas but i get no elements:</p>
<ul>
<li>bin/rules_loop.sh: line 40: db//rules_loop.log: No such file or directory</li>
<li>bin/rules_loop.sh: line 41: db//rules/areas.osm3s: No such file or directory</li>
<li>bin/rules_loop.sh: line 42: db//rules_loop.log: No such file or directory</li>
</ul>
<p>it says the theres no such file, but there is. So im wondering what i can do to show the script that the files do exist.</p>
<p>nohup bin/rules_loop.sh db &amp;</p>
<p>That was the line i ran. I can see the script is still active in my ps -ef but im not confident it will finish correctly with these errors.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '17, 13:02</strong></p>
<img src="https://secure.gravatar.com/avatar/df016c4850efd816d96876d5ad7cd935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iggbert&#39;s gravatar image" />
<p><span>iggbert</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iggbert has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55910" class="comments-container">
&#10;</div>
<div id="comment-tools-55910" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55910-form-container" class="comment-form-container">
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

<span id="60219"></span>

<div id="answer-container-60219" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60219-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60219-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60219-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's been a long time since this question was asked...</p>
<p>The rules_loop.sh script needs either an absolute path to the database directory, or a relative path with respect to the bin directory. Note that this is different to all the other tools that need to be started - these require relative paths with respect to the current directory.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '17, 18:54</strong></p>
<img src="https://secure.gravatar.com/avatar/9fbbc400eb10c1432ab84779b6f7e539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mueschel&#39;s gravatar image" />
<p><span>mueschel</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mueschel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60219" class="comments-container">
&#10;</div>
<div id="comment-tools-60219" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60219-form-container" class="comment-form-container">
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

