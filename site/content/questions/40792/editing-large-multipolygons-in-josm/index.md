+++
type = "question"
title = "Editing large multipolygons in JOSM"
description = '''I&#x27;m working away at splitting large multipolygons in northern Thailand into smaller pieces so editing them becomes easier. I&#x27;ve made quite a bit of progress since my last questions in this area. (here and here). I must admit I have not yet tackled the multiple boundary relation problem in the second...'''
date = "2015-02-05T01:48:00Z"
lastmod = "2015-02-12T12:00:00Z"
weight = 40792
keywords = [ "josm", "edits", "multipolygon" ]
aliases = [ "/questions/40792" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Editing large multipolygons in JOSM](/questions/40792/editing-large-multipolygons-in-josm)

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
<span id="post-40792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40792-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm working away at splitting large multipolygons in northern Thailand into smaller pieces so editing them becomes easier. I've made quite a bit of progress since my last questions in this area. (<a href="https://help.openstreetmap.org/questions/40118/editing-large-structures-in-josm-splitting-relations">here</a> and <a href="https://help.openstreetmap.org/questions/40203/josm-how-do-i-select-a-way-for-editing-that-is-part-of-multiple-relations">here</a>). I must admit I have not yet tackled the multiple boundary relation problem in the second link. I understand what needs to be done but it's still too complicated. I am gaining experience though and will attempt it soon.</p>
<p>Now, I'm looking for a way to select and operate on one multipolygon and all of its inner polygons. There is this particular large multipolygon that I have managed to (almost) isolate from its even larger parent and I'm ready to have it stand on its own. Except that it and all its inner members are still members of that larger parent. In order to remove it from that relation and put it into its own new relation means selecting every outer member, and every inner member, removing them from the parent, step by step, and then creating a new multipolygon using all of the many outer members then subsequently adding all the inner members back into it. It seems to me that if I could isolate the whole thing in some way, maybe on its own layer, I could then do that more efficiently.</p>
<p>Hopefully I've explained my goal well enough to get some advice.</p>
<p>Thanks in advance....</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-edits" rel="tag" title="see questions tagged &#39;edits&#39;">edits</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '15, 01:48</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-40792" class="comments-container">
<span id="40802"></span>
<div id="comment-40802" class="comment">
<div id="post-40802-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you speaking about this relation : <a href="http://www.openstreetmap.org/relation/1599039#map=9/18.3363/97.9390">http://www.openstreetmap.org/relation/1599039#map=9/18.3363/97.9390</a> ?</p>
</div>
<div id="comment-40802-info" class="comment-info">
<span class="comment-age">(05 Feb '15, 13:15)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="40803"></span>
<div id="comment-40803" class="comment">
<div id="post-40803-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If it is this relation, then it's easier to remove the left side outer from the existing relation and create a new multipolygon for it (easier because it has only outer ways). To make the editing job easier, you could also add temporarily on your local JOSM a dummy tag on the related ways like "bla=bla" then you can select them later with the "search" tool in JOSM (but don't forget to remove them before you upload your finished work)</p>
</div>
<div id="comment-40803-info" class="comment-info">
<span class="comment-age">(05 Feb '15, 13:18)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="40813"></span>
<div id="comment-40813" class="comment">
<div id="post-40813-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's actually this one, which is a lot easier to edit because the northern part is already separate, or almost separate, after many preparatory edits:</p>
<p><a href="https://www.openstreetmap.org/relation/1339894#map=10/18.9992/99.4270">https://www.openstreetmap.org/relation/1339894#map=10/18.9992/99.4270</a></p>
<p>You can see where my editing stopped with the one you refer to because of the multiple uses of its western edge. True, it doesn't contain any inner areas but the western edge is shared by several boundaries.</p>
<p>In my present case, I want to split off the northern part of the large 254 member multipolygon in the link I supplied just now, the portion north of route 120.</p>
</div>
<div id="comment-40813-info" class="comment-info">
<span class="comment-age">(06 Feb '15, 00:14)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="40949"></span>
<div id="comment-40949" class="comment">
<div id="post-40949-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>if you want to add a tag to an object, but you want to be certain that this tag won't get uploaded to the server, use something like odbl= ore created_by=. There are a few more.</p>
<p>Those tags are not needed anymore and JOSM will discard them before uploading modified objects.</p>
<p>There is also the todo list, which may be an even better idea to use, as it doesn't 'modify' the objects. An object where you add, then subsequently remove a tag, without doing anything else, will still get a new version in its history.</p>
<p>Polyglot</p>
</div>
<div id="comment-40949-info" class="comment-info">
<span class="comment-age">(11 Feb '15, 06:26)</span> <span class="comment-user userinfo">Polyglot</span>
</div>
</div>
<span id="40970"></span>
<div id="comment-40970" class="comment">
<div id="post-40970-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/6242/polyglot">@Polyglot</a>: I think you're suggesting a way to "mark for editing" pieces of the multipolygon I wish to split from the parent. If I"download object" and all its members, I could add a tag created_by=AlaskaDave to all those members, then select them by searching for that tag, delete them from original relation and then select again and add to a new relation. Is that what you're saying?</p>
</div>
<div id="comment-40970-info" class="comment-info">
<span class="comment-age">(12 Feb '15, 04:39)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="40971"></span>
<div id="comment-40971" class="comment not_top_scorer">
<div id="post-40971-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In fact it was Pieren who suggested to add temporary tags to the objects needing your attention. I merely suggested a way to make sure those temporary tags won't be able to make it into the data that gets uploaded. I'm using this trick a lot when preparing data for import/integration.</p>
<p>However, if you find those objects by means of a search, it's better to use JOSM's todo plugin.</p>
<p>Jo</p>
</div>
<div id="comment-40971-info" class="comment-info">
<span class="comment-age">(12 Feb '15, 06:37)</span> <span class="comment-user userinfo">Polyglot</span>
</div>
</div>
<span id="40972"></span>
<div id="comment-40972" class="comment not_top_scorer">
<div id="post-40972-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Quite right. Thanks to both of you for the helpful suggestions.</p>
<p>I use the ToDo plugin fairly often for working on parts of a selection set. Good trick.</p>
</div>
<div id="comment-40972-info" class="comment-info">
<span class="comment-age">(12 Feb '15, 09:00)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-40792" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-40792-form-container" class="comment-form-container">
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

<span id="40959"></span>

<div id="answer-container-40959" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40959-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-40959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AlaskaDave has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As long as we do not want to touch the members at all we can work with incomplete data and only download the relation and its members with <a href="https://josm.openstreetmap.de/wiki/Help/Action/DownloadObject">Download object</a>. The rest can be done within the <a href="https://josm.openstreetmap.de/wiki/Help/Dialog/RelationEditor">relation editor</a> with the last two buttons in the middle panel</p>
<ol>
<li>Download object (relation) with check for downloading members set</li>
<li>Open relation editor, select all members on the left side and sort them (5th button on the left)</li>
<li>Copy/duplicate relation (second button on the top)</li>
<li>Select members to move on the left and move selection to the right side (6th button), then delete selection (7th button)</li>
<li>Select all remaining members on the left and move selection to the right (6th button)</li>
<li>Change to relation editor of copy and delete all selected members (7th button)</li>
<li>Maybe adjust tags of relation - Done</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '15, 13:52</strong></p>
<img src="https://secure.gravatar.com/avatar/764da2975f565c20e7b6770bc3f30276?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skyper&#39;s gravatar image" />
<p><span>skyper</span><br />
<span class="score" title="111 reputation points">111</span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skyper has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Feb '15, 12:06</strong> </span></p>
</div>
</div>
<div id="comments-container-40959" class="comments-container">
<span id="40968"></span>
<div id="comment-40968" class="comment">
<div id="post-40968-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>This is what I was looking for. Thank you very much.</p>
<p>I will experiment with some smaller relations before attacking the one I'm interested in.</p>
</div>
<div id="comment-40968-info" class="comment-info">
<span class="comment-age">(12 Feb '15, 00:23)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="40973"></span>
<div id="comment-40973" class="comment">
<div id="post-40973-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Forgot to mention sorting of members in advance to make it easier. Gonna adjust answer.</p>
</div>
<div id="comment-40973-info" class="comment-info">
<span class="comment-age">(12 Feb '15, 12:00)</span> <span class="comment-user userinfo">skyper</span>
</div>
</div>
</div>
<div id="comment-tools-40959" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40959-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40947"></span>

<div id="answer-container-40947" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40947-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have created an enhancement request in JOSM bugtracker. Might be good to receive an warning from validator to prevent multipolygons growing that large at all.</p>
<p><a href="https://josm.openstreetmap.de/ticket/11101">https://josm.openstreetmap.de/ticket/11101</a></p>
<p>For your polygon: Try adding additional ways to OSM whre you intend to split the polygon, maybe following roads. These will be new and can be added without conflict. The critical time frame to split alt reconnect the polygon will be minimized, reducing the chance of conflicts.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '15, 04:27</strong></p>
<img src="https://secure.gravatar.com/avatar/09b2b8d17e144e0bf320379096429046?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stephan%20Knauss&#39;s gravatar image" />
<p><span>Stephan Knauss</span><br />
<span class="score" title="450 reputation points">450</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stephan Knauss has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Feb '15, 04:30</strong> </span></p>
</div>
</div>
<div id="comments-container-40947" class="comments-container">
<span id="40969"></span>
<div id="comment-40969" class="comment">
<div id="post-40969-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I always add ways to isolate before splitting. The multipolygon I'm presently working with is already isolated that way but I was looking for a method to minimize the time involved in selecting, removing the parts of that multipolygon from its parent and then collecting all those same pieces and with them creating a new, separate multipolygon.</p>
<p>Skyper has given me that method. Thanks for your answer and bugtracker submission.</p>
</div>
<div id="comment-40969-info" class="comment-info">
<span class="comment-age">(12 Feb '15, 04:34)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-40947" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40947-form-container" class="comment-form-container">
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

