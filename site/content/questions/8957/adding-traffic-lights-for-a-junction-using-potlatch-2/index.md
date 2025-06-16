+++
type = "question"
title = "Adding traffic lights for a junction using Potlatch 2"
description = '''Hi I want to add traffic lights to a junction. I tried adding a &#x27;building&#x27; object removed all the existing tags and added the tag &#x27;highway=&#x27;traffic_signals&#x27; . But its not working I checked another traffic lights tag that had been previously added by someone else . That also has the tag highway=&#x27;traf...'''
date = "2011-11-13T11:57:00Z"
lastmod = "2011-11-15T15:26:00Z"
weight = 8957
keywords = [ "signals", "traffic" ]
aliases = [ "/questions/8957" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Adding traffic lights for a junction using Potlatch 2](/questions/8957/adding-traffic-lights-for-a-junction-using-potlatch-2)

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
<span id="post-8957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8957-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I want to add traffic lights to a junction. I tried adding a 'building' object removed all the existing tags and added the tag 'highway='traffic_signals' . But its not working</p>
<p>I checked another traffic lights tag that had been previously added by someone else . That also has the tag highway='traffic_signals' and that is working</p>
<p>I don't understand what i am doing wrong</p>
<p>Thanks in advance</p>
<p>regards</p>
<p>Mathew</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-signals" rel="tag" title="see questions tagged &#39;signals&#39;">signals</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Nov '11, 11:57</strong></p>
<img src="https://secure.gravatar.com/avatar/9092ab3945f2a2680834fc62e2ca751f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mjk6035&#39;s gravatar image" />
<p><span>mjk6035</span><br />
<span class="score" title="91 reputation points">91</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mjk6035 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '11, 22:36</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-8957" class="comments-container">
&#10;</div>
<div id="comment-tools-8957" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8957-form-container" class="comment-form-container">
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

<span id="8985"></span>

<div id="answer-container-8985" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8985-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Traffic Signals are tags on a node in a way, not a building. If you look at <a href="https://www.openstreetmap.org/?lat=43.1653395295143&amp;lon=-77.6912301778793&amp;zoom=17">these roads near Rochester, NY</a>, you will see the traffic lights are actually placed at a node in the way. In fact, the <a href="https://www.openstreetmap.org/browse/node/212668235">node that forms the 5 point junction</a> is tagged as "highway=traffic_signals".</p>
<p>The basic procedure for adding a traffic signal to a way is</p>
<ol>
<li>Start Potchlatch</li>
<li>Select the node in the way where you want to add the traffic signal</li>
<li>Select "Advanced" to go to the advanced tag editing</li>
<li>Click "Add" top add a new key,value pair</li>
<li>For the new Key (tag), enter "highway"</li>
<li>For the new Value, enter "traffic_signals"</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '11, 14:09</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffdc5279fd70540799b762c14e66665?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jwernerny&#39;s gravatar image" />
<p><span>jwernerny</span><br />
<span class="score" title="401 reputation points">401</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jwernerny has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8985" class="comments-container">
<span id="9000"></span>
<div id="comment-9000" class="comment">
<div id="post-9000-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks for the reply .Actually I chose the 'building' object so that I could remove any existing tags and then add the highway='traffic_signals' tag.</p>
<p>You mentioned that you need to add tag to a node where you want the traffic lights to be displayed . But what if there is no node there.</p>
<p>Thanks in advance</p>
<p>regards</p>
<p>Mathew</p>
</div>
<div id="comment-9000-info" class="comment-info">
<span class="comment-age">(15 Nov '11, 05:19)</span> <span class="comment-user userinfo">mjk6035</span>
</div>
</div>
<span id="9014"></span>
<div id="comment-9014" class="comment">
<div id="post-9014-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@mjk6035</span> To add a new node to a way in Potlatch 2, simply shift-click on the way where you want the node to be.</p>
</div>
<div id="comment-9014-info" class="comment-info">
<span class="comment-age">(15 Nov '11, 15:26)</span> <span class="comment-user userinfo">jwernerny</span>
</div>
</div>
</div>
<div id="comment-tools-8985" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8985-form-container" class="comment-form-container">
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

