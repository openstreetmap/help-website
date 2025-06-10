+++
type = "question"
title = "Overpass query: how to select unclosed ways that have no tags?"
description = '''This is what I have until now: (way({{bbox}}); - way({{bbox}})[~&quot;.&quot;~&quot;.&quot;];)-&amp;gt;.w1; rel(bw.w1);way(r)-&amp;gt;.w2; (.w1; - .w2;); (._; &amp;gt;;); out meta;  But this only selects ways that have no tags and are not part of a relation, so this query gives me untagged areas (closed ways) as well. How can I so...'''
date = "2016-08-05T09:09:00Z"
lastmod = "2021-10-20T18:08:00Z"
weight = 51255
keywords = [ "ways", "untagged", "overpass-turbo", "relations", "tags" ]
aliases = [ "/questions/51255" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass query: how to select unclosed ways that have no tags?](/questions/51255/overpass-query-how-to-select-unclosed-ways-that-have-no-tags)

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
<span id="post-51255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51255-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is what I have until now:</p>
<pre><code>(way({{bbox}}); - way({{bbox}})[~&quot;.&quot;~&quot;.&quot;];)-&gt;.w1;
rel(bw.w1);way(r)-&gt;.w2;
(.w1; - .w2;);
(._; &gt;;);
out meta;</code></pre>
<p>But this only selects ways that have no tags and are not part of a relation, so this query gives me untagged areas (closed ways) as well. How can I solve that issue? I know how to do it with other tools, but I need to know if it can be done with Overpass-turbo.</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-untagged" rel="tag" title="see questions tagged &#39;untagged&#39;">untagged</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Aug '16, 09:09</strong></p>
<img src="https://secure.gravatar.com/avatar/0464ec5533673976b9a83b8bfaab3c03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manuela_butuc&#39;s gravatar image" />
<p><span>manuela_butuc</span><br />
<span class="score" title="156 reputation points">156</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manuela_butuc has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Aug '16, 13:32</strong> </span></p>
</div>
</div>
<div id="comments-container-51255" class="comments-container">
&#10;</div>
<div id="comment-tools-51255" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51255-form-container" class="comment-form-container">
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

<span id="51263"></span>

<div id="answer-container-51263" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51263-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-51263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The feature request <a href="https://github.com/drolbr/Overpass-API/issues/197">#197</a> implies that filtering closed or non-closed ways is currently not possible with Overpass API.</p>
<p>I'd suggest to take a look at JOSM filters instead to do some post processing, more specifically the <code>closed</code> filter. See this blog for details: <a href="https://www.mapbox.com/blog/2012-08-15-using-filters-josm/">https://www.mapbox.com/blog/2012-08-15-using-filters-josm/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Aug '16, 12:17</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-51263" class="comments-container">
<span id="51265"></span>
<div id="comment-51265" class="comment">
<div id="post-51265-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Basically, that was my question, if it can be done in overpass-turbo or not. Thanks for your answer, it was really helpful!</p>
</div>
<div id="comment-51265-info" class="comment-info">
<span class="comment-age">(05 Aug '16, 13:31)</span> <span class="comment-user userinfo">manuela_butuc</span>
</div>
</div>
</div>
<div id="comment-tools-51263" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51263-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82283"></span>

<div id="answer-container-82283" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82283-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For those googling it's now possible to check for a closed polygon &amp; if there are tags on a way:</p>
<pre><code>way(if:is_closed()==0)(if:count_tags() == 0);</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '21, 18:08</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-82283" class="comments-container">
&#10;</div>
<div id="comment-tools-82283" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82283-form-container" class="comment-form-container">
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

