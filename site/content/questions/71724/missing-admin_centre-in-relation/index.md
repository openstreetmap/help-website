+++
type = "question"
title = "Missing admin_centre in relation"
description = '''Hi, I&#x27;d like to add a node to the members in a relation so as to reflect that a city is the admin_centre of a state, more specifically Ajman (3766482) and Sharjah (3766486), since they are missing.  Is there a way to do this using the &quot;Edit With ID&quot; feature? '''
date = "2019-11-19T14:10:00Z"
lastmod = "2019-12-04T10:36:00Z"
weight = 71724
keywords = [ "node", "member", "relation", "admin_centre" ]
aliases = [ "/questions/71724" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Missing admin_centre in relation](/questions/71724/missing-admin_centre-in-relation)

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
<span id="post-71724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71724-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'd like to add a node to the members in a relation so as to reflect that a city is the admin_centre of a state, more specifically Ajman (3766482) and Sharjah (3766486), since they are missing.</p>
<p>Is there a way to do this using the "Edit With ID" feature?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-member" rel="tag" title="see questions tagged &#39;member&#39;">member</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-admin_centre" rel="tag" title="see questions tagged &#39;admin_centre&#39;">admin_centre</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '19, 14:10</strong></p>
<img src="https://secure.gravatar.com/avatar/6bb7c379dadac2bf492b7fc4b66f6f85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Clinton%20Mercieca&#39;s gravatar image" />
<p><span>Clinton Merc...</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Clinton Mercieca has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71724" class="comments-container">
&#10;</div>
<div id="comment-tools-71724" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71724-form-container" class="comment-form-container">
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

<span id="71748"></span>

<div id="answer-container-71748" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71748-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-71748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Theoretically, it is possible. In practice it gets a bit cumbersome or even impossible. Here's what you have to do:</p>
<ol>
<li>In edit mode select the node that should become admin_centre.</li>
<li>In the left panel scroll down to the bottom and open the section "all relations".</li>
<li>Press the "plus" button underneath. You see a new empty box above.</li>
<li>Click on "select a relation" and select the relation that you want to add the admin_centre to, e.g. Ajman (3766482)</li>
<li>Add "admin_centre" in the "role" field underneath.</li>
</ol>
<p>The problem lies in step 4. As far as I know you cannot manually add a relation there but have to select one of the entries in the drop down list. That list only includes a few entries, though. I suspect some existing member of the relation has to be visible in the editor window for the relation to show up.</p>
<p>For Ajman I succeeded getting the boundary in the relation list like this: I selected the node 262479959 (place=city, name=عجمان). I am guessing this is the admin_centre you want to add. I then scrolled out as much as was possible without losing the selection of the node and moved the map to the northwest so that the node was still visible in the bottom right hand corner of the editor window and the sea became visible in the top left hand corner. At that point the relation 3766482 became available for selection in the drop down list.</p>
<p>So, yes it is possible but would always prefer the JOSM editor over iD if I wanted to do something like this. You might want to give it a try if you can run JAVA apps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Nov '19, 13:32</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Nov '19, 13:33</strong> </span></p>
</div>
</div>
<div id="comments-container-71748" class="comments-container">
<span id="71987"></span>
<div id="comment-71987" class="comment">
<div id="post-71987-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, this was very helpful</p>
</div>
<div id="comment-71987-info" class="comment-info">
<span class="comment-age">(04 Dec '19, 10:36)</span> <span class="comment-user userinfo">Clinton Merc...</span>
</div>
</div>
</div>
<div id="comment-tools-71748" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71748-form-container" class="comment-form-container">
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

