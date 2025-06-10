+++
type = "question"
title = "Overpass &#x27;around&#x27;. Could someone explain this routine please?"
description = '''Hi I&#x27;ve run out of intelligence for Isolated Buildings Routine way[building]({{bbox}})-&amp;gt;.a; foreach .a (  way.a(around:1000);  way._(if:count(ways) == 1);  out center; );    How does it know we want to find  objects further away than 1000m?  All other examples I read find  objects within the spec...'''
date = "2018-06-05T22:59:00Z"
lastmod = "2018-06-06T12:20:00Z"
weight = 64035
keywords = [ "overpass", "around" ]
aliases = [ "/questions/64035" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass 'around'. Could someone explain this routine please?](/questions/64035/overpass-around-could-someone-explain-this-routine-please)

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
<span id="post-64035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64035-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I've run out of intelligence for <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Isolated_Buildings">Isolated Buildings Routine</a></p>
<pre><code>way[building]({{bbox}})-&gt;.a;
foreach .a (
  way.a(around:1000);
  way._(if:count(ways) == 1);
  out center;
);</code></pre>
<ul>
<li><p>How does it know we want to find objects <strong>further</strong> away than 1000m? All other examples I read find objects <strong>within</strong> the specified distance.</p></li>
<li><p>Underscores are the default variable name for the default set. As it explicitly creates set 'a', what is in the default set? Is it a copy of set 'a'?</p></li>
</ul>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-around" rel="tag" title="see questions tagged &#39;around&#39;">around</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jun '18, 22:59</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-64035" class="comments-container">
<span id="64036"></span>
<div id="comment-64036" class="comment">
<div id="post-64036-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not sure about the set question. As for your other question, it looks like it's counting how many buildings are within 1000m of each building. If there's only one (the building in question), then it's included as part of the results because there aren't any other buildings within 1000m.</p>
</div>
<div id="comment-64036-info" class="comment-info">
<span class="comment-age">(06 Jun '18, 00:09)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="64047"></span>
<div id="comment-64047" class="comment">
<div id="post-64047-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, yes, of course. Thanks. Clearer now. I tried swapping '_' with 'a' &amp; got different results so It appears it isn't a copy of 'a'</p>
</div>
<div id="comment-64047-info" class="comment-info">
<span class="comment-age">(06 Jun '18, 12:20)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-64035" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64035-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

