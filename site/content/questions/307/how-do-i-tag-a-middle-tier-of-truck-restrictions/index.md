+++
type = "question"
title = "How do I tag a middle tier of truck restrictions?"
description = '''New York City has three tiers of truck routes: through, local, and undesignated. The former is hgv=yes and the latter is hgv=destination. (There are also some hgv=no roads.) Local truck routes are also, to some extent, hgv=destination, but allow trucks with a destination in the same borough (NYC has...'''
date = "2010-07-18T05:31:00Z"
lastmod = "2010-07-22T16:05:00Z"
weight = 307
keywords = [ "hgv", "truck", "tagging" ]
aliases = [ "/questions/307" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I tag a middle tier of truck restrictions?](/questions/307/how-do-i-tag-a-middle-tier-of-truck-restrictions)

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
<span id="post-307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-307-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>New York City has <span>three tiers</span> of truck routes: through, local, and undesignated. The former is hgv=yes and the latter is hgv=destination. (There are also some hgv=no roads.) Local truck routes are also, to some extent, hgv=destination, but allow trucks with a destination in the same borough (NYC has five boroughs). In other words, a truck bound for Lower Manhattan could enter Manhattan at the other end and use a local truck route, while hgv=destination on this local route would imply that it cannot do this, but has to use a through truck route most of the way. What tag would I use for the local truck routes?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hgv" rel="tag" title="see questions tagged &#39;hgv&#39;">hgv</span> <span class="post-tag tag-link-truck" rel="tag" title="see questions tagged &#39;truck&#39;">truck</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jul '10, 05:31</strong></p>
<img src="https://secure.gravatar.com/avatar/0c334b9f230e39c1e73a2b0322a23fb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NE2&#39;s gravatar image" />
<p><span>NE2</span><br />
<span class="score" title="1359 reputation points"><span>1.4k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NE2 has one accepted answer">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jul '10, 05:34</strong> </span></p>
</div>
</div>
<div id="comments-container-307" class="comments-container">
&#10;</div>
<div id="comment-tools-307" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-307-form-container" class="comment-form-container">
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

<span id="430"></span>

<div id="answer-container-430" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-430-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Since routing engines have no representation of NYC borough boundaries, exact modelling is not possible. But existing data should approximate what they're trying to formalise. Routing software will favour motorway, trunk and primary roads already for longer routes, which almost takes care of the distinction between in-borough and thru-borough traffic. At least, it meets the spirit of the distinction.</p>
<p>A mapping like</p>
<ul>
<li>through → <strong>hgv=designated</strong> + <em>highway=motorway/trunk/primary</em></li>
<li>local → <strong>hgv=designated</strong> + <em>highway=secondary/tertiary/...</em></li>
<li>non-designated → <strong>hgv=destination</strong></li>
</ul>
<p>should suffice I think. If local traffic uses a through route as a result, that's better than through traffic using a local route :/</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '10, 13:01</strong></p>
<img src="https://secure.gravatar.com/avatar/b4a99bb74962d3cedff3e6d591847852?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrew%20Chadwick&#39;s gravatar image" />
<p><span>Andrew Chadwick</span><br />
<span class="score" title="1129 reputation points"><span>1.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrew Chadwick has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-430" class="comments-container">
<span id="431"></span>
<div id="comment-431" class="comment">
<div id="post-431-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It doesn't make sense to tie the highway classifications to truck restrictions.</p>
<p>I've temporarily tagged the local routes hgv=local, which of course has no meaning.</p>
</div>
<div id="comment-431-info" class="comment-info">
<span class="comment-age">(22 Jul '10, 13:04)</span> <span class="comment-user userinfo">NE2</span>
</div>
</div>
<span id="434"></span>
<div id="comment-434" class="comment">
<div id="post-434-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@NE2 from your link:</p>
<blockquote>
<p>The Through or "Thru" Truck Route Network is primarily composed of major urban arterials and highways</p>
</blockquote>
<p>its is already the case that through routes are major roads. I don't suggest you mess with the existing classifications in OSM, merely that hgv=designated plus existing classifications should approximate NYC's rules. Ish.</p>
<p>Of course, if you know the territory better than I and this isn't so, I'll have a rethink.</p>
</div>
<div id="comment-434-info" class="comment-info">
<span class="comment-age">(22 Jul '10, 13:19)</span> <span class="comment-user userinfo">Andrew Chadwick</span>
</div>
</div>
<span id="439"></span>
<div id="comment-439" class="comment">
<div id="post-439-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But some of the local routes are also primary. And there are some that go from through to local at the borough lines (in other words they're only through if you're going to the next borough).</p>
</div>
<div id="comment-439-info" class="comment-info">
<span class="comment-age">(22 Jul '10, 16:05)</span> <span class="comment-user userinfo">NE2</span>
</div>
</div>
</div>
<div id="comment-tools-430" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-430-form-container" class="comment-form-container">
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

