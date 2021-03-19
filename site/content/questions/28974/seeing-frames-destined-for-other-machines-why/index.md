+++
type = "question"
title = "Seeing frames destined for other machines, why?"
description = '''This is not a wireshark question but a general networking question. My machine running wireshark on the adapter in promiscuous mode sometimes receives frames destined for another machine on the subnet even though the network is fully switched, why? my machine&#x27;s mac address is :aa:bb:cc:xx:yy:zz, in ...'''
date = "2014-01-16T13:59:00Z"
lastmod = "2014-01-16T15:01:00Z"
weight = 28974
keywords = [ "frames" ]
aliases = [ "/questions/28974" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Seeing frames destined for other machines, why?](/questions/28974/seeing-frames-destined-for-other-machines-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28974-score" class="post-score" title="current number of votes">0</div><span id="post-28974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is not a wireshark question but a general networking question. My machine running wireshark on the adapter in promiscuous mode sometimes receives frames destined for another machine on the subnet even though the network is fully switched, why?</p><p>my machine's mac address is :aa:bb:cc:xx:yy:zz, in promiscuous mode, no ip other machine's mac address is : aa:bb:cc:kk:ll:mm, ip:192.168.101.2 Internet server : ip:64.208.138.115</p><p>Now why is my machine receiving some frames of the conversation between 192.168.101.2 &lt;-&gt; 64.208.138.115 even though the machines are connected to a switch? one reason could be that the switch did not know the mac address for 192.168.101.2 and decided to flood all ports with the frame maybe ?</p><p>Tushar.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-frames" rel="tag" title="see questions tagged &#39;frames&#39;">frames</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '14, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/b7cb3cdffa3d69b446038a1f44db1423?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tushar&#39;s gravatar image" /><p><span>tushar</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tushar has no accepted answers">0%</span></p></div></div><div id="comments-container-28974" class="comments-container"></div><div id="comment-tools-28974" class="comment-tools"></div><div class="clear"></div><div id="comment-28974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28975"></span>

<div id="answer-container-28975" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28975-score" class="post-score" title="current number of votes">1</div><span id="post-28975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tushar has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The last sentence of your question is the answer. Switches "forget" learned MAC addresses every once in a while to allow them to be refreshed, and for that one packet will be flooded.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '14, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28975" class="comments-container"><span id="28976"></span><div id="comment-28976" class="comment"><div id="post-28976-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jasper!</p><p>-Tushar.</p></div><div id="comment-28976-info" class="comment-info"><span class="comment-age">(16 Jan '14, 15:01)</span> <span class="comment-user userinfo">tushar</span></div></div></div><div id="comment-tools-28975" class="comment-tools"></div><div class="clear"></div><div id="comment-28975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

