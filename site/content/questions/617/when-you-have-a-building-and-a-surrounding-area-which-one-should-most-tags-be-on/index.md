+++
type = "question"
title = "When you have a building and a surrounding area, which one should most tags be on?"
description = '''For example, a school building and its grounds could both be tagged amenity=school (edit: though apparently this is not the correct way of tagging). But which one should tags like name and operator be applied to?'''
date = "2010-08-10T23:49:00Z"
lastmod = "2010-08-12T03:26:00Z"
weight = 617
keywords = [ "building", "tagging" ]
aliases = [ "/questions/617" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [When you have a building and a surrounding area, which one should most tags be on?](/questions/617/when-you-have-a-building-and-a-surrounding-area-which-one-should-most-tags-be-on)

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
<span id="post-617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-617-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For example, a school building and its grounds could both be tagged amenity=school (edit: though apparently this is not the correct way of tagging). But which one should tags like name and operator be applied to?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Aug '10, 23:49</strong></p>
<img src="https://secure.gravatar.com/avatar/0c334b9f230e39c1e73a2b0322a23fb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NE2&#39;s gravatar image" />
<p><span>NE2</span><br />
<span class="score" title="1359 reputation points"><span>1.4k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NE2 has one accepted answer">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Aug '10, 16:46</strong> </span></p>
</div>
</div>
<div id="comments-container-617" class="comments-container">
<span id="626"></span>
<div id="comment-626" class="comment">
<div id="post-626-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>why was this question voted down? It's a perfectly reasonable question.</p>
</div>
<div id="comment-626-info" class="comment-info">
<span class="comment-age">(11 Aug '10, 08:25)</span> <span class="comment-user userinfo">David Dean</span>
</div>
</div>
<span id="638"></span>
<div id="comment-638" class="comment">
<div id="post-638-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't mind - every downvote takes away only one point, while every upvote gives me 15 points :) Maybe when I grind up into the thousands I'll sell this account on ebay.</p>
</div>
<div id="comment-638-info" class="comment-info">
<span class="comment-age">(12 Aug '10, 03:26)</span> <span class="comment-user userinfo">NE2</span>
</div>
</div>
</div>
<div id="comment-tools-617" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-617-form-container" class="comment-form-container">
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

<span id="622"></span>

<div id="answer-container-622" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-622-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The school building and its grounds should not both be tagged as amenity=school.</p>
<p>Per the <a href="https://wiki.openstreetmap.org/wiki/Good_practice">good practice</a> of "One feature, one OSM-object", only one object should be tagged as amenity=school (assuming there is only one school at that location).</p>
<p>And assuming the school grounds are mapped, it should be tagged as amenity=school, plus name= and operator= etc as appropriate. The school building should be tagged as building=yes, or something like building=school if you want to be more specific.</p>
<p><strong>Note:</strong></p>
<p>The above is for information that applies to the school <em>as a whole</em>, like the name and the type of school. Information specific to one element should still be tagged on that element. For example, if one school building has its own name, or if different buildings have different postal addresses, they should get their own <code>name=</code> or <code>addr:</code> tags.</p>
<p>This may or may not affect the tags for the whole area: In the example, the whole area would still get a <code>name=</code> tag (because the school probably also has a name of its own, just like the building), while it would not get <code>addr:</code> tags (because if different buildings have different addresses, there is no meaningful address for the school as a whole).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '10, 04:03</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Mar '15, 11:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span></p>
</div>
</div>
<div id="comments-container-622" class="comments-container">
<span id="623"></span>
<div id="comment-623" class="comment">
<div id="post-623-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hmmm, OK. So what about a large resort hotel? You want routing software to know where the main check-in building is, but if you tag that as the resort, what do you do with the grounds? If you tag the grounds as tourism=hotel, how do you tell software where to go?</p>
</div>
<div id="comment-623-info" class="comment-info">
<span class="comment-age">(11 Aug '10, 05:37)</span> <span class="comment-user userinfo">NE2</span>
</div>
</div>
<span id="630"></span>
<div id="comment-630" class="comment">
<div id="post-630-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You'd probably have a separate node for the entrance connected to the "site" with a relation. I don't think there are established tags for this, but it may be possible to combine <a href="https://wiki.openstreetmap.org/wiki/Tag:building%3Dentrance">https://wiki.openstreetmap.org/wiki/Tag:building%3Dentrance</a> and <a href="https://wiki.openstreetmap.org/wiki/Relations/Proposed/Site">https://wiki.openstreetmap.org/wiki/Relations/Proposed/Site</a> .</p>
</div>
<div id="comment-630-info" class="comment-info">
<span class="comment-age">(11 Aug '10, 14:13)</span> <span class="comment-user userinfo">RoToRa</span>
</div>
</div>
</div>
<div id="comment-tools-622" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-622-form-container" class="comment-form-container">
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

