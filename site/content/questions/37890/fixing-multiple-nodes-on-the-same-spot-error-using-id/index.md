+++
type = "question"
title = "fixing &quot;multiple nodes on the same spot&quot; error using iD"
description = '''I have been using keep right! to check consistency of my local map, and a regular warning I encounter is &quot;multiple nodes on the same spot&quot;. For example, nodes #3042490495, #3061858823, and #3042490472 are in the same place. Is it possible to merge these using the iD editor?'''
date = "2014-10-23T00:53:00Z"
lastmod = "2014-10-23T01:46:00Z"
weight = 37890
keywords = [ "ideditor", "keepright", "nodes" ]
aliases = [ "/questions/37890" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [fixing "multiple nodes on the same spot" error using iD](/questions/37890/fixing-multiple-nodes-on-the-same-spot-error-using-id)

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
<span id="post-37890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37890-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been using <a href="http://keepright.at">keep right!</a> to check consistency of my local map, and a regular warning I encounter is "multiple nodes on the same spot". For example, nodes <a href="http://www.openstreetmap.org/node/3042490495">#3042490495</a>, <a href="http://www.openstreetmap.org/node/3061858823">#3061858823</a>, and <a href="http://www.openstreetmap.org/node/3042490472">#3042490472</a> are in the same place. Is it possible to merge these using the iD editor?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-keepright" rel="tag" title="see questions tagged &#39;keepright&#39;">keepright</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '14, 00:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a56aacf4d1e927dcd675dfc85cb7e992?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="u003f&#39;s gravatar image" />
<p><span>u003f</span><br />
<span class="score" title="351 reputation points">351</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="u003f has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37890" class="comments-container">
<span id="37891"></span>
<div id="comment-37891" class="comment">
<div id="post-37891-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>A side note, just to be sure: Please note that those are just warnings of potential(!) problems. Please check that those are really problems before you do a change to our data.</p>
</div>
<div id="comment-37891-info" class="comment-info">
<span class="comment-age">(23 Oct '14, 01:12)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-37890" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37890-form-container" class="comment-form-container">
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

<span id="37893"></span>

<div id="answer-container-37893" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37893-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For Potlatch2 or JOSM you could use J or M (keyboard shortcuts), respectively (see also <span>section in DE:Keep Right Users Guide</span> (German)). The merge function in iD (C) seems not to be able to merge nodes which means that you would need to do that manually (copy over tags, way/relation membership and delete the other node(s)).</p>
<p>I suggest to use a more advanced editor (preferably JOSM) to do fixes based on keepright warnings (you seem to be ready to go beyond iD if you care for keepright).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '14, 01:46</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Oct '14, 01:51</strong> </span></p>
</div>
</div>
<div id="comments-container-37893" class="comments-container">
&#10;</div>
<div id="comment-tools-37893" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37893-form-container" class="comment-form-container">
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

