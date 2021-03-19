+++
type = "question"
title = "Time zone used by wireshark"
description = '''When looking at a packet capture, is it possible to set the time zone used by Wireshark to a time zone other than the system time? My colleagues and I are a occasionally tripped up when working with each other from different time zones (east coast and west coast).'''
date = "2013-10-15T10:23:00Z"
lastmod = "2013-10-15T22:34:00Z"
weight = 26014
keywords = [ "timezone" ]
aliases = [ "/questions/26014" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Time zone used by wireshark](/questions/26014/time-zone-used-by-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26014-score" class="post-score" title="current number of votes">0</div><span id="post-26014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When looking at a packet capture, is it possible to set the time zone used by Wireshark to a time zone other than the system time? My colleagues and I are a occasionally tripped up when working with each other from different time zones (east coast and west coast).</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timezone" rel="tag" title="see questions tagged &#39;timezone&#39;">timezone</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '13, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/71a12eeab93dcad7f31a41637075e3d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="syzdek&#39;s gravatar image" /><p><span>syzdek</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="syzdek has no accepted answers">0%</span></p></div></div><div id="comments-container-26014" class="comments-container"></div><div id="comment-tools-26014" class="comment-tools"></div><div class="clear"></div><div id="comment-26014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26019"></span>

<div id="answer-container-26019" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26019-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26019-score" class="post-score" title="current number of votes">3</div><span id="post-26019-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="syzdek has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There isn't a way to set the timezone within Wireshark but it's easy enough to do from a shell prompt before starting Wireshark. The method to do that is described in the already-existing feature request to allow you to do it in the GUI: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2629">bug 2629</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '13, 11:18</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-26019" class="comments-container"><span id="26023"></span><div id="comment-26023" class="comment"><div id="post-26023-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jeff. Didn't know about the TZ option.</p></div><div id="comment-26023-info" class="comment-info"><span class="comment-age">(15 Oct '13, 14:22)</span> <span class="comment-user userinfo">hansangb</span></div></div><span id="26026"></span><div id="comment-26026" class="comment"><div id="post-26026-score" class="comment-score"></div><div class="comment-text"><p>You're welcome.</p><p>If an Answer answers your question, please be sure to Accept it by clicking on the checkbox. That way the question won't show up in the list of unanswered questions. (See the FAQ for more details.)</p></div><div id="comment-26026-info" class="comment-info"><span class="comment-age">(15 Oct '13, 15:16)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="26028"></span><div id="comment-26028" class="comment"><div id="post-26028-score" class="comment-score"></div><div class="comment-text"><p>It's a similar trick like temporarily changing the temp dir for Wireshark, by setting the tmp/temp environment variables on a command line / batch before running Wireshark.</p></div><div id="comment-26028-info" class="comment-info"><span class="comment-age">(15 Oct '13, 15:57)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="26029"></span><div id="comment-26029" class="comment"><div id="post-26029-score" class="comment-score"></div><div class="comment-text"><p><span>@Jasper</span>, a possible new feature for tracewrangler as well? I don't have a particular need myself, but it seems like something suitable for the tool. Just an idea.</p></div><div id="comment-26029-info" class="comment-info"><span class="comment-age">(15 Oct '13, 16:27)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="26032"></span><div id="comment-26032" class="comment"><div id="post-26032-score" class="comment-score"></div><div class="comment-text"><p>Jeff, I really should read the FAQ. I find it hard to follow the thread as latest comments are not at the end etc. But if I never read Gerald's release notes...what hope is there for me! LOL</p></div><div id="comment-26032-info" class="comment-info"><span class="comment-age">(15 Oct '13, 17:29)</span> <span class="comment-user userinfo">hansangb</span></div></div><span id="26038"></span><div id="comment-26038" class="comment not_top_scorer"><div id="post-26038-score" class="comment-score"></div><div class="comment-text"><p><span>@hansangb</span>: Doh! Sorry, I thought you were the OP/asker of the question! Sorry, I completely missed that you weren't!</p></div><div id="comment-26038-info" class="comment-info"><span class="comment-age">(15 Oct '13, 19:27)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="26041"></span><div id="comment-26041" class="comment not_top_scorer"><div id="post-26041-score" class="comment-score"></div><div class="comment-text"><p>Oh dear, that release note running gag now even shows up when there is no Sharkfest going on... ;-))</p></div><div id="comment-26041-info" class="comment-info"><span class="comment-age">(15 Oct '13, 22:32)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="26042"></span><div id="comment-26042" class="comment not_top_scorer"><div id="post-26042-score" class="comment-score"></div><div class="comment-text"><p><span>@cmaynard</span>: good idea - it should be pretty easy to implement, so I might just add it as an option to the editing task settings.</p></div><div id="comment-26042-info" class="comment-info"><span class="comment-age">(15 Oct '13, 22:34)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-26019" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-26019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26016"></span>

<div id="answer-container-26016" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26016-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26016-score" class="post-score" title="current number of votes">1</div><span id="post-26016-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I can tell (also from <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChAdvTimezones.html">http://www.wireshark.org/docs/wsug_html_chunked/ChAdvTimezones.html)</a> Wireshark has no option to adjust the time zone for you. So either you temporarily set your time zone to the one of your colleagues while working with the file, or you use editcap to adjust the timing. I always adjusted my time zone while working with traces taken in a different time zone, but maybe you may want to put in a <a href="http://bugs.wireshark.org">feature request</a>. It shouldn't be too much of a problem for one of the developers to add an option/command line parameter/preference setting to adjust the time zone to a "per Wireshark" setting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '13, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-26016" class="comments-container"><span id="26017"></span><div id="comment-26017" class="comment"><div id="post-26017-score" class="comment-score"></div><div class="comment-text"><p>Or just ask for support for GMT. Most network folks work in GMT/zulu anyway. I thought that's what Absolute Time did...maybe I was wrong.</p></div><div id="comment-26017-info" class="comment-info"><span class="comment-age">(15 Oct '13, 10:51)</span> <span class="comment-user userinfo">hansangb</span></div></div><span id="26027"></span><div id="comment-26027" class="comment"><div id="post-26027-score" class="comment-score"></div><div class="comment-text"><p>Absolute Time is just a time column that displays date and time of day (and no relative times like "relative time" and "delta time"), adjusted from UTC to the local time zone. And that's perfectly fine with me - I'd be confused if it would show UTC ;-)</p></div><div id="comment-26027-info" class="comment-info"><span class="comment-age">(15 Oct '13, 15:56)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-26016" class="comment-tools"></div><div class="clear"></div><div id="comment-26016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

