+++
type = "question"
title = "How to get all addr:street addr:housenumber addr:city ?"
description = '''Hi! I&#x27;m need to get all street name, house number and city. I&#x27;m using osmconvert with the next query:  osmconvert chile-latest.osm --csv=&quot;addr:street addr:housenumber addr:city&quot; -o=1.csv The problem is I can&#x27;t get every street and house number, for example, if I get all lat and long, I can get 7.000...'''
date = "2014-12-01T18:33:00Z"
lastmod = "2019-07-16T16:45:00Z"
weight = 38985
keywords = [ "osmconvert" ]
aliases = [ "/questions/38985" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to get all addr:street addr:housenumber addr:city ?](/questions/38985/how-to-get-all-addrstreet-addrhousenumber-addrcity)

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
<span id="post-38985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38985-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I'm need to get all street name, house number and city. I'm using osmconvert with the next query: osmconvert chile-latest.osm --csv="addr:street addr:housenumber addr:city" -o=1.csv</p>
<p>The problem is I can't get every street and house number, for example, if I get all lat and long, I can get 7.000.000 records, but when I use below query, I can get just 5.000 records. If i look at the map, show a lot more than what I can get. How I can get all the street name, house number and city? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Dec '14, 18:33</strong></p>
<img src="https://secure.gravatar.com/avatar/02e87dbe453ed7f88a9f1ba87f6a248e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patriciodilet&#39;s gravatar image" />
<p><span>patriciodilet</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patriciodilet has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38985" class="comments-container">
<span id="39007"></span>
<div id="comment-39007" class="comment">
<div id="post-39007-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>do you have the same "error if you try your query on another raw OSM file from another area in the world? for example Luxembourg or similar?</p>
<p>Maybe in the result file you only have elements that have all three tags with any value, any all others are skipped?</p>
</div>
<div id="comment-39007-info" class="comment-info">
<span class="comment-age">(02 Dec '14, 17:20)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="39060"></span>
<div id="comment-39060" class="comment">
<div id="post-39060-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe you want to run osmconvert with the additional parameter --all-to-nodes</p>
</div>
<div id="comment-39060-info" class="comment-info">
<span class="comment-age">(04 Dec '14, 22:13)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="39062"></span>
<div id="comment-39062" class="comment">
<div id="post-39062-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"if I get all lat and long, I can get 7.000.000 records"</p>
<p>That sounds a lot - I suspect that this includes <em>every node</em> in Chile, not just those places that have addresses (every park bench, every tree, every node of every way that makes up every road, etc.)</p>
</div>
<div id="comment-39062-info" class="comment-info">
<span class="comment-age">(04 Dec '14, 22:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-38985" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38985-form-container" class="comment-form-container">
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

<span id="39080"></span>

<div id="answer-container-39080" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39080-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using your slightly modified command (with the file being from December 5th)</p>
<pre><code>osmconvert chile-latest.osm.pbf  --csv=&quot;addr:street addr:housenumber addr:city&quot; -o=1.csv</code></pre>
<p>I get a file with 235.934 lines which each contains a more or less address (sometimes only a street name or a housenumber)</p>
<p>In short: works for me. (at least it seems so)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '14, 14:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-39080" class="comments-container">
&#10;</div>
<div id="comment-tools-39080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39080-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70099"></span>

<div id="answer-container-70099" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70099-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How you did it in overpass-turbo?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '19, 14:54</strong></p>
<img src="https://secure.gravatar.com/avatar/769f93fa803088a3bbd1921f2da6a761?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sterben_123&#39;s gravatar image" />
<p><span>Sterben_123</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sterben_123 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70099" class="comments-container">
<span id="70101"></span>
<div id="comment-70101" class="comment">
<div id="post-70101-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16929/sterben_123">@Sterben_123</a>: Please create a new question for your issue.</p>
</div>
<div id="comment-70101-info" class="comment-info">
<span class="comment-age">(16 Jul '19, 16:45)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-70099" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70099-form-container" class="comment-form-container">
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

