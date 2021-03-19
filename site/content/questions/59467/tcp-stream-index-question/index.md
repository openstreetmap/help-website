+++
type = "question"
title = "TCP Stream Index Question"
description = '''I just watched a video by Laura Chappell talking about stream index and that WS starts at 0 and works its way up with each new conversation. I assumed that each new conversation would have to start with a Syn, Syn/Ack, Syn, but when I started looking at my streams and filtering on just one particula...'''
date = "2017-02-16T06:12:00Z"
lastmod = "2017-02-16T09:34:00Z"
weight = 59467
keywords = [ "index", "question", "steam", "tcp" ]
aliases = [ "/questions/59467" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Stream Index Question](/questions/59467/tcp-stream-index-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59467-score" class="post-score" title="current number of votes">0</div><span id="post-59467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just watched a video by Laura Chappell talking about stream index and that WS starts at 0 and works its way up with each new conversation. I assumed that each new conversation would have to start with a Syn, Syn/Ack, Syn, but when I started looking at my streams and filtering on just one particular stream, I found quite a few without the 3 way handshake. So what does this mean?</p><p>Ex. Stream number 39 when I open this up and sort the stream by number so it starts with the first packet, it shows the flag being PSH, ACK and in the info section shows Application data, Application data. This stream is only 15 packets long and doesn't have a FIN bit in the stream either.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-index" rel="tag" title="see questions tagged &#39;index&#39;">index</span> <span class="post-tag tag-link-question" rel="tag" title="see questions tagged &#39;question&#39;">question</span> <span class="post-tag tag-link-steam" rel="tag" title="see questions tagged &#39;steam&#39;">steam</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '17, 06:12</strong></p><img src="https://secure.gravatar.com/avatar/a6414c2ff8204ee9c4a3bc2a646c4644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rock90&#39;s gravatar image" /><p><span>rock90</span><br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rock90 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Feb '17, 07:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-59467" class="comments-container"></div><div id="comment-tools-59467" class="comment-tools"></div><div class="clear"></div><div id="comment-59467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59474"></span>

<div id="answer-container-59474" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59474-score" class="post-score" title="current number of votes">2</div><span id="post-59474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Streams do not have to start with a handshake to have a number assigned. Wireshark does it by looking at the 5 Tuple: source IP, source port, destination IP, destination port, and layer 4 protocol (in your case: TCP). So when a new combination is seen it gets the next stream index.</p><p>There's one exception to the rule: if Wireshark sees a 5 Tuple and another identical 5 Tuple starting with new TCP handshake, it will also increase the stream index.</p><p>For more information about 5 Tuple handling, there's this blog entry: <a href="https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/">https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '17, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-59474" class="comments-container"><span id="59478"></span><div id="comment-59478" class="comment"><div id="post-59478-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper, I will definitely check out your blog.</p></div><div id="comment-59478-info" class="comment-info"><span class="comment-age">(16 Feb '17, 09:34)</span> <span class="comment-user userinfo">rock90</span></div></div></div><div id="comment-tools-59474" class="comment-tools"></div><div class="clear"></div><div id="comment-59474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

