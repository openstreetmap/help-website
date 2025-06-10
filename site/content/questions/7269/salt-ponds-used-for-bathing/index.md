+++
type = "question"
title = "Salt ponds used for bathing"
description = '''There are some salt water ponds near here. They are part of a large salt extraction process and I have marked them as salt ponds. However, one in particular is used for public bathing. The mud is spread on people and then washed off. As water=salt_pond it isn&#x27;t even rendered in Osmarender. It needs ...'''
date = "2011-08-22T19:08:00Z"
lastmod = "2011-08-23T10:27:00Z"
weight = 7269
keywords = [ "salinas", "salt_pond" ]
aliases = [ "/questions/7269" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Salt ponds used for bathing](/questions/7269/salt-ponds-used-for-bathing)

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
<span id="post-7269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7269-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are some salt water ponds near here. They are part of a large salt extraction process and I have marked them as salt ponds. However, one in particular is used for public bathing. The mud is spread on people and then washed off. As water=salt_pond it isn't even rendered in Osmarender. It needs to be rendered as it is popular (it's a tourist attraction). Is there a way to mark it as:</p>
<ol>
<li>Used for public bathing</li>
<li>Preferably some way of denoting the mud bath use</li>
<li>Having it render (although I suspect using the right tags will solve that issue).</li>
</ol>
<p>As an aside... if it wasn't a salt_pond -- how would I mark the water as salty?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-salinas" rel="tag" title="see questions tagged &#39;salinas&#39;">salinas</span> <span class="post-tag tag-link-salt_pond" rel="tag" title="see questions tagged &#39;salt_pond&#39;">salt_pond</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '11, 19:08</strong></p>
<img src="https://secure.gravatar.com/avatar/f975d12117093ce5b3b4748dc4927400?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobChafer&#39;s gravatar image" />
<p><span>RobChafer</span><br />
<span class="score" title="220 reputation points">220</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobChafer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7269" class="comments-container">
<span id="7272"></span>
<div id="comment-7272" class="comment">
<div id="post-7272-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Does the pond that does not render have natural=water, as well as water=salt_pond?</p>
</div>
<div id="comment-7272-info" class="comment-info">
<span class="comment-age">(23 Aug '11, 08:02)</span> <span class="comment-user userinfo">Ebenezer</span>
</div>
</div>
</div>
<div id="comment-tools-7269" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7269-form-container" class="comment-form-container">
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

<span id="7273"></span>

<div id="answer-container-7273" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7273-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7273-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-7273-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RobChafer has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>Sounds to me as well that you might have forgotten to add <a href="http://wiki.openstreetmap.org/wiki/Key:water">natural=water</a> to you water=salt_pond</li>
<li>Since it's a tourist attraction, dont forget the name and the <a href="http://wiki.openstreetmap.org/wiki/Tourism">tourism</a> tags. Maybe you can use your own value for the tourism tag here to specify it's a mud bath ? - check <a href="http://taginfo.openstreetmap.org/keys/?key=tourism#values">taginfo</a>.</li>
<li>Another tag to check is <a href="http://wiki.openstreetmap.org/wiki/Key:leisure">leisure</a> (=swimming_pool ?). Again, browse taginfo.</li>
<li><a href="http://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">Dont tag for the renderer</a>.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '11, 10:22</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Aug '11, 14:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-7273" class="comments-container">
<span id="7274"></span>
<div id="comment-7274" class="comment">
<div id="post-7274-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep, I had forgotten natural=water. Thanks for your help.</p>
</div>
<div id="comment-7274-info" class="comment-info">
<span class="comment-age">(23 Aug '11, 10:27)</span> <span class="comment-user userinfo">RobChafer</span>
</div>
</div>
</div>
<div id="comment-tools-7273" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7273-form-container" class="comment-form-container">
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

