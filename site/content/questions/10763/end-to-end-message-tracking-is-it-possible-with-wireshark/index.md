+++
type = "question"
title = "End to End message tracking -is it possible with wireshark"
description = '''We are planning to implement end-to-end message tracking functionality.We have various products/appliations running on Linux servers and they exchange messges(XML,HTTP,HTTPS,LDAP) in our architecure.We thought of using tshark(for https-SSL) and tcpflow(for other protocols) and we are able to track e...'''
date = "2012-05-07T22:03:00Z"
lastmod = "2012-05-08T22:25:00Z"
weight = 10763
keywords = [ "tshark" ]
aliases = [ "/questions/10763" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [End to End message tracking -is it possible with wireshark](/questions/10763/end-to-end-message-tracking-is-it-possible-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10763-score" class="post-score" title="current number of votes">0</div><span id="post-10763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are planning to implement end-to-end message tracking functionality.We have various products/appliations running on Linux servers and they exchange messges(XML,HTTP,HTTPS,LDAP) in our architecure.We thought of using tshark(for https-SSL) and tcpflow(for other protocols) and we are able to track each and every messge which is flowing from one linux server to the other.I wanted to know how we can implement the messge correlation?If the communication was only SOAP XML ,then we would have used any custom xml element like (&lt;messageid&gt;),but our architecture has many applications which use different communication protocols</p><p>Using wireshark/tshark is there any way that we can assigin a unique number to the messsages that flow from one application to another application(running on linux).</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '12, 22:03</strong></p><img src="https://secure.gravatar.com/avatar/54dfb1796a8beedf9843a326d673eaae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vikram&#39;s gravatar image" /><p><span>vikram</span><br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vikram has no accepted answers">0%</span></p></div></div><div id="comments-container-10763" class="comments-container"></div><div id="comment-tools-10763" class="comment-tools"></div><div class="clear"></div><div id="comment-10763-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10770"></span>

<div id="answer-container-10770" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10770-score" class="post-score" title="current number of votes">1</div><span id="post-10770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm sorry, but without scripting that's not possible, as wireshark cannot know which 'message' belongs to a certain 'application data flow', IF those messages are not in the same TCP connection (which is likely if you use HTTP as a transport protocol). Maybe MATE can help a bit, however I suggest to script something with Sharktools (Python) or Net::Sharktools (Perl)</p><p>Wiki:<br />
<strong><a href="http://wiki.wireshark.org/Tools">http://wiki.wireshark.org/Tools</a></strong></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '12, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 May '12, 03:10</strong> </span></p></div></div><div id="comments-container-10770" class="comments-container"><span id="10802"></span><div id="comment-10802" class="comment"><div id="post-10802-score" class="comment-score"></div><div class="comment-text"><p>irrespective of which application is running on a linux box or technology or protocol,I am thinking if there is any way when a messge goes from linux box A to linux box B can we generated a unique number and make sure that the number also goes along with the message ,if it is possible then we will be able to track the message. Not sure, if the transport protocols like http may already have any of their headers which will carry a unique number for each and every number.</p></div><div id="comment-10802-info" class="comment-info"><span class="comment-age">(08 May '12, 22:17)</span> <span class="comment-user userinfo">vikram</span></div></div><span id="10803"></span><div id="comment-10803" class="comment"><div id="post-10803-score" class="comment-score"></div><div class="comment-text"><p>There is nothing built into http itself. However, most http applications use some form of Session-ID to keep track of user sessions. Those Session-IDs are "stored" either in a Cookie, or they are encoded in the URL (JSESSIONID, PHPSESSIONID, et.c). In some rare cases they are part of an HTTP Header. The later case need special http applications on both sides (no browser!)</p><p>So, basically you need to understand your application protocol and figure out if there is a unique Session-ID which you can filter on.</p></div><div id="comment-10803-info" class="comment-info"><span class="comment-age">(08 May '12, 22:25)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-10770" class="comment-tools"></div><div class="clear"></div><div id="comment-10770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

