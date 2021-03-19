+++
type = "question"
title = "Filter repeat destination IPs showing"
description = '''Hi, i dont think this is possible but i thought id check. i want to audit which ips are being accessed by one source host over a certain link. this bit easy as i can see all ips in the dump... how ever i want to only see one hit to the destination ips in the output...not all traffic so that i can ma...'''
date = "2012-02-15T09:05:00Z"
lastmod = "2012-02-15T09:53:00Z"
weight = 9032
keywords = [ "filter", "duplicate", "repeat" ]
aliases = [ "/questions/9032" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Filter repeat destination IPs showing](/questions/9032/filter-repeat-destination-ips-showing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9032-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>i dont think this is possible but i thought id check.</p><p>i want to audit which ips are being accessed by one source host over a certain link. this bit easy as i can see all ips in the dump...</p><p>how ever i want to only see one hit to the destination ips in the output...not all traffic so that i can make a list of servers remote side for my audit....i plan on running this for a few days hence not wanting all traffic to each host...just need to knw which servers are accessed from the source host. be bice if i cld see a list of all ips in a row just listed once</p><p>thanks!</p></div><div id="question-tags" class="tags-container tags">filter duplicate repeat</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '12, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/464bdb6a5998e7f2fd7379cf0207f224?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jesh1980&#39;s gravatar image" /><p>jesh1980<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jesh1980 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Feb '12, 09:07</p></div></div><div id="comments-container-9032" class="comments-container"></div><div id="comment-tools-9032" class="comment-tools"></div><div class="clear"></div><div id="comment-9032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9033"></span>

<div id="answer-container-9033" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9033-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>wouldn't the Statistics -&gt; Endpoint report help?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '12, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/dbc4d8cb6be85bd586ca4bf211e1337c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thetechfirm&#39;s gravatar image" /><p>thetechfirm<br />
<span class="score" title="64 reputation points">64</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thetechfirm has no accepted answers">0%</span></p></div></div><div id="comments-container-9033" class="comments-container"><span id="9034"></span><div id="comment-9034" class="comment"><div id="post-9034-score" class="comment-score"></div><div class="comment-text"><p>that actually looks like what i want...can i extract all this?</p></div><div id="comment-9034-info" class="comment-info"><span class="comment-age">(15 Feb '12, 09:29)</span> jesh1980</div></div><span id="9035"></span><div id="comment-9035" class="comment"><div id="post-9035-score" class="comment-score"></div><div class="comment-text"><p>you can use the Copy Button at the bottom and paste the data into Excel and muck around all you want.</p></div><div id="comment-9035-info" class="comment-info"><span class="comment-age">(15 Feb '12, 09:31)</span> thetechfirm</div></div><span id="9036"></span><div id="comment-9036" class="comment"><div id="post-9036-score" class="comment-score"></div><div class="comment-text"><p>yea i tried that, looks like i can only one line at a time...</p></div><div id="comment-9036-info" class="comment-info"><span class="comment-age">(15 Feb '12, 09:35)</span> jesh1980</div></div><span id="9038"></span><div id="comment-9038" class="comment"><div id="post-9038-score" class="comment-score"></div><div class="comment-text"><p>huh?, Go to Statistics - &gt;Endpoints and click on the IP tab. Then if you press on the Copy button and paste the results into notepad you should see the CSV formatted data.</p><p>Are you saying that when you paste the data, you only see one line?</p></div><div id="comment-9038-info" class="comment-info"><span class="comment-age">(15 Feb '12, 09:47)</span> thetechfirm</div></div><span id="9041"></span><div id="comment-9041" class="comment"><div id="post-9041-score" class="comment-score"></div><div class="comment-text"><p>ok i got it, im all good!</p><p>thanks for you help :)</p><p>appreciated buddy!</p></div><div id="comment-9041-info" class="comment-info"><span class="comment-age">(15 Feb '12, 09:49)</span> jesh1980</div></div></div><div id="comment-tools-9033" class="comment-tools"></div><div class="clear"></div><div id="comment-9033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9042"></span>

<div id="answer-container-9042" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9042-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can also use Tshark with a bit of scripting as shown in the answer to <a href="http://ask.wireshark.org/questions/4827/determining-unique-mac-and-ip-addresses-in-a-pcap">this</a> question (which is remarkably similar to yours).</p><p>For Windows PowerShell users the equivalent recipes are:</p><pre><code>Count unique IP addresses: tshark -r &lt;input.pcap&gt; -T fields -e ip.dst ip.src | Sort-Object | Get-Unique

Count unique Ethernet addresses: tshark -r &lt;input.pcap&gt; -T fields -e eth.dst eth.src | Sort-Object | Get-Unique</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '12, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Feb '12, 10:00</p></div></div><div id="comments-container-9042" class="comments-container"><span id="9057"></span><div id="comment-9057" class="comment"><div id="post-9057-score" class="comment-score"></div><div class="comment-text"><p>thanks..i have knw idea how to do that so may go with the first option</p></div><div id="comment-9057-info" class="comment-info"><span class="comment-age">(16 Feb '12, 03:45)</span> jesh1980</div></div><span id="9058"></span><div id="comment-9058" class="comment"><div id="post-9058-score" class="comment-score"></div><div class="comment-text"><p>Tshark is the command line version of wireshark, and outputs text strings corresponding to the input capture, live or from a file.</p><p>The advantage of using Tshark is that the output can then be processed by other applications. My example for Windows users and uses PowerShell, the replacement for the old CMD shell and the linked example is for *nix users.</p></div><div id="comment-9058-info" class="comment-info"><span class="comment-age">(16 Feb '12, 04:11)</span> grahamb ♦</div></div></div><div id="comment-tools-9042" class="comment-tools"></div><div class="clear"></div><div id="comment-9042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

