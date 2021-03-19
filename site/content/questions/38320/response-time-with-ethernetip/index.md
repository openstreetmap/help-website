+++
type = "question"
title = "Response time with Ethernet/IP"
description = '''How can I estimate the response time between a master controller and a slave?'''
date = "2014-12-04T04:23:00Z"
lastmod = "2014-12-06T07:30:00Z"
weight = 38320
keywords = [ "rtethernetip" ]
aliases = [ "/questions/38320" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Response time with Ethernet/IP](/questions/38320/response-time-with-ethernetip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38320-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I estimate the response time between a master controller and a slave?</p></div><div id="question-tags" class="tags-container tags">rtethernetip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '14, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/3783a13e9c0308c92d54210fcf61c638?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Furio%20Buonopane&#39;s gravatar image" /><p>Furio Buonopane<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Furio Buonopane has no accepted answers">0%</span></p></div></div><div id="comments-container-38320" class="comments-container"><span id="38369"></span><div id="comment-38369" class="comment"><div id="post-38369-score" class="comment-score">2</div><div class="comment-text"><p>Can you please add (much) more details?</p><ul><li>What kind or "master controller" and "slave" are you talking about?</li><li>What kind of protocol are they using.</li><li>How do you define "response time" in your scenario?</li></ul></div><div id="comment-38369-info" class="comment-info"><span class="comment-age">(05 Dec '14, 10:33)</span> Kurt Knochner ♦</div></div><span id="38377"></span><div id="comment-38377" class="comment"><div id="post-38377-score" class="comment-score">1</div><div class="comment-text"><p>The protocol is Ethernet/IP as in the question title. In this case the master initiates the request and the slave responds. I'm not sure if enip has request/response tracking and timing.</p></div><div id="comment-38377-info" class="comment-info"><span class="comment-age">(05 Dec '14, 14:11)</span> grahamb ♦</div></div><span id="38381"></span><div id="comment-38381" class="comment"><div id="post-38381-score" class="comment-score">2</div><div class="comment-text"><p>Ethernet and IP are two different protocols, neither of which have any concept of a "master" or a "slave".</p><p>Applications that run over IP can have that relationship, and Wireshark has several protocol-specific request/response time measuring logic, but the answer to the question depends on the protocol. Since both Ethernet and IP are stateless, they don't have the concept of a "session", or a "request", or a "response", thus there is nothing for Wireshark to calculate at that layer.</p></div><div id="comment-38381-info" class="comment-info"><span class="comment-age">(05 Dec '14, 16:31)</span> Quadratic</div></div><span id="38391"></span><div id="comment-38391" class="comment"><div id="post-38391-score" class="comment-score"></div><div class="comment-text"><p>Thank you all for the quick responses. Ethernet/IP stands for Ethernet idustrial protocol and is based on a single protocol CIP (Common Industrial Protocol). My question is: is there any function in wireshark to calculate the time of sending and receiving packets between a master controller and a slave?</p><p>Thanks</p><p>Furio Buonopane</p></div><div id="comment-38391-info" class="comment-info"><span class="comment-age">(06 Dec '14, 03:36)</span> Furio Buonopane</div></div><span id="38392"></span><div id="comment-38392" class="comment"><div id="post-38392-score" class="comment-score">1</div><div class="comment-text"><p>When looking at the source code, there does not seem to be any Request / Response tracking in the CIP dissector allowing you to compute a time</p></div><div id="comment-38392-info" class="comment-info"><span class="comment-age">(06 Dec '14, 05:47)</span> Pascal Quantin</div></div></div><div id="comment-tools-38320" class="comment-tools"></div><div class="clear"></div><div id="comment-38320-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38393"></span>

<div id="answer-container-38393" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38393-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As I hinted and @Pascal Quantin confirmed, there is no request\response tracking in the CIP dissector. The best you can do is to filter the display to show only the communications to the specific slave you're interested in and then set the time display format to be "Seconds since last Displayed Packet". The time column will then show the delta time between the request and the response.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '14, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38393" class="comments-container"><span id="38394"></span><div id="comment-38394" class="comment"><div id="post-38394-score" class="comment-score"></div><div class="comment-text"><p>Ok perfect thanks a lot! I entered the column for the delta time. Now, Can I export from wireshark only the delta time column?</p></div><div id="comment-38394-info" class="comment-info"><span class="comment-age">(06 Dec '14, 07:38)</span> Furio Buonopane</div></div><span id="38395"></span><div id="comment-38395" class="comment"><div id="post-38395-score" class="comment-score"></div><div class="comment-text"><p>Sure: File -&gt; Export Packet Dissections -&gt; As .csv</p><p>With that, just make sure that column is in the time format you want when you save it, and that's how it'll appear in a comma-separated file.</p></div><div id="comment-38395-info" class="comment-info"><span class="comment-age">(06 Dec '14, 08:27)</span> Quadratic</div></div><span id="38396"></span><div id="comment-38396" class="comment"><div id="post-38396-score" class="comment-score">1</div><div class="comment-text"><p>Or use the <code>-T fields -e frame.time_delta</code> options along with other <code>-e field.name</code> options for any other required fields and using <code>-E separator=xxx</code> to control the field separator.</p></div><div id="comment-38396-info" class="comment-info"><span class="comment-age">(06 Dec '14, 09:23)</span> grahamb ♦</div></div></div><div id="comment-tools-38393" class="comment-tools"></div><div class="clear"></div><div id="comment-38393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

