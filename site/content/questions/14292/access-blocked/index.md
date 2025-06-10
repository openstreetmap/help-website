+++
type = "question"
title = "Access Blocked"
description = '''Hi there. I have invoked the &quot;Access Blocked&quot; message for over-using the server. I accept that I have probably hit the server a lot whilst testing an application but this testing is winding down now. In real-use, there will be fewer than 10 people accessing the map tile server and most days there wi...'''
date = "2012-07-16T12:45:00Z"
lastmod = "2012-07-19T10:36:00Z"
weight = 14292
keywords = [ "access", "blocked" ]
aliases = [ "/questions/14292" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Access Blocked](/questions/14292/access-blocked)

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
<span id="post-14292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14292-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there. I have invoked the "Access Blocked" message for over-using the server. I accept that I have probably hit the server a lot whilst testing an application but this testing is winding down now. In real-use, there will be fewer than 10 people accessing the map tile server and most days there will be no access at all. Can I have the restriction withdrawn now that I'm aware of the issue and I will massively reduce my usage? Aside: does the block 'time-out' at all in order to give me a second chance in the future? Second: How does this restriction apply? To me as an individual accessing the server from work (identifiable, I imagine, by an IP address?), or to anyone else who might use my application from their location? Any clarification would be most useful but the outcome I seek is to be given a warning and let back in to play :-)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-blocked" rel="tag" title="see questions tagged &#39;blocked&#39;">blocked</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '12, 12:45</strong></p>
<img src="https://secure.gravatar.com/avatar/bfcef0afb35b31516a6597d6c7f11b09?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TimHaydnJones&#39;s gravatar image" />
<p><span>TimHaydnJones</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TimHaydnJones has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14292" class="comments-container">
<span id="14293"></span>
<div id="comment-14293" class="comment">
<div id="post-14293-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Map tiles? Come chat in #osm-dev on OFTC via <a href="http://irc.openstreetmap.org/">http://irc.openstreetmap.org/</a></p>
</div>
<div id="comment-14293-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 12:51)</span> <span class="comment-user userinfo">Firefishy ♦♦</span>
</div>
</div>
</div>
<div id="comment-tools-14292" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14292-form-container" class="comment-form-container">
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

<span id="14294"></span>

<div id="answer-container-14294" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14294-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14294-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14294-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For the tile server it's not about how many people use it, but how many tiles they download. Heavy use, or any "scraping" use (where you download tiles for storing them rather than for displaying them live in the browser) are not allowed.</p>
<p>If you have been blocked on the tile server then a message to the admins (and not to this help forum) is recommended, explaining exactly how your requests are identifiable (user agent, IP, whatever).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '12, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-14294" class="comments-container">
<span id="14295"></span>
<div id="comment-14295" class="comment">
<div id="post-14295-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik - I did visit the admins site but a) couldn't see how I message any of them from there and b) for example, on Tom H's Discussion page, it says repeatedly "Do not leave messages for me here"</p>
</div>
<div id="comment-14295-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 12:57)</span> <span class="comment-user userinfo">TimHaydnJones</span>
</div>
</div>
<span id="14296"></span>
<div id="comment-14296" class="comment">
<div id="post-14296-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I am an admin, come chat in #osm-dev on OFTC via <a href="http://irc.openstreetmap.org/">http://irc.openstreetmap.org/</a></p>
</div>
<div id="comment-14296-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 12:58)</span> <span class="comment-user userinfo">Firefishy ♦♦</span>
</div>
</div>
<span id="14299"></span>
<div id="comment-14299" class="comment">
<div id="post-14299-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>come chat in #osm-dev on OFTC via <a href="http://irc.openstreetmap.org/">http://irc.openstreetmap.org/</a> It's not apparent to me what I do when I get there</p>
</div>
<div id="comment-14299-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 13:17)</span> <span class="comment-user userinfo">TimHaydnJones</span>
</div>
</div>
<span id="14317"></span>
<div id="comment-14317" class="comment">
<div id="post-14317-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(expanding a bit on Firefishy's comment)</p>
<p>There are many different ways of contacting other people in OSM, as described <a href="https://wiki.openstreetmap.org/wiki/Contact#IRC">here</a>. One of them is <a href="https://wiki.openstreetmap.org/wiki/IRC">IRC</a> (various channels on oftc.net) which you can access using a regular IRC client or, for the most popular OSM channels, by a web front-end <a href="http://irc.openstreetmap.org/">here</a>. One of those channels is #osm-dev, so simply click on the link, select #osm-dev from the drop-down list and choose an identifying nickname instead of the default "CGI*" one. Then ask your questions!</p>
</div>
<div id="comment-14317-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 16:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="14329"></span>
<div id="comment-14329" class="comment">
<div id="post-14329-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks SomeoneElse</p>
</div>
<div id="comment-14329-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 21:32)</span> <span class="comment-user userinfo">TimHaydnJones</span>
</div>
</div>
<span id="14393"></span>
<div id="comment-14393" class="comment not_top_scorer">
<div id="post-14393-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm still confused. The irc site seems to be so slow as to be completely unusable in real terms. It takes 5-10 minutes for any response to any action to appear (whether that be to post a message or try to navigate between the channels). In fact, I'm normally disconnected before I get to chat to anyone (and 'Click to reconnect' either does nothing or is so slow that I've given up before it does something).</p>
</div>
<div id="comment-14393-info" class="comment-info">
<span class="comment-age">(19 Jul '12, 09:36)</span> <span class="comment-user userinfo">TimHaydnJones</span>
</div>
</div>
<span id="14394"></span>
<div id="comment-14394" class="comment not_top_scorer">
<div id="post-14394-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've just retried the web interface - it seems OK from where I am (a UK ADSL connection)</p>
</div>
<div id="comment-14394-info" class="comment-info">
<span class="comment-age">(19 Jul '12, 10:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-14294" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-14294-form-container" class="comment-form-container">
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

