+++
type = "question"
title = "How to tag a parking that requires a fee only at &quot;bathing weather&quot;"
description = '''Recently I came across a parking space at a public bathing beach that requires a fee with some very very fuzzy condition: a fee is required &quot;at bathing weather&quot;, which is not specified any further. The parking can be used all the time, but at certain times there&#x27;s someone sitting there and collectin...'''
date = "2014-07-03T12:21:00Z"
lastmod = "2014-07-04T09:39:00Z"
weight = 34586
keywords = [ "seasonal", "opening_hours", "tagging" ]
aliases = [ "/questions/34586" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag a parking that requires a fee only at "bathing weather"](/questions/34586/how-to-tag-a-parking-that-requires-a-fee-only-at-bathing-weather)

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
<span id="post-34586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34586-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Recently I came across a parking space at a public bathing beach that requires a fee with some very very fuzzy condition: a fee is required "at bathing weather", which is not specified any further. The parking can be used all the time, but at certain times there's someone sitting there and collecting a fee at the entrance. I guess they just place someone there to collect a fee when they expect more than <em>x</em> cars to park park there so that the return on investment (i.e. paying someone to collect the fee) is positive.</p>
<p>The question is, is there a way to map that? I fear, there's no "soft" tag that directly allows to enter such a fuzzy condition, but maybe some opening hours like style might work. I came across the <a href="https://wiki.openstreetmap.org/wiki/Key:conditional">conditional restrictions</a> wiki page, but this seems to only apply for access rules. With this one could specify a condition that tries to reproduce the situation as good as possible, for example by requiring a fee from may to september from 9:00 to 17:00. Surely there will be days within in this time where noone asks for a fee, but if you expect a fee and don't have to pay one is better than arriving there to see that a fee is required. But does the conditional scheme also apply for other tags than <code>access</code>?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-seasonal" rel="tag" title="see questions tagged &#39;seasonal&#39;">seasonal</span> <span class="post-tag tag-link-opening_hours" rel="tag" title="see questions tagged &#39;opening_hours&#39;">opening_hours</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jul '14, 12:21</strong></p>
<img src="https://secure.gravatar.com/avatar/08858c52af8d4cabb3fef25d99a94a5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bbauer&#39;s gravatar image" />
<p><span>bbauer</span><br />
<span class="score" title="86 reputation points">86</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bbauer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34586" class="comments-container">
&#10;</div>
<div id="comment-tools-34586" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34586-form-container" class="comment-form-container">
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

<span id="34593"></span>

<div id="answer-container-34593" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34593-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34593-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-34593-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bbauer has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Answering the last part first:</p>
<pre><code>But does the conditional scheme also apply for other tags than access?</code></pre>
<p>Yes, it gets used quite a lot for things like maxweight, etc.</p>
<p>With regard to the first part I wouldn't worry too much about translating your knowledge about when the fee is collected into OSM tags. I'd just make sure that what you know is tagged in English (perhaps as "fee=bathing_weather", perhaps as a note, perhaps as something else), and let people who worry about consuming the data decide what to do when they encounter it.</p>
<p>Essentially, mappers are OSM's scarcest resource, and anything that frees up their time to do more mapping is good, even if it requires data consumers to handle exceptions. It may also, as has happened with "opening hours", cause the people who care about ensuring that the data in that tag is machine readable to better define exceptions for English statements just like this one.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '14, 14:23</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jul '14, 12:13</strong> </span></p>
</div>
</div>
<div id="comments-container-34593" class="comments-container">
&#10;</div>
<div id="comment-tools-34593" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34593-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="34589"></span>

<div id="answer-container-34589" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34589-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How about simply not inventing a new tag for it? Unless this parking is in some tropical location, most of the time it is free. The other condition is so fuzzy, that no matter what tag you invent, it will never be used by any tool consuming OSM data.</p>
<p>So simply put this information into a description or note tag. At least then there is a small chance it will be seen some time.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '14, 13:54</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-34589" class="comments-container">
<span id="34592"></span>
<div id="comment-34592" class="comment">
<div id="post-34592-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>or "fee=seasonal"</p>
</div>
<div id="comment-34592-info" class="comment-info">
<span class="comment-age">(03 Jul '14, 14:18)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="34630"></span>
<div id="comment-34630" class="comment">
<div id="post-34630-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My intention was <strong>not</strong> to create another tag that is used only once, but to find a way to use the existing tags to fit the given situation at least as good as possible. Even if the parking is not in a tropical area and therefore free most of the time, this information is not of great use, as the parking is only used to get to the bathing beach, i.e. when it's bathing weather...</p>
</div>
<div id="comment-34630-info" class="comment-info">
<span class="comment-age">(04 Jul '14, 09:39)</span> <span class="comment-user userinfo">bbauer</span>
</div>
</div>
</div>
<div id="comment-tools-34589" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34589-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="34603"></span>

<div id="answer-container-34603" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34603-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-34603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>'Opening hours' may be another good way to handle this one actually, on the parking lot.</p>
<p>opening_hours=sunrise-sunset open "Fee in 'Bathing weather'"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '14, 18:28</strong></p>
<img src="https://secure.gravatar.com/avatar/41e323a2904da3bb06060a206cefc025?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Skybunny&#39;s gravatar image" />
<p><span>Skybunny</span><br />
<span class="score" title="60 reputation points">60</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Skybunny has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34603" class="comments-container">
&#10;</div>
<div id="comment-tools-34603" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34603-form-container" class="comment-form-container">
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

