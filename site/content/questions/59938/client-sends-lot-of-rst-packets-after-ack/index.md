+++
type = "question"
title = "Client sends lot of RST packets after ACK"
description = '''Hi, I have a problem with a tcp connection and I&#x27;m trying to figure if the problem comes from the client or the server side. After a request is sent by the client, the server responds with ACK and the client starts sending a lot of RST packets, causing the server to be unreachable (I have to manuall...'''
date = "2017-03-08T14:26:00Z"
lastmod = "2017-03-09T06:44:00Z"
weight = 59938
keywords = [ "rst" ]
aliases = [ "/questions/59938" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Client sends lot of RST packets after ACK](/questions/59938/client-sends-lot-of-rst-packets-after-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59938-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a problem with a tcp connection and I'm trying to figure if the problem comes from the client or the server side. After a request is sent by the client, the server responds with ACK and the client starts sending a lot of RST packets, causing the server to be unreachable (I have to manually reboot it).</p><p>Here is a capture of the wireshark trace. <img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_03-08-17_at_05.23_PM.PNG" alt="alt text" /></p><p>I notice the server never sends a FIN packet, is it required? Also, is it normal for a client to send that amount o RST packet?</p><p>Thanks for your help,</p></div><div id="question-tags" class="tags-container tags">rst</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '17, 14:26</strong></p><img src="https://secure.gravatar.com/avatar/8f64945bb01abe6bb17c19bcd3ec1f2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mgregoire&#39;s gravatar image" /><p>mgregoire<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mgregoire has no accepted answers">0%</span></p></img></div></div><div id="comments-container-59938" class="comments-container"><span id="59939"></span><div id="comment-59939" class="comment"><div id="post-59939-score" class="comment-score"></div><div class="comment-text"><p>Looks strange is there a Firewall in between. Could you provide us the trace <a href="https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/">https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/</a></p></div><div id="comment-59939-info" class="comment-info"><span class="comment-age">(08 Mar '17, 14:34)</span> Christian_R</div></div><span id="59959"></span><div id="comment-59959" class="comment"><div id="post-59959-score" class="comment-score"></div><div class="comment-text"><p>You can download the trace here : <a href="https://exoc-my.sharepoint.com/personal/mgregoire_exoc_onmicrosoft_com/_layouts/15/guestaccess.aspx?docid=059fc6be222034e34bf5044f28a016a88&amp;authkey=AWtZ0JjakF9PAyNe6jzw4Nw">https://exoc-my.sharepoint.com/personal/mgregoire_exoc_onmicrosoft_com/_layouts/15/guestaccess.aspx?docid=059fc6be222034e34bf5044f28a016a88&amp;authkey=AWtZ0JjakF9PAyNe6jzw4Nw</a></p><p>The 2 devices are connected to a Cisco SG300 managed switch on my local network. From what I know, there's know firewall between.</p></div><div id="comment-59959-info" class="comment-info"><span class="comment-age">(09 Mar '17, 05:51)</span> mgregoire</div></div></div><div id="comment-tools-59938" class="comment-tools"></div><div class="clear"></div><div id="comment-59938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59961"></span>

<div id="answer-container-59961" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59961-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like a completely chaotic server reaction to me. All the packets from 192.168.71.9 have a TCP window value of zero (even though Wireshark only marks some of them). Also, the TCP sequence number of the Server jumps from 38 to 1091042821 (both relative).</p><p>The packets of length 232 from 192.168.71.9 are interesting as well, as they contain alphabetical characters like in a ping payload - this doesn't look good to me, more like a faulty device, maybe even leaking arbitrary memory (which would be very uh-oh...).</p><p>As far as I can tell there's no hop between the two according to the TTLs being 128 and 64 (Windows Client and Linux Server would be my guess, but that's not very exact, of course).</p><p>Verdict: the server TCP stack seems to have gone completely nuts, for unknown reasons (maybe a damaged network card, broken drivers, etc)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '17, 06:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '17, 06:45</p></div></div><div id="comments-container-59961" class="comments-container"><span id="59965"></span><div id="comment-59965" class="comment"><div id="post-59965-score" class="comment-score"></div><div class="comment-text"><p>It looks really strange, there is a is completed FIN and after that this:<br />
(1) First .176 sends an RST<br />
(2) then .9 sends an ACK with (ZERO Window).<br />
(3) then an RST again from 71.176<br />
... And now the really strange thing:<br />
The system .9 sends a FIN,ACK,PUSH packet with the same IP.ID as the packet of (2) and a length of 232 Byte.</p></div><div id="comment-59965-info" class="comment-info"><span class="comment-age">(09 Mar '17, 06:58)</span> Christian_R</div></div><span id="59966"></span><div id="comment-59966" class="comment"><div id="post-59966-score" class="comment-score"></div><div class="comment-text"><p>I think the stack is nuts, plain and simple :-)</p></div><div id="comment-59966-info" class="comment-info"><span class="comment-age">(09 Mar '17, 07:00)</span> Jasper ♦♦</div></div><span id="59968"></span><div id="comment-59968" class="comment"><div id="post-59968-score" class="comment-score"></div><div class="comment-text"><p>@Jasper the SEQ seems O.K. this is a correct mislead by the relative view. Because the session is correctly closed for the Wireshark point of view.</p></div><div id="comment-59968-info" class="comment-info"><span class="comment-age">(09 Mar '17, 07:02)</span> Christian_R</div></div><span id="59969"></span><div id="comment-59969" class="comment"><div id="post-59969-score" class="comment-score"></div><div class="comment-text"><p>@Christian_R Oh, bugger... yes, you're correct, so it's a Wireshark display error... the stack is still crazy :-)</p></div><div id="comment-59969-info" class="comment-info"><span class="comment-age">(09 Mar '17, 07:04)</span> Jasper ♦♦</div></div><span id="59970"></span><div id="comment-59970" class="comment"><div id="post-59970-score" class="comment-score"></div><div class="comment-text"><p>@Jasper: But have no explanation for the crazy behaviour. And I think, too, that the most reasonable cause is a corrupted stack.</p></div><div id="comment-59970-info" class="comment-info"><span class="comment-age">(09 Mar '17, 07:07)</span> Christian_R</div></div><span id="59979"></span><div id="comment-59979" class="comment not_top_scorer"><div id="post-59979-score" class="comment-score"></div><div class="comment-text"><p>Ok I will check on the server side, from what I understand it might be malfunctioning... Thanks a lot for your input!</p></div><div id="comment-59979-info" class="comment-info"><span class="comment-age">(10 Mar '17, 06:16)</span> mgregoire</div></div></div><div id="comment-tools-59961" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-59961-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

