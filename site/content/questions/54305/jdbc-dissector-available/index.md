+++
type = "question"
title = "JDBC Dissector Available?"
description = '''Hi all. Long time since I&#x27;ve posted, but I&#x27;m a daily user of Wireshark - can&#x27;t live without it :-) (I haven&#x27;t posted in many moons because I haven&#x27;t needed to. Wireshark consistently delivers.) Recently, I needed to diagnose some slow DB query activity. I was told that the protocol in use is JDBC. I...'''
date = "2016-07-25T09:31:00Z"
lastmod = "2016-07-25T22:24:00Z"
weight = 54305
keywords = [ "jdbc" ]
aliases = [ "/questions/54305" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JDBC Dissector Available?](/questions/54305/jdbc-dissector-available)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54305-score" class="post-score" title="current number of votes">0</div><span id="post-54305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all. Long time since I've posted, but I'm a daily user of Wireshark - can't live without it :-)</p><p>(I haven't posted in many moons because I haven't needed to. Wireshark consistently delivers.)</p><p>Recently, I needed to diagnose some slow DB query activity. I was told that the protocol in use is JDBC. I captured the traffic and loaded it up in Wireshark, hoping/expecting that I could simply do a "Decode As", specify JDBC, and see the innards of the request-response pairs.</p><p>No such luck. It seems that there is no JDBC dissector.</p><p>I then tried decoding as TDS, but that didn't help - just a bunch of "malformed" notices.</p><p>I'm not much of a DB guy, so I'm stuck...</p><p>Is there hope for me? Is there a dissector I SHOULD be using? Do I need to get more information from my DB team on exactly what protocol/variant/DB version is being used?</p><p>Thx for any help!!</p><p>feenyman99</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-jdbc" rel="tag" title="see questions tagged &#39;jdbc&#39;">jdbc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '16, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p><span>feenyman99</span><br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span></p></div></div><div id="comments-container-54305" class="comments-container"></div><div id="comment-tools-54305" class="comment-tools"></div><div class="clear"></div><div id="comment-54305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54317"></span>

<div id="answer-container-54317" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54317-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54317-score" class="post-score" title="current number of votes">0</div><span id="post-54317-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What database (Oracle, etc) is being used ?</p><p>JDBC is just a standard Java API used to access a DB. A client-side library translates the query to the appropriate on-the-wire protocol required to access a particular type of DB.</p><p>If the database is Oracle, Wireshark does not have a dissector for same.</p><p>See: <a href="https://wiki.wireshark.org/Oracle">Wireshark Wiki: Oracle</a></p><hr /><p>Having said the above, if the DB is Oracle, it's possible you may be able to decode well enough for your purposes.</p><p>See: <a href="https://ask.wireshark.org/questions/17894/oracle-sqlnet-tracing">Wireshark Oracle SQLNET tracing</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '16, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jul '16, 13:18</strong> </span></p></div></div><div id="comments-container-54317" class="comments-container"><span id="54321"></span><div id="comment-54321" class="comment"><div id="post-54321-score" class="comment-score"></div><div class="comment-text"><p>Yes, the database is Oracle.</p><p>And, yes, the truth is, the payload is pretty easy to interpret, even for a non-DB joe like me.</p><p>But, I guess Wireshark has spoiled me. I would have expected that I could filter on different JDBC request types, or filter on just JDBC requests, or on just JDBC responses, like I can with something like AJP13.</p><p>It's no biggie. I just figured I was missing something obvious when I could not see JDBC-specific decodes.</p><p>Thanx Bill, for the explanation.</p><p>feenyman99</p></div><div id="comment-54321-info" class="comment-info"><span class="comment-age">(25 Jul '16, 18:41)</span> <span class="comment-user userinfo">feenyman99</span></div></div><span id="54325"></span><div id="comment-54325" class="comment"><div id="post-54325-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-54325-info" class="comment-info"><span class="comment-age">(25 Jul '16, 22:24)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-54317" class="comment-tools"></div><div class="clear"></div><div id="comment-54317-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

