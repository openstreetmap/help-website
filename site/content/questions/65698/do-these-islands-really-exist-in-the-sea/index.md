+++
type = "question"
title = "Do these islands really exist in the sea?"
description = '''In many cases area objects that require land, for instance island in the sea, lake or river, have an additional tag place=island/islet, like here https://osm.org/go/YnCwtMF--?layers=D&amp;amp;way=12379111 . However, as in the link, we cannot find any islands in the sea. Is this editing practice acceptab...'''
date = "2018-09-02T21:48:00Z"
lastmod = "2018-09-03T13:40:00Z"
weight = 65698
keywords = [ "island", "place", "tagging" ]
aliases = [ "/questions/65698" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Do these islands really exist in the sea?](/questions/65698/do-these-islands-really-exist-in-the-sea)

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
<span id="post-65698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65698-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In many cases area objects that require land, for instance island in the sea, lake or river, have an additional tag place=island/islet, like here <a href="https://osm.org/go/YnCwtMF--?layers=D&amp;way=12379111">https://osm.org/go/YnCwtMF--?layers=D&amp;way=12379111</a> . However, as in the link, we cannot find any islands in the sea. Is this editing practice acceptable?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-island" rel="tag" title="see questions tagged &#39;island&#39;">island</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '18, 21:48</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Sep '18, 13:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-65698" class="comments-container">
&#10;</div>
<div id="comment-tools-65698" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65698-form-container" class="comment-form-container">
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

<span id="65705"></span>

<div id="answer-container-65705" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65705-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The island you are linking to and some other near it are not mapped correctly. Island in the sea have to be mapped with a <em>natural=coastline</em> around its perimeter (unlike islands in rivers or lakes which must not have this tag). In this case they are mapped with <em>natural=wood</em>. To map these correctly, put <em>natural=coastline</em> tags on the ways and add a multipolygon relation for <em>natural=wood</em> tag. Adding a <em>place=island/islet</em> is optional, many islands, especialy unnamed ones don't have it. Traditionally <em>place=island/islet</em> was often used on nodes to mark the place where a label would go, today it can be used also on ways or relations. But for ways it only makes sense really, if the way encloses the whole island. For larger islands this is probably not the case, as the coastline is split into multiple ways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '18, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-65705" class="comments-container">
<span id="65706"></span>
<div id="comment-65706" class="comment">
<div id="post-65706-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah yes, quite right, Jochen. I never noticed the missing coastline. How would one go about setting up a relation to handle both natural=coastline and natural=wood? I have mapped many wooded islands and have always added the wooded area as a separate way.</p>
</div>
<div id="comment-65706-info" class="comment-info">
<span class="comment-age">(03 Sep '18, 10:03)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="65710"></span>
<div id="comment-65710" class="comment">
<div id="post-65710-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For simple islets I just add a second way with coastline or wood as applicable sharing the nodes. I keep multipolygon relations solely for things which have holes or which will get too big. Basically the idea is that this approach is always more obvious in editors than a relation.</p>
</div>
<div id="comment-65710-info" class="comment-info">
<span class="comment-age">(03 Sep '18, 13:40)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65705-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65701"></span>

<div id="answer-container-65701" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65701-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can see several islands or islets in this vicinity, both with DigitalGlobe imagery and Google. There are several other tags on that way that don't make sense, for example, boat=yes, ship=permissive, waterway=river name=Orinoco, so my guess is that the mapper accidentally copied these tags onto the way describing the island but other than that, place=island and natural=wood appear to match reality.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '18, 01:19</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Sep '18, 01:20</strong> </span></p>
</div>
</div>
<div id="comments-container-65701" class="comments-container">
&#10;</div>
<div id="comment-tools-65701" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65701-form-container" class="comment-form-container">
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

