+++
type = "question"
title = "[closed] Overpass API how much hardware is enough?"
description = '''Hello,  I&#x27;m trying to decide what server setup (hardware) to buy for a local Overpass API instance. Would anybody mind sharing their current server specs for their own instances and some other information, such as number of concurrent users, maximum bandwidth, amount of RAM/ number of cores, SSD vs ...'''
date = "2016-02-04T17:07:00Z"
lastmod = "2016-02-04T21:28:00Z"
weight = 47917
keywords = [ "hardware", "overpass_api", "installation", "overpass" ]
aliases = [ "/questions/47917" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Overpass API how much hardware is enough?](/questions/47917/overpass-api-how-much-hardware-is-enough)

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
<span id="post-47917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47917-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I'm trying to decide what server setup (hardware) to buy for a local Overpass API instance. Would anybody mind sharing their current server specs for their own instances and some other information, such as number of concurrent users, maximum bandwidth, amount of RAM/ number of cores, SSD vs HDD etc?</p>
<p>I couldn't find much information on the public instances other than:</p>
<pre><code>Name    Data coverage   Endpoint    Version     Attic data  Hardware    Usage policy
Main Overpass API instance  Global  http://overpass-api.de/api/     0.7.52  Yes     4 physical cores, 32 GB RAM, SSD    Both servers have a total capacity of about 1.000.000 requests per day. You can safely assume that you don&#39;t disturb other users when you do less than 10.000 queries per day or download less than 5 GB data per day.
Rambler Overpass API instance   Global  http://overpass.osm.rambler.ru/cgi/     0.7.52  Yes     8 cores, 64 GB RAM, hard disks</code></pre>
<p>Taken from: <a href="http://wiki.openstreetmap.org/wiki/Overpass_API#Introduction">http://wiki.openstreetmap.org/wiki/Overpass_API#Introduction</a></p>
<p>Does anyone have some more specific stats? The queries I'll be making are small 100m bbox queries mostly with around a max of 50,000 concurrent users. Could anyone please advise me?</p>
<p>Thanks for your time.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hardware" rel="tag" title="see questions tagged &#39;hardware&#39;">hardware</span> <span class="post-tag tag-link-overpass_api" rel="tag" title="see questions tagged &#39;overpass_api&#39;">overpass_api</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '16, 17:07</strong></p>
<img src="https://secure.gravatar.com/avatar/1382f87fca144452793d096a71d332da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gmeister41&#39;s gravatar image" />
<p><span>gmeister41</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gmeister41 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>04 Feb '16, 21:28</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-47917" class="comments-container">
<span id="47918"></span>
<div id="comment-47918" class="comment">
<div id="post-47918-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it is quite the same (or at least similar) question as <a href="/questions/41895">sensible-spec-for-overpass-api-instance</a></p>
</div>
<div id="comment-47918-info" class="comment-info">
<span class="comment-age">(04 Feb '16, 17:23)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="47920"></span>
<div id="comment-47920" class="comment">
<div id="post-47920-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That doesnt answer the question, it merely points to contact email addresses of people with Overpass servers. Would be good to get some specs in one place.</p>
</div>
<div id="comment-47920-info" class="comment-info">
<span class="comment-age">(04 Feb '16, 18:18)</span> <span class="comment-user userinfo">gmeister41</span>
</div>
</div>
<span id="47924"></span>
<div id="comment-47924" class="comment">
<div id="post-47924-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11113/gmeister41"></a><a href="http://help.openstreetmap.org/users/11113/gmeister41">@gmeister41</a>: yes, the current answer is not that helpful, I rather mean if the question is the same. If it is, we should close this one and collect more helpful answers over there. :-)</p>
</div>
<div id="comment-47924-info" class="comment-info">
<span class="comment-age">(04 Feb '16, 20:10)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="47925"></span>
<div id="comment-47925" class="comment">
<div id="post-47925-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I figured the bump might be useful to get some new answers so maybe we should close that one :-)</p>
</div>
<div id="comment-47925-info" class="comment-info">
<span class="comment-age">(04 Feb '16, 21:08)</span> <span class="comment-user userinfo">gmeister41</span>
</div>
</div>
<span id="47926"></span>
<div id="comment-47926" class="comment">
<div id="post-47926-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11113/gmeister41"></a><a href="http://help.openstreetmap.org/users/11113/gmeister41">@gmeister41</a>: right, so - let's focus the collection over there (if you want otherwise, we can keep this one open too...). As a start you could post your finding of the public instance specs as an answer - at least this is a start.</p>
</div>
<div id="comment-47926-info" class="comment-info">
<span class="comment-age">(04 Feb '16, 21:28)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-47917" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47917-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question" by aseerel4c26 04 Feb '16, 21:28

</div>

</div>

</div>

