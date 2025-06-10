+++
type = "question"
title = "Mapping a radar antenna"
description = '''How would you map this:   It&#x27;s a radar installation operated by the FAA, and a significant local landmark (to give an idea of dimensions, the ball on top measures 60 feet across on an aerial photo, stands 60-80 feet in the air, and is visible from at least 40 miles away on a good day).'''
date = "2016-07-24T09:09:00Z"
lastmod = "2016-07-24T09:53:00Z"
weight = 51070
keywords = [ "radar", "antenna", "tagging" ]
aliases = [ "/questions/51070" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Mapping a radar antenna](/questions/51070/mapping-a-radar-antenna)

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
<span id="post-51070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51070-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How would you map this:</p>
<p><span><img src="//i.imgur.com/ivO9yxcl.jpg" alt="photo of the radar antenna" /></span></p>
<p>It's a radar installation operated by the FAA, and a significant local landmark (to give an idea of dimensions, the ball on top measures 60 feet across on an aerial photo, stands 60-80 feet in the air, and is visible from at least 40 miles away on a good day).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-radar" rel="tag" title="see questions tagged &#39;radar&#39;">radar</span> <span class="post-tag tag-link-antenna" rel="tag" title="see questions tagged &#39;antenna&#39;">antenna</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jul '16, 09:09</strong></p>
<img src="https://secure.gravatar.com/avatar/313c7f1fb7839c95ba6bb396791f56f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carnildo&#39;s gravatar image" />
<p><span>Carnildo</span><br />
<span class="score" title="831 reputation points">831</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carnildo has 2 accepted answers">40%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jul '16, 10:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-51070" class="comments-container">
&#10;</div>
<div id="comment-tools-51070" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51070-form-container" class="comment-form-container">
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

<span id="51072"></span>

<div id="answer-container-51072" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51072-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51072-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-51072-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Carnildo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would go for something like this:</p>
<ul>
<li>building=service</li>
<li><a href="https://wiki.openstreetmap.org/wiki/Tag:man_made%3Dtower">man_made=tower</a></li>
<li>tower:type=radar</li>
<li>tower:construction=dome</li>
<li>height=35</li>
<li>source:height=estimation from side photo and aerial imagery</li>
<li>operator=FAA</li>
<li>seamark:type=landmark</li>
<li>seamark:landmark:category=dome</li>
<li>seamark:landmark:function=radar</li>
<li><a href="https://wiki.openstreetmap.org/wiki/Key:image">image</a>=<a href="https://i.imgur.com/ivO9yxc.jpg">https://i.imgur.com/ivO9yxc.jpg</a></li>
</ul>
<p>(height given in metres, assumed that you mean 0.3048 metre feet. And based on a back-of-the-envelope calculation which resulted in 115 ft total height)</p>
<p>I am not that sure about how useful the seamark stuff is, as it more or less duplicates the other tags. I think that at least if there is marine traffic in that area it might be useful to use those tags too.</p>
<p>And if you know more technical (function) details, over there are additional tag suggestions <a href="https://wiki.openstreetmap.org/wiki/Key:radio_transponder">https://wiki.openstreetmap.org/wiki/Key:radio_transponder</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '16, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jul '16, 17:57</strong> </span></p>
</div>
</div>
<div id="comments-container-51072" class="comments-container">
&#10;</div>
<div id="comment-tools-51072" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51072-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51071"></span>

<div id="answer-container-51071" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51071-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's <a href="http://www.openstreetmap.org/way/160402280">one example</a>. You can use those keys and values to <a href="http://taginfo.openstreetmap.org/search?q=communications_dish#values">search</a> <a href="http://taginfo.openstreetmap.org/tags/?key=building&amp;value=ground_station">taginfo</a>, and see what other people have used. Also look at other similar things elsewhere to come up with other suggestions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '16, 09:49</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-51071" class="comments-container">
&#10;</div>
<div id="comment-tools-51071" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51071-form-container" class="comment-form-container">
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

