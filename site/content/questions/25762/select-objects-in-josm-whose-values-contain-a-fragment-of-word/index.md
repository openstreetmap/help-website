+++
type = "question"
title = "Select objects in JOSM whose values contain a fragment of word"
description = '''I want to select all objects that have the word some in its value. The key is roof:material. I tried &quot;roof:material&quot;=some* and checked the regexp box. It does not find match. The existing values are some parts CGI, some RCC, some RCC some tiles etc.'''
date = "2013-08-25T10:07:00Z"
lastmod = "2013-08-26T00:32:00Z"
weight = 25762
keywords = [ "filter", "josm", "search", "values" ]
aliases = [ "/questions/25762" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Select objects in JOSM whose values contain a fragment of word](/questions/25762/select-objects-in-josm-whose-values-contain-a-fragment-of-word)

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
<span id="post-25762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25762-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to select all objects that have the word <strong>some</strong> in its value. The key is <strong>roof:material</strong>.</p>
<p>I tried <strong>"roof:material"=some*</strong> and checked the regexp box. It does not find match. The existing values are <strong>some parts CGI, some RCC</strong>, <strong>some RCC some tiles</strong> etc.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-values" rel="tag" title="see questions tagged &#39;values&#39;">values</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '13, 10:07</strong></p>
<img src="https://secure.gravatar.com/avatar/651103e616e49724bb139f1a3e0a1a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amritkarma&#39;s gravatar image" />
<p><span>amritkarma</span><br />
<span class="score" title="684 reputation points">684</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amritkarma has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-25762" class="comments-container">
&#10;</div>
<div id="comment-tools-25762" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25762-form-container" class="comment-form-container">
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

<span id="25770"></span>

<div id="answer-container-25770" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25770-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-25770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="amritkarma has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The search function <em>key:valuefragment</em> is what you are looking for (described in the find window). <em>No RegExp</em> needed.</p>
<p>Your key contains the ":" which is a problem here as JOSM uses it as a special character in the search syntax.</p>
<ul>
<li>Use this: <code>roof\:material:some</code> (you can <span>escape</span> it with the "\" (like in RegExps)).</li>
<li>Or use this: <code>"roof:material":some</code> (the enclosing in doublequotes disables the special meaning of the ":" - see the last but one entry in the <span>search examples</span>).</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '13, 11:53</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Aug '13, 12:00</strong> </span></p>
</div>
</div>
<div id="comments-container-25770" class="comments-container">
<span id="25787"></span>
<div id="comment-25787" class="comment">
<div id="post-25787-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Also note, if you do need to use a regexp, that the syntax is different and "some*" does not match what you think, but "som", "some", "somee", "someee", etc. See <a href="https://en.wikipedia.org/wiki/Regular_expression">https://en.wikipedia.org/wiki/Regular_expression</a> Regexps are more powerful but alo more complicated.</p>
</div>
<div id="comment-25787-info" class="comment-info">
<span class="comment-age">(26 Aug '13, 00:32)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-25770" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25770-form-container" class="comment-form-container">
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

