+++
type = "question"
title = "oneway for the general public, two-way for residents"
description = '''How to tag a street which is one-way for the general public, but two-way for local residents? oneway:destination=no (analogous &quot;oneway:bicycle=no&quot;)?'''
date = "2014-07-31T10:52:00Z"
lastmod = "2014-07-31T23:01:00Z"
weight = 35349
keywords = [ "destination", "tagging", "oneway" ]
aliases = [ "/questions/35349" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [oneway for the general public, two-way for residents](/questions/35349/oneway-for-the-general-public-two-way-for-residents)

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
<span id="post-35349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35349-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How to tag a street which is one-way for the general public, but two-way for local residents? <code>oneway:destination=no</code> (analogous "<code>oneway:bicycle=no</code>")?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jul '14, 10:52</strong></p>
<img src="https://secure.gravatar.com/avatar/b24eed3b0787d840164ae65e6b4c4260?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arathos&#39;s gravatar image" />
<p><span>Arathos</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arathos has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jul '14, 12:01</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-35349" class="comments-container">
&#10;</div>
<div id="comment-tools-35349" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35349-form-container" class="comment-form-container">
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

<span id="35381"></span>

<div id="answer-container-35381" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35381-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-35381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Arathos has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There <em>is</em> an approved tagging scheme for those situations where traffic rules depend on factors such as the time, the weather, or who you are. It's called <a href="http://wiki.openstreetmap.org/wiki/Conditional_restrictions">"conditional restrictions"</a>.</p>
<p>This is how we would do this. First, let's set the default for regular traffic:</p>
<pre><code>oneway = yes</code></pre>
<p>Then set the exception, and for whom this exception applies:</p>
<pre><code>oneway:conditional = no @ destination</code></pre>
<p>By the way, the reason why <code>oneway:destination</code> would not be correct is that, unlike <code>bicycle</code>, <code>destination</code> is not a type of vehicle.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '14, 19:57</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-35381" class="comments-container">
<span id="35385"></span>
<div id="comment-35385" class="comment">
<div id="post-35385-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much!</p>
</div>
<div id="comment-35385-info" class="comment-info">
<span class="comment-age">(31 Jul '14, 23:01)</span> <span class="comment-user userinfo">Arathos</span>
</div>
</div>
</div>
<div id="comment-tools-35381" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35381-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35353"></span>

<div id="answer-container-35353" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35353-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>IMHO it doesn't really matter. Currently there is no established tagging for your scenario (see <a href="http://taginfo.openstreetmap.org/search?q=oneway">http://taginfo.openstreetmap.org/search?q=oneway</a> ), that in turns implies nobody would actually use the tagging (in this specific case it can further be assumed that the residents don't really need to navigate with an app down the road they live on).</p>
<p>In the end you are simply documenting the situation and in such a case the tagging should simply not conflict with existing usage, and as you can see from taginfo it doesn't.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '14, 11:15</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-35353" class="comments-container">
<span id="35382"></span>
<div id="comment-35382" class="comment">
<div id="post-35382-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Whether tagging styles are "established" is of course subjective. However, the ":conditional" suffix is not only approved by a vote, it has also about 50000 uses, although of course distributed across various main keys.</p>
</div>
<div id="comment-35382-info" class="comment-info">
<span class="comment-age">(31 Jul '14, 20:09)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="35384"></span>
<div id="comment-35384" class="comment">
<div id="post-35384-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I would agree with Tordanik that his suggestion is clearly more consistent with the conditional tagging scheme. Using it would increase the likelihood of the tagging being used if ever somebody wanted to modify routing for such a case.</p>
</div>
<div id="comment-35384-info" class="comment-info">
<span class="comment-age">(31 Jul '14, 22:59)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-35353" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35353-form-container" class="comment-form-container">
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

