+++
type = "question"
title = "Bridges duplicating highway segments"
description = '''In the north-eastern USA, there are many, many places where highway bridges duplicate a highway road segment. That is to say, a long segment of highway crosses over another road with nodes on the highway just before and after the other road, and there is a segment of highway crossing the other road....'''
date = "2010-12-25T05:27:00Z"
lastmod = "2010-12-26T15:49:00Z"
weight = 1909
keywords = [ "bridge", "highway" ]
aliases = [ "/questions/1909" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Bridges duplicating highway segments](/questions/1909/bridges-duplicating-highway-segments)

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
<span id="post-1909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1909-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the north-eastern USA, there are many, many places where highway bridges duplicate a highway road segment.</p>
<p>That is to say, a long segment of highway crosses over another road with nodes on the highway just before and after the other road, and there is a segment of highway crossing the other road. But, the highway segment that crosses is NOT marked as a bridge. However, there is also a second road segment that has been placed directly on top of the short crossing segment and this second road segment IS marked as a bridge. Sometimes this second segment is tagged with the highway's name and refs, etc, but more often than not it isn't. Of course, running the validator on these segments shows up the overlapping roads.</p>
<p>The fix is to delete the duplicate bridge segment, break the underlying highway into three segments (before, crossing, and after) and tag the crossing segment with a bridge tag.</p>
<p>I have done this now for several roads, recently Connecticut's Merritt Parkway (CT-15), and also the western end of the Long Island Expressway (LIE). But there are many other instances of this problem.</p>
<p>Is it possible to automate the fixing of this problem? I can see many other instances of this on other roads too all over the north-east US: in the NY area, in Connecticut and in Massachusetts and possibly in other areas too. Finding and fixing them all will be lots of work if it has to be done manually.</p>
<p>An example that I have not yet fixed exists on the Long Island Expressway here: 40.7834724N -71.5894013W: select either of the highway bridges and delete it and you will see the underlying road segment.</p>
<p>Thanks, Jaiy.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Dec '10, 05:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0fee73d51555cb4c6fe881f9e56c0e19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaiy&#39;s gravatar image" />
<p><span>Jaiy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaiy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1909" class="comments-container">
&#10;</div>
<div id="comment-tools-1909" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1909-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="1910"></span>

<div id="answer-container-1910" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1910-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It might be possible to make a bot that fixes these problems. But it is hard and there is a chance that other problems might arise. If you look at the history you might discover that some of the duplicated ways are actually made by bots that were trying to fix other part of the TIGER import.</p>
<p>It is better to do it properly manually and maybe fix other problems too then to let loose bots.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Dec '10, 10:31</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-1910" class="comments-container">
&#10;</div>
<div id="comment-tools-1910" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1910-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1911"></span>

<div id="answer-container-1911" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1911-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Trying to fix these problems automatically would probably not be helpful. But there are some tools which can be useful in finding these sort of errors.</p>
<p>One useful tool is <a href="http://keepright.ipax.at/">Keep Right</a>. It shows a map of "overlapping ways" and "intersections without junctions", which seem to be part of the problems you are describing. So worth checking your local area on there, and fixing any errors.</p>
<p>The <a href="http://wiki.openstreetmap.org/wiki/JOSM/Validator">JOSM Validator</a> can also highlight these problems.</p>
<p>Also, as much of these errors are probably from the TIGER import, you could look at the <code>tiger:reviewed</code> tag. If something is tagged as <code>tiger:reviewed=no</code>, that means no one has checked it, so there may be problems with it. I think JOSM highlights everything that has this tag. If you have checked a road, and are pretty sure it is correct, then you can remove this tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Dec '10, 13:52</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-1911" class="comments-container">
&#10;</div>
<div id="comment-tools-1911" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1911-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1920"></span>

<div id="answer-container-1920" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1920-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for those quick replies.</p>
<p>Unfortunately, the dup bridges that I am removing appear to be added by individual contributors - there's no indication they were made by a bot. I can keep on editing them, but it is very slow... the process involves examining an entire highway, often several hundred kilometers long, in close-up mode looking for bridges, and then performing a sequence of edits to remove the dup bridges, split the underlying way, and mark the crossing segments as a bridges. And, given how dense the NY area is, the JOSM downloads can only be done in small areas at a time. So, it is very tedious and time-consuming work. I have been using the JOSM validator to help find these, and it does, but it also finds lots of other errors/warnings nearby that delay the task at hand. Is there a way to use the validator to just validate the entire length of a single way?</p>
<p>As for the TIGER data... I have been leaving that alone. I just read the Wiki pages about the TIGER data and TIGER_fixup, so maybe I will start deleting tiger:reviewed=no tags as I go. But, am I supposed to review all the TIGER fields or just that the road has the correct position, type, name, ref and intersections? I can do this part, but the validity of tags like tiger:source, tiger:tlid and tiger:upload_uuid, I have no idea.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Dec '10, 15:49</strong></p>
<img src="https://secure.gravatar.com/avatar/0fee73d51555cb4c6fe881f9e56c0e19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaiy&#39;s gravatar image" />
<p><span>Jaiy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaiy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1920" class="comments-container">
&#10;</div>
<div id="comment-tools-1920" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1920-form-container" class="comment-form-container">
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

