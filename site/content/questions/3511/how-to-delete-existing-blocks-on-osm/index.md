+++
type = "question"
title = "How to delete existing blocks on OSM?"
description = '''We uploaded our GPS trace .How can we make corrections on the pre-existing map details ? Also blocks added are not visible after saving changes. '''
date = "2011-03-04T07:30:00Z"
lastmod = "2011-03-04T11:13:00Z"
weight = 3511
keywords = [ "editing", "tagging" ]
aliases = [ "/questions/3511" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to delete existing blocks on OSM?](/questions/3511/how-to-delete-existing-blocks-on-osm)

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
<span id="post-3511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3511-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We uploaded our GPS trace .How can we make corrections on the pre-existing map details ? Also blocks added are not visible after saving changes.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '11, 07:30</strong></p>
<img src="https://secure.gravatar.com/avatar/5af4fcdeac93a94d7108e3713ea464bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BabuSudhakar&#39;s gravatar image" />
<p><span>BabuSudhakar</span><br />
<span class="score" title="17 reputation points">17</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BabuSudhakar has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '11, 13:08</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span></p>
</div>
</div>
<div id="comments-container-3511" class="comments-container">
&#10;</div>
<div id="comment-tools-3511" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3511-form-container" class="comment-form-container">
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

<span id="3519"></span>

<div id="answer-container-3519" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3519-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-3519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The user <a href="http://www.openstreetmap.org/user/BabuSudhakar">BabuSudhakar</a> has so far only the changesets <a href="http://www.openstreetmap.org/browse/changeset/7444772">7444772</a> and <a href="http://www.openstreetmap.org/browse/changeset/7452141">7452141</a>.</p>
<p>The reason for your additions not showing up on the map, for example <a href="http://www.openstreetmap.org/browse/way/102654160">102654160</a>, is that they have no <a href="http://wiki.openstreetmap.org/wiki/Tags">tags</a>. The renderer doesn't know if the thing you have entered is a house, a fence, a lake or a border etc.</p>
<p>You have to enter at least one tag that describes your object. Read more about it in the <a href="http://wiki.openstreetmap.org/wiki/Beginners_Guide">Beginners Guide</a>, specifically at section <a href="http://wiki.openstreetmap.org/wiki/Beginners_Guide_1.4">Adding Details, and Tagging</a>. If the thing you have entered is a <a href="http://wiki.openstreetmap.org/wiki/Building">building</a> the tags could look like:</p>
<ul>
<li>building = yes</li>
<li>name = The Robotics Institute</li>
</ul>
<p>After you have edited and saved your changes it may take from seconds to hours before the result is rendered and shows up on the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '11, 11:13</strong></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnurk has 18 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '11, 13:11</strong> </span></p>
</div>
</div>
<div id="comments-container-3519" class="comments-container">
&#10;</div>
<div id="comment-tools-3519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3519-form-container" class="comment-form-container">
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

