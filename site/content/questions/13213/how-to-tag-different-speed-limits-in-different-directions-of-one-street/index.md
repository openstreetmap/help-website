+++
type = "question"
title = "How to tag different speed limits in different directions of one street?"
description = '''How should speed limits be tagged if they are different in the two directions of a street? E.g. reduced speed limit before a crossing road:  &amp;lt;&amp;lt; (70) &amp;lt;&amp;lt; | (50) &amp;lt;&amp;lt; (70) &amp;lt;&amp;lt; [Speed limit right2left]  ———————————————————————+——————————————————————— [Street]  &amp;gt;&amp;gt; (70) &amp;gt;&amp;gt;...'''
date = "2012-06-03T01:29:00Z"
lastmod = "2012-06-03T13:23:00Z"
weight = 13213
keywords = [ "speedlimit", "directions" ]
aliases = [ "/questions/13213" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag different speed limits in different directions of one street?](/questions/13213/how-to-tag-different-speed-limits-in-different-directions-of-one-street)

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
<span id="post-13213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13213-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How should speed limits be tagged if they are different in the two directions of a street? E.g. reduced speed limit before a crossing road:</p>
<pre><code>    &lt;&lt;       (70)       &lt;&lt; |    (50)   &lt;&lt;  (70)  &lt;&lt;     [Speed limit right2left]
    ———————————————————————+———————————————————————     [Street]
    &gt;&gt;  (70)  &gt;&gt;   (50)    | &gt;&gt;       (70)       &gt;&gt;     [Speed limit left2right]
    ~~~ 70 ~~~&gt;&lt;~~~~~~~~~ ??? ~~~~~~~~~&gt;&lt;~~~ 70 ~~~     [Speed limit tags]</code></pre>
So how to tag this -------^ part of the street?
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-speedlimit" rel="tag" title="see questions tagged &#39;speedlimit&#39;">speedlimit</span> <span class="post-tag tag-link-directions" rel="tag" title="see questions tagged &#39;directions&#39;">directions</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '12, 01:29</strong></p>
<img src="https://secure.gravatar.com/avatar/435b6135a82b9a1bad92356eb172cd80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="K-M-H&#39;s gravatar image" />
<p><span>K-M-H</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="K-M-H has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jun '12, 01:35</strong> </span></p>
</div>
</div>
<div id="comments-container-13213" class="comments-container">
&#10;</div>
<div id="comment-tools-13213" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13213-form-container" class="comment-form-container">
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

<span id="13223"></span>

<div id="answer-container-13223" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13223-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See <a href="http://wiki.openstreetmap.org/wiki/Key:maxspeed#Driving_direction">http://wiki.openstreetmap.org/wiki/Key:maxspeed#Driving_direction</a> Note you will have to split the street multiple times for this to work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '12, 13:18</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-13223" class="comments-container">
&#10;</div>
<div id="comment-tools-13223" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13223-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13224"></span>

<div id="answer-container-13224" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13224-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd say maxspeed:forward and maxspeed:backward are the tags you want. "forward" when the car drives in the same direction as the OSM way.</p>
<p>The "*:forward" subtag style is common enough in OSM, and taginfo will show you that it is <a href="http://taginfo.openstreetmap.org/search?q=maxspeed">commonly used for maxspeed</a> too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '12, 13:23</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-13224" class="comments-container">
&#10;</div>
<div id="comment-tools-13224" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13224-form-container" class="comment-form-container">
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

