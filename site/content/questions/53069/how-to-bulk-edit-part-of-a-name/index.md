+++
type = "question"
title = "How to bulk edit part of a name?"
description = '''I found a neighbourhood where all roads are tagged as &#x27;West 1 Rd.&#x27;, &#x27;West 2 Rd.&#x27; etc, and I want to rename these to &#x27;West 1 Road&#x27; etc. How do I do this? I downloaded the subjects only using Overpass api, but in JOSM you only seem to be able to bulk edit many names to one name, not replace only part ...'''
date = "2016-11-22T11:12:00Z"
lastmod = "2016-11-24T09:04:00Z"
weight = 53069
keywords = [ "bulk", "josm", "rename", "bulk_editing", "overpass" ]
aliases = [ "/questions/53069" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to bulk edit part of a name?](/questions/53069/how-to-bulk-edit-part-of-a-name)

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
<span id="post-53069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53069-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I found a neighbourhood where all roads are tagged as 'West 1 Rd.', 'West 2 Rd.' etc, and I want to rename these to 'West 1 Road' etc.</p>
<p>How do I do this? I downloaded the subjects only using Overpass api, but in JOSM you only seem to be able to bulk edit many names to one name, not replace only part of the name. I also tried to replace all 'Rd.' by 'Road' using Notepad++, but JOSM won't upload it because I didn't add new timestamps to the objects when doing that.</p>
<p>It's about this area <a href="http://www.openstreetmap.org/#map=16/22.9508/113.2692">http://www.openstreetmap.org/#map=16/22.9508/113.2692</a></p>
<p>(I am aware of the dangers of mechanical edits, but in this case, the number is limited enough to check each result, but too bothersome to do one-by-one)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bulk" rel="tag" title="see questions tagged &#39;bulk&#39;">bulk</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-rename" rel="tag" title="see questions tagged &#39;rename&#39;">rename</span> <span class="post-tag tag-link-bulk_editing" rel="tag" title="see questions tagged &#39;bulk_editing&#39;">bulk_editing</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Nov '16, 11:12</strong></p>
<img src="https://secure.gravatar.com/avatar/545d479d671eeaf68d3eb37d373d7188?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ff5722&#39;s gravatar image" />
<p><span>ff5722</span><br />
<span class="score" title="141 reputation points">141</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ff5722 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53069" class="comments-container">
&#10;</div>
<div id="comment-tools-53069" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53069-form-container" class="comment-form-container">
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

<span id="53078"></span>

<div id="answer-container-53078" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53078-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-53078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ff5722 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For your limited case, this method should work. I tried it a few months ago and it worked for me. Thanks to user escada for the method.</p>
<p>Basically, you use <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">Overpass turbo</a> (<a href="http://overpass-turbo.eu/)">http://overpass-turbo.eu/)</a> to find the objects to edit, then the editor <a href="https://wiki.openstreetmap.org/wiki/Level0">Level0</a> (<a href="http://level0.osmz.ru/)">http://level0.osmz.ru/)</a> to change them.</p>
<p>escada describes the details in <a href="http://www.openstreetmap.org/user/escada/diary/28268">this post on the OpenStreetMap blog</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Nov '16, 12:30</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Nov '16, 08:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span></p>
</div>
</div>
<div id="comments-container-53078" class="comments-container">
<span id="53080"></span>
<div id="comment-53080" class="comment">
<div id="post-53080-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, this worked exactly as I needed it!</p>
</div>
<div id="comment-53080-info" class="comment-info">
<span class="comment-age">(22 Nov '16, 12:47)</span> <span class="comment-user userinfo">ff5722</span>
</div>
</div>
<span id="53082"></span>
<div id="comment-53082" class="comment">
<div id="post-53082-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please note that my diary entry was describing how to fix a number of items that I mapped before. So I had visited them and knew my mapping was wrong or incomplete (fire hydrants &amp; petanque pitches). In general you are not allowed to make such mechanical edits. You should "visit" each place you want to change. As for the URLs in my diary, I could have written a program that attempted to access each URL to really make sure that they were not working. Otherwise you have to follow the mechanical edits policy</p>
</div>
<div id="comment-53082-info" class="comment-info">
<span class="comment-age">(22 Nov '16, 16:58)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="53094"></span>
<div id="comment-53094" class="comment">
<div id="post-53094-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Aren't edits like this allowed (or at least permitted) as long as you check each entry manually? In this case the number was limited enough to let me check each modified name before submitting it.</p>
</div>
<div id="comment-53094-info" class="comment-info">
<span class="comment-age">(24 Nov '16, 09:04)</span> <span class="comment-user userinfo">ff5722</span>
</div>
</div>
</div>
<div id="comment-tools-53078" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53078-form-container" class="comment-form-container">
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

