+++
type = "question"
title = "bytes missing in capture file"
description = '''Network guys set up a span port with some traffic to my box. Currently I am observing strange behaviour. Consequently and repeatedly I see &quot;X bytes missing in capture file&quot;. I have done such scenario: Open an URL in my browser and tap F5 or ctrl-F5. File is opened correctly. In capture file I see: E...'''
date = "2012-10-22T02:16:00Z"
lastmod = "2013-02-04T00:57:00Z"
weight = 15146
keywords = [ "capture", "problem", "bytes", "tcpdump", "missing" ]
aliases = [ "/questions/15146" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [bytes missing in capture file](/questions/15146/bytes-missing-in-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15146-score" class="post-score" title="current number of votes">0</div><span id="post-15146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Network guys set up a span port with some traffic to my box. Currently I am observing strange behaviour.</p><p>Consequently and repeatedly I see "X bytes missing in capture file". I have done such scenario: Open an URL in my browser and tap F5 or ctrl-F5. File is opened correctly.</p><p>In capture file I see: ET /pc/resources/Ocean/images/logo.gif HTTP/1.1 Host: 10.5.34.230:8080 User-Agent: Mozilla/5.0 (Windows NT 5.1; rv:16.0) Gecko/20100101 Firefox/16.0 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,<em>/</em>;q=0.8 Accept-Language: en-US,en;q=0.5 Accept-Encoding: gzip, deflate Connection: keep-alive Pragma: no-cache Cache-Control: no-cache</p><p>[4380 bytes missing in capture file].p .......:..Z..z... ........... ....P..z................;</p><p>Capture is done by: tcpdump -i any -c 1000 -nn -s 0 -w /tmp/1 host 10.5.34.230 and host 10.5.1.189</p><p>This behaviour is observed for this one machine. Net guys say that span port is configured correctly and couple of more span ports are targeted to my box and seems to be fine.</p><p>I have chcecked this when interface which feeds my box is busy and when its not busy. I have used tcpdump to any interface as well as eth6 (which is the interface receiving traffic).</p><p>The server is a virual one (vmware). Server guy configured it to use only one interface.</p><p>This response is always the same. Always in the same place, always 4380 bytes (for this particular object).</p><p>How to diagnose this problem further?</p><p>I will ask server admin for access to make capture on his server but I need some advice for network guys or for me to be sure I have set up everything correctly.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-bytes" rel="tag" title="see questions tagged &#39;bytes&#39;">bytes</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '12, 02:16</strong></p><img src="https://secure.gravatar.com/avatar/e4a5e9c8c63c17cba9e349911226a1e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ptoki&#39;s gravatar image" /><p><span>ptoki</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ptoki has no accepted answers">0%</span></p></div></div><div id="comments-container-15146" class="comments-container"></div><div id="comment-tools-15146" class="comment-tools"></div><div class="clear"></div><div id="comment-15146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="15150"></span>

<div id="answer-container-15150" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15150-score" class="post-score" title="current number of votes">0</div><span id="post-15150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>xxx bytes missing in capture file</p></blockquote><p>Wireshark will only show that error message, if you follow a TCP stream and wireshark is not able to reassemble all TCP segements, as some packets are missing in the capture file. There are several reasons why that might happen:</p><ul><li>Your capture device was not able to write all packets to disk (overload)</li><li>You stopped tcpdump too early</li><li>Not all packtes have reached tcpdump (mirror port problem or similar)</li></ul><p>Now, the interesting part would be to figure out which one of the above conditions causes the problem.</p><p>Suggestion: Mirror the traffic to a second port and capture there with a second machine. Then compare the capture files. If they contain the same data, the missing packets are dropped "somewhere" (monitored port, source system, "on the way"). If the capture files are different, the system with less packets in the capture file was not able to write all packets to disk (overload).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '12, 04:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Oct '12, 04:26</strong> </span></p></div></div><div id="comments-container-15150" class="comments-container"></div><div id="comment-tools-15150" class="comment-tools"></div><div class="clear"></div><div id="comment-15150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15167"></span>

<div id="answer-container-15167" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15167-score" class="post-score" title="current number of votes">0</div><span id="post-15167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think this is in fact a problem with the SPAN port, and I'm not talking about a wrong configuration, just a wrong approach. If you SPAN one full duplex line to a SPAN port and both receive and transmit channels are 100% busy you have a problem, because the monitor port of the SPAN session will only be able to transmit half of it to the analyzer - which means, 50% of the packets will be dropped at the switch.</p><p>This gets worse if you add more SPAN source sessions to the same monitor port - as soon as the switch has to transmit more packets out the monitor port than there is bandwidth it will drop the frames. That leads to tcpdump not capturing them, because they never got to the device. This can also happen if not all source ports are busy both ways, it is enough to add more source port traffic to the monitor port than it has bandwidth towards the analyzer/capture machine.</p><p>My guess is, that when you test your transmission the buffers of the switch get slammed shut, always leading to the dropout of the same packets each single time.</p><p>How to solve this: make sure that you do not mirror more bits/s to the output port than the line has bandwidth. If you have a really crowded connection and you can't reduce the amount of traffic you should think about using full duplex TAPs instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '12, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Oct '12, 08:34</strong> </span></p></div></div><div id="comments-container-15167" class="comments-container"></div><div id="comment-tools-15167" class="comment-tools"></div><div class="clear"></div><div id="comment-15167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18273"></span>

<div id="answer-container-18273" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18273-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18273-score" class="post-score" title="current number of votes">0</div><span id="post-18273-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have partially solved this issue. Reason to this was problem with cisco nexus device. One nexus had span port configured and sent to another switch. And there was problem with MTU between them.</p><p>Our support confirmed this problem and suggested changing MTU. This helped a bit but not between nexus and catalyst 6500.</p><p>So we changed method of collecting traffic.</p><p>Thank You both for suggestions but it was not the case here. Missing bytes was always in the same place in tcp communication thats why I did not expect to have problem with bandwidth or network card or cpu usage or similar.</p><p>Problems with bandwidth we have succesfully solved by network teaming (bonding) of interfaces which are fed by span ports.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '13, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/e4a5e9c8c63c17cba9e349911226a1e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ptoki&#39;s gravatar image" /><p><span>ptoki</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ptoki has no accepted answers">0%</span></p></div></div><div id="comments-container-18273" class="comments-container"></div><div id="comment-tools-18273" class="comment-tools"></div><div class="clear"></div><div id="comment-18273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

