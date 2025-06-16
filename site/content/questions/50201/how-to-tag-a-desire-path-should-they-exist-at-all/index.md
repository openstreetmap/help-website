+++
type = "question"
title = "How to tag a desire path? Should they exist at all?"
description = '''These are not official paths, by definition. In addition, many of them cross features (e.g. railroad tracks) that make their use illegal. Yet, they are used. Are there any existing examples of a tagged desire path? More information: https://en.wikipedia.org/wiki/Desire_path'''
date = "2016-06-14T20:13:00Z"
lastmod = "2016-06-17T08:14:00Z"
weight = 50201
keywords = [ "access", "paths", "footpaths", "tagging", "tags" ]
aliases = [ "/questions/50201" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag a desire path? Should they exist at all?](/questions/50201/how-to-tag-a-desire-path-should-they-exist-at-all)

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
<span id="post-50201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50201-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>These are not official paths, by definition. In addition, many of them cross features (e.g. railroad tracks) that make their use illegal. Yet, they <em>are</em> used. Are there any existing examples of a tagged desire path?</p>
<p>More information:</p>
<p><a href="https://en.wikipedia.org/wiki/Desire_path">https://en.wikipedia.org/wiki/Desire_path</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-paths" rel="tag" title="see questions tagged &#39;paths&#39;">paths</span> <span class="post-tag tag-link-footpaths" rel="tag" title="see questions tagged &#39;footpaths&#39;">footpaths</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jun '16, 20:13</strong></p>
<img src="https://secure.gravatar.com/avatar/bc6023f6fc4754cdc48990821c02d063?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lwburk&#39;s gravatar image" />
<p><span>lwburk</span><br />
<span class="score" title="96 reputation points">96</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lwburk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jun '16, 20:14</strong> </span></p>
</div>
</div>
<div id="comments-container-50201" class="comments-container">
&#10;</div>
<div id="comment-tools-50201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50201-form-container" class="comment-form-container">
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

<span id="50203"></span>

<div id="answer-container-50203" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50203-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-50203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="lwburk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We map what is there, not what should be there. You should tag the legal access as additional information, though.</p>
<p>So, for <a href="https://en.wikipedia.org/wiki/File:Desire_line.jpg">https://en.wikipedia.org/wiki/File:Desire_line.jpg</a> I would go for</p>
<ul>
<li><code>highway=path</code></li>
<li><code>surface=ground</code></li>
<li><code>smoothness=bad</code> (just a guess from the image)</li>
<li><code>width=0.4</code> (if I would have measured/guessed it from reality)</li>
<li>if needed: <a href="https://wiki.openstreetmap.org/wiki/Key:access">access</a> tags depending on the legal situation and signage. If a sign forbids use officially (whyever it is there) but no one (including the owner) cares, then I possibly would tag it <code>access=permissive</code> + <code>access:legal=private</code> (or something similar … I am not sure if we have an established tag here) + <code>access:description=officially forbidden by a sign which no one including the owner cares about</code> (a tag describing the access to make it clear to users and mappers). Similarly, if a sign forbids use by all vehicles, but clearly only motor vehicles are meant (just the wrong sign was put up) I would not use <code>vehicle=no</code>. Note the <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions">suggested default access assumptions</a>.</li>
</ul>
<p>Somewhat questionable is a "desire path" which crosses a railway line. Is there a path for the 5 metres across the railway line? Likely you cannot see it, you can just assume some use, but there is no real-world feature. In this special case (also influenced by the danger) I would tend to not map the part which is across the railway line.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jun '16, 20:42</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jun '16, 20:49</strong> </span></p>
</div>
</div>
<div id="comments-container-50203" class="comments-container">
<span id="50270"></span>
<div id="comment-50270" class="comment">
<div id="post-50270-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There's also the "informal=" tag, to distinguish evolved paths from constructed ones: <a href="https://wiki.openstreetmap.org/wiki/Key:informal">https://wiki.openstreetmap.org/wiki/Key:informal</a></p>
</div>
<div id="comment-50270-info" class="comment-info">
<span class="comment-age">(17 Jun '16, 08:14)</span> <span class="comment-user userinfo">Carnildo</span>
</div>
</div>
</div>
<div id="comment-tools-50203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50203-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50202"></span>

<div id="answer-container-50202" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50202-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-50202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We map what is on the ground.<br />
If there is a trodden path, map</p>
<pre><code>highway=path  
surface=ground
width=0.2</code></pre>
<p>Some mappers recommend to split/disconnect/delete such paths on railway landuses so that routers won't route along there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jun '16, 20:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span> </br></p>
</div>
</div>
<div id="comments-container-50202" class="comments-container">
<span id="50204"></span>
<div id="comment-50204" class="comment">
<div id="post-50204-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And what about an desire path making a short cut down a slope, through a fence which is demolished to get through ? Accees=no ?</p>
</div>
<div id="comment-50204-info" class="comment-info">
<span class="comment-age">(14 Jun '16, 22:14)</span> <span class="comment-user userinfo">Leeuw</span>
</div>
</div>
<span id="50205"></span>
<div id="comment-50205" class="comment">
<div id="post-50205-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/11592/leeuw"></a><a href="https://help.openstreetmap.org/users/11592/leeuw">@Leeuw</a>: in my opinion it is quite clear that in that case (without knowing more details) no one is allowed to walk there. <code>access=no</code> or <code>=private</code>. Or was the fence an accident and everybody (including the owner) agrees that it should be removed soon?</p>
<p>It may be good to map the fence as a barrier too.</p>
</div>
<div id="comment-50205-info" class="comment-info">
<span class="comment-age">(14 Jun '16, 22:52)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="50229"></span>
<div id="comment-50229" class="comment">
<div id="post-50229-score" class="comment-score">
4
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/11592/leeuw">@Leeuw</a>: first and foremost the path exists, thus it should be mapped.<br />
Adding any access tag doesn't prevent people walking it in RL.</p>
</div>
<div id="comment-50229-info" class="comment-info">
<span class="comment-age">(15 Jun '16, 14:39)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
</div>
<div id="comment-tools-50202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50202-form-container" class="comment-form-container">
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

