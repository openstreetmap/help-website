+++
type = "question"
title = "Detection of Intersections in the maps"
description = '''Hello all  I am trying to write a program in c++ to automatically detect the roads on a selected area of the map. I was able to do detect the roads from the Ways and tags attached to them. But I could not find any specific tag that is related to an intersection between two roads. Only thing close to...'''
date = "2012-08-23T13:56:00Z"
lastmod = "2017-06-27T13:19:00Z"
weight = 15442
keywords = [ "intersection", "road", "tags" ]
aliases = [ "/questions/15442" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Detection of Intersections in the maps](/questions/15442/detection-of-intersections-in-the-maps)

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
<span id="post-15442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15442-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all</p>
<p>I am trying to write a program in c++ to automatically detect the roads on a selected area of the map. I was able to do detect the roads from the Ways and tags attached to them. But I could not find any specific tag that is related to an intersection between two roads. Only thing close to is a traffic signal tag. I was wondering if any one know more authentic way to determine the intersections. Hope my question was not ambiguous.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Aug '12, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/73bfa9669a927682b021cd4e2132047c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jawadch&#39;s gravatar image" />
<p><span>jawadch</span><br />
<span class="score" title="121 reputation points">121</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jawadch has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Aug '12, 13:57</strong> </span></p>
</div>
</div>
<div id="comments-container-15442" class="comments-container">
&#10;</div>
<div id="comment-tools-15442" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15442-form-container" class="comment-form-container">
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

<span id="15443"></span>

<div id="answer-container-15443" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15443-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15443-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-15443-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jawadch has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the OSM XML for a way, you'll see data such as:</p>
<pre><code>  &lt;nd ref=&quot;322896584&quot;/&gt;</code></pre>
<p>That indicates a node that is part of your way. If that exists in two ways, those ways join.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '12, 14:00</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-15443" class="comments-container">
<span id="15445"></span>
<div id="comment-15445" class="comment">
<div id="post-15445-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I checked it and it is true for the case in which two streets are intersecting. But is it also true for the case when on street e.g. a residential is ending in a main street?</p>
</div>
<div id="comment-15445-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 14:03)</span> <span class="comment-user userinfo">jawadch</span>
</div>
</div>
<span id="15447"></span>
<div id="comment-15447" class="comment">
<div id="post-15447-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, it should be. If not, someone hasn't joined the roads properly, as described <a href="/questions/1022/what-are-the-most-common-mapping-mistakes-that-other-users-make/1023">here</a>.</p>
</div>
<div id="comment-15447-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 14:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="15448"></span>
<div id="comment-15448" class="comment">
<div id="post-15448-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot. I should be able to detect it now.</p>
</div>
<div id="comment-15448-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 14:08)</span> <span class="comment-user userinfo">jawadch</span>
</div>
</div>
<span id="15452"></span>
<div id="comment-15452" class="comment not_top_scorer">
<div id="post-15452-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If one way street is going from south to north(longitude will be increasing) will the node references in the Way of that street will be such that the longitude of the first node ref is minimum and the longitude of the last node ref will be max. In short are the node ref in Way of "one way" roads along the direction of that road?</p>
</div>
<div id="comment-15452-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 14:52)</span> <span class="comment-user userinfo">jawadch</span>
</div>
</div>
<span id="15453"></span>
<div id="comment-15453" class="comment">
<div id="post-15453-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes - <a href="https://www.openstreetmap.org/browse/way/8123741">here</a>'s a stretch of oneway road (it has the tag "oneway=yes" and runs from south to north). The <a href="https://www.openstreetmap.org/browse/node/326365">first node</a> is at the south end and the <a href="https://www.openstreetmap.org/browse/node/252410326">end node</a> is at the north end. As you can see, the references of the nodes may vary (later nodes have higher reference numbers) but the order of nodes in the way will be in the order that they appear on the ground.</p>
</div>
<div id="comment-15453-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 15:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="15455"></span>
<div id="comment-15455" class="comment not_top_scorer">
<div id="post-15455-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot again :)</p>
</div>
<div id="comment-15455-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 15:23)</span> <span class="comment-user userinfo">jawadch</span>
</div>
</div>
<span id="15458"></span>
<div id="comment-15458" class="comment">
<div id="post-15458-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>As an addidtion to the oneway issue, there are also other tags (although not much used). oneway=-1 means the nodes are ordered in opposite direction (when the way goes from S to N, the nodes are oredered from N to S)</p>
<p>And some discouraged alternatives like "true" and "reversed" instead of "yes" and "-1": <a href="https://wiki.openstreetmap.org/wiki/Oneway">https://wiki.openstreetmap.org/wiki/Oneway</a></p>
</div>
<div id="comment-15458-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 16:29)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
<span id="32271"></span>
<div id="comment-32271" class="comment not_top_scorer">
<div id="post-32271-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have extracted the intersections that I need, my question is how to detect each twe adjacent intersection so I can define an adge to connect them and create a connected graph of inresection nodes. Thank you in advance for helps</p>
</div>
<div id="comment-32271-info" class="comment-info">
<span class="comment-age">(10 Apr '14, 12:45)</span> <span class="comment-user userinfo">Angeasg</span>
</div>
</div>
</div>
<div id="comment-tools-15443" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-15443-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32270"></span>

<div id="answer-container-32270" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32270-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have extracted the intersections that I need, my question is how to detect each twe adjacent intersection so I can define an adge to connect them and create a connected graph of inresection nodes. Thank you in advance for helps</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '14, 12:45</strong></p>
<img src="https://secure.gravatar.com/avatar/9b153a8a544d4db806cfe0e8228350f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Angeasg&#39;s gravatar image" />
<p><span>Angeasg</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Angeasg has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32270" class="comments-container">
<span id="32274"></span>
<div id="comment-32274" class="comment">
<div id="post-32274-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You might do better asking a new question describing what you're trying to do rather than asking a new question in an answer to an old one :)</p>
</div>
<div id="comment-32274-info" class="comment-info">
<span class="comment-age">(10 Apr '14, 13:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-32270" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32270-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56777"></span>

<div id="answer-container-56777" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56777-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,, can y send me the code ? I need to do the same and return the name os intersection, but I dont know how.. Tanks..</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '17, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/225f82d24943afac1db51fce7782cad9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mneto&#39;s gravatar image" />
<p><span>mneto</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mneto has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56777" class="comments-container">
&#10;</div>
<div id="comment-tools-56777" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56777-form-container" class="comment-form-container">
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

