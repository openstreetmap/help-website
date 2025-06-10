+++
type = "question"
title = "Marking unadopted roads in the UK"
description = '''I am wanting to properly tag an unadopted road (AKA private street), a term used in the UK for a road that is not maintained by the council it falls under, but by residents of the road itself. However, unlike a private road (or driveway), an unadopted road is still a public highway. It is not design...'''
date = "2021-11-07T01:43:00Z"
lastmod = "2021-11-09T20:11:00Z"
weight = 82501
keywords = [ "unadopted", "highway", "private" ]
aliases = [ "/questions/82501" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Marking unadopted roads in the UK](/questions/82501/marking-unadopted-roads-in-the-uk)

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
<span id="post-82501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82501-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am wanting to properly tag an unadopted road (AKA private street), a term used in the UK for a road that is not maintained by the council it falls under, but by residents of the road itself. However, unlike a private road (or driveway), an unadopted road is still a public highway. It is not designated a public footpath, byway etc. - it is just a public highway. Is there a way to tag this? I was thinking the 'operator' tag but I am not sure what to put. Any advice?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-unadopted" rel="tag" title="see questions tagged &#39;unadopted&#39;">unadopted</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-private" rel="tag" title="see questions tagged &#39;private&#39;">private</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Nov '21, 01:43</strong></p>
<img src="https://secure.gravatar.com/avatar/fd19e70020b017d188191d2e1130adae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nathan_A_RF&#39;s gravatar image" />
<p><span>Nathan_A_RF</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nathan_A_RF has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82501" class="comments-container">
&#10;</div>
<div id="comment-tools-82501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82501-form-container" class="comment-form-container">
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

<span id="82506"></span>

<div id="answer-container-82506" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82506-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82506-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82506-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Nathan_A_RF has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you can't point to the entity maintaining, there's not really a suitable <code>operator=*</code> value yet. In my country, only rarely can you find the name for it somewhere.</p>
<p>There are 328 <a href="https://taginfo.openstreetmap.org/tags/unadopted=yes">https://taginfo.openstreetmap.org/tags/unadopted=yes</a> , plus 10 <a href="https://taginfo.openstreetmap.org/tags/designation=unadopted">https://taginfo.openstreetmap.org/tags/designation=unadopted</a> (if it's not designated as anything) instances. Looks quite fine to use together with <code>access=yes</code> (or the appropriate combination there). The former was mentioned in a certain <a href="https://www.openstreetmap.org/user/alexkemp/diary/39477">https://www.openstreetmap.org/user/alexkemp/diary/39477</a> .</p>
<p>Can't read a clear conclusion from <a href="https://lists.openstreetmap.org/pipermail/talk-gb/2010-May/009588.html">https://lists.openstreetmap.org/pipermail/talk-gb/2010-May/009588.html</a> .</p>
<p>A caveat from my foreign experience: <code>ownership=private</code> is not always correct for these non-government "private" roads. Sometimes it could be held by a cooperative, NGO, or some other form of organization.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '21, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Nov '21, 08:23</strong> </span></p>
</div>
</div>
<div id="comments-container-82506" class="comments-container">
<span id="82533"></span>
<div id="comment-82533" class="comment">
<div id="post-82533-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I'll put unadopted=yes for now.</p>
</div>
<div id="comment-82533-info" class="comment-info">
<span class="comment-age">(09 Nov '21, 20:11)</span> <span class="comment-user userinfo">Nathan_A_RF</span>
</div>
</div>
</div>
<div id="comment-tools-82506" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82506-form-container" class="comment-form-container">
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

