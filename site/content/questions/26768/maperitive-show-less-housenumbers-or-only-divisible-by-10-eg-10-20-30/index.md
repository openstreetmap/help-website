+++
type = "question"
title = "Maperitive: show less housenumbers or only divisible by 10 (e.g. 10, 20, 30,...)"
description = '''I want to show addr:housenumber on zoom level 16 but for some cities (like Berlin) the street names are covered by house numbers. It looks ok in Maperitive, but if use &quot;generate-tiles&quot;, the numbers are cluttered together. My question is: how can I show &quot;less&quot; house numbers? I posted the rule below. ...'''
date = "2013-09-26T10:32:00Z"
lastmod = "2013-09-26T17:19:00Z"
weight = 26768
keywords = [ "rules", "housenumbers", "maperitive" ]
aliases = [ "/questions/26768" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Maperitive: show less housenumbers or only divisible by 10 (e.g. 10, 20, 30,...)](/questions/26768/maperitive-show-less-housenumbers-or-only-divisible-by-10-eg-10-20-30)

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
<span id="post-26768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26768-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to show addr:housenumber on zoom level 16 but for some cities (like Berlin) the street names are covered by house numbers. It looks ok in Maperitive, but if use "generate-tiles", the numbers are cluttered together.</p>
<p>My question is: how can I show "less" house numbers?</p>
<p>I posted the rule below. I played aroud with placement-value and halo-width, but with no success. The worst actually: the house numbers are rendered above the street names. Even if that wasn't the case, the tiles would work for me.</p>
<p>Another idea was to use regex to only show numbers which end with a "0" - i.e. are divisible by 10.</p>
<p>There is a little documentation about this under feature selector: <a href="http://maperitive.net/docs/Feature_Selectors.html">http://maperitive.net/docs/Feature_Selectors.html</a>. But I don't know how I could parse the value of addr:housenumber through regex.</p>
<p>Any ideas? Thanks, micz</p>
<p>P.S. here some more info and the rules:</p>
<p><a href="http://stackoverflow.com/questions/12403842/check-number-divisibility-with-regular-expressions">http://stackoverflow.com/questions/12403842/check-number-divisibility-with-regular-expressions</a></p>
<pre><code>target : housenumber
    define
        min-zoom : 16
        text : [[addr:housenumber]]
        text-halo-width : 0
        text-color: #666666
        font-weight: normal
        font-size : 13
        placement-value : 0.01
    draw : text</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rules" rel="tag" title="see questions tagged &#39;rules&#39;">rules</span> <span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Sep '13, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/974752b1f7f0af39b1a5e810d8263107?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="micz&#39;s gravatar image" />
<p><span>micz</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="micz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26768" class="comments-container">
<span id="26792"></span>
<div id="comment-26792" class="comment">
<div id="post-26792-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Have you already tried to ask that on <a href="https://groups.google.com/forum/#!forum/maperitive">https://groups.google.com/forum/#!forum/maperitive</a> ?</p>
</div>
<div id="comment-26792-info" class="comment-info">
<span class="comment-age">(26 Sep '13, 17:19)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-26768" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26768-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

