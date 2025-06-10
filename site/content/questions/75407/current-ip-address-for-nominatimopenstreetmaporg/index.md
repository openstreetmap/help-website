+++
type = "question"
title = "Current IP Address for nominatim.openstreetmap.org"
description = '''What are the current ip addresses for nominatim.openstreetmap.org and amsterdam.nominatim.openstreetmap.org for our firewall rules. Thank you.'''
date = "2020-06-22T21:48:00Z"
lastmod = "2020-06-23T15:05:00Z"
weight = 75407
keywords = [ "ip", "address" ]
aliases = [ "/questions/75407" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Current IP Address for nominatim.openstreetmap.org](/questions/75407/current-ip-address-for-nominatimopenstreetmaporg)

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
<span id="post-75407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75407-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What are the current ip addresses for nominatim.openstreetmap.org and amsterdam.nominatim.openstreetmap.org for our firewall rules. Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jun '20, 21:48</strong></p>
<img src="https://secure.gravatar.com/avatar/eac3aeebdc1a134668a4b5e021dfb41e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Radio_Guy&#39;s gravatar image" />
<p><span>Radio_Guy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Radio_Guy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75407" class="comments-container">
&#10;</div>
<div id="comment-tools-75407" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75407-form-container" class="comment-form-container">
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

<span id="75413"></span>

<div id="answer-container-75413" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75413-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The IP addresses change regularly, so it is unwise to put any IP directly into your firewall. Many firewalls accept hostnames (like nominatim.openstreetmap.org) and so you should use that instead.</p>
<p>If you firewall only accepts IP addresses, then you should automatically update it by looking up the current IP addresses (via DNS), and updating your firewall rules appropriately. I would suggest doing this every few minutes - the DNS TTL will give you an indication of how long you should cache the IP address. (Of course, this is the entire point of DNS in the first place).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jun '20, 08:18</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-75413" class="comments-container">
&#10;</div>
<div id="comment-tools-75413" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75413-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75419"></span>

<div id="answer-container-75419" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75419-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In addition to Andy's direct answer, if you find yourself having to go through an outbound firewall to get to OSM's instance of Nominatim it's perhaps worth setting up your own instance of Nominatim inside your network. OpenStreetMap isn't a "map service" in the same way that other providers are; the data's free (within our licensing rules) and the software used to process it is mostly free too.</p>
<p>If you ran your own service you wouldn't need to be concerned about people outside your network knowing what nominatim calls you were making.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jun '20, 15:05</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-75419" class="comments-container">
&#10;</div>
<div id="comment-tools-75419" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75419-form-container" class="comment-form-container">
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

