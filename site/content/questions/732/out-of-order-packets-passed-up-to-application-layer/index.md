+++
type = "question"
title = "Out-of-order packets...  Passed up to application layer?"
description = '''Hello, My question does not really pertain directly to Wireshark, but rather to TCP. I hope that is OK. If not, let me know... This question was prompted by Laura Chappell&#x27;s Tip #57, that I just received, and it involves out-of-order packets. She asks the question: &quot;Does your application depend on p...'''
date = "2010-10-28T15:05:00Z"
lastmod = "2010-11-03T20:20:00Z"
weight = 732
keywords = [ "out-of-order" ]
aliases = [ "/questions/732" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Out-of-order packets... Passed up to application layer?](/questions/732/out-of-order-packets-passed-up-to-application-layer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-732-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>My question does not really pertain directly to Wireshark, but rather to TCP. I hope that is OK. If not, let me know...</p><p>This question was prompted by Laura Chappell's Tip #57, that I just received, and it involves out-of-order packets. She asks the question: "Does your application depend on packets arriving in order before the data is presented or do a few out-of-order packets go unnoticed...?"</p><p>This puzzled me because I <em>thought</em> that TCP would NOT pass out-of-order packets to the application layer, but rather would wait until the packets were ordered before placing them in the application buffer. In other words, if the packets come in like this: 5, 6, 8, 9, 10, 7, 11, ..., then TCP might pass packets 5 &amp; 6 to the application buffer, but would NOT place 8 in the buffer until 7 is received, when it could then place packets 7 thru 10 in the buffer, IN ORDER. In this way, the application might be "delayed" by out of order packets, but would never "see" out of order packets.</p><p>Is my understanding incorrect?</p><p>thx, Feenyman99</p></div><div id="question-tags" class="tags-container tags">out-of-order</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '10, 15:05</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p>feenyman99<br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span></p></div></div><div id="comments-container-732" class="comments-container"><span id="735"></span><div id="comment-735" class="comment"><div id="post-735-score" class="comment-score"></div><div class="comment-text"><p>Thanks to Sake for clearing that up... yes - you're right that TCP won't pass out-of-order packets up, but it's the buffering delay caused by out-of-order packets data that slows things down. Whether we notice that all depends on the application behavior. Clear as mud?</p></div><div id="comment-735-info" class="comment-info"><span class="comment-age">(28 Oct '10, 15:34)</span> lchappell ♦</div></div></div><div id="comment-tools-732" class="comment-tools"></div><div class="clear"></div><div id="comment-732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="733"></span>

<div id="answer-container-733" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-733-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are ringht, TCP segments can arrive at the NIC out-of-order, but they are always presented to the Application in-order. Of course if packets arrive at the NIC out-of-order, there will be a delay in presenting the data to the Application.</p><p>Some applications will not have a problem with the delay (like Laura's example of showing a webpage in a browser) but other applications might have a problem with the delay (for instance when streaming audio over TCP). IMHO, that is what Laura was pointing out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '10, 15:22</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-733" class="comments-container"><span id="740"></span><div id="comment-740" class="comment"><div id="post-740-score" class="comment-score"></div><div class="comment-text"><p>Awesome - thx for the quick response. Out-of-order packets and resultant app delays now make perfect sense, thx to Sake and Laura. Love those tips, Laura - keep 'em comin :-)</p></div><div id="comment-740-info" class="comment-info"><span class="comment-age">(29 Oct '10, 05:26)</span> feenyman99</div></div></div><div id="comment-tools-733" class="comment-tools"></div><div class="clear"></div><div id="comment-733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="769"></span>

<div id="answer-container-769" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-769-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>One rule of thumb you can use is by looking at the PSH bit. Often (very often, actually) when applications try to control the flow of the data, it will send chunks of data to TCP. This is often referred to as "buffer tearing." So if you see some amount of data that's being transferred followed by one packet with the PSH bit set, this is your problem. Regardless of what your TCP window size may be (send or receive window), you can't send more than what the application buffer allows you to send. So you can count the number of application bytes being transferred between the PSH bits. Typically, this will be on a boundary number like 2048, 16348 or 65536.<br />
</p><p>So to add insult to inury, if one of the packets go missing, the entire chunk (after the missing piece) will need to be resent. Again, this can have a huge impact on performance as the new transfer may have to follow tcp slowstart rules. TCP enhancements like Selective ACK can help greatly in cases like this.</p><p>If you look at some of the Sharkfest sessions (Advanced TCP) by me (Hansang Bae), you'll see several examples of this "bound by PSH bit" scenario. Good luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '10, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Nov '10, 14:41</p></div></div><div id="comments-container-769" class="comments-container"></div><div id="comment-tools-769" class="comment-tools"></div><div class="clear"></div><div id="comment-769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="809"></span>

<div id="answer-container-809" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-809-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're seeing "bursts" of out-of-order packets, you also want to check the elapsed time of the "burst." I've seen situation where a high-speed, low-latency network will actually create what appears to be a horrendous flood of out-of-orders, but a time check shows that the mess unscrambled itself within a second or so...don't let the out-of-order flag send you down a rabbit hole in your troubleshooting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '10, 20:20</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-809" class="comments-container"></div><div id="comment-tools-809" class="comment-tools"></div><div class="clear"></div><div id="comment-809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

