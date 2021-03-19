+++
type = "question"
title = "window close notification"
description = '''Hi,  I have a requirement to launch the multiple wireshark instances for multiple trace files from my application. For example, number M subscribers are monitored in number N nodes/server, it will lead to N*M wireshark windows opened. Because of these many wireshark instance memory consumption is hu...'''
date = "2012-12-04T04:03:00Z"
lastmod = "2012-12-05T11:22:00Z"
weight = 16530
keywords = [ "window" ]
aliases = [ "/questions/16530" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [window close notification](/questions/16530/window-close-notification)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16530-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a requirement to launch the multiple wireshark instances for multiple trace files from my application. For example, number M subscribers are monitored in number N nodes/server, it will lead to N*M wireshark windows opened. Because of these many wireshark instance memory consumption is huge.</p><p>I would like to threshold the number of wireshark instances to be opened at a time (for ex. 10 instances). So when user tries to open the 11th wireshark instance that should not be allowed. I can know the number of wireshark instance open, but how could I find that when a wireshark window is closed, my application get the notification so that it allows to open the other wireshark instance?</p><p>please help.</p></div><div id="question-tags" class="tags-container tags">window</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '12, 04:03</strong></p><img src="https://secure.gravatar.com/avatar/97e620804d00012d2cec1885d6422a13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manojdeoli&#39;s gravatar image" /><p>manojdeoli<br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manojdeoli has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Dec '12, 04:04</p></div></div><div id="comments-container-16530" class="comments-container"><span id="16532"></span><div id="comment-16532" class="comment"><div id="post-16532-score" class="comment-score"></div><div class="comment-text"><p>on a side note... I'd use dumpcap directly instead of Wireshark, because if your only intent is to capture you do not need Wireshark at all, and can spare a lot of memory. Dumpcap is the capture tool used by Wireshark to capture the actual data, and is installed in the same program directory.</p></div><div id="comment-16532-info" class="comment-info"><span class="comment-age">(04 Dec '12, 04:19)</span> Jasper ♦♦</div></div><span id="16546"></span><div id="comment-16546" class="comment"><div id="post-16546-score" class="comment-score"></div><div class="comment-text"><blockquote><p>my application get the notification so that it allows to open the other wireshark instance?</p></blockquote><p>How do you start Wireshark within your application?</p></div><div id="comment-16546-info" class="comment-info"><span class="comment-age">(04 Dec '12, 08:10)</span> Kurt Knochner ♦</div></div><span id="16563"></span><div id="comment-16563" class="comment"><div id="post-16563-score" class="comment-score"></div><div class="comment-text"><p>I have java application, and I am launching it with CLI command: wireshark &lt;path of="" trace="" file=""&gt;.</p></div><div id="comment-16563-info" class="comment-info"><span class="comment-age">(04 Dec '12, 20:13)</span> manojdeoli</div></div><span id="16578"></span><div id="comment-16578" class="comment"><div id="post-16578-score" class="comment-score"></div><div class="comment-text"><p>can you please post the java code? Just the lines that start the external application.</p></div><div id="comment-16578-info" class="comment-info"><span class="comment-age">(05 Dec '12, 02:14)</span> Kurt Knochner ♦</div></div><span id="16583"></span><div id="comment-16583" class="comment"><div id="post-16583-score" class="comment-score"></div><div class="comment-text"><p>Here is code:</p><p><code> final String wiresharkLocation = "/usr/local/bin/"; final String cmd = wiresharkLocation+"wireshark /tmp/manoj/7898.pcap" ; System.out.println(" cmd for launchWireshark : " + cmd); try {      Process process = Runtime.getRuntime().exec(cmd); } catch (Exception e) {     e.printStackTrace();     System.out.println("Exception at Wireshark launch. " + e); }</code></p></div><div id="comment-16583-info" class="comment-info"><span class="comment-age">(05 Dec '12, 04:19)</span> manojdeoli</div></div></div><div id="comment-tools-16530" class="comment-tools"></div><div class="clear"></div><div id="comment-16530-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16606"></span>

<div id="answer-container-16606" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16606-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Process process = Runtime.getRuntime().exec(cmd);</p></blockquote><p>Try calling the method exitValue() of the <a href="http://docs.oracle.com/javase/1.5.0/docs/api/java/lang/Process.html">Process</a> object.</p><p>HINT: This is more a Java question than a Wireshark question and you might get better answers in forum dedicated to Java programming.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '12, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Dec '12, 12:45</p></div></div><div id="comments-container-16606" class="comments-container"></div><div id="comment-tools-16606" class="comment-tools"></div><div class="clear"></div><div id="comment-16606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

