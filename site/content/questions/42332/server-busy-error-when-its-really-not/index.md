+++
type = "question"
title = "Server Busy Error (when it&#x27;s really not)"
description = '''I&#x27;ve been trying to download a section of a map as a PDF for many days but have been unable to. I keep getting an error page that reads &quot;The server is too busy at the moment. Please wait a few minutes before trying again.&quot; In looking at other similar questions that have been asked, the typical respo...'''
date = "2015-04-15T02:56:00Z"
lastmod = "2015-04-16T18:59:00Z"
weight = 42332
keywords = [ "download", "export", "server" ]
aliases = [ "/questions/42332" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Server Busy Error (when it's really not)](/questions/42332/server-busy-error-when-its-really-not)

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
<span id="post-42332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42332-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been trying to download a section of a map as a PDF for many days but have been unable to. I keep getting an error page that reads "The server is too busy at the moment. Please wait a few minutes before trying again."</p>
<p>In looking at other similar questions that have been asked, the typical response is "because the servers are overloaded. Wait until they're below 25", as seen in this question/answer <a href="https://help.openstreetmap.org/questions/21192/error-export-load-average-on-the-server-is-too-high-at-the-moment">https://help.openstreetmap.org/questions/21192/error-export-load-average-on-the-server-is-too-high-at-the-moment</a></p>
<p>It's recommended to check this page to make sure that the level is below 25. I'm seeing that it's well below 25 (below 10 even) and yet I still keep getting this error.</p>
<p><a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/load.html">http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/load.html</a></p>
<p>I have tried exporting a smaller chunk of the map but that still doesn't help. Any help or advice would be appreciated. Much thanks ahead of time!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '15, 02:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ca7c5a640cf34837a624fae1426736ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EChrisDenney&#39;s gravatar image" />
<p><span>EChrisDenney</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EChrisDenney has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '15, 12:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42332" class="comments-container">
<span id="42347"></span>
<div id="comment-42347" class="comment">
<div id="post-42347-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>interesting, maybe the pdf creation is done by another server now. However, the time at around 2:00 UTC (the time of your question) looks like a very low load time on yevaud and I guess this is a similar pattern also for other servers (due to geographic/time zone distribution of our users). Maybe asking the server admins (e.g via the <a href="https://trac.openstreetmap.org/wiki/OsmComponentReports">"admin" component at our trac</a>) would be applicable if that does not work for anybody all the time.</p>
</div>
<div id="comment-42347-info" class="comment-info">
<span class="comment-age">(15 Apr '15, 13:18)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="42357"></span>
<div id="comment-42357" class="comment not_top_scorer">
<div id="post-42357-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the response aseerel4c26. I had it working for me last week, but then when I tried it again this weekend it didn't work. I tried it every day since then, multiple times per day, at multiple hours of the day. Same results.</p>
<p>How might I mention this to the server admins? I visited the link you provided but don't see a way of getting a message to them.</p>
</div>
<div id="comment-42357-info" class="comment-info">
<span class="comment-age">(15 Apr '15, 19:21)</span> <span class="comment-user userinfo">EChrisDenney</span>
</div>
</div>
<span id="42358"></span>
<div id="comment-42358" class="comment">
<div id="post-42358-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Also take a look at similar questions, for example <a href="https://help.openstreetmap.org/questions/22/how-do-i-export-map-images-of-larger-areas">How do I export map images of larger areas?</a>.</p>
</div>
<div id="comment-42358-info" class="comment-info">
<span class="comment-age">(15 Apr '15, 19:39)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="42359"></span>
<div id="comment-42359" class="comment not_top_scorer">
<div id="post-42359-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/158/scai"></a><a href="http://help.openstreetmap.org/users/158/scai">@scai</a>: right, other options exist.</p>
<p><a href="http://help.openstreetmap.org/users/10841/echrisdenney"></a><a href="http://help.openstreetmap.org/users/10841/echrisdenney">@EChrisDenney</a>: Yes, I meant the server admins (I can do that for you, of course). I will try an PDF export of a small, not densely mapped area later to see if it works for me. If it works for someone, please mention here.</p>
</div>
<div id="comment-42359-info" class="comment-info">
<span class="comment-age">(15 Apr '15, 20:12)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="42362"></span>
<div id="comment-42362" class="comment">
<div id="post-42362-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/158/scai">@scai</a> <a href="http://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a> I'm actually trying to export a very small area, just one street in a quiet suburban neighborhood. <a href="https://www.openstreetmap.org/#map=18/42.13273/-72.73832">https://www.openstreetmap.org/#map=18/42.13273/-72.73832</a></p>
</div>
<div id="comment-42362-info" class="comment-info">
<span class="comment-age">(15 Apr '15, 20:52)</span> <span class="comment-user userinfo">EChrisDenney</span>
</div>
</div>
<span id="42389"></span>
<div id="comment-42389" class="comment">
<div id="post-42389-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I have asked the admins: <a href="https://trac.openstreetmap.org/ticket/5308">https://trac.openstreetmap.org/ticket/5308</a></p>
</div>
<div id="comment-42389-info" class="comment-info">
<span class="comment-age">(16 Apr '15, 14:51)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="42391"></span>
<div id="comment-42391" class="comment">
<div id="post-42391-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thank you so much <a href="http://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a>. I really hope I can use this tool again as it was very valuable to me.</p>
</div>
<div id="comment-42391-info" class="comment-info">
<span class="comment-age">(16 Apr '15, 16:45)</span> <span class="comment-user userinfo">EChrisDenney</span>
</div>
</div>
</div>
<div id="comment-tools-42332" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-42332-form-container" class="comment-form-container">
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

<span id="42393"></span>

<div id="answer-container-42393" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42393-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I had asked the admins: <a href="https://trac.openstreetmap.org/ticket/5308">https://trac.openstreetmap.org/ticket/5308</a> . It looks like there was an error in the webserver program code, which has been fixed now (thank you, <a href="http://help.openstreetmap.org/users/1/tomh">@TomH</a>). Except than in the very busiest periods you now should be able to do exports. I tried to export a whole small city to pdf (server load is at 170 - quite a busy time): works.</p>
<p>The server <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/load.html">load</a> number is no direct limit any more, but you may use it to to spot not-that-busy periods in case it does not work at a specific point in time.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '15, 18:59</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-42393" class="comments-container">
<span id="42392"></span>
<div id="comment-42392" class="comment">
<div id="post-42392-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's fixed! Oh my goodness thank you so much. This was very stressful for me as I had a very important project I was working on. Thank you so much <a href="http://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a></p>
</div>
<div id="comment-42392-info" class="comment-info">
<span class="comment-age">(16 Apr '15, 16:52)</span> <span class="comment-user userinfo">EChrisDenney</span>
</div>
</div>
</div>
<div id="comment-tools-42393" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42393-form-container" class="comment-form-container">
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

