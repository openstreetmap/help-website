+++
type = "question"
title = "what does TCP windows scale zero means ?"
description = '''I was analyzing a issue where I see the below TCP optiosn set , I see the server setting the windows scale to 0 , what does these mean? I have the capture on the client but not on the server.  Is server not accepting the window scaling at all ? Do the server see the client receive window size as 655...'''
date = "2011-03-26T08:34:00Z"
lastmod = "2011-03-31T20:40:00Z"
weight = 3144
keywords = [ "windows", "scale", "tcp" ]
aliases = [ "/questions/3144" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [what does TCP windows scale zero means ?](/questions/3144/what-does-tcp-windows-scale-zero-means)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3144-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3144-score" class="post-score" title="current number of votes">0</div><span id="post-3144-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was analyzing a issue where I see the below TCP optiosn set , I see the server setting the windows scale to 0 , what does these mean? I have the capture on the client but not on the server.</p><ol><li>Is server not accepting the window scaling at all ? Do the server see the client receive window size as 65535 even though we offer them (65535*2^7)</li><li>Is this good ? Does The server see the 65535*2^7 as the receive window advertised by us ? we are seeing 65535 constantly being advertised as the receive window size by the server.</li></ol><p><strong>TCP Options set by Client in SYN<br />
TCP Options Field Value</strong></p><p>Maximum Segment Size 1460 / TCP SACK Permitted option TRUE/ Windows Scale 7(multiply by 128)/</p><p><strong>TCP Options set by Server in SYN+ACK<br />
TCP Options Field Value</strong></p><p>Maximum Segment Size 1300/ TCP SACK Permitted option Not specified in the options/ Windows Scale 0(multiply by 1)/</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-scale" rel="tag" title="see questions tagged &#39;scale&#39;">scale</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '11, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/1023ff7387209c8a9c1cbff327b2fac0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sreekanth&#39;s gravatar image" /><p><span>sreekanth</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sreekanth has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-3144" class="comments-container"></div><div id="comment-tools-3144" class="comment-tools"></div><div class="clear"></div><div id="comment-3144-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3145"></span>

<div id="answer-container-3145" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3145-score" class="post-score" title="current number of votes">2</div><span id="post-3145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It means that the server is RFC 1323 aware, but it's not going to go beyond what's advertised. In other words, it's not going to shift the windows field by any factor.</p><p>Almost all systems use the same SEND window space as the RECEIVE window size. So the server in question (the one that sent the syn+ack) will only send 65535 per RTT.<br />
</p><p>So if you require a bigger window size, just set it on the server.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '11, 11:29</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Mar '11, 11:29</strong> </span></p></div></div><div id="comments-container-3145" class="comments-container"><span id="3146"></span><div id="comment-3146" class="comment"><div id="post-3146-score" class="comment-score"></div><div class="comment-text"><p>Thanks Hansangb ,</p><p>Ideally the client receive window should become the server send window, right? In this case if the Server is RFC 1323 aware, it should set (65535*2^7) as its send window and receive window as 65535, even if it set its window scale factor as zero.</p><p>Am I wrong anyway ?</p><p>The server is not managed by us , and the capture we have is of the client's end , I am not sure what is the receive window they are seeing as being advertised by us .</p></div><div id="comment-3146-info" class="comment-info"><span class="comment-age">(26 Mar '11, 19:59)</span> <span class="comment-user userinfo">sreekanth</span></div></div><span id="3195"></span><div id="comment-3195" class="comment"><div id="post-3195-score" class="comment-score"></div><div class="comment-text"><p>The sender will use the min() of his SENDER window or receiver's RECEIVE window. This is to ensure that the sender can guarantee delivery from his SEND buffer in case there's packet loss. Almost <em>all</em> systems will set the SEND window to the RECEIVE window. Some systems will let you change one or the other (AIX for example) but it's extremely rare. So assume the SEND window is the same as the RECEIVE window. Unless there are FWs in the middle that are terminating the TCP (tcp level proxy), what you see is what the other guy sent (and vice versa)</p></div><div id="comment-3195-info" class="comment-info"><span class="comment-age">(28 Mar '11, 18:57)</span> <span class="comment-user userinfo">hansangb</span></div></div><span id="3202"></span><div id="comment-3202" class="comment"><div id="post-3202-score" class="comment-score"></div><div class="comment-text"><p>My 2 cents. If the server doesn't need to allocate that extra buffer, don't force it. If the server will be sending lots of data and not receiving it then you shouldn't force the RECV window to be large. This can quickly waste memory. Consider your options and your needs carefully.</p></div><div id="comment-3202-info" class="comment-info"><span class="comment-age">(29 Mar '11, 08:55)</span> <span class="comment-user userinfo">GeonJay</span></div></div><span id="3262"></span><div id="comment-3262" class="comment"><div id="post-3262-score" class="comment-score"></div><div class="comment-text"><p>Thanks Hasangb &amp; Geon , I sent the same observations to the owner of server , I will post any new update here.</p></div><div id="comment-3262-info" class="comment-info"><span class="comment-age">(31 Mar '11, 20:40)</span> <span class="comment-user userinfo">sreekanth</span></div></div></div><div id="comment-tools-3145" class="comment-tools"></div><div class="clear"></div><div id="comment-3145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

