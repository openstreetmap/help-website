+++
type = "question"
title = "Tshark and bash scripting"
description = '''I capture everything on port 25 into a pcap file using dumpcap. Sometimes, I see a malicious email campaign come through, so now, I want to find all the times it occurs. So far, I have this bash script: sudo tshark -n -t ad -r $2 -R &quot;smtp.command___line contains $1 || data-text-lines contains $1 || ...'''
date = "2012-09-04T12:42:00Z"
lastmod = "2012-09-06T13:58:00Z"
weight = 14037
keywords = [ "tshark", "bash" ]
aliases = [ "/questions/14037" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark and bash scripting](/questions/14037/tshark-and-bash-scripting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14037-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I capture everything on port 25 into a pcap file using <code>dumpcap</code>. Sometimes, I see a malicious email campaign come through, so now, I want to find all the times it occurs. So far, I have this bash script:</p><pre><code>sudo tshark -n -t ad -r $2 -R &quot;smtp.command___line contains $1 || data-text-lines contains $1 || imf contains $1&quot; -T fields -e frame.time -e ip.src -e ip.dst -e tcp.stream -e smtp.command_line -e data-text-lines</code></pre><p>An example output of this script is shown below:</p><pre><code>Sep  4, 2012 05:53:47.577902000 redacted IP    redacted IP    138     MAIL FROM:&lt;[email protected]welcome.aexp.com&gt; SIZE=14138\x0d\x0a</code></pre><p>In the script above, <code>$2</code> is the pcap file, and <code>$1</code> is what I'm looking for. I then want to take the identified <code>tcp.stream</code> and dump that out to a file. I can do that easily enough with one stream, but I'm interested in doing that for, say, 4 to 5 different streams. I'm thinking of using a <code>for</code>-loop or something that will look like the below:</p><pre><code>./findstreams bleh.pcap &lt;- command typed in
138 139 140             &lt;- streams to pick out</code></pre><p>I think the <code>tshark</code> command would be:</p><pre><code>tshark -r $1 -P -w /tmp/ick``date +%m-%N`&#39;.pcap -R &#39;tcp.stream == $variable&#39;</code></pre><p>...but I'm not sure how to get the <code>$variable</code> part to "work". Thanks for any help you can give.</p></div><div id="question-tags" class="tags-container tags">tshark bash</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '12, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/37898d970fb9980bdd2168e913a50ca2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DigiAngel&#39;s gravatar image" /><p>DigiAngel<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DigiAngel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Sep '12, 15:31</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-14037" class="comments-container"><span id="14043"></span><div id="comment-14043" class="comment"><div id="post-14043-score" class="comment-score"></div><div class="comment-text"><p>One thing that sticks out to me is the usage of a variable inside a single-quoted string (i.e., <code>'tcp.stream == $variable'</code>). The single-quotes prevent the variable from being expanded in bash. Assuming you meant to expand that variable, you need to use double-quotes instead.</p></div><div id="comment-14043-info" class="comment-info"><span class="comment-age">(04 Sep '12, 15:16)</span> helloworld</div></div><span id="14044"></span><div id="comment-14044" class="comment"><div id="post-14044-score" class="comment-score"></div><div class="comment-text"><p>Another: do you really need to use <code>sudo</code> in your first <code>tshark</code> commmand? Most users resort to <code>sudo</code> only when <code>tshark</code> can't access the capture interfaces on their host, but you're only reading in a pcap file (thus no capture interfaces would be accessed...I would hope).</p></div><div id="comment-14044-info" class="comment-info"><span class="comment-age">(04 Sep '12, 15:22)</span> helloworld</div></div><span id="14045"></span><div id="comment-14045" class="comment"><div id="post-14045-score" class="comment-score"></div><div class="comment-text"><p>Yea that's a good point with sudo. And agreed..it's double quote nice catch.</p></div><div id="comment-14045-info" class="comment-info"><span class="comment-age">(04 Sep '12, 15:44)</span> DigiAngel</div></div></div><div id="comment-tools-14037" class="comment-tools"></div><div class="clear"></div><div id="comment-14037-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="14040"></span>

<div id="answer-container-14040" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14040-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to parse the output of the first tshark command. It will print out the stream number (tcp.stream). Then loop over those stream numbers.</p><p>Reagards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '12, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-14040" class="comments-container"><span id="14041"></span><div id="comment-14041" class="comment"><div id="post-14041-score" class="comment-score"></div><div class="comment-text"><p>Yea it's the looping part I'm getting stuck on ;)</p></div><div id="comment-14041-info" class="comment-info"><span class="comment-age">(04 Sep '12, 14:50)</span> DigiAngel</div></div><span id="14042"></span><div id="comment-14042" class="comment"><div id="post-14042-score" class="comment-score"></div><div class="comment-text"><p>can you please post the output of the first tshark command?</p></div><div id="comment-14042-info" class="comment-info"><span class="comment-age">(04 Sep '12, 14:58)</span> Kurt Knochner ♦</div></div><span id="14046"></span><div id="comment-14046" class="comment"><div id="post-14046-score" class="comment-score"></div><div class="comment-text"><p>Sep 4, 2012 05:53:47.577902000 ip ip 138 MAIL FROM:[email protected] SIZE=14138\x0d\x0a Sep 4, 2012 05:53:48.358362000 ip ip 138 Sep 4, 2012 05:53:49.907442000 ip ip 139 RCPT TO:[email protected]\x0d\x0a</p><p>So in this case, the sessions I want to see in their entirety are 138 and 139. Thanks for looking all.</p></div><div id="comment-14046-info" class="comment-info"><span class="comment-age">(04 Sep '12, 15:45)</span> DigiAngel</div></div></div><div id="comment-tools-14040" class="comment-tools"></div><div class="clear"></div><div id="comment-14040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14062"></span>

<div id="answer-container-14062" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14062-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you have a command like <code>./findstreams</code> that you can encapsulate the first tshark call in, it will make this next part much easier.</p><pre><code>for stream in `./findstreams blah.pcap`; do tshark &lt;all your options&gt; -R &quot;tcp.stream==$stream&quot;; done</code></pre><p>The trick is using back-ticks (`) around the first command, and using Bash's "for var in set; do;done" to loop over it. For a trivial example of it in action, look at this:</p><pre><code>for i in 1 2 3 4 5; do echo &quot;i is $i&#39;; done</code></pre><p>And for substituting a command in there, think about <code>ls</code></p><pre><code>for i in `ls`; do echo $i; done</code></pre><p>You may run into punctuation-soup when trying to embed all of this into a single command, so the more you can put into separate scripts, the better off you'll probably be.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Sep '12, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/365cfc3c62b61b2ed219b5d146e8ad3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zachad&#39;s gravatar image" /><p>zachad<br />
<span class="score" title="331 reputation points">331</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zachad has 3 accepted answers">21%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Sep '12, 12:27</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-14062" class="comments-container"><span id="14090"></span><div id="comment-14090" class="comment"><div id="post-14090-score" class="comment-score"></div><div class="comment-text"><p>Thank you....I will give this a shot and show my results.</p></div><div id="comment-14090-info" class="comment-info"><span class="comment-age">(06 Sep '12, 06:58)</span> DigiAngel</div></div></div><div id="comment-tools-14062" class="comment-tools"></div><div class="clear"></div><div id="comment-14062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14096"></span>

<div id="answer-container-14096" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14096-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>So...looks like this is it, where $1 is the search item and $2 is the pcap file. Thanks of the help all!</p><p>for stream in <code>tshark -n -t ad -r $2 -R "smtp.command_line contains $1 || data-text-lines contains $1 || imf contains $1" -T fields -e tcp.stream -e data-text-lines | sort -u</code>; do tshark -r $2 -w test-$stream.pcap -R "tcp.stream==$stream" ; done</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '12, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/37898d970fb9980bdd2168e913a50ca2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DigiAngel&#39;s gravatar image" /><p>DigiAngel<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DigiAngel has no accepted answers">0%</span></p></div></div><div id="comments-container-14096" class="comments-container"></div><div id="comment-tools-14096" class="comment-tools"></div><div class="clear"></div><div id="comment-14096-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

