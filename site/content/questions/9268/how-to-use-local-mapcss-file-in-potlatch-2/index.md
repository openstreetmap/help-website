+++
type = "question"
title = "How to use local MapCSS file in Potlatch 2"
description = '''What is the easiest way to use a custom map style in Potlatch 2? I guess you can upload the mapcss file to a server or set up a rails port locally, but is there a simpler method? For starters, a text input field where you can paste the style would be great.'''
date = "2011-11-28T18:35:00Z"
lastmod = "2011-11-29T06:43:00Z"
weight = 9268
keywords = [ "potlatch2", "potlatch", "mapcss" ]
aliases = [ "/questions/9268" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to use local MapCSS file in Potlatch 2](/questions/9268/how-to-use-local-mapcss-file-in-potlatch-2)

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
<span id="post-9268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9268-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is the easiest way to use a custom map style in Potlatch 2?</p>
<p>I guess you can upload the mapcss file to a server or set up a rails port locally, but is there a simpler method? For starters, a text input field where you can paste the style would be great.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-potlatch" rel="tag" title="see questions tagged &#39;potlatch&#39;">potlatch</span> <span class="post-tag tag-link-mapcss" rel="tag" title="see questions tagged &#39;mapcss&#39;">mapcss</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Nov '11, 18:35</strong></p>
<img src="https://secure.gravatar.com/avatar/766400faa78a96dce84422cdb20779d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bastik&#39;s gravatar image" />
<p><span>bastik</span><br />
<span class="score" title="651 reputation points">651</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bastik has 5 accepted answers">41%</span></p>
</div>
</div>
<div id="comments-container-9268" class="comments-container">
&#10;</div>
<div id="comment-tools-9268" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9268-form-container" class="comment-form-container">
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

<span id="9269"></span>

<div id="answer-container-9269" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9269-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-9269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bastik has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's no way at present to use a local file of any kind in Potlatch 2, but development work is underway to make loading local files possible.</p>
<p>To <a href="http://wiki.openstreetmap.org/wiki/Potlatch_2/Deploying_Potlatch_2">deploy a custom Potlatch 2 installation</a> you don't need to have your own Rails port. You can just point your PL2 at the main editing API, or at the <a href="http://apis.dev.openstreetmap.org/">dev server</a> for testing. Then it's just a case of uploading your MapCSS file to your web space and configuring it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '11, 18:46</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Nov '11, 20:43</strong> </span></p>
</div>
</div>
<div id="comments-container-9269" class="comments-container">
<span id="9272"></span>
<div id="comment-9272" class="comment">
<div id="post-9272-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, it worked fine with default configuration.</p>
<p>You don't even need to upload anything, the server.rb script starts a local web server. (Only caveat: OAuth doesn't work, so you cannot upload any edits.)</p>
<p>The wiki page says "Pull down all the files from ...". How are you supposed to do that, "wget -r -R '*index.html*'"?</p>
</div>
<div id="comment-9272-info" class="comment-info">
<span class="comment-age">(28 Nov '11, 21:04)</span> <span class="comment-user userinfo">bastik</span>
</div>
</div>
<span id="9281"></span>
<div id="comment-9281" class="comment">
<div id="post-9281-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I used wget to do that. I think there has been talks about a zip file.. Which would be nice I guess.</p>
</div>
<div id="comment-9281-info" class="comment-info">
<span class="comment-age">(29 Nov '11, 06:43)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
</div>
<div id="comment-tools-9269" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9269-form-container" class="comment-form-container">
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

