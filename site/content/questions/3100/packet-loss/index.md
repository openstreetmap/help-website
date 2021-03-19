+++
type = "question"
title = "packet loss"
description = '''hi i try to check packet loss when i send a file how i can do this how i can the begin and end of file on the stream and how i can know if there is  any loss happen and how i can know these packets are concern the same group(file) thanx'''
date = "2011-03-25T00:02:00Z"
lastmod = "2011-03-25T01:28:00Z"
weight = 3100
keywords = [ "html77" ]
aliases = [ "/questions/3100" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [packet loss](/questions/3100/packet-loss)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3100-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi i try to check packet loss when i send a file how i can do this how i can the begin and end of file on the stream and how i can know if there is any loss happen and how i can know these packets are concern the same group(file) thanx</p></div><div id="question-tags" class="tags-container tags">html77</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '11, 00:02</strong></p><img src="https://secure.gravatar.com/avatar/ac2a6402ceea6ed5f01ce0f11cf40c5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flower&#39;s gravatar image" /><p>flower<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flower has no accepted answers">0%</span></p></div></div><div id="comments-container-3100" class="comments-container"></div><div id="comment-tools-3100" class="comment-tools"></div><div class="clear"></div><div id="comment-3100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3104"></span>

<div id="answer-container-3104" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3104-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could isolate the stream using a conversation filter (I usually select one packet of the flow and use the popup menu to go "conversation filter -&gt; tcp"). Then I'd edit the automatically generated filter by enclosing it in brackets and adding " and tcp.analysis.lost_segment". If you see packets after applying it you probably had packet loss. I say "probably" because you might also have had packet drops on capturing the flow, meaning that there was no real loss, you just didn't capture everything.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '11, 01:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3104" class="comments-container"><span id="3110"></span><div id="comment-3110" class="comment"><div id="post-3110-score" class="comment-score"></div><div class="comment-text"><p>how i can edit filter by enclosing it in brackets and where i add tcp.analysis.lost_segment plz can you describe with more details i'm not proffesional in using wireshark</p></div><div id="comment-3110-info" class="comment-info"><span class="comment-age">(25 Mar '11, 03:30)</span> flower</div></div><span id="3112"></span><div id="comment-3112" class="comment"><div id="post-3112-score" class="comment-score"></div><div class="comment-text"><p>if you use the Conversation Filter popup you should see that a filter is generated in the filter bar right on top of the packet list which is usually empty when you haven't edit. In there you can edit the filter.</p></div><div id="comment-3112-info" class="comment-info"><span class="comment-age">(25 Mar '11, 04:05)</span> Jasper ♦♦</div></div><span id="3116"></span><div id="comment-3116" class="comment"><div id="post-3116-score" class="comment-score"></div><div class="comment-text"><p>ok jasper but when i go to conversation filter from analyze menu i didnit find this option (tcp) i find PN-IO AR and PN-IO AR(with data) is there any solution for this or another way to extract all packets which concern the same file send over communication thanx</p></div><div id="comment-3116-info" class="comment-info"><span class="comment-age">(25 Mar '11, 06:23)</span> flower</div></div><span id="3136"></span><div id="comment-3136" class="comment"><div id="post-3136-score" class="comment-score"></div><div class="comment-text"><p>You're looking in the wrong place :-)</p><p>Select one of the packets of your stream in the packet list (usually the top pane right below the filter input bar). Then right-click and select "Conversation Filter" -&gt; "TCP" from the popup menu, not the main window menu.</p></div><div id="comment-3136-info" class="comment-info"><span class="comment-age">(25 Mar '11, 16:40)</span> Jasper ♦♦</div></div><span id="3150"></span><div id="comment-3150" class="comment"><div id="post-3150-score" class="comment-score"></div><div class="comment-text"><p>thanx jasper i do it but how i isolate certain file packets for example i send an image file to another one and at reciver i want to find the packet loss which concerning only this file suppose if i send alot of files (image, sound, document) how i isolate only the backet loss concerning the image file thanx</p></div><div id="comment-3150-info" class="comment-info"><span class="comment-age">(27 Mar '11, 04:21)</span> flower</div></div><span id="3151"></span><div id="comment-3151" class="comment not_top_scorer"><div id="post-3151-score" class="comment-score"></div><div class="comment-text"><p>What protocol are you using? If you use HTTP or FTP you can use the "find" dialog (Edit -&gt; Find Packet), select "String" and search in Packet List or Details (or even the Packet Bytes). Wireshark will then try to find the filename, jump to the packet, and on that one you use the conversation filter like I described. If your're using HTTP/1.1 you might see multiple file transfers in the isolated flow, so you need to use the request and last image packet as boundaries.</p></div><div id="comment-3151-info" class="comment-info"><span class="comment-age">(27 Mar '11, 04:28)</span> Jasper ♦♦</div></div></div><div id="comment-tools-3104" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-3104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

