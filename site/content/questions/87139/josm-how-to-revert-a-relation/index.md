+++
type = "question"
title = "JOSM: How to revert a relation?"
description = '''JOSM: How to revert a relation? I&#x27;ve a 10 month old changeset where I accidentally deleted all the tags from one of the relations. I wish to revert it. First I downloaded the changeset using the &#x27;revert changeset&#x27; command. I then selected the outer way &amp;amp; used File&amp;gt; Upload selection as recomme...'''
date = "2023-04-18T12:40:00Z"
lastmod = "2023-04-18T19:07:00Z"
weight = 87139
keywords = [ "josm", "revert", "relations" ]
aliases = [ "/questions/87139" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM: How to revert a relation?](/questions/87139/josm-how-to-revert-a-relation)

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
<span id="post-87139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87139-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>JOSM: How to revert a relation?</p>
<p>I've a 10 month old changeset where I accidentally deleted all the tags from one of the relations. I wish to revert it.</p>
<p>First I downloaded the changeset using the 'revert changeset' command. I then selected the outer way &amp; used File&gt; Upload selection as recommended in the first bullet point: <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Reverter#Partial_reverts">https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Reverter#Partial_reverts</a></p>
<p>This only reverted the way by readding tags.</p>
<p>For the second attempt I downloaded using the 'revert changeset' command again. I 'Downloaded incomplete members' to ensure I had the inner way of the relation loaded. I selected the two ways making up the relation. I then used the revert changeset command's 'Revert selection only' option to upload those two ways.</p>
<p>As you can see, the revert re-added tags from four versions previous about 5 years ago!</p>
<p><a href="https://www.openstreetmap.org/relation/2617907/history">https://www.openstreetmap.org/relation/2617907/history</a></p>
<p>I have no filters switched on.</p>
<p>How should I be preforming this action?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '23, 12:40</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-87139" class="comments-container">
&#10;</div>
<div id="comment-tools-87139" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87139-form-container" class="comment-form-container">
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

<span id="87140"></span>

<div id="answer-container-87140" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87140-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DaveF has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://www.openstreetmap.org/changeset/122838356">changeset you are reverting</a> contains versions 5, 6 and 7 of that relation, so reverting the changeset is taking you back to version 4.</p>
<p>In this instance, if it were just the tags you wanted to restore, I'd have used File, Download Object, and downloaded the relation (with referrers and members), then used View History to compare the current version with the version you want, then on the tags from the old version highlight the tags you want to restore (ctrl-click) then right click to restore them (which will create a new version of the relation you can compare with). When happy, upload.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Apr '23, 15:48</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-87140" class="comments-container">
<span id="87141"></span>
<div id="comment-87141" class="comment">
<div id="post-87141-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I'll do that. What's confused me is that i thought Potlatch didn't store different versions of an object in one changeset, but amalgamated any multiple saves into one version when the changeset was closed.</p>
</div>
<div id="comment-87141-info" class="comment-info">
<span class="comment-age">(18 Apr '23, 19:07)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-87140" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87140-form-container" class="comment-form-container">
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

