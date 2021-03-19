+++
type = "question"
title = "Translating hex digits to engineering digits"
description = '''My task is to learn about Wireshark dissectors, so that my team can in general be able to translate hexadecimal digits to engineering digits in Wireshark. My guess is we should think about translating raw data, message data, and data captures (maybe even dumps) in Wireshark output. (I don&#x27;t know wha...'''
date = "2017-09-01T05:08:00Z"
lastmod = "2017-09-07T03:04:00Z"
weight = 63545
keywords = [ "hex" ]
aliases = [ "/questions/63545" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Translating hex digits to engineering digits](/questions/63545/translating-hex-digits-to-engineering-digits)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63545-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My task is to learn about Wireshark dissectors, so that my team can in general be able to translate hexadecimal digits to engineering digits in Wireshark. My guess is we should think about translating raw data, message data, and data captures (maybe even dumps) in Wireshark output. (I don't know what plugins we be will be using!)</p><p>What can you tell me? Do I have to use a dissector to translate hex to engineering units? Is there some sore of GUI Wireshark option I can set? Is there a file I can change?</p><p>Does someone have a complete and easy setup dissector to do this already? What are my options? What is the easiest dissector product to use? Also, what is the best product to use? Whatever my team decides to choose, what will be my limitations? What are problems with doing this?</p><p>(Note: I've watched a TSN.1 dissector video on YouTube, but I know nothing about what will be installed with whatever version of Wireshark that our team decides to use.)</p><p>Has the process of generating engineering units changed in the last decade?</p><p>On the Internet, I found only one article related to this problem. The article title is below, but it didn't tell me anything. It lack inituition. The article only talks about using a custom dissector. Wireshark Topic: How to decode and display as ASCII?</p><p>Finally, if you have an answer for me and my team can you explain it to me in a step by step way with baby steps. I.E.: Can you share with me exactly what the first step, second step, third step, upto the nth step is, in as much detail as possible.</p><p>I've never worked with Wireshark before beyond a few good videos at www rti com.</p><p>Thank you, Mike</p></div><div id="question-tags" class="tags-container tags">hex</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '17, 05:08</strong></p><img src="https://secure.gravatar.com/avatar/45327d89d1ff1135df093945666003ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike123456&#39;s gravatar image" /><p>Mike123456<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike123456 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted 01 Sep '17, 05:13</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-63545" class="comments-container"><span id="63546"></span><div id="comment-63546" class="comment"><div id="post-63546-score" class="comment-score">1</div><div class="comment-text"><p>What do you mean by "engineering digits" and "engineering units"?</p></div><div id="comment-63546-info" class="comment-info"><span class="comment-age">(01 Sep '17, 05:13)</span> Guy Harris ♦♦</div></div><span id="63566"></span><div id="comment-63566" class="comment"><div id="post-63566-score" class="comment-score"></div><div class="comment-text"><p>I went back to my team to answer your question!</p><p>I'll explain to you what my team wants accomplished. By doing that I will explain to you what engineering data units we want. Simply, all we want are 3 "on" and "off" values and 2 integer values.</p><p>Caveat: I'm using all make believe data from a Wireshark Captured data. My team doesn't want me to publish actual data.</p><p>(1) Captured Wireshark data from three areas of Wireshark:</p><pre><code>No. Time     Source    Destination   Protocol Length Info
8   0.055974 192.2.4.8 240.199.089.0 UDP      60     53016-&gt;53016 Len=4</code></pre><p>Message:</p><pre><code>Data (4 bytes)
      Data: 2043c0bd
      [Length: 4]</code></pre><p>Raw Data:</p><pre><code>20   43   c0   bd</code></pre><p>(2) My explanation of the above hexadecimal data:</p><pre><code>Byte 1:  20
Byte 2:  43
Byte 3:  c0
Byte 4:  bd</code></pre><p>Above byte 1 has only 3 bits (above right 3 bits) that have to be translated to "on" or "off" values. I.E.: We want to see "on" or "off" instead of "1" and "0." The other bits (above left 5 bits) can be ignored and not shown at all in the message window. They'll still be visible in the raw data. The 3 right bits represent 3 separate switches.</p><p>Above bytes 2 through 4 have two integer values from -127 to 127. Again some of the bits will not be used and can be ignored and not shown at all in the message window. They'll still be visible in the raw data. The bits that makeup the two integer values are distributed in the 3 above bytes and are not consecutive. Here is the actual placement of the 16 bits that makeup the two integer values between -127 to 127. These two integer values represent a single joystick which can be moved left or right from a resting position.</p><pre><code>0   1    0    0   X7   X6   Y7   Y6
1   1   X5   X4   X3   X2   X1   X0
1   0   Y5   Y4   Y3   Y2   Y1   Y1</code></pre><p>So, my team wants me to pick out the above bits to create and display two integer values.</p><pre><code>X7  X6  X5  X4  X3  X2  X1  X0  Equals some value from -127 to 127
Y7  Y6  Y5  Y4  Y3  Y2  Y1  Y0  Equals some value from -127 to 127</code></pre><p>FYI: This is only my preliminary initial task. I.E.: This is the first message that my team wants me to create a dissector for. There are other messages that I will be given later to work on and display in a nice way.</p></div><div id="comment-63566-info" class="comment-info"><span class="comment-age">(05 Sep '17, 10:41)</span> Mike123456</div></div><span id="63567"></span><div id="comment-63567" class="comment"><div id="post-63567-score" class="comment-score"></div><div class="comment-text"><p>By "left" and "right", as in "left 5 bits" and "right 3 bits", do you mean "upper" and "lower", so that the high-order bit, and the 4 bits below it, are the "left 5 bits", and the 3 bits below that, going down to the low-order bit, are the "right 3 bits", so that, for 0x20, which is 00100000 in binary, the "left 5 bits" are "00100", and the "right 3 bits" are "000", and all 3 bits are "off", and the "00100" can be ignored?</p></div><div id="comment-63567-info" class="comment-info"><span class="comment-age">(05 Sep '17, 18:12)</span> Guy Harris ♦♦</div></div><span id="63568"></span><div id="comment-63568" class="comment"><div id="post-63568-score" class="comment-score"></div><div class="comment-text"><p>Yes, that is exactly what my team tells me to implement.</p></div><div id="comment-63568-info" class="comment-info"><span class="comment-age">(06 Sep '17, 04:26)</span> Mike123456</div></div></div><div id="comment-tools-63545" class="comment-tools"></div><div class="clear"></div><div id="comment-63545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63571"></span>

<div id="answer-container-63571" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63571-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This can (almost) all be achieved by using so called header fields. When you study dissector development (see <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=doc/README.dissector">README.dissector</a>) you'll come across these.</p><p>Further discussion would probably be appropriate on the <a href="https://www.wireshark.org/lists/">Wireshark Developers mailing list</a> since this is not a forum, but a Q&amp;A site.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '17, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-63571" class="comments-container"></div><div id="comment-tools-63571" class="comment-tools"></div><div class="clear"></div><div id="comment-63571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

