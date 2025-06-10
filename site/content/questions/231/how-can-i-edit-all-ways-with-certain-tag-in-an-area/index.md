+++
type = "question"
title = "How can I edit all ways with certain tag in an area?"
description = '''I&#x27;d like to convert some London cycle routes currently tagged with lcn_ref=*, possibly multivalued, with relations. How can I find all ways belonging to a specific cycle route in London, or possibly UK but not larger area and edit them to add them all to a relation and remove the route number from t...'''
date = "2010-07-15T22:41:00Z"
lastmod = "2010-07-17T12:24:00Z"
weight = 231
keywords = [ "editing", "data" ]
aliases = [ "/questions/231" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How can I edit all ways with certain tag in an area?](/questions/231/how-can-i-edit-all-ways-with-certain-tag-in-an-area)

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
<span id="post-231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-231-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to convert some London cycle routes currently tagged with lcn_ref=*, possibly multivalued, with relations. How can I find all ways belonging to a specific cycle route in London, or possibly UK but not larger area and edit them to add them all to a relation and remove the route number from the lcn_ref tag?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jul '10, 22:41</strong></p>
<img src="https://secure.gravatar.com/avatar/e260236f98a32acdb3ce43cc9e1e01a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tko&#39;s gravatar image" />
<p><span>tko</span><br />
<span class="score" title="111 reputation points">111</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tko has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-231" class="comments-container">
&#10;</div>
<div id="comment-tools-231" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-231-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="233"></span>

<div id="answer-container-233" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-233-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tko has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'll want to use the <span>xapi</span> and JOSM. First find the bounds you want by opening JOSM, pressing ctrl-shift-D and selecting the area, then going to the "bookmarks" tab and copying the bounding box coordinates at the top. Close the download window (without downloading anything) and hit ctrl-L, then download <a href="http://xapi.openstreetmap.org/api/0.6/klzzwxh:0000%5bbbox=%5Bpaste">http://xapi.openstreetmap.org/api/0.6/*%5bbbox=[paste</a> the bounding box here]%5d%5blcn_ref=* . After it loads, hit ctrl-F and find "type:way lcn_ref:[route]" (this may return too many; for example if you search for 2 you'll also get 12 and you'll have to remove those). Now add those ways to a new relation. There's no way I know of to automate the generation of roles.</p>
<p>Consider keeping the lcn_ref tags for redundancy; it's much easier to inadvertently screw up a relation than a tag on a way and much harder to restore the relation if you don't have the way tags as backup.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '10, 23:18</strong></p>
<img src="https://secure.gravatar.com/avatar/0c334b9f230e39c1e73a2b0322a23fb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NE2&#39;s gravatar image" />
<p><span>NE2</span><br />
<span class="score" title="1359 reputation points"><span>1.4k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NE2 has one accepted answer">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jul '10, 23:20</strong> </span></p>
</div>
</div>
<div id="comments-container-233" class="comments-container">
<span id="263"></span>
<div id="comment-263" class="comment">
<div id="post-263-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I would just add that you should think very carefully before embarking on this kind of bulk edit. Then stop and think again. Then talk to the community and see if they agree with the change you plan to make. Then just maybe you should start doing the edit.</p>
</div>
<div id="comment-263-info" class="comment-info">
<span class="comment-age">(16 Jul '10, 13:41)</span> <span class="comment-user userinfo">TomH ♦♦</span>
</div>
</div>
<span id="288"></span>
<div id="comment-288" class="comment">
<div id="post-288-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Keeping lcn_ref on the ways is a good point, it can highlight if there's a conflict between the relation and the way tag. But it also means the same information needs to be maintained in two different places; if you don't do it for all new tags it'll slowly lose its meaning.</p>
</div>
<div id="comment-288-info" class="comment-info">
<span class="comment-age">(17 Jul '10, 12:24)</span> <span class="comment-user userinfo">tko</span>
</div>
</div>
</div>
<div id="comment-tools-233" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-233-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="264"></span>

<div id="answer-container-264" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-264-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the area containing the ways isn't too large, it's possible to do this entirely within JOSM:</p>
<p>Start by downloading the area into JOSM. Bring up the search box using Ctrl-F (or the menu item Edit-&gt;Search). The search box offers several features - among them is searching for ways only, and searching for substrings in tag values. There is extensive documentation within the search dialog itself on how to use it.</p>
<p>Using the search dialog, you will select all objects in the downloaded data that match the search. Subsequently, you can perform operations on the entire selection, such as editing tags or adding the selected objects to a relation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '10, 13:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-264" class="comments-container">
&#10;</div>
<div id="comment-tools-264" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-264-form-container" class="comment-form-container">
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

