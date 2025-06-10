+++
type = "question"
title = "How do I fix inconsistent boundaries?"
description = '''I&#x27;ve started doing some work in Massachusetts and noticed that the boundaries around the coastline are aesthetically ugly, as well as inconsistent. The problem seems to be two sets of data (county and state) that don&#x27;t agree. For example, see the area around Logan Airport in Boston, MA or up the coa...'''
date = "2010-10-07T19:14:00Z"
lastmod = "2010-11-28T23:37:00Z"
weight = 1053
keywords = [ "boundaries" ]
aliases = [ "/questions/1053" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I fix inconsistent boundaries?](/questions/1053/how-do-i-fix-inconsistent-boundaries)

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
<span id="post-1053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1053-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've started doing some work in Massachusetts and noticed that the boundaries around the coastline are aesthetically ugly, as well as inconsistent. The problem seems to be two sets of data (county and state) that don't agree. For example, see the area around Logan Airport in Boston, MA or up the coast a bit at Nahant, MA. Neither boundary follows the coastline very closely -- sometime they cut across the land, sometimes they are a ways out. Obviously they were generated to a larger, less accurate scale. What is the best way to:</p>
<p>1) Reconcile the two boundaries so they match, preferably with the current (or adjusted) coastline.</p>
<p>2) Keep the boundaries from displaying along the coastline -- I can see why the boundaries should be there (people may want to extract the shape of the state), but I think the map would look rather strange with a dotted line winding its way all around the coast. Maps such as Google's simply extend the state boundary out to sea when it reaches the coast.</p>
<p>EDIT: OK, I see that other places do indeed have the boundary winding all the way around the coast, so I guess there's no need for 2).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Oct '10, 19:14</strong></p>
<img src="https://secure.gravatar.com/avatar/a5ad728cbc8ae89b774c8c61fbeb20f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OceanVortex&#39;s gravatar image" />
<p><span>OceanVortex</span><br />
<span class="score" title="156 reputation points">156</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OceanVortex has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Oct '10, 01:26</strong> </span></p>
</div>
</div>
<div id="comments-container-1053" class="comments-container">
&#10;</div>
<div id="comment-tools-1053" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1053-form-container" class="comment-form-container">
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

<span id="1079"></span>

<div id="answer-container-1079" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1079-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Note that administrative boundaries are likely to be in a relation, i.e. you will have multiple ways that together form the boundary.</p>
<p>To solve your problem, for the first boundary:</p>
<ul>
<li>Identify the node in the boundary where the boundary should start to run along the coast.</li>
<li>Split the way at that position, if that position is not already one where two separate ways meet.</li>
<li>Identify the node where the boundary should branch inland, away from the coast.</li>
<li>Split the way at that position (as above). If the whole boundary is one circular way, some editors may require that you mark these two nodes at once and then execute the split.</li>
<li>Now delete the boundary way or ways that is/are supposed to coincide with the coastline.</li>
<li>Similar to the above procedure, identify the nodes in the coastline where the boundary should join and leave the coastline, and split the way unless it is already two parts.</li>
<li>Now drag the admin boundary node that is supposed to join the coastline onto the joining node in the coastline, and combine both nodes. (Alternatively extend the admin boundary way by one segment leading up to that coastline node.)</li>
<li>Do the same for the other side, where the boundary leaves the coast.</li>
<li>Finally, add all bits of coastline that now form part of your admin boundary to the boundary relation if there is one. The reason you have split the coastline before is that you can now add only the relevant bits of coastline.</li>
<li>Do not tag the coastline as "boundary=administrative"; being in the relation is enough. Depending on the renderer in use, this will also suppress the coastline being rendered as a boundary.</li>
</ul>
<p>For the second boundary, do the same but of course the coastline will already be split at the right position.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '10, 21:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Oct '10, 21:23</strong> </span></p>
</div>
</div>
<div id="comments-container-1079" class="comments-container">
<span id="1092"></span>
<div id="comment-1092" class="comment">
<div id="post-1092-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your Quote: "Do not tag the coastline as "boundary=administrative"; being in the relation is enough. Depending on the renderer in use, this will also suppress the coastline being rendered as a boundary."</p>
<p>is this generally regarded as 'the thing to do'?. In Italy, municipality boundaries stop at the coast (not at inland lakes, though) Should the boundaries, that follow the coast really not labelled administrative, but only be in relation to the inland borders?</p>
</div>
<div id="comment-1092-info" class="comment-info">
<span class="comment-age">(09 Oct '10, 17:51)</span> <span class="comment-user userinfo">Alexander Ro...</span>
</div>
</div>
<span id="1662"></span>
<div id="comment-1662" class="comment">
<div id="post-1662-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Alexander - I guess you can do whatever you want; tagging the coastline as an admin boundary is not necessary (as the information is already in the relation) but it isn't wrong either. It will, however, cause many renderers to draw a boundary depiction along the coast.</p>
</div>
<div id="comment-1662-info" class="comment-info">
<span class="comment-age">(28 Nov '10, 23:37)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-1079" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1079-form-container" class="comment-form-container">
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

