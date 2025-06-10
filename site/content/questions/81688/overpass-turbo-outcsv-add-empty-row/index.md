+++
type = "question"
title = "Overpass Turbo out:csv add empty row"
description = '''A short question: is it possible to enter a user-specific row using Overpass Turbo with out:csv? For example, an empty row? That would help structuring the csv output. Here, an example where I added out:count here and there to get something close to an empty row. Thanks in advance!'''
date = "2021-09-08T15:27:00Z"
lastmod = "2021-09-10T15:49:00Z"
weight = 81688
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/81688" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass Turbo out:csv add empty row](/questions/81688/overpass-turbo-outcsv-add-empty-row)

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
<span id="post-81688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81688-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A short question: is it possible to enter a user-specific row using Overpass Turbo with <em>out:csv</em>? For example, an empty row? That would help structuring the csv output.</p>
<p>Here, an <a href="https://overpass-turbo.eu/s/1b0e">example</a> where I added <em>out:count</em> here and there to get something close to an empty row.</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Sep '21, 15:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ffb12f7c2548687764b2de9e4562d2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G%C3%A5seborg&#39;s gravatar image" />
<p><span>Gåseborg</span><br />
<span class="score" title="311 reputation points">311</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gåseborg has 4 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-81688" class="comments-container">
&#10;</div>
<div id="comment-tools-81688" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81688-form-container" class="comment-form-container">
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

<span id="81704"></span>

<div id="answer-container-81704" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81704-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Gåseborg has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'll probably have to post process it, but you may be able to develop this:</p>
<pre><code>[bbox:{{bbox}}]
[out:csv(name,NewL;false)];
way[leisure]; 
for (t[&quot;leisure&quot;])
{
 make stat
  name=_.val,
  NewL=&#39;\n\n&#39;;
 out tags;
}</code></pre>
<p><a href="https://overpass-turbo.eu/s/1b1E">https://overpass-turbo.eu/s/1b1E</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '21, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-81704" class="comments-container">
<span id="81713"></span>
<div id="comment-81713" class="comment">
<div id="post-81713-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the workaround! I adapted it slightly to make it easier, just using "make ooo ::id="0"; out tags;" see example on <a href="https://overpass-turbo.eu/s/1b3V">https://overpass-turbo.eu/s/1b3V</a></p>
</div>
<div id="comment-81713-info" class="comment-info">
<span class="comment-age">(10 Sep '21, 14:41)</span> <span class="comment-user userinfo">Gåseborg</span>
</div>
</div>
<span id="81714"></span>
<div id="comment-81714" class="comment">
<div id="post-81714-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good. BTW - if you want all of those mapped entities change 'node' to 'nwr'</p>
</div>
<div id="comment-81714-info" class="comment-info">
<span class="comment-age">(10 Sep '21, 15:49)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-81704" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81704-form-container" class="comment-form-container">
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

