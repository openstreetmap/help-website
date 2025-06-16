+++
type = "question"
title = "How to tag a road that is oneway only in some parts?"
description = '''Hi I&#x27;ve got a road with six nodes. let&#x27;s start a drawing ---+A --------&amp;gt;+B-----------------------+C&amp;lt;------+D------- with + should represent crossroads. AB is oneway from A to B BC is with no restriction CD is oneway from D to C As the road is the same with continuous numerotation, same name .....'''
date = "2010-09-01T18:20:00Z"
lastmod = "2010-09-04T12:22:00Z"
weight = 727
keywords = [ "tagging", "oneway" ]
aliases = [ "/questions/727" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag a road that is oneway only in some parts?](/questions/727/how-to-tag-a-road-that-is-oneway-only-in-some-parts)

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
<span id="post-727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-727-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I've got a road with six nodes. let's start a drawing</p>
<p>---+A --------&gt;+B-----------------------+C&lt;------+D-------<br />
with + should represent crossroads.<br />
AB is oneway from A to B<br />
BC is with no restriction CD is oneway from D to C<br />
As the road is the same with continuous numerotation, same name ... How should I render it for best ?</p>
<p>Thanks for your answer.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Sep '10, 18:20</strong></p>
<img src="https://secure.gravatar.com/avatar/706aa1178829e8df9b80eca96ea17342?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ebeer&#39;s gravatar image" />
<p><span>Ebeer</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ebeer has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Sep '10, 18:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span></br></p>
</div>
</div>
<div id="comments-container-727" class="comments-container">
<span id="736"></span>
<div id="comment-736" class="comment">
<div id="post-736-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You say "How should I render it". Are you trying to build or configure a <a href="https://wiki.openstreetmap.org/wiki/Rendering">rendering</a> system, and encountering this problem in the data? ...or perhaps you just mean "How should I map it"? (how to arrange the ways and tag it within the editor)</p>
</div>
<div id="comment-736-info" class="comment-info">
<span class="comment-age">(04 Sep '10, 12:22)</span> <span class="comment-user userinfo">Harry Wood</span>
</div>
</div>
</div>
<div id="comment-tools-727" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-727-form-container" class="comment-form-container">
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

<span id="728"></span>

<div id="answer-container-728" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-728-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should split the way at the nodes and then apply the oneway=yes tag only to those ways where it applies, reversing the way where needed. All the tags present in the current way should be the same to the new ways thus specifying that this is the same road.</p>
<p>The resulting 5 ways should look something like this:</p>
<ul>
<li>?A: ref=1, name=Main Street, highway=primary</li>
<li>AB: oneway=yes, ref=1, name=Main Street, highway=primary</li>
<li>BC: ref=1, name=Main Street, highway=primary</li>
<li>DC: oneway=yes, ref=1, name=Main Street, highway=primary</li>
<li>D?: ref=1, name=Main Street, highway=primary</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '10, 18:42</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Sep '10, 18:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span></p>
</div>
</div>
<div id="comments-container-728" class="comments-container">
&#10;</div>
<div id="comment-tools-728" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-728-form-container" class="comment-form-container">
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

