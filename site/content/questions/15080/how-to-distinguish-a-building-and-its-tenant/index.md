+++
type = "question"
title = "How to distinguish a building and its tenant?"
description = '''Basically I&#x27;m running into cases where the building has an established name (usually because it&#x27;s an historic building), but is currently occupied by an amenity which bears a different name. The specific case I ran into is the American Security and Trust Company Building, currently occupied by a Ban...'''
date = "2012-08-14T16:48:00Z"
lastmod = "2012-08-14T17:33:00Z"
weight = 15080
keywords = [ "building", "amenity", "name", "tagging" ]
aliases = [ "/questions/15080" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to distinguish a building and its tenant?](/questions/15080/how-to-distinguish-a-building-and-its-tenant)

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
<span id="post-15080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15080-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Basically I'm running into cases where the building has an established name (usually because it's an historic building), but is currently occupied by an amenity which bears a different name.</p>
<p>The specific case I ran into is the <a href="http://www.openstreetmap.org/browse/way/48056817">American Security and Trust Company Building</a>, currently occupied by a <a href="http://www.openstreetmap.org/browse/node/751881364">Bank of America branch</a>. It's slightly less an issue where, like here, both names are "related" (BoA is the ultimate successor of American Security and Trust), but what of the <a href="http://www.openstreetmap.org/browse/way/171562484">New York Savings Bank building</a>, currently occupied by a <a href="http://www.openstreetmap.org/browse/node/1825739832">CVS pharmacy</a> (and previously by a Balducci's supermarket)?</p>
<p>I disapprove of the building-node separation currently in place, but none of the current tagging schemes for multiple names work: clearly the names here refer to different <em>thing</em> (the structure's name, and the amenity/tenant's name), not variant names for one of the two things. It is also clearly not an <code>addr:housename</code>, because it is not used for addressing.</p>
<p>I know very well about the "no tagging for the renderer" mantra, but either way this results in unsatisfying tagging (if only because the more lasting feature, the building, gets tagged with the least lasting). Anybody got suggestions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '12, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/01d01832dff61a6bcf68913f1dc001bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Circeus&#39;s gravatar image" />
<p><span>Circeus</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Circeus has 2 accepted answers">7%</span></p>
</div>
</div>
<div id="comments-container-15080" class="comments-container">
&#10;</div>
<div id="comment-tools-15080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15080-form-container" class="comment-form-container">
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

<span id="15084"></span>

<div id="answer-container-15084" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15084-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My first thought would be to separate between node and contour. As the new amenity or shop in that building probably doesn't use the entire building, that split up would make sense.</p>
<p>Otherwise, you could split between name and operator (the Bank of America is operating the American Security and Trust company building).</p>
<p>Or use name for the current name, and old_name for the name it used to have, but is still visible on the building.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '12, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-15084" class="comments-container">
<span id="15085"></span>
<div id="comment-15085" class="comment">
<div id="post-15085-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Node/contour doesn't work in these cases (if it did I'd do that: I use it for malls, for example). old_name doesn't work. The building hasn't changed name, only its occupier changed (and fairly recently too). Operator is pretty close though! I'm not editing right now but I'll consider that option.</p>
</div>
<div id="comment-15085-info" class="comment-info">
<span class="comment-age">(14 Aug '12, 17:33)</span> <span class="comment-user userinfo">Circeus</span>
</div>
</div>
</div>
<div id="comment-tools-15084" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15084-form-container" class="comment-form-container">
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

