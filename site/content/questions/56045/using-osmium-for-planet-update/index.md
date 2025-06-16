+++
type = "question"
title = "Using osmium for planet update"
description = '''I&#x27;m currently using osmupdate to update the latest planet to the very recent time: ./osmupdate tmp.pbf updated.pbf --hour --day --keep-tempfiles --drop-author  Now I wanted to try osmium to compare the performance but I cannot find a simple osmium command that does all the magic behind the scene (li...'''
date = "2017-05-05T10:25:00Z"
lastmod = "2017-05-05T22:14:00Z"
weight = 56045
keywords = [ "osmium", "update" ]
aliases = [ "/questions/56045" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Using osmium for planet update](/questions/56045/using-osmium-for-planet-update)

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
<span id="post-56045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56045-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm currently using osmupdate to update the latest planet to the very recent time:</p>
<pre><code>./osmupdate tmp.pbf updated.pbf --hour --day --keep-tempfiles --drop-author</code></pre>
<p>Now I wanted to try osmium to compare the performance but I cannot find a simple osmium command that does all the magic behind the scene (like fetching the necessary change files from the servers), I only found the normal <a href="http://osmcode.org/osmium-tool/manual.html#working-with-change-files">apply-changes command</a>. Is there an osmupdate equivalent for osmium like (?)</p>
<pre><code>./osmium updatemagic tmp.pbf updated.pbf</code></pre>
<p>Related question is <a href="/questions/53298/planet-full-history-update">this</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 May '17, 10:25</strong></p>
<img src="https://secure.gravatar.com/avatar/fec61c70a4cc98b1e84a5dfbde1e9a6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peatar&#39;s gravatar image" />
<p><span>peatar</span><br />
<span class="score" title="351 reputation points">351</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peatar has one accepted answer">8%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 May '17, 10:58</strong> </span></p>
</div>
</div>
<div id="comments-container-56045" class="comments-container">
&#10;</div>
<div id="comment-tools-56045" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56045-form-container" class="comment-form-container">
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

<span id="56059"></span>

<div id="answer-container-56059" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56059-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Frederik Ramm has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no Osmium command that can do that automagically, but there is one in the <a href="http://osmcode.org/pyosmium/">PyOsmium</a> package. It is called <a href="http://docs.osmcode.org/pyosmium/latest/tools_uptodate.html">pyosmium-up-to-date</a> and it uses the Osmium C++ code internally, so it is as fast as Osmium.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '17, 22:14</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-56059" class="comments-container">
&#10;</div>
<div id="comment-tools-56059" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56059-form-container" class="comment-form-container">
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

