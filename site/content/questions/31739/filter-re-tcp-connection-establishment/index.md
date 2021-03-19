+++
type = "question"
title = "filter re tcp connection establishment"
description = '''source send multiple request to established tcp connection with server .....i want only first request send by the source to capture tcp connection establishment send by source i am using filter &quot;tcp.flags.syn == 1 and tcp.flag.ack == 0&quot; but my problem is server resend the tcp connection establishmen...'''
date = "2014-04-10T19:20:00Z"
lastmod = "2014-04-10T20:05:00Z"
weight = 31739
keywords = [ "reconnection", "establishment", "tcp" ]
aliases = [ "/questions/31739" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [filter re tcp connection establishment](/questions/31739/filter-re-tcp-connection-establishment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31739-score" class="post-score" title="current number of votes">0</div><span id="post-31739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>source send multiple request to established tcp connection with server .....i want only first request send by the source</p><p>to capture tcp connection establishment send by source i am using filter "tcp.flags.syn == 1 and tcp.flag.ack == 0"</p><p>but my problem is server resend the tcp connection establishment request and i want to remove this resend request</p><p>please help....</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reconnection" rel="tag" title="see questions tagged &#39;reconnection&#39;">reconnection</span> <span class="post-tag tag-link-establishment" rel="tag" title="see questions tagged &#39;establishment&#39;">establishment</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '14, 19:20</strong></p><img src="https://secure.gravatar.com/avatar/8b45e81e7b825ca5d14327d460018c85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Deepak1991&#39;s gravatar image" /><p><span>Deepak1991</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Deepak1991 has no accepted answers">0%</span></p></div></div><div id="comments-container-31739" class="comments-container"></div><div id="comment-tools-31739" class="comment-tools"></div><div class="clear"></div><div id="comment-31739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31741"></span>

<div id="answer-container-31741" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31741-score" class="post-score" title="current number of votes">0</div><span id="post-31741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When you see a retransmitted TCP SYN packet, expand the Packet Details pane for the TCP packet details. Do one of the fields say something about it being a retransmission? For example an expert Note-level field saying "This frame is a (suspected) retransmission" or something like that?</p><p>If so, you can select that field to see the name of it; the name of the field will be shown on the lower left status bar. It will be something like "tcp.analysis.retransmission" or something similar. Whatever it is, add the negation of it to your filter. So like this:</p><pre><code>tcp.flags.syn == 1 and tcp.flags.ack == 0 and not tcp.analysis.retransmission</code></pre><p>Or something like that. I can't try it myself to know exactly because I don't have a capture with such duplicates. So this is just a guess.</p><p>If you don't see something like that, you might have sequence analysis turned off - turn it on in your preferences (Edit-&gt;Preferences-&gt;Protocols-&gt;TCP-&gt;"Analyze TCP sequence numbers"). It's on by default I believe.</p><p>There are also other fields (non-expert fields) that might only be in SYN retransmissions, which you should be able to use the negation of instead, or be able to use a filter with "<code>field.name == 0</code>" (depending on the type of field it is).</p><p>It would help if you could post a screenshot of the packet details pane, or better yet post the capture file on cloudshark.org or some other site.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '14, 19:53</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Apr '14, 20:04</strong> </span></p></div></div><div id="comments-container-31741" class="comments-container"><span id="31742"></span><div id="comment-31742" class="comment"><div id="post-31742-score" class="comment-score"></div><div class="comment-text"><p>Yup, that works for me. It occurred to me after posting the above that I could easily capture such a thing myself, by just trying to web browse or telnet to some random IP in the Internet... I guess I'm tired.</p><p>:)</p></div><div id="comment-31742-info" class="comment-info"><span class="comment-age">(10 Apr '14, 20:05)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-31741" class="comment-tools"></div><div class="clear"></div><div id="comment-31741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

