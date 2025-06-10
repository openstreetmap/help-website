+++
type = "question"
title = "Nominatim import --osm2pgsql-cache X parameter"
description = '''Hi guys, i have little doubt, I tried to find it out over google but I found conflicting opinions. I&#x27;m installing nominatim 2.3.1 following the wiki guide. For the map import I use the command: ./utils/setup.php --osm-file &amp;lt;map&amp;gt; --all --osm2pgsql-cache &amp;lt;x&amp;gt; 2&amp;gt;&amp;amp;1 | tee setup.log  No...'''
date = "2015-10-26T14:16:00Z"
lastmod = "2018-11-04T16:22:00Z"
weight = 46129
keywords = [ "nominatim" ]
aliases = [ "/questions/46129" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim import --osm2pgsql-cache X parameter](/questions/46129/nominatim-import-osm2pgsql-cache-x-parameter)

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
<span id="post-46129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46129-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys, i have little doubt, I tried to find it out over google but I found conflicting opinions. I'm installing nominatim 2.3.1 following the wiki guide. For the map import I use the command:</p>
<pre><code>./utils/setup.php --osm-file &lt;map&gt; --all --osm2pgsql-cache &lt;x&gt; 2&gt;&amp;1 | tee setup.log</code></pre>
<p>Now I would like to know how to set the 'x' parameter. Someone said that I have to set it with the amount value of my machine RAM, other said to set it with half of my machine RAM. Still others say to set it with '18000' regardless the amoun of my RAM.</p>
<p>Please help me because I wouldn't make mistakes beacuse the process is damned long and I don't want to restart it again.</p>
<p>Thanks a lot Giacomo</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Oct '15, 14:16</strong></p>
<img src="https://secure.gravatar.com/avatar/e6e1580c3bf447dab7c4a377186b60dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="giacomo-keybiz&#39;s gravatar image" />
<p><span>giacomo-keybiz</span><br />
<span class="score" title="33 reputation points">33</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="giacomo-keybiz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46129" class="comments-container">
&#10;</div>
<div id="comment-tools-46129" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46129-form-container" class="comment-form-container">
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

<span id="66655"></span>

<div id="answer-container-66655" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66655-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This appears to be poorly documented (what units is &lt;x&gt; measured in? for example)?</p>
<p>Based on my reading, the units are MB and you should tune the value to be ~ 2/3s of your available RAM on your system. You want to avoid swapping at all costs because it will slow things down.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Nov '18, 16:22</strong></p>
<img src="https://secure.gravatar.com/avatar/dabc2477fcb5006a22c9eefb48d75b90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="d%C3%B3nal&#39;s gravatar image" />
<p><span>dónal</span><br />
<span class="score" title="156 reputation points">156</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dónal has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-66655" class="comments-container">
&#10;</div>
<div id="comment-tools-66655" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66655-form-container" class="comment-form-container">
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

