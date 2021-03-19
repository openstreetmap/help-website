+++
type = "question"
title = "tshark 2.2.6 doesn&#x27;t display data.text field on some computer"
description = '''I want to capture and display the UDP traffic on a certain port using tshark. I want to display the text content on each captured line. I have two computers both running CentOS 7. I built from sources latest Wireshark 2.2.6 following the tutorial here: http://blog.jeffli.me/blog/2016/08/14/build-lat...'''
date = "2017-04-24T23:52:00Z"
lastmod = "2017-04-25T08:15:00Z"
weight = 61023
keywords = [ "netcat", "data.text", "tshark", "centos", "linux" ]
aliases = [ "/questions/61023" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [tshark 2.2.6 doesn't display data.text field on some computer](/questions/61023/tshark-226-doesnt-display-datatext-field-on-some-computer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61023-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to capture and display the UDP traffic on a certain port using <code>tshark</code>. I want to display the text content on each captured line.</p><p>I have two computers both running CentOS 7. I built from sources latest Wireshark 2.2.6 following the tutorial here: <a href="http://blog.jeffli.me/blog/2016/08/14/build-latest-wireshark-in-centos-7/">http://blog.jeffli.me/blog/2016/08/14/build-latest-wireshark-in-centos-7/</a></p><p>I installed the resulting RPMs on both computers. After that I ran (as root) the following <code>tshark</code> command on both computers:</p><pre><code>/usr/local/bin/tshark -f &quot;port 3901&quot; -i any -T fields -e frame.number -e frame.time -e ip.src -e ip.dst -e data.text</code></pre><p>Then I ran the following on <strong>computer A</strong> (that's my desktop computer, running CentOS 7 in graphical mode):</p><pre><code>echo &quot;test message&quot; | nc -u 192.168.224.60 3901</code></pre><p><code>tshark</code> showed the following line:</p><pre><code>1   Apr 24, 2017 14:05:25.926688950 EEST    192.168.224.60  192.168.224.60  test message</code></pre><p>That's exactly what I need.</p><p>Now.. I did exactly the same test on <strong>computer B</strong> (this is the remote computer running CentOS 7 in text mode), just the IP is different there.</p><p><code>tshark</code> refuses to display the <code>data.text</code> field. It outputs a line like this, without <code>data.text</code> field:</p><pre><code>1   Apr 24, 2017 11:06:19.947384620 UTC 192.168.0.60    192.168.0.60</code></pre><p>I'm using the same <code>nc</code> version (6.4) on both computers.</p><p>I have no idea what could cause this different behavior of computer <strong>A</strong> vs <strong>B</strong>. What could prevent <code>tshark</code> on computer <strong>B</strong> from displaying the <code>data.text</code>?</p><p>[<strong>Edit</strong>]</p><p>I shared one capture from each computer below so you can compare them:</p><p>Computer A : <a href="https://goo.gl/kAyOrr">https://goo.gl/kAyOrr</a></p><p>Computer B : <a href="https://goo.gl/Cuu8I9">https://goo.gl/Cuu8I9</a></p><p>I made the captures by running the following line on each computer:</p><pre><code>tshark -i any -f &quot;port 3901&quot; -w &quot;capture.pcap&quot;</code></pre><p>Then I sent two test messages on each computer:</p><pre><code>echo &quot;test message&quot; | nc -u 192.168.0.2 3901
echo &quot;test message again&quot; | nc -u 192.168.0.2 3901</code></pre></div><div id="question-tags" class="tags-container tags">netcat data.text tshark centos linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '17, 23:52</strong></p><img src="https://secure.gravatar.com/avatar/d74baf1a0f84390f050cc05a8052323f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ciprian&#39;s gravatar image" /><p>ciprian<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ciprian has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Apr '17, 05:14</p></div></div><div id="comments-container-61023" class="comments-container"><span id="61028"></span><div id="comment-61028" class="comment"><div id="post-61028-score" class="comment-score">1</div><div class="comment-text"><p>The data.text field is usually populated when no dissector can actually dissect the packet as a "fallback". It's possible that the host that doesn't display the message is dissecting it as something else, maybe down to a differetn preference.</p><p>Can you share captures from host A &amp; B in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DropBox etc.?</p></div><div id="comment-61028-info" class="comment-info"><span class="comment-age">(25 Apr '17, 03:05)</span> grahamb ♦</div></div><span id="61038"></span><div id="comment-61038" class="comment"><div id="post-61038-score" class="comment-score"></div><div class="comment-text"><p>I edited my question as you suggested and I added the captured files.</p></div><div id="comment-61038-info" class="comment-info"><span class="comment-age">(25 Apr '17, 05:17)</span> ciprian</div></div></div><div id="comment-tools-61023" class="comment-tools"></div><div class="clear"></div><div id="comment-61023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="61049"></span>

<div id="answer-container-61049" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61049-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try enabling the data dissector's preference to show the data as text:</p><pre><code>tshark -r computerA.pcap -o data.show_as_text:TRUE -T fields -e frame.number -e frame.time -e ip.src -e ip.dst -e data.text</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '17, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-61049" class="comments-container"><span id="61050"></span><div id="comment-61050" class="comment"><div id="post-61050-score" class="comment-score"></div><div class="comment-text"><p>Excelent! That <code>-o data.show_as_text:TRUE</code> did the job. I added that to my initial command and it started to show the data.text on any computer. Thanks a lot.</p></div><div id="comment-61050-info" class="comment-info"><span class="comment-age">(25 Apr '17, 11:33)</span> ciprian</div></div><span id="61051"></span><div id="comment-61051" class="comment"><div id="post-61051-score" class="comment-score">1</div><div class="comment-text"><p>Great!</p><p>By the way, if you don't want to have to specify that option on the command-line each time, you can permanently set it in Wireshark via <code>Edit -&gt; Preferences -&gt; Protocols -&gt; Data -&gt; Show data as text</code>.</p></div><div id="comment-61051-info" class="comment-info"><span class="comment-age">(25 Apr '17, 11:39)</span> cmaynard ♦♦</div></div><span id="61055"></span><div id="comment-61055" class="comment"><div id="post-61055-score" class="comment-score"></div><div class="comment-text"><p>There is no graphical interface on the remote Linux host. But I'm fine with specifying that option in the command.</p></div><div id="comment-61055-info" class="comment-info"><span class="comment-age">(26 Apr '17, 02:04)</span> ciprian</div></div><span id="61059"></span><div id="comment-61059" class="comment"><div id="post-61059-score" class="comment-score"></div><div class="comment-text"><p>Well, you can also change it by directly editing the Wireshark <em><code>preferences</code></em> file, typically located at <em><code>$HOME/.wireshark/preferences</code></em> on UNIX-compatible systems and <em><code>%APPDATA%\Wireshark\preferences</code></em> (or, if <code>%APPDATA%</code> isn't defined, <em><code>%USERPROFILE%\Application Data\Wireshark\preferences</code></em>) on Windows systems.</p><p>I only mention this for the benefit of anyone who might not necessarily want to specify extra options on the command-line.</p></div><div id="comment-61059-info" class="comment-info"><span class="comment-age">(26 Apr '17, 07:36)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-61049" class="comment-tools"></div><div class="clear"></div><div id="comment-61049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61041"></span>

<div id="answer-container-61041" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61041-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Both captures display the data for me, but as I'm using a single version of wireshark for both captures, this leads me even more strongly to think that there is something different about the setup on computer B.</p><p>Have you tried using computer B to display the capture from computer A, e.g. <code>tshark -r computerA.pcap -T fields -e frame.number -e frame.time -e ip.src -e ip.dst -e data.text</code>?</p><p>If this still doesn't display the data text, then either the application or the preferences must be different on B.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '17, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-61041" class="comments-container"><span id="61042"></span><div id="comment-61042" class="comment"><div id="post-61042-score" class="comment-score"></div><div class="comment-text"><p>I ran the suggested command four times, two times on each of the two computers A and B, using alternatively both .pcap files. data.text was never displayed, no matter the computer or pcap file.</p><p>And where to look for those preferences? I have exactly the same wireshark version on both computers.</p></div><div id="comment-61042-info" class="comment-info"><span class="comment-age">(25 Apr '17, 06:26)</span> ciprian</div></div><span id="61045"></span><div id="comment-61045" class="comment"><div id="post-61045-score" class="comment-score"></div><div class="comment-text"><p>Try letting tshark show the complete info to see what it is being dissected as:</p><p><code>tshark -r computerA.pcap</code>.</p></div><div id="comment-61045-info" class="comment-info"><span class="comment-age">(25 Apr '17, 06:44)</span> grahamb ♦</div></div></div><div id="comment-tools-61041" class="comment-tools"></div><div class="clear"></div><div id="comment-61041-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

