+++
type = "question"
title = "Tirex-Master: missing path"
description = '''Hi, i&#x27;m new at OSM and I tried to install Tirex on debian. I already installed it on Centos successfully but on debian it won&#x27;t work. Every time I try to start the tirex-master I get this message:   missing path at /usr/bin/tirex-master line 518  I have no clue what this means because the line reads...'''
date = "2014-03-15T22:38:00Z"
lastmod = "2014-03-16T22:38:00Z"
weight = 31580
keywords = [ "tirex", "missing_path", "error" ]
aliases = [ "/questions/31580" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tirex-Master: missing path](/questions/31580/tirex-master-missing-path)

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
<span id="post-31580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31580-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, i'm new at OSM and I tried to install Tirex on debian. I already installed it on Centos successfully but on debian it won't work. Every time I try to start the tirex-master I get this message:</p>
<pre><code>    missing path at /usr/bin/tirex-master line 518</code></pre>
<p>I have no clue what this means because the line reads the config directory. When I provide the config dir via -c it doesn't work, too.</p>
<p>Sorry if the question has been posted already. Thanks for help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tirex" rel="tag" title="see questions tagged &#39;tirex&#39;">tirex</span> <span class="post-tag tag-link-missing_path" rel="tag" title="see questions tagged &#39;missing_path&#39;">missing_path</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Mar '14, 22:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a36cd0da8b4e5004f5a80b4ac57d32a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adopin&#39;s gravatar image" />
<p><span>adopin</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adopin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Mar '14, 00:55</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-31580" class="comments-container">
&#10;</div>
<div id="comment-tools-31580" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31580-form-container" class="comment-form-container">
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

<span id="31587"></span>

<div id="answer-container-31587" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31587-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-31587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suggest that you run (as user tirex) the command "strace -f tirex-master -d 2&gt;&amp;1 | less" which will list the system calls that tirex makes; towards the end of the list, just before the program terminates, you will see which files it tried to open and failed. Then check whether you have your config files right.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Mar '14, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-31587" class="comments-container">
<span id="31611"></span>
<div id="comment-31611" class="comment">
<div id="post-31611-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the command. With this command I found the problem: I copied a wrong file into the renderer directory so tirex wanted to load the content of the directory which was not set in the file.</p>
</div>
<div id="comment-31611-info" class="comment-info">
<span class="comment-age">(16 Mar '14, 22:38)</span> <span class="comment-user userinfo">adopin</span>
</div>
</div>
</div>
<div id="comment-tools-31587" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31587-form-container" class="comment-form-container">
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

